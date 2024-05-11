import numpy as np
from scipy.special import gamma as G
from scipy.integrate import quad, dblquad

def f(t, v):
  return G((v+1)/2)/G(v/2)*(1+t**2/v)**(-(v+1)/2)*1/(np.sqrt(np.pi*v))

print(quad(lambda t: f(t, 1), -np.inf, np.inf))

c2 = 1/dblquad(lambda y,x : x**2*y, -1, 1, lambda x: x**2, 1)[0]

def f2(y,x):
  return c2*x**2*y

print(dblquad(f2, -1, 1, lambda x: x**2, 1))

print(dblquad(f2, 0, 1, lambda x: x**2, lambda x: x))
