import numpy as np
import matplotlib.pyplot as plt


ITERATIONS = 10000000
FORWARD = 6
ANGLE_FORWARD = np.radians(45)
BACK = 0.25

PROB_0 = 0.01
PROB_1 = 0.85
PROB_2 = 0.07


def step(x0, y0):
    r = np.random.random()
    if r < PROB_0:
        p = 0
        xf = 0.0
        yf = 0.16 * y0
    elif PROB_0 <= r < PROB_0 + PROB_1:
        p = 1
        xf = 0.85 * x0 + 0.04 * y0
        yf = -0.04 * x0 + 0.85 * y0 + 1.6
    elif PROB_0 + PROB_1 <= r < PROB_0 + PROB_1 + PROB_2 :
        p = 2
        xf = 0.2 * x0 - 0.26 * y0
        yf = 0.23 * x0 + 0.22 * y0 + 1.6
    else:
        p = 3
        xf = -0.15 * x0 + 0.28 * y0
        yf = 0.26 * x0 + 0.24 * y0 + 0.44
    return xf, yf, p

def run():
    vector_x = [0]
    vector_y = [0]
    x, y = (0,0)
    p_0, p_1, p_2, p_3 = 0,0,0,0
    
    for _ in range(ITERATIONS):
        x, y, p = step(x, y)
        
        vector_x.append(x)
        vector_y.append(y)

        if p == 0:
            p_0 += 1
        elif p == 1:
            p_1 += 1
        elif p == 2:
            p_2 += 1
        elif p == 3:
            p_3 += 1

    print(p_0, p_1, p_2, p_3)    

    plt.scatter(vector_x, vector_y, s=0.01)
    # plt.plot(vector_x)
    plt.show()







if __name__ == "__main__":
    run()