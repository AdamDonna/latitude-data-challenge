import unittest
from anonymise import AnonymiseData

class TestDataGenerator(unittest.TestCase):

    def test_first_name_consistently_anonymised(self):
        """Scenario, first_name needs to map to a new value"""
        rows = [{
            "first_name": "Adam",
            "last_name": "blogs",
            "address": "",
            "date_of_birth": "",
        }, {
            "first_name":"Adam",
            "last_name": "Joe",
            "address": "",
            "date_of_birth": "",
        }]
        anon_rows = list(AnonymiseData().anonymise_rows(rows))
        count_of_names = len(list(set(row.get("first_name") for row in anon_rows)))
        self.assertEqual(1, count_of_names)

    def test_last_name_consistently_anonymised(self):
        """Scenario, last_name needs to map to a new value"""
        rows = [{
            "first_name": "Joe",
            "last_name": "Blogs",
            "address": "",
            "date_of_birth": "",
        }, {
            "first_name":"Adam",
            "last_name": "Blogs",
            "address": "",
            "date_of_birth": "",
        }]
        anon_rows = list(AnonymiseData().anonymise_rows(rows))
        count_of_last_name = len(list(set(row.get("last_name") for row in anon_rows)))
        self.assertEqual(1, count_of_last_name)

    def test_address_consistently_anonymised(self):
        """Scenario, address needs to map to a new value"""
        rows = [{
            "first_name": "Adam",
            "last_name": "blogs",
            "address": "12 some street",
            "date_of_birth": "",
        }, {
            "first_name":"Jimmy",
            "last_name": "Joe",
            "address": "12 some street",
            "date_of_birth": "",
        }]
        anon_rows = list(AnonymiseData().anonymise_rows(rows))
        count_of_address = len(list(set(row.get("address") for row in anon_rows)))
        self.assertEqual(1, count_of_address)