#!/Users/jacogericke/anaconda3/bin/python3

import cvxpy
import matplotlib.pyplot as plt

range1 = []
range2 = []
sol = []

for i in range(20):
    y = 30-(4*i)
    if y >= 0:
        range1.append(y)
    y = 20-(i/2)
    if y >= 0:
        range2.append(y)
    
plt.plot(range1)
plt.plot(range2)

plt.ylabel('some numbers')



### CVX STUFF ###

x = cvxpy.Variable()
y = cvxpy.Variable()

maxi = y + (3*x)
constr1 =  30 - (4*x)  >= y
constr2 = 20 - (x/2) >= y
constrA = x >= 0
constrB = y >= 0
 
knapsack_problem = cvxpy.Problem(cvxpy.Maximize(maxi), [constr1, constr2, constrA, constrB])

# Solving the problem
knapsack_problem.solve()

print(knapsack_problem.solution)

max_val = knapsack_problem.solution.opt_val


for i in range(20):
    sol.append(max_val - (3*i))

plt.plot(sol)    


plt.show()




