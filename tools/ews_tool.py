import pandas as pd

df = pd.read_csv("credit_data.csv")

def early_warning_tool(customer_id: int):

    row = df.iloc[customer_id]

    alerts = []

    if row["credit_utilization"] > 0.8:
        alerts.append("High credit utilization")

    if row["missed_payments"] >= 2:
        alerts.append("Multiple missed payments")

    if row["dpd"] > 30:
        alerts.append("High Days Past Due")

    return alerts