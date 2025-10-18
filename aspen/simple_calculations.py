'''
Intended for simple calculations as a set of a standalone functions. 
'''

import numpy as np


def scientific_notation(input_value: float) -> tuple[float, int]:
    """
    Convert a number to scientific notation.

    Args:
        input_value (float): The number to convert.

    Returns:
        tuple[float, int]: The coefficient and exponent of the input value in scientific notation.
    """
    # Check for non-finite values
    if not np.isfinite(input_value):
        raise ValueError(f"Input {input_value} is not finite -- can't convert to scientific notation.")
    # Check for zero
    if input_value == 0:
        return 0.0, 0
    exponent =  np.log10(abs(input_value))//1 # float 
    exponent = int(exponent) # int 
    coefficient = input_value / (10 ** exponent)
    return coefficient, exponent


def round_uncertainty(pbest : float, dp: float) -> tuple[float, float]:
    """
    Rounds the uncertainty to one or two significant figures and rounds the best estimate to the same decimal place.
    Args:
        pbest (float): The best estimate.
        dp (float): The uncertainty.
    Returns:
        tuple[float, float]: The rounded best estimate and uncertainty.
    """
    # A negative second input for round means rounding to the left of the decimal point.
    round_to = -int(scientific_notation(dp)[1]) if (scientific_notation(dp)[0])//1>2 \
        else 1-int(scientific_notation(dp)[1])
    return round(pbest, round_to), round(dp, round_to)