import requests
import math 

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource

# Initialize flask and flask extensions
app = Flask(__name__)
api = Api(app)
cors = CORS(app)

# Returns a True or False depending on if the number is a prime number
def is_prime(number):
    # Conditions for number to be prime
    if (number < 2):
        return False
    if (number == 2):
        return True 
    if (number % 2 == 0) and (number != 2):
        return False 
    
    root_of_number = math.sqrt(number)
    #   Loop from 3 to square root of number.
    for i in range(3, int(root_of_number)):
        # Check only odd numbers
        if (number % 2 != 0):
            # If number is divisible by any return False
            if (number % i == 0) :
                return False 
    return True
    
# Returns True or False depending on if number is perfect.
def is_perfect(number):
    sum = 0
    for i in range(1, (number-1)):
        if (number % i == 0):
            sum += i
    # Number is perfect if equal to the sum of its factors.
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

# Returns the sum of digits in a number
def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum
        
# Resource class for the api       
class Number(Resource):
    def get(self):
        try:
            number = request.args.get("number")
            is_prime_number = is_prime(int(number))
            is_perfect_number = is_perfect(int(number))
            numbers_properties = get_properties(int(number))
            numbers_digit_sum = sum_digits(number)
            numbers_fun_fact = requests.get(f"http://numbersapi.com/{number}/math").text
        
            return {
                "number":number,
                "is_prime":is_prime_number,
                "is_perfect":is_perfect_number ,
                "properties":numbers_properties,
                "digit_sum":numbers_digit_sum,
                "fun_fact":numbers_fun_fact
            }, 200
            
        except ValueError:
            error=True
            
            return {
                "number":number, 
                "error":error
            }, 400 

api.add_resource(Number, '/api/classify-number') 
    
if __name__ == "__main__":
    app.run(debug=True)