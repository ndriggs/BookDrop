import json
import os
from flask import Flask
from sqlalchemy import create_engine, MetaData, Table, select, text
import pymysql

app = Flask(__name__)

@app.route('/')


def get_appraisal_value(isbn):
    engine = create_engine('mysql+pymysql://root:feelingcloudy@127.0.0.1/appraisal_database')
    connection = engine.connect()
    metadata = MetaData()
    appraisal_values = Table('appraisal_values', metadata, autoload=True, autoload_with=engine)
    #query = text("SELECT 'Appraisal Price' FROM appraisal_values WHERE 'ASIN' = '" + isbn + "'")
    query = text("SELECT * FROM appraisal_values")
    prelim_results = connection.execute(query)
    results = prelim_results.fetchall()
    print(results)
    print(len(results))
    return json.dumps({'result': [dict(row) for row in results]})

if __name__ == '__main__':
    get_appraisal_value('9782947687')
