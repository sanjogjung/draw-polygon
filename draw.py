import matplotlib.pyplot as plt
from skimage.draw import rectangle
import sys
import skimage

class Draw:
    def __init__(self, filename):
        self.image = skimage.io.imread(filename)

    def set_parameters(self):
        """
        setting the start row and column of the rectangle
        setting the end row and columns of the rectangle
        generating the pixels position for plotting the rectangle
        replacing generated pixel position with max pixel intensity

        """
        self.start = (int(self.image.shape[0] / 4), int(self.image.shape[1] / 4))
        self.end = (int(self.image.shape[0]/1.5), int(self.image.shape[1]/1.5))
        self.rr, self.cc = rectangle(start=self.start, end=self.end, shape=(self.image.shape[0], self.image.shape[1]))
        for i in range(self.image.ndim):
            self.image[self.rr, self.cc, i] = 255

    def draw(self):
        """
        plotting the image
        """
        plt.imshow(self.image)
        plt.show()


if __name__ == '__main__':
    path = sys.argv[1:]
    d1 = Draw(path[0])
    d1.set_parameters()
    d1.draw()

