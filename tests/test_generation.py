import unittest 
import os.path
from tempfile import TemporaryDirectory
from generate_data import Generatedata

class TestDataGenerator(unittest.TestCase):

    def test_generator(self):
        """Generate row of data in expected format"""
        g = Generatedata()
        row = g.generate_row()
        self.assertEqual(list(row.keys()), ["first_name", "last_name", "address", "date_of_birth"])
    
    def test_write_file(self):
        """Write a file of row data"""
        with TemporaryDirectory() as temp_dir:
            output_path = f"{temp_dir}/output.csv"
            g = Generatedata(10, output_path)
            g.write_file()
            self.assertTrue(os.path.exists(output_path))
