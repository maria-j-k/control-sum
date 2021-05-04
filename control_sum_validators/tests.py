import pytest

from control_sum_validators import pesel_validator

leap_data =  [
        (1999, False), # not divisible by 4
        (2024, True), # divisible by 4 but not 100
        (1900, False), # divisible by 100, but not 400
        (2000, True),  # divisible by 400
        ]

control_sum_data = [
        ('88051301462', True),
        ('88051301431', True), 
        ('88051301862', False), 
        ('88051301432', False), 
        ]

verify_date_data = [
        ('88041400000', (1988, 4, 14)),   # data poprawna
        ('88822900000', (1888, 2, 29)), # 29 lutego, rok przestępny
        ('87222900000', (2088, 2, 0)), # 29 lutego, rok zwykły
        ('88441400000', (2188, 4, 14)), # shorter, correct
        ('88643100000', (2288, 4, 0)), # shorter, wrong
        ('88050100000', (1988, 5, 1)),   # longer, correct
        ('88053400000', (1988, 5, 0)),   # longer, wrong
        ]


parse_date_data = [
        ('88041400000', (1988, 4, 14)),   # data poprawna, wiek 20
        ('88841400000', (1888, 4, 14)), # data poprawna, wiek 19
        ('88241400000', (2088, 4, 14)), # data poprawna, wiek 21
        ('88441400000', (2188, 4, 14)), # data poprawna, wiek 22
        ('88641400000', (2288, 4, 14)), # data poprawna, wiek 23
        ('88201400000', (1988, 0, 14)),   # month < 1
        ('88054400000', (1988, 0, 14)),   # month > 12
        ]

verify_pesel_data = [
        ('88051301462', 'f', True),
        ('88051301431', 'm', True), 
        ('88051301462', 'm', False),
        ('88051301431', 'f', False), 
        ]


gender = 'Please enter a correct gender symbol: "f" for female, "m" for male.'
length =  'Please enter a correct number.'
invalid = 'PESEL is not valid'
valid = 'PESEL is valid'

validator_data = [
        ('88051301462', 'f', valid),
        ('88051301431', 'f', invalid), 
        ('880513014311', 'f', length),
        ('8805130143', 'f', length),
        ('880513014l', 'f', length),
        ('88051301462', 'g', gender),
        ]



@pytest.mark.parametrize("year, expected", leap_data)  
def test_leap(year, expected):
    return pesel_validator.leap(year) == expected


@pytest.mark.parametrize("pesel, expected", parse_date_data)  
def test_parse_date(pesel, expected):
    return pesel_validator.parse_date(pesel) == expected


@pytest.mark.parametrize("pesel, expected", verify_date_data)  
def test_verify_date(pesel, expected):
    return pesel_validator.verify_date(pesel) == expected

@pytest.mark.parametrize("pesel, expected", control_sum_data)  
def test_check_control_sum(pesel, expected):
    return pesel_validator.check_control_sum(pesel) == expected


@pytest.mark.parametrize("pesel, gender, expected", verify_pesel_data)  
def test_verify_pesel(pesel, gender, expected):
    return pesel_validator.verify_pesel(pesel, gender) == expected

@pytest.mark.parametrize("pesel, gender, expected", validator_data)  
def test_pesel_validator(pesel, gender, expected):
    return pesel_validator.pesel_validator(pesel, gender) == expected

