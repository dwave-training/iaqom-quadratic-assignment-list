[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/iaqom-quadratic-assignment-list?quickstart=1)
  
# Quadratic Assignment Problem With the Stride<sup>TM</sup> Hybrid Solver Using a List Variable

For the quadratic assignment problem (QAP), use a list symbol to represent the decision variable. Convert the mathematical formulation into a Python model suitable for submission to the Stride hybrid solver.

The objective is to minimize the total cost of interaction between facilities. The decision variable represents the order in which facilities are assigned to locations. In this example, assume that the total number of facilities is equal to the total number of locations. There is one constraint: each facility must be assigned to exactly one location.

The code in the repo is intended to help you answer the quiz questions in the online course and, thus, does not contain any `TODO` sections.

## Quiz: Coding the QAP

Open and review `qap_list_constants_decision.py` to answer the questions in the course quiz Coding the QAP.   
