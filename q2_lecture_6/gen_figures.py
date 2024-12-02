import numpy as np

from test_functions import logarithm_natural, sign_fcn
from regularInterpolation import newton_divided_difference_coefficients, newton_divided_difference_interpolation, lagrangian_interpolation, plot_interpolation

def test_newton():
    x_vals = np.array([1,4,5,6])
    x_sample = np.linspace(0.5,8,30)
    y_vals = np.array([logarithm_natural(x) for x in x_vals])
    coefficients = newton_divided_difference_coefficients(y_vals, x_vals)
    result = newton_divided_difference_interpolation(coefficients=coefficients, x_points=x_vals, x_sample=4.5)
    print(result)
    results_multi = newton_divided_difference_interpolation(coefficients=coefficients, x_points=x_vals, x_sample=x_sample)
    plot_interpolation(func= logarithm_natural, x_points=x_vals, x_sample = x_sample, interpolation_results=results_multi, title="Newton's divided-difference interpolation")

def test_newton_sign():
    x_vals = np.array([-1.25, -0.75, -0.25, 0.25, 0.75, 1.25])
    x_sample = np.linspace(-1.5,1.5,50)
    y_vals = np.array([sign_fcn(x) for x in x_vals])
    coefficients = newton_divided_difference_coefficients(y_vals, x_vals)
    results_multi = newton_divided_difference_interpolation(coefficients=coefficients, x_points=x_vals, x_sample=x_sample)
    plot_interpolation(func= sign_fcn, x_points=x_vals, x_sample = x_sample, interpolation_results=results_multi, title="Newton's divided-difference interpolation")

def test_lagrange():
    x_vals = np.array([1,4,5,6])
    x_sample=np.linspace(0.5,8,30)
    y_vals = np.array([logarithm_natural(x) for x in x_vals])
    result = lagrangian_interpolation(y_vals, x_points=x_vals, x_sample=2)
    print(result)
    results_multi = lagrangian_interpolation(y_vals, x_points=x_vals, x_sample=x_sample)
    plot_interpolation(func= logarithm_natural, x_points=x_vals, x_sample = x_sample, interpolation_results=results_multi, title="Lagrange interpolation")

def test_lagrange_sign():
    x_vals = np.array([-0.8, -0.26667, 0.26667, 0.8])
    x_sample = np.linspace(-0.8,0.8,100)
    y_vals = np.array([sign_fcn(x) for x in x_vals])
    results_multi = lagrangian_interpolation(y_vals, x_points=x_vals, x_sample=x_sample)
    plot_interpolation(func= sign_fcn, x_points=x_vals, x_sample = x_sample, interpolation_results=results_multi, title="Lagrange interpolation")

test_lagrange_sign()