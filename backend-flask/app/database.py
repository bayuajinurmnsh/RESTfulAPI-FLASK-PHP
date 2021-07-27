import sqlite3
from sqlite3 import Error
from flask import jsonify

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_product_to_json(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")

    rows = cur.fetchall()
    output=[]
    for row in rows:
        product_data={}
        product_data['id_product'] =row[0] 
        product_data['name_product'] = row[1]
        product_data['type_product'] = row[2]
        product_data['created_date'] = row[3]
        product_data['price'] = row[4]
        output.append(product_data)
    return jsonify({'product' : output})

def select_specific_product_to_json(conn,id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM product WHERE id_product=?", (id,))

    rows = cur.fetchall()
    output=[]
    for row in rows:
        product_data={}
        product_data['id_product'] =row[0] 
        product_data['name_product'] = row[1]
        product_data['type_product'] = row[2]
        product_data['created_date'] = row[3]
        product_data['price'] = row[4]
        output.append(product_data)
    return jsonify({'product' : output})

def check_public_id(conn,public_id):
    cur = conn.cursor()
    data_find = cur.execute("SELECT * FROM user WHERE public_id=?", (public_id,))
    rows = cur.fetchall()
    if len(rows) > 0:
        output = []
        for row in rows:
            output.append(row[4])
        
        data=output[0]
        return data

    else:
        data=0
        return data

def insert_product(conn, tmp_data):
    
    #check data before insert

    sql = ''' INSERT INTO product(product_name,product_type,created,price)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tmp_data)
    conn.commit()
    x = conn.total_changes
    if x !=0:
        return True
    else:
        return False


def update_product(conn,tmp_data):
    
    sql = ''' UPDATE product
              SET product_name = ? ,
                  product_type = ? ,
                  created = ?,
                  price = ?
              WHERE id_product = ?'''
    cur = conn.cursor()
    cur.execute(sql, tmp_data)
    conn.commit()
    x = conn.total_changes
    if x !=0:
        return True
    else:
        return False

def delete_product(conn,id):
    
    sql = 'DELETE FROM product WHERE id_product=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    x = conn.total_changes
    if x!=0:
        return True
    else:
        return False