from jinja2 import StrictUndefined
from flask import (Flask, abort, flash, Markup, redirect,
                   render_template, request, Response, session, url_for)

app = Flask(__name__, static_url_path="/static", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
