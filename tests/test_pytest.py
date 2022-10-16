import pytest
import unittest
from parameterized import parameterized
from secretary_program import check_document_existance, get_doc_owner_name, append_doc_to_shelf, delete_doc
from Yndex_API import create_folder

# def test_check_document_existance():
#     ressult = check_document_existance("2207 876234")
#     assert True == ressult
#
# def test_get_doc_owner_name():
#     result = get_doc_owner_name("2207 876234")
#     assert "Василий Гупкин" == result
#
# def test_append_doc_to_shelf():
#     result = append_doc_to_shelf("876234", '5')
#     assert ["876234"] == result
#
# def test_delete_doc():
#     result = delete_doc("2207 876234")
#     assert "2207 876234", True == result


FIXTURES = [
    ("new_folder", 409)
]

class Testfunctions(unittest.TestCase):
    def test_create_folder1(self):
        result = create_folder('new_folder')
        self.assertEqual(201, result)

    @parameterized.expand(FIXTURES)
    def test_create_folder2(self, path, ex_result):
        result = create_folder(path)
        self.assertEqual(ex_result, result)


