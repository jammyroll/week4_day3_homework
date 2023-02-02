from db.run_sql import run_sql

from models.author import *
from models.book import *

def save(author):
    sql = "INSERT INTO authors (first_name, last_name,age,alive) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [author.first_name,author.last_name,author.age,author.alive]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors=[]
    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'],row['last_name'],row['age'],row['alive'],row['id'])
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = 'SELECT * FROM authors WHERE id = %s'
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        author = Author(result['first_name'],result['last_name'],result['age'],result['alive'],result['id'])
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM author WHERE id = %s"
    values = [id]
    run_sql(sql,values)


def update(author):
    sql = 'UPDATE authors SET (first_name, last_name, age, alive) = (%s,%s,%s,%s) WHERE id = %s'
    values = [author.first_name,author.last_name,author.age,author.alive,author.id]
    run_sql(sql,values)

def books(author):
    books = []
    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql,values)

    for row in results:
        book = Book(row['title'],row['year'],row['description'],row['author'],row['read'],row['id'])
        books.append(book)
    return books