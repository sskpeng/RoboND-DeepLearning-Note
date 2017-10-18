# TensorFlow for Deep Learning

### This document for note in the course material.

### Tensor
`tf.constant()` returns a constant tensor

### Session
A "TensorFlow Session" is an environment for running a graph.

```sh
with tf.Session() as sess:
    output = sess.run(hello_constant)
    print(output)
```
### Input
`tf.placeholder()` returns a tensor that gets its value from data passed to the `tf.session.run()` function, allowing you to set the input right before the session runs.

```sh
x = tf.placeholder(tf.string)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})
```

### Math
#### Addition, subtraction and Multiplication
`tf.add(a, b)` returns `a + b`

`tf.subtract(a, b)` returns `a - b`

`tf.multiply(a, b)` returns `a * b`

`tf.divide(a, b)` returns `a / b`

#### Converting types
```sh
tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))   # 1
```
### TensorFlow Softmax

```sf
x = tf.nn.softmax([2.0, 1.0, 0.2])
```

### TensorFlow Cross-Entropy

```sf
softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

cross_entropy = -tf.reduce_sum(tf.multiply(one_hot, tf.log(softmax)))

with tf.Session() as sess:
    print(sess.run(cross_entropy, feed_dict={softmax: [0.7, 0.2, 0.1], one_hot: [1.0, 0.0, 0.0]}))

```
