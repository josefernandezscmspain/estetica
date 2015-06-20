from flask import Flask
from flask_restful import  Api
from estetica.customers import Customer, CustomersList

app = Flask(__name__)
api = Api(app)



##
## Actually setup the Api resource routing here
##
api.add_resource(CustomersList, '/v1.0/customers')
api.add_resource(Customer, '/v1.0/customer/<string:user_id>')


if __name__ == '__main__':
    app.run(debug=True)
