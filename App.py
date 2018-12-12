from flask import Flask, request, abort
import datetime
import json


app = Flask(__name__)


class Restaurant:

    def __init__(self, id_, name, opens_at, closes_at):
        self.id = id_
        self.name = name
        self.opens_at = self.encode_time(opens_at)
        self.closes_at = self.encode_time(closes_at)

    def encode_time(self, time_str):
        return datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')


# 'The restaurants dict will hold all Restaurant entities'
restaurants = {}

# 'A flag to indicate the next Restaurant.id, that will be assigned (This should simulate the pk)'
id_flag = 0


@app.route('/restaurant', methods=['POST'])
def restaurant():

    global id_flag

    # 'Check if the request contains the required key'
    if 'restaurant' in request.form:

        # 'Check if the JSON-Format is valid'
        try:
            restaurant_data = json.loads(request.form['restaurant'])
        except json.decoder.JSONDecodeError:
            return abort(400)

        # 'Create a new Restaurant'
        new_restaurant = Restaurant(id_=id_flag, name=restaurant_data['name'],
                                    opens_at=restaurant_data['opens_at'], closes_at=restaurant_data['closes_at'])

        # 'Increase the id_flag and add the new Restaurant to the dict
        id_flag += 1
        restaurants[new_restaurant.id] = new_restaurant

        return json.dumps({'Restaurant created with ID': new_restaurant.id}), 201, {'ContentType': 'application/json'}
    else:
        return abort(422)


@app.route('/restaurant/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def restaurant_id(id):

    # 'Id should be an integer'
    if isinstance(id, int):

        if request.method == 'GET':

            # 'Check if the requested id is stored in our restaurants dict'
            if id in restaurants:
                return json.dumps({'id': restaurants[id].id,
                                   'name': restaurants[id].name,
                                   'opens_at': str(restaurants[id].opens_at),
                                   'closes_at': str(restaurants[id].closes_at)}),\
                       200, {'ContentType': 'application/json'}
            else:
                abort(404)

        if request.method == 'PUT':

            # 'Check if the request contains the required key'
            if 'restaurant' in request.form:

                # 'Check if the JSON-Format is valid'
                try:
                    restaurant_data = json.loads(request.form['restaurant'])
                except json.decoder.JSONDecodeError:
                    return abort(400)

                # 'Grab the Restaurant to update and update the fields'
                restaurant_to_update = restaurants[id]
                restaurant_to_update.name = restaurant_data['name']
                restaurant_to_update.opens_at = restaurant_data['opens_at']
                restaurant_to_update.closes_at = restaurant_data['closes_at']

                return json.dumps({'Restaurant updated with ID': restaurant_to_update.id}), 200, \
                       {'ContentType': 'application/json'}
            else:
                abort(422)

        if request.method == 'DELETE':

            # 'Check if requested id is stored in dict'
            if id in restaurants:

                # 'Delete requested Restaurant'
                del restaurants[id]
                return json.dumps({'Restaurant deleted with ID': id}), 201, {'ContentType': 'application/json'}
            else:
                abort(404)
    else:
        abort(400)
