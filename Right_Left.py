
# By: Aya Ahmad Saad

# Data
x_ = [115, 91, 123, 70, 164, 73, 68, 67, 83, 88, 65, 87, 100, 99, 89, 119, 114, 452, 451, 142, 106, 190, 163,
      115, 147, 130, 164, 127, 190, 133, 113, 130, 139, 140, 140, 124, 162, 142, 136, 206, 204, 650, 633, 173,
      138, 229, 197, 145]  # first feature
y_ = [136, 98, 86, 113, 111, 98, 77, 119, 104, 114, 126, 93, 70, 80, 95, 182, 183, 469, 381, 91, 121, 48, 116, 
      82, 135, 96, 84, 109, 109, 99, 77, 121, 105, 115, 125, 88, 70, 80, 95, 180, 181, 456, 365, 92, 120, 48, 
      131, 76]  # second features
w_ = [243*207, 224*225, 271*186, 201*251, 275*183, 212*238, 187*269, 194*259, 225*225, 225*255, 200*252, 
      211*238, 259*194, 243*207, 225*224, 320*400, 320*400, 1050*1280, 1080*1068, 300*168, 253*199, 
      300*168, 252*200, 273*184, 243*207, 224*225, 271*186, 201*251, 275*183, 212*238, 187*269, 194*259, 225*225, 225*255, 200*252, 
      211*238, 259*194, 243*207, 225*224, 320*400, 320*400, 1050*1280, 1080*1068, 300*168, 253*199, 
      300*168, 252*200, 273*184] #third feature
class_ = ['Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 
          'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'Right', 
          'Right', 'Right', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 
          'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Left', 
          'Left', 'Left']  # Label or target varible.


# Preprocessing
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x = le.fit_transform(x_)
y = le.fit_transform(y_)
z = le.fit_transform(w_)

features = list(zip(x, y, z))
label = le.fit_transform(class_)

# Visulization
import matplotlib.pyplot as plt
def visulize():
      plt.scatter(x[0:25], y[0:25], color='g', marker='s', label='Right')
      plt.scatter(x[25:49], y[25:49], color='r', marker='*', label='Left')
      plt.show()
# visulize()

# Train and Test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.3, random_state=42)


# Model
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

# predict
predicted = model.predict(x_test)


# For accuracy and evaluation
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, predicted)
def accuracy():
      return score*100
# accuracy()


# User
import numpy as np
def enterData(x_user, y_user, w_user):
      x_.append(x_user)
      y_.append(y_user)
      w_.append(w_user)
      x = le.fit_transform(x_)
      y = le.fit_transform(y_)
      z = le.fit_transform(w_)
      new_user = np.array([(x[-1], y[-1], z[-1])])
      new_out = model.predict(new_user)
      return new_out[0]
