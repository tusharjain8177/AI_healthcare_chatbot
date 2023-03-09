from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import csv,numpy as np,pandas as pd
import os
import pickle

data = pd.read_csv(os.path.join("datasets", "Training.csv"))
df = pd.DataFrame(data)

model = pickle.load(open(os.path.join("models", "model.pkl"), "rb"))
indices = [i for i in range(132)]
symptoms = df.columns.values[:-1]

dictionary = dict(zip(symptoms,indices))

dimensionality_reduction = data.groupby(data['prognosis']).max()

def dosomething(symptom):
    user_input_symptoms = symptom
    user_input_label = [0 for i in range(132)]
    for i in user_input_symptoms:
        idx = dictionary[i]
        user_input_label[idx] = 1

    user_input_label = np.array(user_input_label)
    user_input_label = user_input_label.reshape((-1,1)).transpose()
    return(model.predict(user_input_label))

