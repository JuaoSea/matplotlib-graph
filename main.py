import numpy as np
import matplotlib.pyplot as plt


volume = [0.38, 0.56, 0.80, 0.96]
mass = [2.938, 4.135, 6.088, 7.199]


z = np.polyfit(volume, mass, 1)
p = np.poly1d(z)

plt.plot(volume, p(volume), c="r", label="Density", zorder=2)
text = (f"y={z[0]:0.2f}x{z[1]:+0.2f}")
plt.gca().text(0.71, 0.025, text,transform=plt.gca().transAxes, fontsize=12)

plt.scatter(volume, mass, c="black", label="Samples", marker="*", zorder=3)
 
plt.xlabel("Volume (mL)")
plt.ylabel("Mass (g)")
plt.title("Group 1 - Black")

plt.grid(zorder=1, linestyle="--")
plt.legend()

plt.savefig("graph.png")
plt.show()
