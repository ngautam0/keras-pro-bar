"""
This example trains a model on the MNIST data set use keras-tqdm progress bars.
"""
from mnist_model import mnist_model
from keras_tqdm import TQDMCallback

if __name__ == "__main__":
    mnist_model(verbose=0, callbacks=[TQDMCallback()])
