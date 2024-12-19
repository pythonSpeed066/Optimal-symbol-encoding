from graphviz import Digraph
import heapq
from frequency_creating import frequency_dict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Построение дерева Хаффмана
def build_huffman_tree(frequency_dict):
    heap = [HuffmanNode(char, frequency_dict[char]['probability']) for char in frequency_dict]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]


# Генерация кодов
def generate_huffman_codes(root, code='', codes=None):
    if codes is None:
        codes = {}
    if root:
        if root.char is not None:
            codes[root.char] = code
        generate_huffman_codes(root.left, code + '0', codes)
        generate_huffman_codes(root.right, code + '1', codes)
    return codes


# Визуализация дерева Хаффмана
def visualize_huffman_tree(root):
    dot = Digraph()

    def add_nodes_edges(node, parent_id=None, label=""):
        if node:
            node_id = f"{id(node)}"  # Уникальный идентификатор узла
            if node.char is not None:
                # Листовой узел: добавляем символ и вероятность
                dot.node(node_id, f"'{node.char}'\n{node.freq:.4f}", shape="box", style="filled", color="lightblue")
            else:
                # Внутренний узел: добавляем только вероятность
                dot.node(node_id, f"{node.freq:.4f}", shape="circle")

            if parent_id is not None:
                # Добавляем ребро от родителя к текущему узлу
                dot.edge(parent_id, node_id, label=label)

            # Рекурсивно обрабатываем потомков
            add_nodes_edges(node.left, node_id, label="0")
            add_nodes_edges(node.right, node_id, label="1")

    add_nodes_edges(root)
    dot.render("huffman_tree", format="png", cleanup=True)
    dot.view()


# Построение и визуализация
root = build_huffman_tree(frequency_dict)
codes = generate_huffman_codes(root)
visualize_huffman_tree(root)

# Вывод кодов
print("Символ", "Вероятность", "Код", sep="\t")
for char in frequency_dict:
    print(f"{char}\t{frequency_dict[char]['probability']:.4f}\t{codes[char]}")
