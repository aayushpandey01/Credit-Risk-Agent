import pickle
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "pd_model.pkl")
data_path = os.path.join(BASE_DIR, "credit_data.csv")

with open(model_path, "rb") as f:
    model = pickle.load(f)

df = pd.read_csv(data_path)

def predict_pd(customer_id: int):

    row = df.iloc[[customer_id]]
    X = row.drop("default", axis=1)

    prob = model.predict_proba(X)[:, 1][0]

    return {
        "customer_id": customer_id,
        "pd": float(prob),
        "features": row.to_dict()
    }