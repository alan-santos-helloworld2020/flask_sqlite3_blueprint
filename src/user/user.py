from flask import request,jsonify
from . import main_user
import json
import datetime
import jwt
from server import app


@main_user.route("/user", methods=['POST'])
def user():
    body = request.json
    if body['user'] == "admin" and body["password"] == "123":
        token = jwt.encode({'username': body['user'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
                    },app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({'auth': True, 'token': token})
    else:
        return jsonify({'auth': False, 'token': False})
