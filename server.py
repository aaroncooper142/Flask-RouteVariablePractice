from flask import Flask
import random

correct_number = random.randint(0,9)
print(correct_number)

app = Flask(__name__)



@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif width=200>'


@app.route("/<int:number>")
def enter_number(number):
    if number < correct_number:
        return '<h1 style="color: red">Too low, try again</h1>' \
               '<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif width=200>'
    elif number > correct_number:
        return '<h1 style="color: purple">Too High, try again</h1>' \
               '<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif width=200>'
    elif number == correct_number:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif width=200>'
    else:
        return 'Error'


if __name__ == "__main__":
    app.run(debug=True) #debug=True will prompt some documentation if there are any errors
