from pathlib import Path
from itertools import chain

FOLDER_PATH = Path('D:/Files')

SUBFOLDER_NAME_TO_EXTENSIONS = {
    'video': ('mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpg', 'mpeg', 'm4v', 'h264', 'webm'),
    'audio': ('mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'wma'),
    'image': ('jpg', 'png', 'bmp', 'jpeg', 'svg', 'tif', 'tiff', 'webp'),
    'archive': ('zip', 'rar', '7z', 'z', 'gz', 'pkg', 'deb'),
    'text': ('pdf', 'txt', 'doc', 'docx', 'rtf', 'odt'),
    'spreadsheet': ('xlsx', 'xls', 'xlsm'),
    'presentation': ('pptx', 'ppt'),
    'book': ('fb2', 'epub', 'mobi'),
    'gif': ('gif',),
    'another': ('psd',),
}


SUBFOLDER_NAMES = tuple(SUBFOLDER_NAME_TO_EXTENSIONS.keys())
EXTENSIONS = tuple(chain.from_iterable(
    (SUBFOLDER_NAME_TO_EXTENSIONS.values())))


def get_subfolder_name_by_extension(extension: str) -> str:
    for subfolder_name, tuple_of_extensions in SUBFOLDER_NAME_TO_EXTENSIONS.items():
        if extension in tuple_of_extensions:
            return subfolder_name
