# Test the independence of A (even dice rolls) and B (dice rolls 4 and under)
import numpy as np

A = np.array([2, 4, 6])
B = np.arange(1, 5)

AcapB = np.intersect1d(A, B)

n = 10000

samples = np.random.randint(1, 7, n)

PA = np.sum(np.isin(samples, A))/n
PB = np.sum(np.isin(samples, B))/n


PAintB = np.sum(np.isin(samples, AcapB))/n

print(f"Intersect: {PAintB}\nProduct: {PA*PB}")
