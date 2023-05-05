import matplotlib.pyplot as plt
from detecto.utils import read_image

image = read_image('image.jpg')
plt.imshow(image)
plt.show()