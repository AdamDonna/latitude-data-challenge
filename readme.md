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
I think this solution is solid for large datasets because it chunks the file into small sections to be processed for anonymisation.
I'm not across the types of distribution frameworks there are for distribution and which is best to work with this.

On my laptop it took about 48min for the 2gb file to be generated and about as long for it to be processes.

For a distributed solution I think this would work well. I think this because the `anonymise` class allows `anonymise_rows` to be called for any rows and produce the correct statistical output (same anonymisation for the same name) because the translations are on the initialisation of the class (this would get into trouble in a distributed scenarion if there were key based race conditions).
This solution would work in a distributed setup because pandas lets us chunk up the rows, this lends to the idea that we can parallelise the chunking, and since the anonymised rows can work independent of knowing the full context of the file parallel chunks would work.