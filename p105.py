import pandas as pd
import plotly.express as px
import statistics

data = pd.read_csv("data.csv")

datalist = list(data)
datalist = [int(i) for i in datalist]
standard = statistics.stdev(datalist)
print(standard)

mean = statistics.mean(datalist)
print(mean)