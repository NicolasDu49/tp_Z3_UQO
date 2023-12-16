from z3 import *

def gcd_model(a_val, b_val):
    # Initialize Z3 solver
    s = Solver()

    # Create Z3 variables
    a = Int('a')
    b = Int('b')
    gcd_val = Int('gcd_val')

    # Add constraints for non-negative inputs and equality to input values
    s.add(a == a_val, b == b_val, a >= 0, b >= 0)

    # Constraint that gcd_val divides both a and b
    s.add(a % gcd_val == 0, b % gcd_val == 0)

    # Constraint that gcd_val is the largest such divisor
    # We ensure there's no larger value that divides both a and b
    larger_divisor = Int('larger_divisor')
    s.add(ForAll([larger_divisor], Implies(And(larger_divisor > gcd_val, larger_divisor <= a), Not(And(a % larger_divisor == 0, b % larger_divisor == 0)))))

    # Constraints for the unreachable code
    # Adding constraints that would make the unreachable code reachable
    s.add(Or(a < 0, b < 0))

    # Check if the constraints are satisfiable
    if s.check() == sat:
        print("Model \"Greater Common Diviser\" is satisfiable.")
        # model = s.model()
        # print(model)
    else:
        print("Unsatisfiable constraints")

# Example usage
a_val = 48
b_val = 18
gcd_model(a_val, b_val)
