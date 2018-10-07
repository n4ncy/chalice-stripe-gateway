# chalice-stripe-gateway

Seemless payment gateway deployment with Chalice and AWS

## Deploying

Once you've configured the aws cli you can then run 
`chalice deploy`

You'll need to set the `STRIPE_KEY` Environment Variable and the `JWT_SECRET` in the Lambda and you're good to go !


## Usage

https://yourendpoint.aws.blah.blah/payment - POST
Body: JWT String
