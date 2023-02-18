from flask import Flask, render_template, request, jsonify
from get_disease import dosomething

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    symptom = data['queryResult']['parameters']['symptoms_name']
    output = dosomething(symptom)

    response = {
        'fulfillmentText':"You may have {}.".format(output[0])
    }
    return jsonify(response)



