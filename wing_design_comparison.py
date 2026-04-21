import matplotlib.pyplot as plt

rho = 1.225
wing_area = 20

velocities = range(0, 101, 5)

drag_low = []     # efficient design
drag_medium = []  # normal
drag_high = []    # poor design

for v in velocities:
    drag_low.append(0.5 * rho * v**2 * wing_area * 0.02)
    drag_medium.append(0.5 * rho * v**2 * wing_area * 0.04)
    drag_high.append(0.5 * rho * v**2 * wing_area * 0.08)

plt.plot(velocities, drag_low, label="Efficient Wing (Low Drag)")
plt.plot(velocities, drag_medium, label="Normal Wing")
plt.plot(velocities, drag_high, label="Poor Design (High Drag)")

plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag Force (N)")
plt.title("Comparison of Wing Designs")

plt.legend()
plt.show()
