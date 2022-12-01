#Importando flask y algunos paquetes(modulos)
from flask import Flask, render_template, url_for, redirect
from datetime import datetime
from confiDB import * #Importando conexion BD

''' 
La variable __name__ se pasa como primer argumento al crear una instancia del objeto 
Flask ( una aplicación Python Flask ). En este caso, __name__ representa el nombre 
del paquete de aplicaciones y Flask lo utiliza para identificar recursos como plantillas, 
activos estáticos y la carpeta de instancias.
'''
app = Flask(__name__) #Creando la aplicacion 

#Creando mi primer Decorador o ruta para el Home
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



#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    

#Arrancando la aplicacion    
if __name__ == '__main__': 
    app.run(debug=True, port=5000) 