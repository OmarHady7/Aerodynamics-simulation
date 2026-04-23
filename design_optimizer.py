rho = 1.225
velocity = 100

best_drag = float("inf")
best_design = None

# Try different wing areas and drag coefficients
for A in range(10, 51, 5):  # wing area
    for Cd in [0.02, 0.03, 0.04, 0.05]:  # design types
        
        drag = 0.5 * rho * velocity**2 * A * Cd
        
        if drag < best_drag:
            best_drag = drag
            best_design = (A, Cd)

print("Best Design Found:")
print("Wing Area:", best_design[0])
print("Drag Coefficient:", best_design[1])
print("Drag Force:", best_drag)
