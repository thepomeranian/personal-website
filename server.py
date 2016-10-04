from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request

app = Flask(__name__, static_url_path = "/static", static_folder = "static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/blog')
def blog():
  return render_template('blog.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
