import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt

from typing import Callable, List, Union


def newton_divided_difference_coefficients(y_points: npt.NDArray, x_points: npt.NDArray) -> npt.NDArray:
    """
    Computes the Newton divided difference polynomial of a given function f.
    
    Parameters:
        y_points (npt.NDArray): The list of known values to compute the divided differences.
        x_points (npt.NDArray): The list of x values to compute the divided differences.
        
    Returns:
        npt.NDArray: The Newton divided difference polynomial.
    """
    degree = len(x_points)-1
    # if len(x_points) < degree + 1:
    #     raise ValueError("Not enough points to compute the polynomial of the given degree.")
    
    # Initialize divided difference table
    n = len(x_points)
    divided_diff = [[0] * n for _ in range(n)]
    
    # Fill the first column with function values
    for i in range(n):
        divided_diff[i][0] = y_points[i]
    
    # Calculate divided differences
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (x_points[i + j] - x_points[i])

    # Extract coefficients for the polynomial
    coefficients = [divided_diff[0][i] for i in range(degree + 1)]
    
    return coefficients

def newton_divided_difference_interpolation(coefficients: List[float], x_points:npt.NDArray, x_sample: Union[float, npt.NDArray]) -> Union[float, npt.NDArray]:
    """
    Returns interpolation result using Newton's divided-difference method for given coefficients b0, b1,..., bn for a 
    Netwon's polynomial of degree n
    Args
    ----
        coefficients (List[float]): List of predeterined coefficients b0, b1, ..., bn 
        x_points (npt.NDArray): Given points used for interpolation
        piq (Union[float, npt.NDArray]): Point(s) in question, where to deterine interpolation at

    Returns
    ------- 
        result (Union[float, npt.NDArray]): Interpolation result(s)
    """

    if type(x_sample) in [float, int]:
        x_sample = np.array([x_sample])

    results_arr = np.zeros(len(x_sample))
    for idx, p in enumerate(x_sample):
        result = coefficients[0]
        for i in range(1, len(coefficients)):
            term = coefficients[i]

            for j in range(i):
                term *= (p - x_points[j])
            result += term
        results_arr[idx] = result

    if len(results_arr) == 1:
        return results_arr[0]

    return results_arr

def lagrangian_interpolation(y_points:npt.NDArray, x_points:npt.NDArray, x_sample:Union[float, npt.NDArray]) -> Union[float, npt.NDArray]:
    """
    Lagrange interpolating polynomial for given set of points (x_points, y_points)
    Args
    ----
        y_points (npt.NDArray): Known y-values
        x_points (npt.NDArray): Corresponding x-values
        x_sapmle (Union[float, npt.NDArray]): points in question for inteprolation
    
    Returns
    -------
        results_arr (Union[float, npt.NDArray]): interpolated values
    """
    if type(x_sample) in [float, int]:
        x_sample = np.array([x_sample])
        
    n = len(x_points)
    results_arr = np.zeros(len(x_sample))
    for idx, p in enumerate(x_sample):
        result= 0
        for i in range(n):
            f_i = y_points[i]
            lagrange_i = 1
            for j in range(n):
                if j != i:
                    lagrange_i *= (p - x_points[j])/(x_points[i] - x_points[j])
            
            result += f_i*lagrange_i   
        results_arr[idx] = result

    if len(results_arr) == 1:
        return results_arr[0]

    return results_arr

def plot_interpolation(func: Callable, x_points:npt.NDArray, x_sample:npt.NDArray, interpolation_results:npt.NDArray, title:str) -> None:
    """
    Plot Lagrange interpolating polynomial for given range and true function

    Args
    ---
        func (Callable): known true function
        x_points (npt.NDArray): known points
    """

    y_sample = np.array([func(x) for x in x_sample])

    y_support = np.array([func(x) for x in x_points])

    plt.figure(figsize=(8,6))
    plt.plot(x_sample, interpolation_results, linestyle="--", label=f"{title}, \ndegree: {len(x_points)-1}")
    plt.plot(x_sample, y_sample, label="True function")
    plt.scatter(x_points, y_support, color='r')
    plt.title(f"{title}", fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.ylim(top = 2.8*np.max(y_sample), bottom = 2.8*np.min(y_sample))

    plt.legend(fontsize=10, loc='upper left')
    plt.show()