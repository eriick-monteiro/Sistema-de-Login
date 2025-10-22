from flask import Flask

# Loading Environment Variables
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


# Creating App Instance
app = Flask(__name__)
app.secret_key = SECRET_KEY


# Loading all Routes from Views
from views import *


# Starting
if __name__ == "__main__":
    app.run(debug=True)