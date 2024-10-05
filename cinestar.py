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
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/cines")
def cines():
    cursor.callproc("sp_getCines")
    for row in cursor.stored_results():
        cines = row.fetchall()
    return render_template ("cines.html", cine = cines)



@app.route('/cine/<int:id>')
def cine(id):
   cursor.callproc('sp_getCineTarifas', (id, ))
   for data in cursor.stored_results():
      tarifas = data.fetchall()
   
   cursor.callproc('sp_getCinePeliculas', (id, ))
   for data in cursor.stored_results():
      horarios = data.fetchall()
   
   cursor.callproc('sp_getCine', (id, ))
   for data in cursor.stored_results():
      cines = data.fetchall()
   
   return render_template('cine.html', tarifas=tarifas, horarios=horarios, cines=cines, id=id)




@app.route('/peliculas/<id>')
def peliculas(id):
   id = 1 if id == 'cartelera' else 2 if id  == 'estrenos' else 0 
   if id == 0 : 
      return render_template('index.html')
   
   if id == 1:
         cursor.callproc('sp_getPeliculass')
         for data in cursor.stored_results():
            peliculas = data.fetchall()
         return render_template('peliculas.html', peliculas = peliculas)
   if id == 2:
         cursor.callproc('sp_getPeliculasEstrenoss')
         for data in cursor.stored_results():
            estrenos = data.fetchall()
         return render_template('estrenos.html', estrenos = estrenos)

@app.route('/pelicula/<int:id>')
def pelicula(id):
   #cursor.execute("select * from pelicula where id = %s", (id,))
   cursor.callproc('sp_getPelicula',(id, ))
   for data in cursor.stored_results(): 
      pelicula = data.fetchall()
   return render_template('pelicula.html', pelicula=pelicula, id = id)

   

if __name__ == "__main__" :
    app.run(debug=True)
    
    
