import numpy as np
I=np.eye(5)-np.eye(5,k=-1)-np.eye(5,k=1)
print(I)
