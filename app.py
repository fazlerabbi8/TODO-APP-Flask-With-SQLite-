import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS todos("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "title TEXT NOT NULL,"
        "completed INTEGER DEFAULT 0"
        ")"
    )

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)