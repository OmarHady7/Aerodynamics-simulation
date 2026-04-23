import matplotlib.pyplot as plt

rho = 1.225
velocity = 80
wing_area = 20

angles = range(0, 16)  # 0 to 15 degrees
lift_values = []

for angle in angles:
    if angle <= 12:
        Cl = 0.1 * angle
    else:
        Cl = 1.2 - 0.1 * (angle - 12)  # stall behavior
    
    lift = 0.5 * rho * velocity**2 * wing_area * Cl
    lift_values.append(lift)

plt.plot(angles, lift_values)

plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Lift Force")
plt.title("Lift vs Angle of Attack (with Stall)")

plt.show()
