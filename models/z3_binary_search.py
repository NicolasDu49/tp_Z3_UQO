from z3 import *

def binary_search_model(arr, target):
    # Initialize Z3 solver
    s = Solver()

    # Create Z3 variables
    size = len(arr)
    arr_sort = Array('Arr', IntSort(), IntSort())
    target_z3 = Int('target')
    index_z3 = Int('index')
    found = Bool('found')

    # Add constraints for array values
    for i in range(size):
        s.add(Select(arr_sort, IntVal(i)) == arr[i])

    # Add constraint for target value
    s.add(target_z3 == target)

    
    # Create additional Z3 variables for low_index and high_index
    low_index = Int('low_index')
    high_index = Int('high_index')

    # Add initial constraints for low_index and high_index
    s.add(low_index == 0)
    s.add(high_index == size - 1)

    # Add constraint that low_index is always less than high_index
    s.add(low_index < high_index)

    # Constraint for the correctness of the found index
    s.add(Implies(found, And(index_z3 >= low_index, index_z3 <= high_index, Select(arr_sort, index_z3) == target)))
    
    # Constraint for the correctness of the found index
    s.add(Implies(found, And(index_z3 >= 0, index_z3 < size, Select(arr_sort, index_z3) == target)))

    # Constraint for target not found
    s.add(Implies(Not(found), And(index_z3 == -1, Not(Or([Select(arr_sort, IntVal(i)) == target for i in range(size)])))))

    # Constraint for the array being sorted
    for i in range(size - 1):
        s.add(Select(arr_sort, IntVal(i)) <= Select(arr_sort, IntVal(i + 1)))

    # Check if the constraints are satisfiable
    if s.check() == sat:
        print("Model \"Binary Search\" is satisfiable.")
        # print(" Here's the model:\n")
        # print(s.model)
    else:
        print("Unsatisfiable constraints")

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10
binary_search_model(arr, target)