from scipy.integrate import dblquad

# Find normalization constant of f(x,y) = x**2*y constrained to x**2 <= y <= 1
# Check distribution by integrating

c = 1/dblquad(lambda y, x: x**2*y, -1, 1, lambda x: x**2, 1)[0]


def f(y, x):
    return (x**2 <= y and y <= 1)*c*x**2*y


print(f"P(R^2) = {dblquad(f, -1, 1, 0, 1)}")  # vanishes outside this region

# Calculate probability on A = {(x,y): x**2 <= y <= x}
print(f"P(A) = {dblquad(f, 0, 1, lambda x: x**2, lambda x: x)}")
