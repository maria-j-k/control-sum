# control-sum
Simple api to check validity of PESEL, Polish personal indetification number

### how to run
clone the repository

instal from requirements.txt

export FLASK_APP=control_sum for Unix-based system or set FLASK_APP=control_sum on Windows

### usage
endpoint: 

_/pesel/\<p\>/\<g\>_

where 'p' is a string representing PESEL number and 'g' is a character representing gender: 'f' for female, 'm' for male.

### returned value

String evaluating validity of PESEL number.

*PESEL is valid* for valid PESEL number.

*Please enter a correct gender symbol: "f" for female, "m" for male.* or *Please enter a correct number.* if the input is incorrect.

*PESEL is not valid* if input is correct, but the number doesn't pass validation.
