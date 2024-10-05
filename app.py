from os import path
from pathlib import Path

from flask import Flask, render_template

template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
my_app = Flask(__name__)


@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/<page>')
def pages(page):
    return render_template(str(Path('pages')) + '/' + page.lower() + '.html')

if __name__ == "__main__":
    app.run(port=8080,debug=True)
