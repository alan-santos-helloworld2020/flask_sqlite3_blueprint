from flask import Flask,Response,request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)


app.config['SECRET_KEY'] = '123456789'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.sqlite"
db = SQLAlchemy(app)

class Clientes(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      data = db.Column(db.String,nullable=False)
      nome = db.Column(db.String, unique=True, nullable=False)
      telefone = db.Column(db.String, unique=True, nullable=False)
      email = db.Column(db.String, unique=True, nullable=False)
      cep = db.Column(db.String, unique=True, nullable=False)

      def __init__(self,data,nome,telefone,email,cep):
            self.data = data
            self.nome = nome
            self.telefone = telefone
            self.email = email
            self.cep = cep

      def to_json(self):
            return {"id":self.id,"data":self.data,"nome":self.nome,"telefone":self.telefone,"email":self.email,"cep":self.cep}

from src.clientes import main
app.register_blueprint(main)

from src.user import main_user
app.register_blueprint(main_user)



if __name__ == "__main__":
    app.run(debug=True,port=3000)
