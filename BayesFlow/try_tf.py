import numpy as np
import tensorflow as tf
from tensorflow.keras.regularizers import l2

n_dense = 1
h_dim = 3

module = tf.keras.Sequential([
    tf.keras.layers.Dense(h_dim, activation='elu', kernel_initializer='glorot_uniform') 
    for _ in range(n_dense)
])
print(module)
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
rank_2_tensor = tf.constant([[1, 2],
                             [3, 4],
                             [5, 6]], dtype=tf.float16)

y = module(rank_2_tensor)
print("yyy")
print(y[0][0])