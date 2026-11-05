import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --------------------------
# Link lengths
L1, L2, L3 = 2, 1.5, 1

# --------------------------
# Forward kinematics function
def forward_kinematics(theta1, theta2, theta3):
    # Base
    x0, y0 = 0, 0
    
    # First joint
    x1 = x0 + L1 * np.cos(theta1)
    y1 = y0 + L1 * np.sin(theta1)
    
    # Second joint
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    
    # End-effector
    x3 = x2 + L3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3 * np.sin(theta1 + theta2 + theta3)
    
    return [x0, x1, x2, x3], [y0, y1, y2, y3]

# --------------------------
# Initial angles
theta1, theta2, theta3 = 0, 0, 0
x, y = forward_kinematics(theta1, theta2, theta3)

# --------------------------
# Plot setup
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot(x, y, marker='o', linewidth=4)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_title("3-Link Robotic Arm Simulator")

# --------------------------
# Slider setup
axcolor = 'lightgoldenrodyellow'
ax1 = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
ax2 = plt.axes([0.15, 0.06, 0.65, 0.03], facecolor=axcolor)
ax3 = plt.axes([0.15, 0.02, 0.65, 0.03], facecolor=axcolor)

s1 = Slider(ax1, 'Theta1', -np.pi, np.pi, valinit=0)
s2 = Slider(ax2, 'Theta2', -np.pi, np.pi, valinit=0)
s3 = Slider(ax3, 'Theta3', -np.pi, np.pi, valinit=0)

# --------------------------
# Update function
def update(val):
    theta1 = s1.val
    theta2 = s2.val
    theta3 = s3.val
    x, y = forward_kinematics(theta1, theta2, theta3)
    line.set_data(x, y)
    fig.canvas.draw_idle()

s1.on_changed(update)
s2.on_changed(update)
s3.on_changed(update)

# --------------------------
plt.show()