from flask import Flask, render_template, request, redirect
from repositories import author_repository 
from repositories import book_repository
from flask import Blueprint
from models.book import Book
import pdb

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
@books_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template('books/new.html', authors = authors)


# CREATE
# POST '/books'
@books_blueprint.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    publisher = request.form['publisher']
    genre = request.form['genre']

    author = author_repository.select(author_id)

    book = Book(title, genre, publisher, author)

    book_repository.save(book)
    return redirect('/books')

# SHOWO
# GET '/books/<id>'
@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template('/books/show.html', book = book)



# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route('/books/<id>/edit')
def edit(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book = book, authors = authors)

# UPDATE
# PUT '/books/<id>'
@books_blueprint.route('/books/<id>', methods=["POST"])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, genre, publisher, author, id)
    # pdb.set_trace()
    book_repository.update(book)
    return redirect('/books')



# DELETE
# DELETE '/books/<id>'
@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

