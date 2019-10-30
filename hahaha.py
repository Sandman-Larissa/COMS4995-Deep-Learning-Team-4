import numpy as np
params = [np.load('model/%d.npy' % i) for i in range(15)]
#print (params)
params[2] = np.concatenate(params[2:6], axis=1)
params[3:6] = []
for a in params:
    print (a.shape)