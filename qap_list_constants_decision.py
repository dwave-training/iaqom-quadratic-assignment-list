"""
Requirements:
    Objective: Minimize the total cost of interaction between facilities.
    Constraint: Each facility must be assigned to exactly one location.

Given constants:
    distance_matrix (array): A 3x3 array representing the distance between locations.
    flow_matrix (array): A 3x3 array representing the flow between facilities.
    num_facilities (int): Number of facilities.
"""

# Import any required packages.
import numpy as np
from dwave.optimization import Model

# Initialize the nonlinear model object.
model = Model()

# Define the constants.
# Distance Matrix: the distance between locations.
distance_matrix = np.array([[0, 2, 3],
                            [1, 0, 5],
                            [4, 6, 0]
                            ])

# Flow Matrix: the flow between facilities.
flow_matrix = np.array([
                        [0, 5, 2],
                        [4, 0, 1],
                        [3, 6, 0]
                        ])

# Total number of facilities.
num_facilities = distance_matrix.shape[0]

# Add the constants to the model object.
distance = model.constant(distance_matrix)
flow = model.constant(flow_matrix)

# Define the list variable and store it in order.
order = model.list(num_facilities)
