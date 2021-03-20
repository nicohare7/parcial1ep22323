from flask import render_template, request, redirect, url_for
from src import app
from src.models.user import UserModel

@app.route('/usuarios')
def usuarios():
    usuariosModel = UserModel()
    usuarios = usuariosModel.traerTodos()   
    return render_template('usuarios/index.html', usuarios = usuarios)

@app.route('/usuarios/crear', methods =['GET', 'POST'])
def crear_usuario():
    if request.method == 'GET':       
        return render_template('usuarios/crear.html')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    celular = request.form.get('celular')
    email = request.form.get('email')
    password = request.form.get('password')    
  
    usuariosModel = UserModel()
    usuariosModel.crear_usuario(nombre, apellido, celular, email, password)
    
    return redirect(url_for('usuarios'))
  