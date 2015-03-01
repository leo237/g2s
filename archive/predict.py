import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier


train_df = pd.read_csv('training.csv', header=-1)  
test_df = pd.read_csv('test.csv', header=-1)


#TRAINING
train_data = train_df.values
test_data = test_df.values

forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit( train_data[0:20,0:195], train_data[0:20,196] )

print train_data[0:20,196]
output = forest.predict(test_data)
print output