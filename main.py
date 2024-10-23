if __name__ == "__main__":
    # Пример использования
    original_text = "q \nbbbbq\nqertx\nqcvcv\n nb\nm"

    # Сохраним оригинальный текст для сжатия
    with open('example.txt', 'w', encoding='utf-8') as f:
        f.write(original_text)

    # Архивация текстового файла
    compress_file('example.txt', 'compressed.lz77')

    # Распаковка
    decompress_file('compressed.lz77', 'decompressed.txt')

    # Проверка результата
    with open('decompressed.txt', 'r', encoding='utf-8') as f:
        decompressed_text = f.read()

    print(original_text)  # Должно напечатать оригинальный текст
    wrong_symbols = check_result(original_text, decompressed_text)
    wrongs = ''.join(' ' if i not in wrong_symbols else '^' for i in range(len(original_text)))
    print(wrongs)
    print(decompressed_text)
    precision = 1 - len(wrong_symbols) / len(original_text)
    print(len(wrong_symbols), precision)