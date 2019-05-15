from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item  # We no longer need jsonify because "flask_restful" did for us
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        # Status code: 201 is for 'created', 200 is server is ok, 202 is accepted(but maybe delay)
        return item, 201


# http://127.0.0.1:5000/item/headphone
api.add_resource(Item, '/item/<string:name>')

app.run(port=5002)  # 5000 is the default port
