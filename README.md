# us-zip-census

`uszipcensus` is a lightweight Python package that converts US ZIP codes into their corresponding Census Division and Region names.

GitHub Repo: https://github.com/kris-szczepaniak/us-zip-census

## Features

- Works with both 5-digit or 5+4-digit format.
- `Division Mapping`: Converts a valid ZIP code to its corresponding Census Division.
- `Region Mapping`: Maps a valid ZIP code to its Census Region.

## Installation

Install uszipcensus via pip:

```bash
pip install uszipcensus
```

# Usage
Import the package and call the functions directly:

```python
import uszipcensus

division = uszipcensus.zip_to_division("12345")
region = uszipcensus.zip_to_region("12345")

print("Division:", division)
print("Region:", region)
```

# API Overview
- `zip_to_division(zip_code: str) -> str`\
Validates the ZIP code and returns the name of the Census Division.
Raises a ValueError if the ZIP code is invalid or if the division cannot be determined.

- `zip_to_region(zip_code: str) -> str`\
Converts a ZIP code to its Census Region by first mapping it to a division.
Raises a ValueError if the region cannot be determined.

# Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.

# Acknowledgements
This package uses a great package `zipcodes`.\
Please find it here: https://pypi.org/project/zipcodes/
