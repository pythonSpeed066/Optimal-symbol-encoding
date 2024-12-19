# Определяем список символов, которые нужно оставить
symbols = [str(digit) for digit in range(10)] + \
          [chr(ord('а') + i) for i in range(33)] + \
          ['.', ',', ':', ';', '-', ' ', '(', ')']


def filter_text_by_symbols(source_text, symbols):
    """
    Фильтрует текст, оставляя только символы из заданного списка.
    """
    return ''.join([char for char in source_text if char in symbols])


# Открываем файл, читаем содержимое, переводим в нижний регистр и фильтруем
try:
    with open('F_M_Dostoevskiy_Prestuplenie_i_nakazanie.txt', 'r', encoding='cp1251') as file:
        source_text = file.read()
    source_text = source_text.lower()
    # Удаляем ненужные символы
    filtered_text = filter_text_by_symbols(source_text, symbols)

    print(f"Длина исходного текста: {len(source_text)} символов")
    print(f"Длина обработанного текста: {len(filtered_text)} символов")
except FileNotFoundError:
    print("Файл не найден. Убедитесь, что он находится в той же директории и имеет правильное название.")

import math


def calculate_information(probability):
    if probability == 0:
        return 0
    else:
        return -math.log2(probability)


def calculate_entropy(probability):
    if probability == 0:
        return 0
    else:
        return -probability * math.log2(probability)


def filter_text_by_symbols(source_text, symbols):
    """
    Фильтрует текст, оставляя только символы из заданного списка.
    """
    return ''.join([char for char in source_text if char in symbols])


def create_character_frequency_dict(text):
    """
    Создаёт словарь частот символов.
    """
    character_frequency = {}
    total_symbols_count = len(text)

    for symbol in symbols:
        count = text.count(symbol)
        probability = count / total_symbols_count if total_symbols_count > 0 else 0
        information = calculate_information(probability)
        entropy = calculate_entropy(probability)
        character_frequency[symbol] = {
            'code': ord(symbol),
            'occurrences': count,
            'probability': probability,
            'information': information,
            'entropy': entropy
        }

    return character_frequency


def calculate_total_entropy(character_frequency):
    """
    Вычисляет общую энтропию.
    """
    return sum(character_frequency[symbol]['entropy'] for symbol in character_frequency)


def validate_probabilities_sum(character_frequency):
    """
    Проверяет, что сумма вероятностей равна 1.
    """
    probabilities_sum = sum(character_frequency[symbol]['probability'] for symbol in character_frequency)
    return abs(probabilities_sum - 1) < 1e-6


def validate_symbols_count(character_frequency, source_text):
    """
    Проверяет, совпадает ли общее количество символов.
    """
    # Учитываем только символы, которые действительно встречаются в тексте
    total_symbols_count = sum(character_frequency[symbol]['occurrences'] for symbol in character_frequency if
                              character_frequency[symbol]['occurrences'] > 0)
    return total_symbols_count == len(source_text)


# Генерация словаря частот символов
frequency_dict = create_character_frequency_dict(filtered_text)

# Печать информации по каждому символу
for key, value in sorted(frequency_dict.items()):
    print(f"{key}: {value}")

# Вычисление общей энтропии
total_entropy = calculate_total_entropy(frequency_dict)
print(f"\nОбщая энтропия источника: {total_entropy:.3f} бит")

# Проверка суммы вероятностей
if validate_probabilities_sum(frequency_dict):
    print("Вероятности в сумме дают 1 с точностью до ошибки округления.")
else:
    print("Вероятности в сумме не дают 1.")

# Проверка общего количества символов
if validate_symbols_count(frequency_dict, filtered_text):
    print(f"Общее количество символов ({len(filtered_text)}) совпадает с суммой количеств вхождений всех символов.")
else:
    print("Общее количество символов не совпадает с суммой количеств вхождений всех символов.")