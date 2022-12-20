import tensorflow as tf
import numpy as np

# training data
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

# model creation
l0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([l0])

# model compilation
model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(0.1))
# model training
model.fit(celsius, fahrenheit, epochs=500, verbose=False)
print("Finished training the model")

# predict
print(model.predict([100.0]))