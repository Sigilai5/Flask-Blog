from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/post/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):
#
#     return new_review(id)

@main.route('/technology')
def technology():
    return render_template('technology.html')

@main.route('/sports')
def sports():
    return render_template('sports.html')

@main.route('/religion')
def religion():
    return render_template('religion.html')

@main.route('/post/<int:id>', methods = ['GET','POST'])
@login_required
def new_post(id):
    return new_post(id)