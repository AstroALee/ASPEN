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
    exponent = int(np.floor(np.log10(abs(input_value))))
    coefficient = input_value / (10 ** exponent)
    return coefficient, exponent

