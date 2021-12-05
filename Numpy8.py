import numpy as np
#create random(2d) array
AR= np.array([[10, 20, 30],
                [40, 5, 66],
                [70, 88, 94],
                [11, 54, 20],
                [43, 35, 96],
                [74, 85, 44]])
#access to 1 row of array
ar1=AR[0]
print(ar1)

#print number of rows in array(AR)
r=AR.shape[0]

#access to middle row
ar2=AR[3]
print(ar2)

#create random 3d array
AR3=np.array([[[10, 25, 70], [30, 55, 55], [20, 45, 7]],
                  [[50, 65, 8], [70, 85, 10], [51, 22, 33]],
                 [[19, 69, 36], [1, 5, 24], [4, 25, 96]],
              [[105, 35, 70], [30, 45, 75], [250, 25, 77]],
              [[540, 55, 28], [7, 85, 0], [51, 22, 53]]])

ar3 = AR3[:,[0,2]]
print(ar3)