import numpy as np
import numpy.random


class FeedForward:
    def __init__(self, input: int, layers: list, output: int):
        self.input = input
        self.layers = layers
        self.output = output

        self.start_matrix = np.random.rand(self.input, self.layers[0])
        self.end_matrix = np.random.rand(self.layers[-1], self.output)

        self.hidden_layers = []

        if len(self.layers) > 1:
            for i in range(0, len(self.layers) - 1):
                self.hidden_layers.append(numpy.random.rand(self.layers[i], self.layers[i + 1]))

    def train(self, X, y, epoch:int):
        pass


ff1 = FeedForward(784, [20, 20], 10)
print(ff1.hidden_layers)
