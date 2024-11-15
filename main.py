import numpy as np
import matplotlib.pyplot as plt

#volume = [0.38, 0.56, 0.80, 0.96]
#mass = [2.938, 4.135, 6.088, 7.199]

volume = [0.37, 0.60, 0.83, 1.05]
mass = [1.075, 1.675, 2.229, 2.795]

z = np.polyfit(volume, mass, 1)
p = np.poly1d(z)

plt.plot(volume, p(volume), c="r", label="Density", zorder=2)
text = (f"y={z[0]:0.3f}x{z[1]:+0.3f}")
plt.gca().text(0.71, 0.025, text,transform=plt.gca().transAxes, fontsize=12)

plt.scatter(volume, mass, c="black", label="Samples", marker="*", zorder=3, s=90)
 
plt.xlabel("Volume (mL)")
plt.ylabel("Mass (g)")
plt.title("Density")

plt.grid(zorder=1, linestyle="--")
plt.legend()

plt.savefig("graph.png")
plt.show()
