from datetime import datetime
from . import main
from flask import Response,request
from flask.json import jsonify
import json
from server import Clientes,db


@main.route("/",methods=['GET'])
def index():
    dados = Clientes.query.all()
    cls = [cl.to_json() for cl in dados]
    return Response(json.dumps(cls)),200

@main.route("/<id>",methods=['GET'])
def pesquisar(id):
    dados = Clientes.query.get(int(id))
    return dados.to_json(),200

@main.route("/",methods=['POST'])
def salvar():
    dados = request.get_json()
    ds =   Clientes(
    data=datetime.now().strftime('%d/%m/%Y'),
    nome=dados['nome'],
    telefone=dados['telefone'],
    email=dados['email'],
    cep=dados['cep']
    )
    db.session.add(ds)
    db.session.commit()
    return json.dumps(dados),201

@main.route("/<id>",methods=['DELETE'])
def deletar(id):
    dados = Clientes.query.get(int(id))
    if dados:
        db.session.delete(dados)
        db.session.commit()
        return jsonify({'msg':True}),201

    return jsonify({'msg':False}),404


