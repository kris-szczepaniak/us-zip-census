"""
Tests main module's functionality
"""

import pytest

from uszipcensus.main import UsZipCensus

zip_code_test_data_negative = [
    "1234", "12345-12", "09999-097"
]

@pytest.mark.parametrize("zip_code", zip_code_test_data_negative)
def test_zip_code_validation_failure(zip_code: str):
    """
    Tests if validation raises expected errors
    """
    with pytest.raises(ValueError):
        UsZipCensus._validate_zip_code(zip_code)


def test_zip_code_type_failure():
    """
    Tests if validation raises expected errors
    """
    with pytest.raises(TypeError):
        UsZipCensus._validate_zip_code(12345)


zip_code_test_data_positive = [
    "99950", "00501", "00501-4412"
]

@pytest.mark.parametrize("zip_code", zip_code_test_data_positive)
def test_zip_code_validation_success(zip_code: str):
    """
    Tests if validation is successful
    """
    assert UsZipCensus._validate_zip_code(zip_code) is True


def test_zip_to_division_info_not_found(mocker):
    """
    Test UsZipCensus.zip_to_division when zip_info not found
    """
    mocker.patch('src.main.UsZipCensus._validate_zip_code', return_value=True)

    with pytest.raises(ValueError):
        UsZipCensus.zip_to_division(zip_code="99999")

def test_zip_to_division_state_not_found(mocker):
    """
    Test UsZipCensus.zip_to_division when state not found
    """
    mocker.patch('src.main.UsZipCensus._validate_zip_code', return_value=True)
    mocker.patch('src.main.matching', return_value=[{}])

    with pytest.raises(ValueError, match="State not found"):
        UsZipCensus.zip_to_division(zip_code="99999")

def test_zip_to_division_division_not_found(mocker):
    """
    Test UsZipCensus.zip_to_division when division not found
    """
    mocker.patch('src.main.UsZipCensus._validate_zip_code', return_value=True)
    mocker.patch('src.main.matching', return_value=[{'state': 'XYZ'}])
    mocker.patch.dict('src.main.state_to_division', {})

    with pytest.raises(ValueError, match="Division not found"):
        UsZipCensus.zip_to_division(zip_code="99999")

division_data_positive = [
    ("99950", "Pacific"),
    ("00501", "Middle Atlantic"),
    ("00501-4412", "Middle Atlantic")
]

@pytest.mark.parametrize("zip_code, division", division_data_positive)
def test_zip_to_division_division_success(zip_code: str, division: str):
    """
    Test UsZipCensus.zip_to_division when zip valid
    """
    assert UsZipCensus.zip_to_division(zip_code) == division

def test_zip_to_region_region_not_found(mocker):
    """
    Test UsZipCensus.zip_to_region when region not found
    """
    mocker.patch('src.main.UsZipCensus._validate_zip_code', return_value=True)
    mocker.patch('src.main.UsZipCensus.zip_to_division', return_value='Mock_Division')

    with pytest.raises(ValueError, match="Region not found"):
        UsZipCensus.zip_to_region(zip_code="99999")

region_data_positive = [
    ("99950", "West"),
    ("00501", "Northeast"),
    ("00501-4412", "Northeast")
]

@pytest.mark.parametrize("zip_code, region", region_data_positive)
def test_zip_to_region_success(zip_code: str, region: str):
    """
    Test UsZipCensus.zip_to_region when region found
    """
    assert UsZipCensus.zip_to_region(zip_code) == region
