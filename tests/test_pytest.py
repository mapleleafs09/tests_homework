import pytest
from main import create_folder, folder_info

def setup():
    print('setup')

def teardown():
    print('teardown')

# Проверка по коду ответа
def test_create_folder():
    folder_name = 'Test_folder'
    response_code = ['<Response [201]>', '<Response [409]>']
    assert create_folder(folder_name) in response_code

# Проверка методом запроса информации о папке
def test_create_folder2():
    folder_name = 'Test_folder1'
    create_folder(folder_name)

    assert folder_info(folder_name)  != {'description': 'Resource not found.',
 'error': 'DiskNotFoundError',
 'message': 'Не удалось найти запрошенный ресурс.'}
