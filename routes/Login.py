from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required

from controllers.Login import Login as Login_controller

class Login(Resource):
    def post(self):
        return Login_controller.post(self)
    @jwt_required
    def get(self):
        return Login_controller.get(self)