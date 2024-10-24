import subprocess
import sys
from lzma import compress_file, decompress_file
try:
    import click
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "click"])


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-d', '--decode', is_flag=True, help='Декодировать файл')
@click.option('-e', '--encode', is_flag=True, help='Закодировать файл')
def cli(filename, decode, encode):
    """Программа для кодирования и декодирования файлов."""
    if decode and encode:
        click.echo("Ошибка: Нельзя одновременно кодировать и декодировать файл.")
        return

    if not decode and not encode:
        click.echo("Ошибка: Необходимо указать режим работы (-d для декодирования или -e для кодирования).")
        return

    if encode:
        compress_file(filename)
        click.echo(f'Файл {filename} успешно декодирован и сохранен как {filename.split(".")[0]}.lz77')
    else:
        decompress_file(filename)
        click.echo(f'Файл {filename} успешно закодирован и сохранен как {filename.split(".")[0]}_decoded.{filename.split(".")[1]}')

if __name__ == '__main__':
    cli()