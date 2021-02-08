import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x = "level", y = "student_id", size = "attempt", color = "attempt")
fig.show()