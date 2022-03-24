import unittest

from main import get_doc_owner_name, documents, directories, check_document_existance, sum, add_new_doc, delete_doc


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass')


# Проверка соответствия имени и номера документа:
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('3333'), "Boksha Dmitry")

# Проверка нахождения документа на заданной полке после создания
    def test_add_new_doc(self):
        shelf = '5'
        args = ['3333','license', 'Boksha Dmitry', shelf]
        add_new_doc(*args)
        check_shelf = directories[shelf]
        self.assertEqual(('3333' in check_shelf), True)

# Проверка удаления документа
    def test_delete_doc(self):
        number = '11-2'
        delete_doc(number)
        for document in documents:
            self.assertEqual((document['number'] == number), False)


