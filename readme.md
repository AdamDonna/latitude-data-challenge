# Latitude data code challenge

This is a proposed solution for quesiton 2 with some analysis

The original problem was 
```

### Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

```

## Installation

This solution can be run on with pipenv to be more or less reusable across environments

```bash
pipenv install
pipenv shell
```

## Tests

This project leverages pythons `unittest` package 
Test can be run with 
```bash
pipenv run python -m unittest
```

## Usage

```python
pipenv run python generate_data.py <output_location> <num_rows_required>
pipenv run python anonymise.py <input_location> <output_location>
```

## Solution analysis
: TODO