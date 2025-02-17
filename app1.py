from flask import Flask, jsonify
import requests as request
import random

app = Flask(__name__)

# Sample data (in-memory database)
items = []

# GET all items
@app.route("/", methods=["GET"])
def hello():
    return "HELLO"

# GET single item
@app.route('/api/items/<string:kitu>', methods=['GET'])
def get_item(kitu):
    nlist = kitu.split("-")
    data = f"use_stripe_sdk=true&mandate_data[customer_acceptance][type]=online&mandate_data[customer_acceptance][online][infer_from_client]=true&return_url=https%3A%2F%2Fsmithvillelittleleague.org%2Fdonate%2F&payment_method={nlist[2]}&key=pk_live_51OctxeJWPL9ZNbRNhPoLAFUyQ9Va0NqbxvJpplzacSF6YItte3vUHvUyjh34IcklHP3JM5xnC7CODJOuXGfnas0Q00MUPtluo5&client_secret={nlist[1]}"

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(500,600)}.{random.randint(1,99)} (KHTML, like Gecko) Chrome/{random.randint(100,150)}.0.0.0 Safari/{random.randint(500,600)}.{random.randint(1,99)}'
        }
    res = request.post(f"https://api.stripe.com/v1/payment_intents/{nlist[0]}/confirm", data=data, headers=headers) 
    return res.json()

if __name__ == '__main__':
    app.run()
