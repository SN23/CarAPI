# CarAPI
This program consists of a Python file and a Dockerfile for running through Docker. 
The Python file contains a a JSON representation of a garage, with multiple cars and attributes about them. 

When run locally and with Flask installed on your computer, this file will present the car data in your web browser at 127.0.0.1:8000/cars.
To access a specific car, you can visit 127.0.0.1:8000/cars/"ID OF CAR YOU WANT"

When run through Docker, this program becomes self contained and requires no installations on a user's computer other than Docker itself.
To achieve this, you must first build the Dockerfile and then run the program through the command line.
Other than this change, the program works in exactly the same manner.
