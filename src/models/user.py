from src.config.db import DB


class UserModel():
    def traerTodos(self):
        cursor = DB.cursor()
        cursor.execute('select * from users ')
        usuarios = cursor.fetchall()
        cursor.close()

        return usuarios

    def crear_usuario(self, nombre, apellido, celular, email, password):
        cursor = DB.cursor()
        cursor.execute('insert into users(nombre,apellido,celular,email,password) values(?,?,?,?,?)', (nombre, apellido, celular, email, password))        
        cursor.close()
        
        