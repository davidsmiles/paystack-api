import os

import requests
from flask import request
from flask_restful import Resource


class TransferRecipient(Resource):

    @classmethod
    def post(cls):
        """
        1. Verify the account number
        2. Create a transfer recipient
        2. Initiate transfer
        4. Listen for transfer status
        :return:
        """

        # Verify
        data = request.get_json()
        account_number = data['account_number']
        amount = data['amount']
        bank_code = data['bank_code']

        headers = {'AUTHORIZATION': f'Bearer {os.environ["TEST_SECRET_KEY"]}'}
        verify_url = f'https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bank_code}'
        response = requests.get(verify_url,
                                headers=headers)

        if response.status_code != 200:
            return response.json(), response.status_code

        # Create a transfer recipient
        _json = response.json()
        _data = {
            'type': 'nuban',
            'name': _json['data']['account_name'],
            'account_number': _json['data']['account_number'],
            'bank_code': bank_code,
            'currency': 'NGN'
        }

        tr_url = 'https://api.paystack.co/transferrecipient'
        response = requests.post(tr_url, headers=headers, data=_data)
        if not response.ok:
            return response.json(), response.status_code

        # Initiate a transfer
        _json = response.json()
        _data = {
            'source': 'balance',
            'amount': amount,
            'recipient': _json['data']['recipient_code'],
            'reason': 'Testing Paystack'
        }
        t_url = 'https://api.paystack.co/transfer'
        response = requests.post(t_url, headers=headers, data=_data)
        if not response.ok:
            return response.json(), response.status_code

        return response.json(), response.status_code



