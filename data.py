import plotly.graph_objects as go
import csv
import pandas as pd

dataFrames = pd.read_csv("data.csv")

student_dataFrames = dataFrames.loc[dataFrames['student_id']]

print("Mean of attempts by each and every student grouped by level")
print(student_dataFrames.groupby("level", as_index=False)["attempt"].mean())

framesInGraph = go.figure(go.Scatter(x = student_dataFrames.groupby("level")["attempt"].mean(),
y = ["Level 1", "Level 2", "Level 3", "Level 4"], color = "attempt", size = "attempt", size_max = 60
))

framesInGraph.show()