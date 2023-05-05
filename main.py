import matplotlib.pyplot as plt
from detecto.utils import read_image

image = read_image('image.jpg')
plt.imshow(image)
plt.show()


from detecto.core import Dataset

dataset = Dataset('./labels/', './images/')

from detecto.visualize import show_labeled_image

image, targets = dataset[0]
show_labeled_image(image, targets['boxes'], targets['labels'])