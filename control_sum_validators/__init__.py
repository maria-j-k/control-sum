from flask import Flask

app = Flask(__name__)

from control_sum_validators import routes, pesel_validator
