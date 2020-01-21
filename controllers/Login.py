from flask import jsonify
from flask_restful import reqparse
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity
)

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('password')

def verify_needed_properties(properties):
    args = parser.parse_args()
    for prop in properties:
        if args.get(prop, None) == None:
            return False

    return True


class Login():
    def post(self):
        def authenticate(email, passwd):
            if email == 'a@b.c' and passwd == '123456':
                return True
            else:
                return False
            
        need = ['email', 'password']
        args = parser.parse_args()
        if not verify_needed_properties(need):
            return "Parametro requerido esta faltando"

        email = args['email']
        passwd = args['password']
        access_token = None

        if authenticate(email, passwd):
            access_token = create_access_token(identity=email)

        return jsonify({"access_token":access_token}, 200)
    def get(self):
        current_user = get_jwt_identity()
        return jsonify({"msg":"Você está logado com {}".format(current_user)}, 200)