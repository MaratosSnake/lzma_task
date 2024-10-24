class File:
    def __init__(self, filename: str):
        self.full_file_name = filename
        self.file_name, self.file_ext = filename.split('.', maxsplit=1)

    def file_name_with_other_ext(self, ext: str):
        return f'{self.file_name}.{ext}'

    def get_decoded_file_name(self, adding='_decoded', ext='txt'):
        return f'{self.file_name}{adding}.{ext}'
