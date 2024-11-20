"""This module contains some utility methods that we want to collect 
separately, so we don't clutter our main script.
"""

# In the separate module, we have to import the modules we need here. Even
# if we have already imported them in our main script. But we can also import 
# additional packages we need here without having to import them in the main 
# script.
import math


def pythagoras(a: float, b: float) -> float:
    """This is where you usually write a short description of what your function 
    does, in the so-called docstring. The docstring is enclosed in triple 
    quotes, so you can write it in multiple lines.

    Pythagorean theorem that calculates the length of the hypothenuse of a right
    angled triangle when given the length of the triangle legs.

    Parameters
    ----------
    a : float
        The length of the first leg of the triangle.
    b : float
        The length of the second leg of the triangle.

    Returns
    -------
    float
        The calculated length of the hypothenuse.
    """
    # Sum the squares of a and b
    csquared = a**2 + b**2

    # Take the square root
    c = math.sqrt(csquared)

    # Return the final calculation result
    return c


def factorial(n: int) -> int:
    """Calculates the factorial of a number.

    Parameters
    ----------
    n : int
        The number whose factorial is to be calculated.

    Returns
    -------
    int
        The final factorial product of n.
    """
    current_product = 1
    for current_number in range(n):
        # Multiply the current iteration number to the current product
        current_product = current_product*(current_number+1)
    
    return current_product