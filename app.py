from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import smtplib
load_dotenv()
import json
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build

# I Initialize Flask app and specify the template folder as the main folder
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
