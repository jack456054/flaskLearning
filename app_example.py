from flask import Flask

app = Flask(__name__)

# Easiest example:
# @app.route('/')  # Ex: 'http://www.google.com/', '/' means the home page
# def home():
#     return "Hello, world!"

stores = [
    {
        'name': 'Y&S',
        'items': [
            {
                'name': 'Headphone'
                'price': 199.00
            }
        ]
    }
]

# HTTP verbs:
# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])  # Default method is 'GET'
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')  # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_store():
    pass

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)
