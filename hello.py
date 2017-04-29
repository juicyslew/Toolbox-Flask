"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "I'm Mr. MeeSeeks! Look at me!"

if __name__ == '__main__':
    app.run()
