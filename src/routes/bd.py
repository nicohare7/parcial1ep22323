from src import app
from src.controllers.basedb import DatabaseController
from flask import make_response, jsonify, request
databaseController = DatabaseController()
@app.route('/database', methods=['GET'])
def databaseList():
    dbs = databaseController.list()
    return make_response(jsonify(dbs), 200)
@app.route('/database', methods=['POST'])
def databaseCreate():
    base_datos = request.json['base_datos']
    databaseController.create(base_datos)
    return make_response('database created successfully', 201)
@app.route('/tables/<basedb>', methods=['GET'])
def tableList(basedb):
    tables = databaseController.search(basedb)
    return make_response(jsonify(tables), 200)
