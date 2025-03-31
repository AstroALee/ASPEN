'''
Colorbar generation and nice colorbars for matplotlib
'''

import numpy as np
from matplotlib.colors import ListedColormap, to_rgba

"""
Notes: Dictionary keys are data, not variables — they are meant to be accessed dynamically, 
and all-caps keys are awkward to type and read in most use cases. So they are lowercase.
"""


# Saint Mary's College of California color dictionary
SMC_COLORS: dict[str, str] = {
    "red" : '#CF3339' ,     # slightly dark red 
    "navy" : '#143257' ,    # dark navy
    "silver" : '#afb0a2' , # darker silver from '#BEC1C1' 
    "origsilver" : '#BEC1C1', # original silver 
    "garden" : '#F3B3A2' , # salmon color 
    "bay" : '#6CC2C3' , # light teal 
    "gray" : '#81959B' , # gael gray 
    "sun" : '#F2BA2A' , # gold 
    "canyon" : '#0A5B5E' , # dark teal green 
    "cross" : '#D1D2C4' , # off-white 
    "lawn" : '#67934F' , # grass green 
    "water" : '#6298C3' , # fountain water, muted blue 
    "skies" : '#13A3CE' , # brighter sky blue 
}

# Northwestern University color dictionary
NORTHWESTERN_COLORS: dict[str, str] = {
    "darkestpurple" : '#260642' , # Darkest purple
    "darkpurple" : '#38185b' , # Dark purple
    "purple" : '#4e2b84' , # Northwestern purple
    "lightpurple" : '#765d9f' , # Light purple
    "lighterpurple" : '#a393c0' , # Lighter purple
    "lightestpurple" : '#e1ddec' , # Lightest purple
    "lightgray" : '#f0f0f0' , # Light gray
}

# UC Berkeley color dictionary
UCB_COLORS: dict[str, str] = {
    "blue" : '#1c2676' , # Berkeley Blue
    "gold" : '#f4b516' , # California Gold
    "rose" : '#770747' , # Rose
    "purple" : '#431170' , # Purple
    "green" : '#19553a' , # Green
    "gray" : '#808080' , # Gray
    "lightgray" : '#f2f2f2' , # Light Gray
    "heritage" : '#c09748' , # Heritage Gold
}

# Color themes used in LaTeX documents 
AARON_TEAL_THEME: dict[str, str] = {
    "color1" : '#348b8a' , # Teal
    "color2" : '#99111f' , # Red
    "color3" : '#d39f0c' , # Gold
    "color4" : '#153257' , # Navy
    "colorlinks" : '#284695' , # Blue
}

AARON_RED_THEME: dict[str, str] = {
    "color1" : '#99111f' , # Red
    "color2" : '#348b8a' , # Teal
    "color3" : '#d39f0c' , # Gold
    "color4" : '#153257' , # Navy
    "colorlinks" : '#284695' , # Blue
}



def make_color_map(listColors: list[str], num_points: int = 512, 
                    leftColor: str | None = None, rightColor: str | None = None ) -> ListedColormap:
    """
    Create a colormap from a list of colors by linearly interpolating across RGB values.

    Args:
        listColors (list of str): List of color hex codes or color names.
        num_points (int, opt = 512): Number of interpolated color points in the resulting colormap.
        leftColor (str, optional): Special color to use for the left end (0) of the colormap.
        rightColor (str, optional): Special color to use for the right end (1) of the colormap.

    Returns:
        ListedColormap: A matplotlib ListedColormap object with the interpolated colors.
    """


    num_provided_colors = len(listColors)
    assert num_provided_colors>1 , f'Need at least two colors for listColors: {listColors}' 
    assert num_points>=num_provided_colors , f"Really... num_points ({num_points}) \
                                                < num_provided_colors ({num_provided_colors})!?" 

    # Convert to RGBA
    colors_RGBA: list[tuple[float, float, float, float]] = [to_rgba(c) for c in listColors]

    # Will hold RGBA values 
    vals: np.ndarray = np.ones((num_points, 4))

    for i in range(4):
        vals[:, i] = np.interp(np.linspace(0, 1, num=num_points), 
                                np.linspace(0, 1, num=num_provided_colors), [c[i] for c in colors_RGBA])

    # Override left and right colors if specified 
    if leftColor is not None:
        left_RGBA = to_rgba(leftColor)
        vals[0, :] = left_RGBA  # set the first color (left end)

    if rightColor is not None:
        right_RGBA = to_rgba(rightColor)
        vals[-1, :] = right_RGBA

    return( ListedColormap(vals) )




# Saint Mary's College Colormaps 
SMC_cmap: ListedColormap = make_color_map([SMC_COLORS['red'],SMC_COLORS['origsilver'],SMC_COLORS['navy']])

# Northwestern Colormap (decent sequential map)
NU_cmap: ListedColormap = make_color_map([NORTHWESTERN_COLORS['lightestpurple'],NORTHWESTERN_COLORS['lighterpurple'],NORTHWESTERN_COLORS['lightpurple'],NORTHWESTERN_COLORS['purple'],NORTHWESTERN_COLORS['darkpurple'],NORTHWESTERN_COLORS['darkestpurple']])

# UC Berkeley Colormap (decent diverging map)
UCB_cmap: ListedColormap = make_color_map([UCB_COLORS['blue'],UCB_COLORS['lightgray'],UCB_COLORS['gold']])
