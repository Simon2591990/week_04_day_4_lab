from flask import Flask, render_template, request, redirect
from repositories import author_repository 
from repositories import book_repository
from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/')
def home():
    return render_template('/index.html')

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

# NEW
# GET '/books/new'

# CREATE
# POST '/books'

# SHOWO
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'

