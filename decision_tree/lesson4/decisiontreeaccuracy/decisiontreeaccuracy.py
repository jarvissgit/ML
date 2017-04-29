import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################



#### your code goes here
import sys 
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt 
import numpy as np
import pylab as pl

def classify(features_train, labels_train):
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train,labels_train)
    return clf

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

predict = clf.predict(features_test)
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test,predict)### you fill this in!
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}


