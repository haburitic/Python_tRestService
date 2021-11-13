from flask import Flask, jsonify, request,make_response
from json import dumps
from flask import request

import json
from bson.json_util import dumps

from pymongo import MongoClient

import ssl

ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL

client = MongoClient('mongodb+srv://test:test@cluster0.oh46f.mongodb.net/DeportesDB', ssl_cert_reqs=ssl.CERT_NONE)

db = client.ContactDB
task=[
    {'id':'1',
    'titulo':'Hola Mundo',
    'description':'Hola Mundo'   
    },
    {'id':'2',
    'titulo':'Hola Mundo',
    'description':'Hola Mundo'   
    }

]
app = Flask(__name__)

@app.route('/todo/api/task', methods=['GET'])
def get_tasks():
    return jsonify({'task':task})

@app.route('/todo/api/task/<int:task_id>', methods=['GET'])
def get_tasksParameters(task_id):
    return jsonify({'task_id':task_id},{'task':task})

@app.route('/addcontacto', methods=['POST'])
def addcontacto():
   try:
        data =  json.loads(request.data)
        nombre = data['nombre']
        apellido = data['apellido']
        numeroDocumento = data['numeroDocumento']

        contacto= {
            'nombre':nombre ,
            'apellido': apellido,
            'numeroDocumento': numeroDocumento

        }

        db.Contacts.insert_one(contacto)
        return dumps({'message' : 'SUCCESS'},
        {'info':contacto} )


   except Exception as error:
       return dumps({'error','error'+error})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ =='__main__':
    app.run(debug=True)