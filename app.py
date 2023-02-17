from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

df1 = pd.read_csv('datasets/symptom_precaution.csv')

model = pickle.load(open('model.pkl', 'rb'))

data = pickle.load(open('data.pkl', 'rb'))

d_dict = pickle.load(open('d.pkl', 'rb'))
d = pd.DataFrame(d_dict)

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
    data = request.get_json()
    # print(data)
    symptoms_name = data['queryResult']['parameters']['symptoms_name']
    disese_name = get_disease(symptoms_name)
    response = {
        'fulfillmentText': "You have {}.".format(disese_name),
    }
    return jsonify(response)

def get_disease(symptoms_name):
    new_data = []
    for i in range(len(data[0])):
        if d.columns[i] in symptoms_name:
            new_data.append(df1[df1['Symptom'] == symptoms_name[i]]['weight'].values[0])
        else:
            new_data.append(0)
    
    disease = model.predict([new_data])[0]
    return disease





if __name__ == '__main__':
    app.run(debug=True, port=5000)