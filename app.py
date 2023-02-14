from flask import Flask, render_template, request, jsonify
from get_disease import get_disease

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
    data = request.get_json()
    # print(data)
    symptoms_name = data['queryResult']['parameters']['symptoms_name']
    disese_name, medicines, doctor = get_disease(symptoms_name)
    response = {
        'fulfillmentText': "You have {}.You should take these medicines: {}. You should consult these doctors: {}".format(disese_name, medicines, doctor)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)