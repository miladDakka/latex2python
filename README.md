# Latex2Python
## Installation
Clone the latex2code app repository from github.
```
git clone https://github.com/miladDakka/latex2python.git
```
## Setup
Begin by changing into the top directory of the application folder using the command line. This assumes you've saved the directory in the home (~) folder (change accordingly).
```
cd ~/latex2python
```
Next, ensure the environment and application variables are properly set up. In this case, the virtualenv is called "base" (change accordingly).
```
export FLASK_APP=application
export FLASK_ENV=base
```
## Usage
To run this application simply type the following command into the command line:
```
flask run
```
## Functionality
The Latex2Python web app will create a user session and store a database of valid latex equations with their corresponding "python translations". The user will begin on the homepage (math2code.html), then click the button: 
```
Create New Latex2Python Formula
```
The user is then presented with a text field, in which a valid LaTeX formula must be entered. Upon then clicking the "Add" button, the user will be automatically taken back to the homepage with the new translation added to the session's database.
