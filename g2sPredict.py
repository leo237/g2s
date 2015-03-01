import numpy as np 
import pandas as pd 
import csv as csv
from sklearn.ensemble import RandomForestClassifier

dataset = np.genfromtxt(open('train.csv','r'), delimiter=',', dtype='f8')[0:]    
target = [x[192] for x in dataset]
train = [x[0:192] for x in dataset]
test = np.genfromtxt(open('test.csv','r'), delimiter=',', dtype='f8')[0:]

rf = RandomForestClassifier(n_estimators=100)
rf.fit(train, target)

output = rf.predict(test)
print output