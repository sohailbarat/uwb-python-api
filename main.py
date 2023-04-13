import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/books')
def get_books():
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )

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
