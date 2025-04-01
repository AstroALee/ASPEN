'''
Colorbar generation and nice colorbars for matplotlib
'''

import numpy as np
from matplotlib.colors import ListedColormap, to_rgba
from cycler import cycler

import matplotlib.pyplot as plt

"""
Notes: Dictionary keys are data, not variables — they are meant to be accessed dynamically, 
and all-caps keys are awkward to type and read in most use cases. So they are lowercase.
"""




# Saint Mary's College of California color dictionary
# Order matters for the cycler 
SMC_COLORS: dict[str, str] = {
    "red" : '#CF3339' ,     # slightly dark red 
    "navy" : '#143257' ,    # dark navy
    "water" : '#6298C3' , # fountain water, muted blue 
    "sun" : '#F2BA2A' , # gold 
    "canyon" : '#0A5B5E' , # dark teal green 
    "silver" : '#afb0a2' , # darker silver from '#BEC1C1' 
    "lawn" : '#67934F' , # grass green 
    "bay" : '#6CC2C3' , # light teal 
    "skies" : '#13A3CE' , # brighter sky blue 
    "garden" : '#F3B3A2' , # salmon color 
    "origsilver" : '#BEC1C1', # original silver 
    "gray" : '#81959B' , # gael gray 
    "cross" : '#D1D2C4' , # off-white 
}

# Cycler for SMC colors
SMC_cycler = cycler(color=SMC_COLORS.values())




# Northwestern University color dictionary
# Order matters for the cycler 
NORTHWESTERN_COLORS: dict[str, str] = {
    "purple" : '#4e2b84' , # Northwestern purple
    "lighterpurple" : '#a393c0' , # Lighter purple
    "darkestpurple" : '#260642' , # Darkest purple
    "lightpurple" : '#765d9f' , # Light purple
    "lightestpurple" : '#e1ddec' , # Lightest purple
    "darkpurple" : '#38185b' , # Dark purple
    "lightgray" : '#f0f0f0' , # Light gray
}

# Cycler for Northwestern colors
NU_cycler = cycler(color=NORTHWESTERN_COLORS.values())



# UC Berkeley color dictionary
# Order matters for the cycler 
UCB_COLORS: dict[str, str] = {
    "blue" : '#1c2676' , # Berkeley Blue
    "heritage" : '#c09748' , # Heritage Gold
    "rose" : '#770747' , # Rose
    "purple" : '#431170' , # Purple
    "green" : '#19553a' , # Green
    "gray" : '#808080' , # Gray
    "lightgray" : '#f2f2f2' , # Light Gray
    "gold" : '#f4b516' , # California Gold
}

# Cycler for UC Berkeley colors
UCB_cycler = cycler(color=UCB_COLORS.values())


# Color themes used in LaTeX documents 
AARON_TEAL_THEME: dict[str, str] = {
    "color1" : '#348b8a' , # Teal
    "color2" : '#99111f' , # Red
    "color3" : '#d39f0c' , # Gold
    "color4" : '#153257' , # Navy
    "colorlinks" : '#284695' , # Blue
}

# Cycler for Aaron's Teal theme
TEAL_cycler = cycler(color=AARON_TEAL_THEME.values())



AARON_RED_THEME: dict[str, str] = {
    "color1" : '#99111f' , # Red
    "color2" : '#348b8a' , # Teal
    "color3" : '#d39f0c' , # Gold
    "color4" : '#153257' , # Navy
    "colorlinks" : '#284695' , # Blue
}

# Cycler for Aaron's Red theme
RED_cycler = cycler(color=AARON_RED_THEME.values())



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

def use_smc_colors_default():
    """
    Set the default color cycle to the Saint Mary's College color scheme.
    """
    plt.rcParams.update({
        'image.cmap' : SMC_cmap,
        'axes.prop_cycle' : SMC_cycler,
    })
    return None


# Northwestern Colormap (decent sequential map)
NU_cmap: ListedColormap = make_color_map([NORTHWESTERN_COLORS['lightestpurple'],NORTHWESTERN_COLORS['lighterpurple'],NORTHWESTERN_COLORS['lightpurple'],NORTHWESTERN_COLORS['purple'],NORTHWESTERN_COLORS['darkpurple'],NORTHWESTERN_COLORS['darkestpurple']])

def use_nu_colors_default():
    """
    Set the default color cycle to the Northwestern color scheme.
    """
    plt.rcParams.update({
        'image.cmap' : NU_cmap,
        'axes.prop_cycle' : NU_cycler,
    })
    return None


# UC Berkeley Colormap (decent diverging map)
UCB_cmap: ListedColormap = make_color_map([UCB_COLORS['blue'],UCB_COLORS['lightgray'],UCB_COLORS['gold']])

def use_ucb_colors_default():
    """
    Set the default color cycle to the UC Berkeley color scheme.
    """
    plt.rcParams.update({
        'image.cmap' : UCB_cmap,
        'axes.prop_cycle' : UCB_cycler,
    })
    return None
