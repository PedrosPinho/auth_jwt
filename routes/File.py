from flask_restful import Resource, Api, reqparse
from controllers.File import File as File_controller
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('content')
parser.add_argument('index')

class File(Resource):
    @jwt_required
    def get(self):
      return File_controller.read_file(self)

    @jwt_required
    def post(self):
        args = parser.parse_args()
        content = args['content']
        return File_controller.append_data(self, content)

    @jwt_required
    def put(self):
        args = parser.parse_args()
        content = args['content']
        index = args['index']
        return File_controller.edit_line(self, content, index)
        
    @jwt_required
    def delete(self):
        args = parser.parse_args()
        index = args['index']
        if index != None:
            File_controller.remove_line(self, index)
        else: 
            File_controller.remove_file(self)
        return
