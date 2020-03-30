import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("maps.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class MapList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        maps = []

        for key in keys:
            maps.append(shelf[key])

        return {'message': 'Success', 'data': maps}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('mapId', required=True)
        parser.add_argument('a0', required=True)
        parser.add_argument('a1', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['mapId']] = args

        return {'message': 'Map uploaded', 'data': args}, 201


class Map(Resource):
    def get(self, mapId):
        shelf = get_db()
        # If the map does not exist in the data store, return a 404 error.
        if not (mapId in shelf):
            return {'message': 'Map not found', 'data': {}}, 404

        return {'message': 'Map found', 'data': shelf[mapId]}, 200


api.add_resource(MapList, '/maps')
api.add_resource(Map, '/map/<string:mapId>')
