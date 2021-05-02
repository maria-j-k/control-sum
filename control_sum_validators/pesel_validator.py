def leap(year):
    '''
    Function checks if a year is a leap year.
    Accepts: 
        integer: four digits integer representing year.
    Returns: 
        boolean: True if year is a leap year, False otherwise.
    '''
    return (not year % 4 and  year % 100) or not year % 400

def check_control_sum(pesel):
    '''
    Checks if the pesel number is correct by checking control digit.
    Accepts: 
        string representing PESEL number.
    Returns: 
        boolean: True if PESEL is correct, False otherwise
    '''
    weights = list('1379137913')
    control = int(pesel[-1])
    products_sum = sum(int(item[0]) * int(item[1]) for item in zip(pesel[:-1], weights))
    res =  10 - (products_sum % 10)
    return control == res

def parse_date(pesel):
    '''
    Fuction extracting form PESEL number date of birth.
    Accepts: 
        string: PESEL number
    Returns: 
        tuple of integers: year, month, day
    '''
    day = int(pesel[4:6])
    month = int(pesel[2:4])
    year = int(pesel[:2])
    
    century, month = month // 20, month %20

    if month < 1 or month > 12:
        month == 0
    if century == 0:
        year = year + 1900
    if century == 1:
        year += 2000
    elif century == 2: 
        year  += 2100
    elif century == 3:
        year += 2200
    
    return(year, month, day)

def verify_date(pesel):
    '''
    Function checking if the date is correct in regards of days in month, the number of month etc.
    Accepts: string PESEL
            
    Returns: tuple of integers representing year, month and day. For each input if invalid returs 0.
    '''
    year, month, day = parse_date(pesel)
   
    if not (year and month and day) or month > 12:
        return 0, 0, 0
    shorter = [4,6,9,11]
    longer = [1,3,5,7,8,10,12]

    if month == 2:
        last_day = 29 if leap(year) else 28
        if day > last_day:
            day = 0
    elif month in shorter and day > 30:
        month = 0
    elif month in longer and day > 31:
        month = 0
    return year, month, day

def verify_pesel(pesel, gender):
    '''
    Function checking if a PESEL number is valid. 
    Accepts: 
        tuple of strings:
                PESEL 
                "f" or "m" for gender
    Returns: boolean
    '''
    g = int(pesel[-2])
    g = 'f' if not g % 2 else 'm'
    if not check_control_sum(pesel):
        return False
    year, month, day = verify_date(pesel)
    if year and month and day:
        if g == gender.lower():
            return True
    return False

def pesel_validator(pesel, gender):
    '''
    Function checks first validity of the input (it's length and type) and passes input to validating functions.
    Accepts: tuple of string (PESEL and gender)
    Returns: string evaluating validity of input.
    '''
    if gender.lower() not in ['f', 'm']:
        return 'Please enter a correct gender symbol: "f" for female, "m" for male.'
    if len(pesel) != 11 or not pesel.isdigit():
        return 'Please enter a correct number.'
    result = verify_pesel(pesel, gender)
    if result:
        return 'Pesel is valid.'
    return 'Pesel is not valid.'


p = '88023000465' # pesel z poprawną sumą kontrolną, ale z niepoprawną datą
