from chalice import Chalice
import stripe
import os
import jwt

app = Chalice(app_name='PaymentGateway')

@app.route('/')
def index():
    return {'version': '1.0.0'}

@app.route('/payment', methods=['POST'])
def chargeUser():
    stripe.api_key = os.environ.get('STRIPE_TOKEN')

    json = jwt.decode(json.load(app.current_request.raw_body), os.environ.get('JWT_SECRET'), algorithms=['HS256'])
    decodeAmount = json['amount']
    decodeToken = json['token']

    return stripe.Charge.create(
        amount=decodeAmount,
        currency="gbp",
        description="Payment Gateway",
        source=decodeToken
    )
