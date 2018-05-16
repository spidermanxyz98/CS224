import tensorflow as tf
import numpy as np


x = tf.placeholder(tf.float32, shape=[None, 7, 2], name='x')
#print('shape', type(tf.shape(x)))
print('zeros', tf.zeros([2,3]))
print('zeros tyep', type(tf.zeros([2,3])))

v = tf.Variable(np.random.randn(3,4), name='v')
print('v type', type(v))
feed_dict = {x: np.random.rand(5,7,2)}
with tf.Session() as sess:
    x_shape = sess.run(tf.shape(x), feed_dict = feed_dict)
    
#print(b_evl)
#print(c_evl)
#print(x_shape)
#print('x_evl', x_evl)
print('x_shape', x_shape)
#print('c_shape', c_shape_evl)
