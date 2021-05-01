import os

import requests
from flask_restful import Resource


class Banks(Resource):

    @classmethod
    def get(cls):
        headers = {'AUTHORIZATION': f'Bearer {os.environ["TEST_SECRET_KEY"]}'}
        url = 'https://api.paystack.co/bank'
        response = requests.get(url, headers=headers)

        return response.json(), response.status_code

