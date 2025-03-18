import numpy as np


class FeedForward:
    def __init__(self, input: int, layers: list, output: int):
        self.input = input
        self.layers = layers
        self.output = output

        self.start_matrix = np.random.rand(self.input, self.layers[0])
        self.end_matrix = np.random.rand(self.layers[-1], self.output)

        if len(self.layers) > 1:
            for layer in range(0, len(self.layers)):
                temp = "hidden_matrix_" + str(layer)






ff1 = FeedForward(784, [20, 20], 10)