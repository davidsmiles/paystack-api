import os

import requests
from flask import request
from flask_restful import Resource


class Verify(Resource):

    @classmethod
    def get(cls):
        data = request.get_json()
        account_number = data['account_number']
        bank_code = data['bank_code']
        headers = {'AUTHORIZATION': f'Bearer {os.environ["TEST_SECRET_KEY"]}'}
        url = f'https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bank_code}'
        response = requests.get(url,
                                headers=headers)

        return response.json(), response.status_code




