from chalice import Chalice
import stripe
import os

app = Chalice(app_name='PaymentGateway')

@app.route('/')
def index():
    return {'version': '1.0.0'}

@app.route('/payment', methods=['POST'])
def chargeUser():
    stripe.api_key = os.environ.get('STRIPE_TOKEN')

    json = app.current_request.json_body
    decodeAmount = json['amount']
    decodeToken = json['token']

    return stripe.Charge.create(
        amount=decodeAmount,
        currency="gbp",
        description="Payment Gateway",
        source=decodeToken
    )
