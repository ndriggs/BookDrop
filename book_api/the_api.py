import json
import os
from flask import Flask, abort, make_response
from sqlalchemy import create_engine, MetaData, Table, select, text
import pymysql
import os

app = Flask(__name__)

@app.route('/<string:isbn>', methods=['GET'])
def get_appraisal_value(isbn):
    engine = create_engine('mysql+pymysql://root:feelingcloudy@127.0.0.1/appraisal_database')
    connection = engine.connect()
    metadata = MetaData()
    appraisal_values = Table('appraisal_values', metadata, autoload=True, autoload_with=engine)
    #query = text("SELECT 'Appraisal Price' FROM appraisal_values WHERE 'ASIN' = '" + isbn + "'")
    query = text("SELECT `Appraisal Price` FROM appraisal_values WHERE `ASIN` = '" + isbn + "'")
    prelim_results = connection.execute(query)
    results = prelim_results.fetchall()
    print(results)
    if len(results) == 0 :
        abort(404)
    return json.dumps({'result': [dict(row) for row in results]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
