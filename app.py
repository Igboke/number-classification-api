from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_perfect(n):
    if n <= 1:
        return False
    sum_div = 1
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_div += i
            complement = n // i
            if complement != i:
                sum_div += complement
    return sum_div == n

def is_armstrong(n):
    if n < 0:
        return False
    digits = list(str(n))
    num_digits = len(digits)
    total = sum(int(d)**num_digits for d in digits)
    return total == n

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def get_fun_fact(number):
    try:
        url = f"http://numbersapi.com/{number}/math"
        response = requests.get(url, params={'json': True})
        response.raise_for_status()
        data = response.json()
        return data.get('text', 'No fun fact available.')
    except requests.exceptions.RequestException:
        return 'No fun fact available.'

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_param = request.args.get('number')
    if not number_param:
        return jsonify({"number": None, "error": True}), 400
    try:
        number = int(number_param)
    except ValueError:
        return jsonify({"number": number_param, "error": True}), 400

    is_prime = check_prime(number)
    is_perfect = check_perfect(number)
    armstrong = is_armstrong(number)
    digit_sum_val = digit_sum(number)
    parity = 'even' if number % 2 == 0 else 'odd'

    properties = []
    if armstrong:
        properties.append('armstrong')
    properties.append(parity)

    fun_fact = get_fun_fact(number)

    response = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum_val,
        "fun_fact": fun_fact
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=False)