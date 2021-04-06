import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.plot([1,2,3,4,5,6,7,8,9,10], [13.405,7.445,5.741,4.785,4.381,3.736,3.388,3.219,2.941,2.859], 'ro')
plt.xlabel("Epochs")
plt.ylabel("Training loss")
plt.title("Training loss Monkaa")
plt.savefig("trainig_monkaa.png")


plt.figure(2)
plt.plot([1,2,3,4,5], [10.670,6.615,5.476,4.809,4.347], 'ro')
plt.xlabel("Epochs")
plt.ylabel("Training loss")
plt.title("Training loss Scene Flow")
plt.savefig("trainig_sceneflow.png")


