from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug import generate_password_hash, check_password_hash

@app.route('/add', methods=['POST'])
def add_dish():
  _json = request.json
  _name = _json['name']
  _note = _json['note']
  # validate the received values
  if _name and _note and request.method == 'POST':
    # save details
    id = mongo.db.dish.insert({'name': _name, 'note': _note)
    resp = jsonify('dish added successfully!')
    resp.status_code = 200
    return resp
  else:
    return not_found()
    
@app.route('/dishs')
def dishs():
  dishs = mongo.db.dish.find()
  resp = dumps(dishs)
  return resp
    
@app.route('/dish/<id>')
def dish(id):
  dish = mongo.db.dish.find_one({'_id': ObjectId(id)})
  resp = dumps(dish)
  return resp

@app.route('/update', methods=['PUT'])
def update_dish():
  _json = request.json
  _id = _json['_id']
  _name = _json['name']
  _note = _json['note']
  # validate the received values
  if _name and _note and _id and request.method == 'PUT':
    # save edits
    mongo.db.dish.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'note': _note)
    resp = jsonify('dish updated successfully!')
    resp.status_code = 200
    return resp
  else:
    return not_found()
    
@app.route('/delete/<id>', methods=['DELETE'])
def delete_dish(id):
  mongo.db.dish.delete_one({'_id': ObjectId(id)})
  resp = jsonify('dish deleted successfully!')
  resp.status_code = 200
  return resp
    
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
