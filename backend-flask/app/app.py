from flask import Flask, request, jsonify, make_response
import sqlite3
import uuid
import datetime
from functools import wraps
import database as db


app = Flask(__name__)


#secret key to protect program
app.config['SECRET_KEY']= 'sdy2874sajhdiuwiqhe83gfhewghweguygygey6fg2738g436grt438'

def token_required(public_id):
    conn = db.create_connection('api.db')
    data = db.check_public_id(conn,public_id)
    
    return data

def role_user(public_id):
    conn = db.create_connection('api.db')
    data=db.check_user_role(conn,public_id)

    return data

@app.route('/product/<public_id>', methods=['GET'])
def api_all_data(public_id):

    check_user = token_required(public_id)
    if check_user==0:
        return jsonify({'message' : 'Token is missing!'}), 401
    
    else:
        conn = db.create_connection('api.db')
        data = db.select_all_product_to_json(conn)
        return data,200

@app.route('/product/<public_id>/<id_product>', methods=['GET'])
def api_one_data(public_id,id_product):

    check_user = token_required(public_id)
    if check_user==0:
        return jsonify({'message' : 'Token is missing!'}), 401
    
    else:
        conn = db.create_connection('api.db')
        data = db.select_specific_product_to_json(conn,id_product)
        return data,200

@app.route('/product/<public_id>', methods=['POST'])
def insert_to_api(public_id):

    check_user = token_required(public_id)
    if check_user!='admin':
        return jsonify({'message' : 'You do not have authorization!'}), 403
    
    else:
        data = request.get_json()
        new_product = (data['product_name'],data['product_type'],data['created'],data['price'])
        conn = db.create_connection('api.db')
        proses_insert = db.insert_product(conn, new_product)
        if proses_insert == True:
            return jsonify({'message' : 'Data has been inserted'}),200
        else:
            return jsonify({'message' : 'Data can not be insert'}),500

@app.route('/product/<public_id>', methods=['PUT'])
def update_to_api(public_id):

    check_user = token_required(public_id)
    if check_user!='admin':
        return jsonify({'message' : 'You do not have authorization!'}), 403
    
    else:
        data = request.get_json()
        update_product = (data['product_name'],data['product_type'],data['created'],data['price'],data['id_product'])
        conn = db.create_connection('api.db')
        proses_update = db.update_product(conn, update_product)
        if proses_update == True:
            return jsonify({'message' : 'Data has been updated'}),200
        else:
            return jsonify({'message' : 'Data can not be update'}),500
        

@app.route('/product/<public_id>', methods=['DELETE'])
def delete_to_api(public_id):

    check_user = token_required(public_id)
    if check_user!='admin':
        return jsonify({'message' : 'You do not have authorization!'}), 403
    
    else:
        data = request.get_json()
        delete_product = (data['id_product'])
        conn = db.create_connection('api.db')
        proses_delete = db.delete_product(conn, delete_product)
        if proses_delete == True:
            return jsonify({'message' : 'Data has been deleted'}),200
        else:
            return jsonify({'message' : 'Data can not be delete'}),500


if __name__ == "__main__":
    app.run(debug=True)