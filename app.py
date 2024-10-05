from os import path
from pathlib import Path

from flask import Flask, render_template
from flask_frozen import Freezer

@app.route('/')
def home():
    return render_template('temp/home.html')


if __name__ == "__main__":
    freezer.freeze()