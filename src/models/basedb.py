from src.conexion_bd.basedb import mysql
from flask import request, redirect, flash
class DatabaseModel():
    def lists(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW DATABASES") 
        data = cursor.fetchall()
        cursor.close()
        return data
    def create(self, base_datos):
        cursor = mysql.get_db().cursor()
        cursor.execute("CREATE DATABASE `%s`" %base_datos,)
        mysql.get_db().commit()
        cursor.close()    
    def listTables(self, basedb):
        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW TABLES FROM `%s`" %basedb)
        data = cursor.fetchall()
        cursor.close()
        return data