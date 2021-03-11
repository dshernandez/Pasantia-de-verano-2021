import numpy as np
import matplotlib.pyplot as plt
import cmath as cmt
from math import e

haddam1=[2**-.5,2**-.5, 2**-.5, -2**-.5]

def op_moneda(state, parameters):
    #Matriz C
    new_state = []
    a, b, c, d = parameters
    for ket, amp in state:
        n, coin = ket
        if coin == 0:
            new_state.append(((n, 0), a*amp))
            new_state.append(((n, 1), b*amp))
        elif coin == 1:
            new_state.append(((n, 0), c*amp))
            new_state.append(((n, 1), d*amp))
    return new_state

def op_shift(state):
    #El operador S
    new_state = []
    for ket, amp in state:
        n, coin = ket
        if coin == 1:
            new_state.append(((n+1, coin), amp))
        if coin == 0:
            new_state.append(((n-1, coin), amp))
    return new_state

def simplify(state):
    #Combinar
    kets = []
    new_state = []
    for ket, amp in state:
        if ket not in kets:
            new_amp = sum(a for k, a in state if k == ket)
            kets.append(ket)
            new_state.append((ket, new_amp))
    return new_state


def marcha(num_iterations, parameters):
    # caminata cuantica para num_iteration pasos con param de C
    state = [((0, 1), 1)]
    for i in range(num_iterations):
        state = op_moneda(state, parameters)
        state = simplify(state)
        state = op_shift(state)
        state = simplify(state)
    return state

def plot_state(state):
    #plottearvector
    min_val = min(state, key=lambda ka: ka[0][0])[0][0]
    max_val = max(state, key=lambda ka: ka[0][0])[0][0]
    X = np.arange(min_val, max_val+1)
    Y = np.zeros((len(X)))
    for i, x in enumerate(X):
        for ket, amp in state:
            if ket[0] == x:
                Y[i] += abs(amp)**2
    plt.plot(X,Y)
    plt.ylabel("$Probabilidad$")
    plt.xlabel("$pasos$")
    plt.title("CAMINATA CUANTICA")
    plt.show()
def general_haddam(p):
    param = [p**.5,(1-p)**.5,(1-p)**.5, -1*(p)**.5 ]
    return param
def main():
    parameters = haddam1
    state = marcha(100, parameters)
    plot_state(state)

if __name__ == '__main__':
    main()