import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

# Returns a True or False depending on if the number is a prime number
def is_prime(number):
    # Conditions for number to be prime
    if (number < 2):
        return False
    if (number == 2):
        return True 
    if (number % 2 == 0) and number > 2:
        return False 
    
    # Checks for factors of number by dividing number by factors in the range
    # of 3 - root of the number.
    root_of_number = number ** 2 
    for i in range(3, root_of_number):
        if (number % i == 0):
            return False 
        return True
    
# Returns True or False depending on if number is perfect.
def is_perfect(number):
    sum = 0
    for i in range(1, (number-1)):
        if (number % i == 0):
            sum += i
            
    if (sum == number):
        return True 
    return False

# Checks if number is armstrong number
def is_armstrong(number):
    sum_of_power = 0
    number_string = number
    number_of_digits = len(number_string) 
    
    for index in range(number_of_digits):
        sum_of_power += int(number_string[index]) ** len(number_string)
        
    if (sum_of_power == number):
        return True 
    return False

# Returns an array containing properties of the number.
def get_properties(number):
    properties = []
    
    if is_armstrong:
        properties.append("armstrong")
    if (number % 2 == 0):
        properties.append("even")
    else: 
        properties.append("odd")
    
    return properties

def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum
        
# Route that returns data.
@app.route('/api/classify-number')
def index():
    try:
        number = request.args.get("number")
        return jsonify({
            "number": number,
            "is_prime": is_prime(int(number)),
            "is_perfect": is_perfect(int(number)),
            "properties": get_properties(int(number)),
            "digit_sum": sum_digits(number),
            "fun_fact": requests.get(f"http://numbersapi.com/{number}/trivia").text
        }), 200
    except ValueError:
        return jsonify({"number":number, "error":True}), 400
    
if __name__ == "__main__":
    app.run(debug=True)