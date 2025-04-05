"""
Provides utility methods for converting US ZIP codes into corresponding
Census Divisions and Regions.
"""

import re

from zipcodes import matching, is_real

from .helpers.divisions import state_to_division
from .helpers.regions import division_to_region


class UsZipCensus:
    """
    Provides utility methods for converting US ZIP codes into corresponding
    Census Divisions and Regions.

    This class encapsulates the functionality to:
      - Validate US ZIP codes (ensuring they are 5-digit or 4+5 digits in proper format).
      - Map a given ZIP code to its associated state using external ZIP code data.
      - Convert the state to its Census Division and then to its Census Region using
        provided mappings.

    Methods:
      zip_to_division(zip_code: str) -> str:
          Validates the provided ZIP code and returns the name of the US Census Division
          to which the ZIP code belongs. Raises a ValueError if the ZIP code is invalid,
          or if state or division information is not found.
      
      zip_to_region(zip_code: str) -> str:
          Determines the Census Region by first converting the ZIP code to its Census Division
          (using zip_to_division) and then mapping that division to the corresponding region.
          Raises a ValueError if the region cannot be determined.

    Raises:
      ValueError: If the ZIP code is not in a valid format, or if necessary data (state,
      division, or region) is missing or cannot be retrieved.

    Example:
      >>> division = USZipCensus.zip_to_division("12345")
      >>> region = USZipCensus.zip_to_region("12345+1234")
    """

    @staticmethod
    def _validate_zip_code(zip_code: str) -> bool:
        """
        Validates a US ZIP code (5-digit or 5+4-digit format).
        
        :param str zip_code: US ZIP code
        :return: ZIP code validity indicator
        :rtype: bool
        """
        if not isinstance(zip_code, str):
            raise TypeError("ZIP code must be a string")
        
        pattern = re.compile(r'^\d{5}(-\d{4})?$')
        if not pattern.match(zip_code):
            raise ValueError("US ZIP code must be either a 5-digit (12345) or 5+4 digits with a hyphen (12345-1234)")

        return is_real(zip_code)

    @staticmethod
    def zip_to_division(zip_code: str) -> str:
        """
        Converts ZIP to US Division name
        
        :param str zip_code: US ZIP code
        :return: Division, to which the ZIP code belongs
        :rtype: str
        :raises ValueError: if ZIP invalid or conversion fails
        """
        if not UsZipCensus._validate_zip_code(zip_code):
            raise ValueError(f"ZIP {zip_code} not valid.")

        zip_info = matching(zip_code)

        if not zip_info:
            raise ValueError("ZIP Code Info Not Found")

        state = zip_info[0].get('state', None)

        if not state:
            raise ValueError("State not found")

        division = state_to_division.get(state, None)

        if not division:
            raise ValueError("Division not found")

        return division

    @staticmethod
    def zip_to_region(zip_code: str) -> str:
        """
        Converts ZIP to US Census region name
        
        :param str zip_code: US ZIP code
        :return: Census reion, to which the ZIP code belongs
        :rtype: str
        :raises ValueError: if ZIP invalid
        """
        if not UsZipCensus._validate_zip_code(zip_code):
            raise ValueError(f"ZIP {zip_code} not valid.")

        division = UsZipCensus.zip_to_division(zip_code)

        region = division_to_region.get(division, None)

        if not region:
            raise ValueError("Region not found")

        return region
