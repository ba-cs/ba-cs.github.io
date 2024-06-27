from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)



mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
