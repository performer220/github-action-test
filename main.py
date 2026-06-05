import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, GitHub Actions and Dependabot!'

if __name__ == '__main__':
    app.run(debug=True)
