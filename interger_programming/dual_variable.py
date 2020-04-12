#!/Users/jacogericke/anaconda3/bin/python3

import cvxpy as cp

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()

# Create two constraints.
constraints = [x + y == 1,
               x - y >= 1]

# Form objective.
obj = cp.Minimize((x-y)**2)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()

# The optimal dual variable (Lagrange multiplier) for
# a constraint is stored in constraint.dual_value.
print(constraints[0], "dual value = ", constraints[0].dual_value)
print(constraints[1], "dual value = ", constraints[1].dual_value)

print(x)
print(y)