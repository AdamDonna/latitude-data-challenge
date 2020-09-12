import argparse
import csv
from faker import Factory 
from collections import defaultdict

class AnonymiseData:

    def __init__(self, input_file="tmp.csv", output_file="anonymised.csv"):
        self.input_file = input_file
        self.output_file = output_file

    def anonymise_rows(self, rows):
        """
        Pass in all the rows and yeilds the next anonymised row
        Default dicts handle anonymising the same values correctly so statistically the same values appear the same amount
        We yield so we dont generate and keep everythign in memory at the same time
        """
        faker  = Factory.create()
        first_name  = defaultdict(faker.first_name)
        last_name  = defaultdict(faker.last_name)
        address  = defaultdict(faker.address)

        for row in rows:
            row['first_name']  = first_name[row['first_name']]
            row['last_name'] = last_name[row['last_name']]
            row['address']  = address[row['address']]
            yield row
        

    def write_file(self):
        """
        Actually does the anonymisation of rows and owns writing the output file
        """
        field_names = ["first_name", "last_name", "address", "date_of_birth"]
        with open(self.input_file, 'r') as read_data:
            with open(self.output_file, 'w') as anonymised_data:
                reader = csv.DictReader(read_data)
                writer = csv.DictWriter(anonymised_data, fieldnames=field_names)
                for idx, row in enumerate(self.anonymise_rows(reader)):
                    if idx> 0 and idx%10000 == 0:
                        print(f"{idx} rows anonymised to file")
                    writer.writerow(row)
           
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Anonymise a dataset.')
    parser.add_argument('input_file', help='Data to be m')
    parser.add_argument('output_file_name', help='File to be created')

    args = parser.parse_args()
    
    fileGenerator = AnonymiseData(input_file=args.input_file, output_file=args.output_file_name)
    fileGenerator.write_file()
    print(f"File anonymised. Output at {args.output_file_name}")