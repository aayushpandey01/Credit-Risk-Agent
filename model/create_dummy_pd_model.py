import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

X = np.random.rand(10, 3)
y = np.random.randint(0, 2, 10)

model = RandomForestClassifier()
model.fit(X, y)

with open('pd_model.pkl', 'wb') as f:
    pickle.dump(model, f)
