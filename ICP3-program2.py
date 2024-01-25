import numpy as np

random_vector = np.random.uniform(1, 20, 20)

reshaped_array = random_vector.reshape(4, 5)

reshaped_array[np.arange(len(reshaped_array)), reshaped_array.argmax(axis=1)] = 0

print("Random Vector:")
print(random_vector)
print("\nReshaped Array:")
print(reshaped_array)