import numpy as np
#load a list of features
X = np.loadtxt(open('X.csv'),delimiter=',',skiprows=1)
#load a list of targets
labels = dict((v.strip(),k) for k,v in  enumerate(list(set(sport for sport in open('y.txt')))))
y = np.array( [labels[sport.strip()] for sport in open('y.txt')])

height = input('What\'s your height in cm?')
weight = input('What\'s your weight in kg?')                                    

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
clf1 = KNeighborsClassifier()
clf2 = SVC(kernel='linear')
clf_dict = {
        'knn':KNeighborsClassifier(),
        'svc':SVC(kernel='linear')
        }
for name,clf in clf_dict.iteritems():
    clf.fit(X,y)
    outcome = clf.predict([height,weight])
    for sport,sport_id in labels.iteritems():
        if sport_id == outcome:
            print "(%s)You could be a %s olympic champion" % (name,sport)
