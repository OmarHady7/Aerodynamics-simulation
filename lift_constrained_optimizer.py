rho = 1.225
velocity = 100

required_lift = 5000  # minimum lift needed

best_drag = float("inf")
best_design = None

for A in range(10, 51, 5):  # wing area
    for Cd in [0.02, 0.03, 0.04]:
        for Cl in [0.5, 0.7, 1.0]:

            drag = 0.5 * rho * velocity**2 * A * Cd
            lift = 0.5 * rho * velocity**2 * A * Cl

            # Only accept designs that meet lift requirement
            if lift >= required_lift:
                if drag < best_drag:
                    best_drag = drag
                    best_design = (A, Cd, Cl)

print("Best Design with Lift Constraint:")
print("Wing Area:", best_design[0])
print("Drag Coefficient:", best_design[1])
print("Lift Coefficient:", best_design[2])
print("Drag:", best_drag)
