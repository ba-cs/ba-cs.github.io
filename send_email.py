import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587
MAIL_SERVER = 'smtp.mail.yahoo.com'
