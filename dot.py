import numpy as np
vector_a = np.array([1, 2])
vector_b = np.array([3, 4])

dot_product = np.dot(vector_a, vector_b)

#magnitude of vectors
magnitude_a = np.linalg.norm(vector_a)
magnitude_b = np.linalg.norm(vector_b)

cos_theta = dot_product / (magnitude_a * magnitude_b)

print("dot product and its properties using python")
print("vector A:",vector_a)
print("vector B:",vector_b)
print("Dot product(A.B):",dot_product)
print("magnitude of A:",magnitude_a)
print("magnitude  of B:",magnitude_b)
print("cosine of the angle between A and B :",cos_theta)
