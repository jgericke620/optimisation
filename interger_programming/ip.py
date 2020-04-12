#!/Users/jacogericke/anaconda3/bin/python3

'''
Maximise the value of your items in your knapsack

Value  =  itemSelection * Values
Weight =  itemSelection * Weights
'''

import cvxpy
import numpy as np


# The data for the Knapsack problem
# P is total weight capacity of sack
# weights and utilities are also specified
weightLimit = 165
weights = np.array([23, 31, 29, 44, 53, 38, 63, 85, 89, 82])
values = np.array([92, 57, 49, 68, 60, 43, 67, 84, 87, 72])

# The variable we are solving for
itemSelection = cvxpy.Variable(len(weights), boolean=True)
# The sum of the weights should be less than or equal to P
weightConstraint = weights * itemSelection <= weightLimit

# Our total utility is the sum of the item utilities
total_utility = values * itemSelection

# We tell cvxpy that we want to maximize total utility 
# subject to weight_constraint. All constraints in 
# cvxpy must be passed as a list
knapsack_problem = cvxpy.Problem(cvxpy.Maximize(total_utility), [weightConstraint])

# Solving the problem
knapsack_problem.solve(solver=cvxpy.GLPK_MI)

print(itemSelection.value)
