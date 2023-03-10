from flask import Flask, render_template, request, jsonify
from get_disease import dosomething
import datetime

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    intent_name = data['queryResult']['intent']['displayName']
    if intent_name == 'symptoms':
        symptom = data['queryResult']['parameters']['symptoms_name']
        disease = dosomething(symptom)
        medicine = get_mediciens(disease[0])
        if type(medicine) == list:
            response = {
                'fulfillmentText': "You may have {}.".format(disease[0]) + " You can take {}.".format(medicine) + "Whould you like to book an appointment?(Yes/No)"
            }
        else:
            response = {
                'fulfillmentText': "You may have {}.".format(disease[0]) + " No medicine found for this disease." + "Whould you like to book an appointment?(Yes/No)"
            }
    elif intent_name == 'Date_Time':
        Date_Time = data['queryResult']['parameters']['date-time']
        if Date_Time < datetime.datetime.now():
            response = {
                'fulfillmentText': "Please Enter a valid date and time."
            }
        else:
            response = {
                'fulfillmentText': "#Patient_Name.Patient_Name, your appointment is booked for {}.".format(Date_Time) + "Thank you for using our service."
            }
        
    # print(response)
    return jsonify(response)


def get_mediciens(disease):
    mediciens = {'gastroenteritis': ['ondansetron',
                                     'doxycycline',
                                     'ceftriaxone',
                                     'ampicillin',
                                     'rotavirus vaccine'],
                 'migraine': ['sumatriptan',
                              'rizatriptan',
                              'onabotulinumtoxinA',
                              'rimegepant',
                              'ubrogepant'],
                 'malaria': ['artemether / lumefantrine',
                             'hydroxychloroquine',
                             'chloroquine',
                             'doxycycline',
                             'mefloquine'],
                 'pneumonia': ['levofloxacin',
                               'clarithromycin',
                               'ceftriaxone',
                               'azithromycin',
                               'doxycycline'],
                 'hyperthyroidism': ['methimazole',
                                     'propylthiouracil',
                                     'potassium iodide',
                                     'iodine / potassium iodide',
                                     'sodium iodide-i-131'],
                 'acne': ['doxycycline',
                          'spironolactone',
                          'minocycline',
                          'clindamycin',
                          'tretinoin'],
                 'urinary-tract-infection': ['nitrofurantoin',
                                             'ciprofloxacin',
                                             'sulfamethoxazole / trimethoprim',
                                             'amoxicillin',
                                             'doxycycline'],
                 'psoriasis': ['clobetasol',
                               'methotrexate',
                               'triamcinolone',
                               'guselkumab',
                               'ixekizumab'],
                 'impetigo': ['mupirocin',
                              'cefadroxil',
                              'cefuroxime',
                              'retapamulin',
                              'ozenoxacin']}
    disease = disease.lower()
    if disease in mediciens:
        return mediciens[disease]
    else:
        return "No medicine found for this disease."
