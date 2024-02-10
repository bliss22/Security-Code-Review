# app.py

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Database initialization
conn = sqlite3.connect('comments.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT)''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    
    # Vulnerability: SQL Injection
    c.execute("INSERT INTO comments (comment) VALUES ('%s')" % comment)
    conn.commit()
    
    return "Comment submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
