import control as ct
import numpy as np
import matplotlib.pyplot as plt

def main():
    num = [1]
    den = [1, 3, 2]
    system = ct.TransferFunction(num, den)

    t = np.linspace(0, 10, 1001)

    t_out, y_out = ct.step_response(system, T=t)

    plt.figure()
    plt.plot(t_out, y_out)
    plt.title('Step Response of the System')
    plt.xlabel('Time (s)')
    plt.ylabel('Output')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()