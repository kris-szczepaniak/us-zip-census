"""
Provides utility methods for converting US ZIP codes into corresponding
Census Divisions and Regions.
"""

from .main import UsZipCensus

zip_to_division = UsZipCensus.zip_to_division
zip_to_region = UsZipCensus.zip_to_region

__all__ = ["zip_to_division", "zip_to_region"]