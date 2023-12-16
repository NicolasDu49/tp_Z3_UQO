from z3 import *

def insertion_sort_model_simple(arr):
    # Initialize Z3 solver
    s = Solver()

    size = len(arr)
    # Create a Z3 array to represent the sorted array
    sorted_arr = Array('SortedArr', IntSort(), IntSort())

    # Constraints for each element in the sorted array to be in the original array
    for i in range(size):
        s.add(Or([Select(sorted_arr, IntVal(i)) == val for val in arr]))

    # Constraint for sorted output
    for i in range(size - 1):
        s.add(Select(sorted_arr, IntVal(i)) <= Select(sorted_arr, IntVal(i + 1)))

    # Constraint for each element in the original array to be in the sorted array
    for val in set(arr):
        count_original = Sum([If(val == arr[i], 1, 0) for i in range(size)])
        count_sorted = Sum([If(Select(sorted_arr, IntVal(i)) == val, 1, 0) for i in range(size)])
        s.add(count_original == count_sorted)

    # Check if the constraints are satisfiable
    if s.check() == sat:
        print("Model \"Insertion Sort\" is satisfiable.")
        # model = s.model()
        # print(model)
    else:
        print("Unsatisfiable constraints")

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort_model_simple(arr)
