from flask import Flask
import sqlite3

conn = sqlite3.Connection("analytics.dat")
db = conn.cursor()

db.execute("CREATE TABLE IF NOT EXISTS domains (id TEXT, domain TEXT, PRIMARY KEY (id))")
db.execute("CREATE TABLE IF NOT EXISTS visitors (id TEXT, domain TEXT, PRIMARY KEY (id), FOREIGN KEY (domain) REFERENCES domains(id))")
db.execute("CREATE TABLE IF NOT EXISTS views (id INT, visitor TEXT, url TEXT, userAgent TEXT, time INT, ipAddress TEXT, source TEXT, PRIMARY KEY (id), FOREIGN KEY (visitor) REFERENCES visitor(id))")
db.execute("CREATE TABLE IF NOT EXISTS retention (id INT, view INT, time INT, positionX INT, positionY INT, PRIMARY KEY (id), FOREIGN KEY (view) REFERENCES views(id))")
db.execute("CREATE TABLE IF NOT EXISTS clicks (id INT, view INT, time INT, text TEXT, PRIMARY KEY (id), FOREIGN KEY (view) REFERENCES views(id))")
db.execute("CREATE TABLE IF NOT EXISTS anchors (id INT, view INT, time INT, value TEXT, PRIMARY KEY (id), FOREIGN KEY (view) REFERENCES views(id))")
db.execute("CREATE TABLE IF NOT EXISTS errors (id INT, view INT, time INT, stack TEXT, PRIMARY KEY (id), FOREIGN KEY (view) REFERENCES views(id))")
conn.commit()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"