[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-quadratic-assignment-list?quickstart=1)
  
# Quadratic Assignment Problem with Stride<sup>TM</sup> Hybrid Solver using a List Variable

For the quadratic assignment problem (QAP), use a list symbol to represent the decision variable. Convert the mathematical formulation into a Python model suitable for submission to the Stride hybrid solver.

The objective is to minimize the total cost of interaction between facilities. The decision variable represents the order in which facilities are assigned to locations. In this example, assume that the total number of facilities is equal to the total number of locations. There is one constraint: each facility must be assigned to exactly one location.

This repository does not contain any `#TODO` sections that need to be completed in the Python file. The provided code is intended to help you answer the quiz questions available in the online course.

## Quiz: Coding QAP

In this quiz, create the model object, define the problem constants, add the constants to the model object, and define the decision variable symbol.

Open the code file `qap_list_constants_decision.py`.

   1. Import the relevant package(s).
   
   2. Create a nonlinear model object called `model`.

   3. Define the constants:
      - `distance_matrix`: the distance between locations.
      - `flow_matrix`: the flow between facilities.
      - `num_facilities`: the total number of facilities.
    
   4. Add the constants to the model object.

   5. Create a list symbol to represent the decision variable and store it in `order`.