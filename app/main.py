from flask import Flask, request, render_template
from confiDB import * #Importando conexion BD


app = Flask(__name__) 

#Creando mi Decorador para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexión desde la función
    mycursor         = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM empleados ORDER BY nombre")
    mycursor.execute(querySQL)
    data = mycursor.fetchall() #fetchall () Obtener todos los registros
    mycursor.close() #cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    total = mycursor.rowcount
    return render_template('public/index.html', dataEmpleados = data)



if __name__ == '__main__': 
    app.run(debug=True, port=5000) 