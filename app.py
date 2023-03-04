from flask import Flask, render_template, request, jsonify
from get_disease import dosomething

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    symptom = data['queryResult']['parameters']['symptoms_name']
    disease = dosomething(symptom)
    medicine = get_mediciens(disease[0])

    response = {
        'fulfillmentText': "You may have {}.".format(disease[0]) + " You can take {}.".format(medicine)
    }
    print(response)
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
    if disease in mediciens:
        return mediciens[disease]
    else:
        return "No medicine found for this disease"
