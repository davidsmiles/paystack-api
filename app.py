import os

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from resources.banks import Banks
from resources.transfer import TransferRecipient
from resources.verify import Verify

app = Flask(__name__)
api = Api(app)

load_dotenv('.env')
app.config.from_object(os.environ['APPLICATION_SETTINGS'])


api.add_resource(Banks, '/banks')
api.add_resource(Verify, '/verify')
api.add_resource(TransferRecipient, '/transfer')

if __name__ == '__main__':
    load_dotenv('.env')
    app.run(port=5000)
