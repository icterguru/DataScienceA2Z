
"""
#########  
https://www.geeksforgeeks.org/transpose-matrix-single-line-python/

"""   
import numpy as np

b0=[[1],[-2]]
bt0 = [[0.1], [-.2]]
b1 =  np.matrix(b0) - 0.1 * np.matrix(bt0)
print(b1) 

import numpy as np

w0=[[1, 2],[3, 4]]
wt0 = [[0.2, -.3], [-.1, .2]]
w1 =  np.matrix(w0) - 0.1 * np.matrix(wt0)
print(w1) 


# You need to install numpy in order to import it 
# Numpy transpose returns similar result when 
# applied on 1D matrix 
matrix=[[1,2,3],[4,5,6]] 
print(matrix) 
print("\n") 
print(np.transpose(matrix)) 



matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)] 
for row in matrix: 
	print(row) 
print("\n") 
t_matrix = zip(*matrix) 
for row in t_matrix: 
	print(row) 


import numpy as np
from numpy import linalg as LA

X = [[1, 2], [3, 4], [4, 2]]
Norm_X = LA.norm(X)
print("X:", X)
print("Norm_X:", Norm_X)


X = [[180, 150], [150, 175], [170, 165]]
y = [[110], [140], [180]]

X_Transpose =np.transpose(X)
X_Transpose__X = np.matrix(X_Transpose)* np.matrix(X)
 
X_Transpose__X__Inv = np.linalg.inv(X_Transpose__X)
X_Transpose__X__Inv__X_Transpose = np.matrix(X_Transpose__X__Inv) * np.matrix(X_Transpose)

Beta = np.matrix(X_Transpose__X__Inv__X_Transpose) * np.matrix(y)
    
print("X:", X)
print("X_Transpose:", X_Transpose)
 
print("X_Transpose . X :", X_Transpose__X)

print("X_Transpose__X Inverse: ", X_Transpose__X__Inv)

print("X_Transpose__X__Inv . X_Transpose: ", X_Transpose__X__Inv__X_Transpose)

print("Beta", Beta)

x_feature = [(175, 170)]
y_predicted = np.matrix(x_feature) * np.matrix(Beta)

print("x_feature: ", x_feature)
print ("y_predicted: ", y_predicted)
