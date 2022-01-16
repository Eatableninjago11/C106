from statistics import correlation
import plotly.express as px
import csv
import numpy as np


def getDataSource(data_path):
    marksInPercentage = []
    days_present = []

with open("Student Marks vs Days Present.csv") as csv_file:
    csv_reader = csv.DictReader()
    df = csv.DictReader(csv_file)
    for row in csv.DictReader(csv_file):
        mark_in_percentage.append(float("marksInPercentage"))
        day_present.append(float("daysPresent"))
        return{x:marksInPercentage, y:daysPresent}
 def findCorrelation(dataSource):
     correlation = np.correlation(dataSource["x"], dataSource["y"])
     print("correlation between marks and percentage")