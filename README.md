# My-First-Flask-Application
This is my first Flask application that simply prints out a message "Hello World" when executed.

## 1. First set up the project as follows: 
Download and install Visual Studio 2019 or Visual Studio 2022 
#
Download the zipped folder and unzip it OR clone the repository to your local machine
#
Open the folder from within Visual Studio 2019 or Visual Studio 2022

## 2. Confirm that your Python version is 3.7 and above:
python3 --version

## 3. Create a Python virtual environment using the following commands:
python3 -m venv venv
#
source ./venv/bin/activate

## 4. To install flask, run the following command:
pip install "Flask==2.2.2"

## 5. Start the application on one terminal using the following command:
flask --app server --debug run

## 6. View the message on another terminal using the following command:
curl -X GET -i -w '\n' localhost:5000