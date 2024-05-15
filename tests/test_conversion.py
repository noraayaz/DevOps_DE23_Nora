import unittest
import os
import json
import csv

class TestConversion(unittest.TestCase):

    def test_csv_columns(self):
        with open('profiles1.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            self.assertEqual(len(headers), 12)

    def test_csv_rows(self):
        with open('profiles1.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertTrue(len(rows) >= 900)

    def test_csv_properties(self):
        expected_headers = ['Givenname', 'Surname', 'Streetaddress', 'City', 'Zipcode', 'Country', 'CountryCode', 'NationalId', 'TelephoneCountryCode', 'Telephone', 'Birthday', 'ConsentToContact']
        with open('profiles1.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            self.assertEqual(headers, expected_headers)

    def test_json_rows(self):
        with open('data.json', 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            self.assertTrue(len(data) >= 900)

if __name__ == '__main__':
    unittest.main()
