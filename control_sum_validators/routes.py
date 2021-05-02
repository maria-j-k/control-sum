from flask import jsonify

from control_sum_validators import app
from control_sum_validators.pesel_validator import pesel_validator

@app.route('/pesel/<p>/<g>', methods=['GET'])
def pesel(p, g):
    return jsonify({'result':  pesel_validator(p, g)})
