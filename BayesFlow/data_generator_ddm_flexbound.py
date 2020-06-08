import sys
sys.path.append('../')

import cddm_data_simulation as cds
import boundary_functions as bf

import numpy as np
import json
import time

output = []

start = time.time()

batch_size = 100000

for i in range(batch_size):
    print("j", i)
    v = np.random.uniform(-3, 3)
    a = np.random.uniform(0.3, 2.0)
    w = np.random.uniform(0.1, 0.9)
    n_samples = 6000
    out = cds.ddm_flexbound(v=v, 
                            a=a, 
                            w=w,
                            ndt = 0.5,
                            delta_t = 0.001, 
                            s = np.sqrt(2),
                            max_t = 20,
                            n_samples = n_samples,
                            boundary_fun = bf.constant,
                            boundary_multiplicative = True, 
                            boundary_params = {})
                        #boundary_params = {"theta": 0.01})

    rt = out[0].reshape(1, n_samples).tolist()
    choice = out[1].reshape(1, n_samples).tolist()

    Dictionary = {'a':a, 'v':v, 'w':w, 'rt':rt, 'choice':choice}                    
    output.append(Dictionary)

end = time.time()

print("Data generation took: {} time".format(end - start))

with open('./data_ddm_flexbound_constant.json', 'w') as outfile:
    json.dump(output, outfile, skipkeys=True, allow_nan=True, indent=4)
