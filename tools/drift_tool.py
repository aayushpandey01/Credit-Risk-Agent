import pickle
import pandas as pd
from model.drift import calculate_psi

df = pd.read_csv("credit_data.csv")

with open("pd_model.pkl", "rb") as f:
    model = pickle.load(f)

def drift_tool():

    X = df.drop("default", axis=1)
    probs = model.predict_proba(X)[:, 1]

    shifted = probs + 0.05  # simulate drift

    psi = calculate_psi(probs, shifted)

    return psi