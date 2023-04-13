import mysql.connector
from flask import Flask, jsonify
from db_handler import db

app = Flask(__name__)

@app.route('/uwb/<int:uwb_id>')
def get_uwb(uwb_id):

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SELECT query to fetch the book data from the database
    cursor.execute("SELECT id, name, uwb_type_id FROM uwbs WHERE id = %s", (uwb_id,))

    # Fetch the row returned by the SELECT query
    row = cursor.fetchone()

    # Close the cursor
    cursor.close()

    if row is None:
        # Return a 404 error if the book is not found
        return jsonify({"error": "UWB not found"}), 404

    # Convert the row to a dictionary and return as JSON
    book = {"id": row[0], "name": row[1], "uwb_type_id": row[2]}
    return jsonify(book)


@app.route('/uwbs')
def get_uwbs():

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SELECT query to fetch the books data from the database
    cursor.execute("SELECT id, name, uwb_type_id FROM uwbs")

    # Fetch all the rows returned by the SELECT query
    rows = cursor.fetchall()

    # Close the cursor and database connections
    cursor.close()
    db.close()

    # Convert the rows to a list of dictionaries and return as JSON
    uwbs = []
    for row in rows:
        uwbs.append({
            "id": row[0],
            "name": row[1],
            "uwb_type_id": row[2]
        })

    return jsonify(uwbs)


if __name__ == '__main__':
    app.run(debug=True)
