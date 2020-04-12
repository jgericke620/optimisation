#!/Users/jacogericke/anaconda3/bin/python3

import cvxpy as cp
import numpy as np

A = cp.Variable()
B = cp.Variable()
C = cp.Variable()
D = cp.Variable()
E = cp.Variable()
S0 = cp.Variable()
S1 = cp.Variable()
S2 = cp.Variable()

z = B + (1.9*D) + (1.5*E) + (1.08*S2)

constraints = [
    A + C + D + S0 == 100000,
    (0.5*A) + (1.2*C) + (1.08*S0) == B + S1,
    A + (0.5*B) + (1.08*S1) == E + S2,
    A <= 75000,
    B <= 75000,
    C <= 75000,
    D <= 75000,
    E <= 75000,
    A >= 0,
    B >= 0,
    C >= 0,
    D >= 0,
    E >= 0,
    S0 >= 0,
    S1 >= 0,
    S2 >= 0
]

obj = cp.Problem(cp.Maximize(z), constraints)
ans = obj.solve()

print(ans)
for var in [A,B,C,D,E]:
    print(var.value)





'''
Multi Period Work Scheduling
from page 109 in Winston
'''

hours = np.array([6000, 7000, 8000, 9500, 11000])

# 50 workers up to 160 h per month
# 1 month to train technichian
# during training he must be supervised for 50 hours by trained tech
# Exp Tech = $2000 pm
# train = $1000 pm
# 



