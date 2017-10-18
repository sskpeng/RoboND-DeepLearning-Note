import numpy as np

def run():
    input = [2.0, 1.0, 0.1]
    sum = 0
    output = []
    for i in range(len(input)):
        sum += np.exp(input[i])
    for i in range(len(input)):
        output.append(np.exp(input[i])/sum)
    return output
out = run()
print (out)