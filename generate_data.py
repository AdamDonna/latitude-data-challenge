from faker import Factory
import csv
import argparse

class Generatedata:

    def __init__(self, num_rows=100, filename="mydata.csv"):
        """Determine how we want to configure the csv file"""
        self.faker  = Factory.create()
        self.num_rows = num_rows
        self.filename = filename

    def generate_row(self):
        """Generate a row of fake data for our csv"""
        return {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "address": self.faker.address(),
            "date_of_birth": self.faker.date_of_birth(),
        }
    
    def write_file(self):
        """Write the csv file"""
        with open(self.filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["first_name", "last_name", "address", "date_of_birth"])
            writer.writeheader()
            total_rows = 0
            while(total_rows <= self.num_rows):
                writer.writerow(self.generate_row())
                total_rows += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a dataset of user data.')
    parser.add_argument('output_file_name', help='File to be created')
    parser.add_argument('num_rows', type=int, help='Number of rows to be generated')

    args = parser.parse_args()
    
    fileGenerator = Generatedata(num_rows=args.num_rows, filename=args.output_file_name)
    fileGenerator.write_file()
    print(f"File created with {args.num_rows} at {args.output_file_name}")