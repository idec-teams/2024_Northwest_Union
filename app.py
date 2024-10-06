from os import path
from pathlib import Path

from flask import Flask, render_template
from flask_frozen import Freezer


template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

@app.cli.command()
def freeze():
    freezer.freeze()

@app.cli.command()
def serve():
    freezer.run()

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/<page>/', defaults={'page': 'home'})  # 默认页面为 home
@app.route('/<page>.html')
def pages(page):
    return render_template('pages/' + page.lower() + '.html')

if __name__ == "__main__":
    freezer.freeze()
    # app.run(port=8080,debug=True)
