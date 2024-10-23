
def encode(data, window_size=1024):
    encoded = []
    n = len(data)
    i = 0

    while i < n:
        match_offset = 0
        match_length = 0

        # Определяем начало окна
        window_start = max(0, i - window_size)

        # Ищем совпадения в окне
        for j in range(window_start, i):
            length = 0
            char = data[i]
            while (i + length < n) and (j + length < i) and (data[j + length] == data[i + length] == char):
                length += 1

            if length > match_length:
                match_length = length
                match_offset = i - j

        # Если нашли совпадение, добавляем в выходной список
        if match_length > 0:
            next_char_index = i + match_length
            next_char = data[next_char_index] if next_char_index < n else '\0'
            encoded.append((match_offset, match_length, next_char))
            i += match_length + 1
        else:
            # Если нет совпадений, просто записываем символ
            encoded.append((0, 0, data[i]))
            i += 1

    return encoded


def decode(encoded):
    decoded = []
    for offset, length, next_char in encoded:
        start = len(decoded)
        # Добавляем символы из предыдущих данных по смещению
        for _ in range(length):
            if offset > 0:
                decoded.append(decoded[start - offset])
        # Добавляем следующий символ
        if next_char != '\0':
            if next_char == '':
                decoded.append('\n')
            else:
                decoded.append(next_char)
    return ''.join(decoded)


def save_to_file(encoded, filename, bytes_mode=False, mode='w', encoding='utf-8'):
    if bytes_mode:
        mode = 'wb'
        encoding = None
    with open(filename, mode, encoding=encoding) as f:
        for offset, length, next_char in encoded:
            f.write(f"{offset} {length} {next_char}\n")


def load_from_file(filename, bytes_mode=False, mode='r', encoding='utf-8'):
    encoded = []
    if bytes_mode:
        mode = 'rb'
        encoding = None
    with open(filename, mode, encoding=encoding) as f:
        for line in f:
            # Строка обрабатывается полностью, включая переносы строк
            if line.strip():  # Если строка не пустая (с пробелами или переносами)
                # Убираем лишний перенос в конце строки, сплит сохраняет символ пробела
                parts = line.strip('\n').split(' ', maxsplit=2)
                if len(parts) == 3:  # Содержит все 3 компонента
                    offset, length, next_char = parts
                    encoded.append((int(offset), int(length), next_char))
    return encoded


def compress_file(input_filename, output_filename=None):
    with open(input_filename, 'r', encoding='utf-8') as f:
        data = f.read()  # Читаем как текст
    encoded = encode(data)
    if output_filename is None:
        output_filename = input_filename
    save_to_file(encoded, output_filename)


def decompress_file(input_filename, output_filename):
    encoded = load_from_file(input_filename)
    lz77 = LZ77()
    decoded = lz77.decode(encoded)
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(decoded)


def check_result(original: str, decoded: str):
    return list(i for i, (o, d) in enumerate(zip(original, decoded)) if o != d)
