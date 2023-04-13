import mysql.connector
from flask import Flask, jsonify
from db_handler import db

app = Flask(__name__)

@app.route('/books/<int:book_id>')
def get_book(book_id):

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SELECT query to fetch the book data from the database
    cursor.execute("SELECT id, title, author FROM books WHERE id = %s", (book_id,))

    # Fetch the row returned by the SELECT query
    row = cursor.fetchone()

    # Close the cursor
    cursor.close()

    if row is None:
        # Return a 404 error if the book is not found
        return jsonify({"error": "Book not found"}), 404

    # Convert the row to a dictionary and return as JSON
    book = {"id": row[0], "title": row[1], "author": row[2]}
    return jsonify(book)


@app.route('/books')
def get_books():

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SELECT query to fetch the books data from the database
    cursor.execute("SELECT id, title, author FROM books")

    # Fetch all the rows returned by the SELECT query
    rows = cursor.fetchall()

    # Close the cursor and database connections
    cursor.close()
    db.close()

    # Convert the rows to a list of dictionaries and return as JSON
    books = []
    for row in rows:
        books.append({
            "id": row[0],
            "title": row[1],
            "author": row[2]
        })

    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)
