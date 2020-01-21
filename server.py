from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

# Importing route classes
from routes.Login import Login
from routes.File import File

# Api configuration
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)

api = Api(app)

api.add_resource(Login, '/login')
api.add_resource(File, '/file')

if __name__ == '__main__':
    app.run()
