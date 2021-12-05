import numpy as np

#Creating random array
AR = np.array([[14.6, 62.5, np.nan],
                  [1, 52.5, np.nan],
                  [np.nan, 62.5, np.nan],
                  [41.2, 52.5, np.nan]])

#remove all calomms wich contains nan
print(AR[:, ~np.isnan(AR).any(axis=0)])
