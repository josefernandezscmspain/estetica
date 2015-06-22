from flask_restful import abort, Resource, reqparse

__author__ = 'jose'



CUSTOMERS = {
    'user1': {'name': 'mike', 'email':'aaa@gmail.com'},
    'user2': {'name': 'lalit','email':'aaa@gmail.com'},
    'user3': {'name': 'sunil','email':'aaa@gmail.com'},
}


def abort_if_customer_doesnt_exist(customer_id):
    if customer_id not in CUSTOMERS:
        abort(404, message="User {} doesn't exist".format(customer_id))

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('name', type=str)

class Customer(Resource):

    def get(self, user_id):
        abort_if_customer_doesnt_exist(user_id)
        return CUSTOMERS[user_id]

    def delete(self, user_id):
        abort_if_customer_doesnt_exist(user_id)
        del CUSTOMERS[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        customer = {'name': args['name'], 'email': args['email']}
        CUSTOMERS[user_id] = customer
        return customer, 201

class CustomersList(Resource):

    def get(self):
        return CUSTOMERS

    def post(self):
        args = parser.parse_args()
        user_id = 'user%d' % (len(CUSTOMERS) + 1)
        CUSTOMERS[user_id] = {'name': args['name'], 'email': args['email']}
        return CUSTOMERS[user_id], 201



