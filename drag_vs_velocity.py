import matplotlib.pyplot as plt

rho = 1.225
wing_area = 20
drag_coefficient = 0.03

velocities = []
drag_forces = []

for v in range(0, 101, 5):
    drag = 0.5 * rho * v**2 * wing_area * drag_coefficient
    velocities.append(v)
    drag_forces.append(drag)

plt.plot(velocities, drag_forces)

plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag Force (N)")
plt.title("Velocity vs Drag Force")

plt.show()
