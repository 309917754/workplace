import tensorflow as tf

a = tf.constant([1.0, 2.0])
b = tf.constant([2.0, 3.0])
sess = tf.Session()
print(sess.run(a + b))

# def test():
#     print("python in VS code")

# if __name__ == "__main__":
#     test()
