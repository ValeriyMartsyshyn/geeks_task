
import numpy as np
  
a1 = np.array([35, 64, 11, 45, 88])
print("Array 1 :", a1)
  
a2 = np.array([22, 33, 99, 44, 55])
print("Array 2 :", a2)
  
print("\nTake 22, 33 and 99 from Array 2 and put them in\
1st, 3rd and 5th position of Array 1")
  
a1.put([0, 4, 2], a2)
  
print("Resultant Array :", a1)
