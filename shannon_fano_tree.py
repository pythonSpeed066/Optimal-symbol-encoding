from graphviz import Digraph

def build_tree(codes):
    tree = {}
    for char, code in codes.items():
        current_node = tree
        for bit in code:
            if bit not in current_node:
                current_node[bit] = {}
            current_node = current_node[bit]
        current_node['value'] = char  # Добавляем символ на соответствующий узел
    return tree

def add_nodes(dot, tree, node_id="root", parent_id=None):
    if parent_id is not None:
        dot.node(node_id, label=node_id)  # Создаем узел
        dot.edge(parent_id, node_id)  # Рисуем ребро

    for bit, subtree in tree.items():
        if bit == "value":  # Если узел содержит символ
            leaf_id = f"{node_id}_leaf"
            dot.node(leaf_id, f"'{subtree}'", shape="box", style="filled", color="lightblue")
            dot.edge(node_id, leaf_id, label="")  # Рисуем ребро от узла до листа
        else:
            child_id = f"{node_id}_{bit}"
            dot.node(child_id, f"'{bit}'", shape="circle")
            dot.edge(node_id, child_id, label=bit)  # Рисуем ребро с меткой бита
            add_nodes(dot, subtree, child_id)

def visualize_shannon_fano(codes):
    tree = build_tree(codes)
    dot = Digraph()
    dot.node("root", "Root", shape="circle")
    add_nodes(dot, tree)
    dot.render("shannon_fano_tree", format="png", cleanup=True)
    dot.view()

codes = {
    ' ': "111", 'о': "110", 'е': "1011", 'а': "1010", 'и': "1001", 'н': "1000",
    'т': "0111", 'с': "01101", 'в': "01100", 'л': "01011", 'р': "01010",
    'к': "01001", 'д': "01000", 'м': "00111", 'у': "001101", ',': "001100",
    'п': "00101", 'ь': "001001", 'я': "001000", 'ч': "000111", 'г': "000110",
    'б': "000101", 'ы': "0001001", 'з': "0001000", 'ж': "0000111", '.': "0000110",
    'й': "0000101", 'х': "0000100", 'ш': "0000011", 'ю': "00000101", '-': "00000100",
    'э': "00000011", 'щ': "000000101", 'ц': "000000100", ';': "000000011",
    'ф': "0000000101", ':': "0000000100", '(': "0000000011", ')': "00000000101",
    '1': "00000000100", '8': "00000000011", '6': "000000000101", 'ъ': "000000000100",
    '2': "000000000011", '5': "0000000000101", '4': "0000000000100", '7': "0000000000011",
    '3': "0000000000010", '0': "0000000000001", '9': "00000000000001"
}

visualize_shannon_fano(codes)


