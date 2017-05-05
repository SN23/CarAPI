# CarAPI
This program consists of a Python file and a Dockerfile for running through Docker. 
The Python file contains a a JSON representation of a garage, with multiple cars and attributes about them. 

When run locally and with Flask installed on your computer, this file will present the car data in your web browser at 127.0.0.1:8000/cars.
<img src="https://github.com/SN23/CarAPI/blob/master/ScreenShot1.png">

To access a specific car, you can visit 127.0.0.1:8000/cars/"ID OF CAR YOU WANT"
<img src="https://github.com/SN23/CarAPI/blob/master/ScreenShot2.png">

When run through Docker, this program becomes self contained and requires no installations on a user's computer other than Docker itself.
To achieve this, you must first build the Dockerfile and then run the program through the command line.
Other than this change, the program works in exactly the same manner.

<h1>Installation</h1>

1. Clone or download the source code files
2. Open the terminal and navigate to the folder
3. Enter the following command docker build -t carapi . to build the image
4. Enter the command docker run -p 8000:8000 carapi to run the container 
