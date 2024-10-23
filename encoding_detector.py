def is_binary_file(file_path, chunk_size=1024):
    with open(file_path, 'rb') as file:
        chunk = file.read(chunk_size)
        if b'\x00' in chunk:  # Проверяем на наличие нулевых байтов
            return True
        return any(char < 32 and char != 9 and char != 10 and char != 13 for char in chunk)