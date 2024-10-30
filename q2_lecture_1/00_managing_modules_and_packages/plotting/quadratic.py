import matplotlib.pyplot as plt
import numpy as np

def plot_quadratic(a, b, c, x_start=-10, x_end=10, num_points=100):
    """
    Plots a quadratic function y = ax^2 + bx + c.

    Parameters
    ----------
    a : float
        Coefficient of the quadratic term.
    b : float
        Coefficient of the linear term.
    c : float
        Constant term.
    x_start : float, optional
        The starting value of x for the plot (default is -10).
    x_end : float, optional
        The ending value of x for the plot (default is 10).
    num_points : int, optional
        The number of points to plot (default is 100).
    
    Returns
    -------
    None
    """
    x = np.linspace(x_start, x_end, num_points)
    y = a * x**2 + b * x + c

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Function Plot')
    plt.legend()
    plt.grid(True)
    plt.show()