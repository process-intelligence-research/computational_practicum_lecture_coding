import math
import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt

from scipy.interpolate import make_interp_spline

from typing import Callable, Union

from test_functions import logarithm_natural, sinus, sign_fcn

def linear_splines(func: Callable, x_points:npt.NDArray, x_sample:Union[float, npt.NDArray]):

    assert len(x_points)>1, "Not enough support points"

    if type(x_sample) in [float, int]:
        x_sample = np.array([x_sample])

    results_arr = np.zeros(len(x_sample))
    for idx, p in enumerate(x_sample):
        # defermine where x_sample is
        assert p >= np.min(x_points) and p <= np.max(x_points), "Point not within range"

        idx = np.searchsorted( x_points, p) - 1
        lower_border =  x_points[idx]
        upper_border = x_points[idx + 1]

        result = func(lower_border)+(func(upper_border)-func(lower_border))/(upper_border-lower_border)*(p-lower_border)
        results_arr[idx]=result

    if len(results_arr)==1:
        return results_arr[0]
    
    return results_arr

def plot_splines(y_points:npt.NDArray, x_points: npt.NDArray, k_plot: int, x_samples: npt.NDArray, title: str):

    plt.figure(figsize=(8, 5))
    
    plt.scatter(x_points, y_points, color="red", label="Known points")  # Highlight the input points
    plt.plot(x_samples, y_interp, label=f"Spline (k={k_plot})", linestyle="--")  # Spline curve
    plt.plot(x_samples, y_true, label='True function')
    plt.title("Spline Interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    k_plot=3
    func = sinus

    x_points = np.array([0,1/4*math.pi,2/3*math.pi,1.1*math.pi,4/3*math.pi, 4.8, 5.2, 1.8*math.pi, 2*math.pi])
    x_samples = np.linspace(0, 2*math.pi, 100)

    y_points = np.zeros_like(x_points)
    
    for i, x in enumerate(x_points):
        y_points[i] = func(x)
        if x == 4.8:
            y_points[i] = -0.7
    interp_spline = make_interp_spline(x = x_points, y =y_points, k = k_plot)

    y_interp = interp_spline(x_samples)
    y_true = np.array([func(x) for x in x_samples])
    title = "Spline interpolation"

    plot_splines(y_points=y_points, x_points=x_points, title=title, x_samples=x_samples, k_plot=k_plot)