rho = 1.225
velocity = 50
wing_area = 20
drag_coefficient = 0.03

drag = 0.5 * rho * velocity**2 * wing_area * drag_coefficient

print("Drag Force =", drag)
