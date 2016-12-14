# test the performance of learnt CNN on its corresponding training data
import sys
import numpy as np
from spark.utils import *
from spark.locality_cnn import LocalityCNN
from time import time

def test(size, batches):
    print('Testing Locality CNN for %d training images (%d batches)' % (size, batches))
    start = time()
    cnn = LocalityCNN(0, batches)
    X, Y = load_training_data(0, size)
    P = cnn.predict_train(X)
    P = np.argmax(P, 1)
    print('Batches: %d' % batches)
    print('Prediction:')
    print(P)
    print('Answer:')
    print(Y)

    C = np.concatenate([P, Y]).reshape(2, -1).T
    C = [x for x in C if x[0] == x[1]]
    print('Correct:')
    print('%d/%d' % (len(C), size))
    end = time()
    print('Total time consumption: %.3f' % (end - start))

if __name__ == '__main__':
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    batches = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    test(size, batches)
