from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item  # We no longer need jsonify because "flask_restful" did for us

        # If "next" didn't find anything, return None
        item = next(filter(lambda x: x[name] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x[name] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json()  # (force=True, silent=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        # Status code: 201 is for 'created', 200 is server is ok, 202 is accepted(but maybe delay)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


# http://127.0.0.1:5000/item/headphone
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)  # 5000 is the default port
