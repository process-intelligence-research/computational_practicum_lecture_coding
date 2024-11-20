import matplotlib.pyplot as plt
import numpy as np

def plot_linear(a, b, x_start=0, x_end=10, num_points=100):
    """
    Plots a linear function y = ax + b.

    Parameters
    ----------
    a : float
        Slope of the linear function.
    b : float
        Intercept of the linear function.
    x_start : float, optional
        The starting value of x for the plot (default is 0).
    x_end : float, optional
        The ending value of x for the plot (default is 10).
    num_points : int, optional
        The number of points to plot (default is 100).
    
    Returns
    -------
    None
    """
    x = np.linspace(x_start, x_end, num_points)
    y = a * x + b

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Function Plot')
    plt.legend()
    plt.grid(True)
    plt.show()