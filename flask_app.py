"""
Put your Flask app code here.
"""
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return render_template('form.html')

def valid_login(name, age):
    valid_name = 'william'
    valid_age = '18'
    if name == valid_name and age == valid_age:
        return True
    return False

def log_the_user_in(name, age):
    return render_template('success.html', name=name, age=age, ninja='Patrick Huston')

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['name'],
                       request.form['age']):
            return log_the_user_in(request.form['name'],
                                   request.form['age'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('form.html', error=error)


if __name__ == '__main__':
    app.run()
