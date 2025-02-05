# Introduction
An api that returns information about a given number in JSON format. 

## How to run the project 
Create and activate a python virtual environment.
On windows:
```
    python -m venv env
    . env\Scripts\activate
```

On Linux:
```
    python3 -m venv env
    source env/bin/activate
```

Install the applications dependencies from requirements.txt

```pip install -r requirements.txt``` 

Then in the project `/src` directory run.

    python server.py

This will start the server listening at 'http://localhost:5000'. To access the resource required for this assignment make a GET request to the endpoint 'http://localhost:5000/classify-number'. With the number provided as an argument. For example `?number=371`.

## Documentation 

```GET /classify-number?number=371```

An endpoint for accessing the 'me' resource object. Make a GET request to the  `/me` URL to get a JSON response containing email, current_datetime, and github url linking to this repository.


## Example usage 

1. Clone the project from 'https://github.com/ubterko/hng12-stage-one-backend'. And proceed to open a terminal at the directory of the app in your machine. 

2. Install the projects dependencies by entering the following in the apps main directory where we have the requirements.txt file.

   ```pip install -r requirements.txt```

3. Wait for the installations to complete then change directory into the `/src` folder in the project main directory run the following commands

     ```python server.py```

    This will start the server listening at 'http://localhost:5000'. 

4. To access the resource required for this assignment make a GET request to the endpoint 'http://localhost:5000/api/classify-number'. 

    This will return a json format data containing 'email', 'current_datetime' and the github url link to this project.

```
{ 
    "number": 2,
    "is_prime": true,
    "is_perfect": false,
    "properties": ["armstrong", "even"],
    "digit_sum": sum_digits(number),
    "fun_fact": "2 is the first magic number in physics."
}
```

## Looking to hire Python developers? 
Pick from our list of competent backend developers. Click below to find our list of Python developers for your projects. 

https://hng.tech/hire/python-developers
