from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(
    host='srv1467.hstgr.io', 
    user='u719737586_cinestar', 
    password='Senati2024@', 
    database='u719737586_cinestar')


cursor = cnx.cursor(dictionary=True)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/cines")
def cines():
    cursor.callproc("sp_getCines")
    for row in cursor.stored_results():
        cines = row.fetchall()

    return render_template ("cines.html", cines = cines)

if __name__ == "__main__" :
    app.run(debug=True)
    
    