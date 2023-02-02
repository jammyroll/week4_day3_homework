from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import book_repository
import repositories.book_repository as book_repository
from repositories import author_repository
import repositories.author_repository as author_repository
from models.book import Book

books_blueprint = Blueprint('books',__name__)
@books_blueprint.route('/books')

def books():
    books = book_repository.select_all()
    return render_template("books/index.html", list_of_books = books)
