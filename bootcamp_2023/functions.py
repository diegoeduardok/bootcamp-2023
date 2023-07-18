import numpy as np

def calculate_distance(rA: np.ndarray, rB: np.ndarray) -> float:
    """
    Calculate distance between two points.

    Parameters
    ----------
    rA, rB: np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance: float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.asarray([0, 0, 0])
    >>> r2 = np.asarray([0, 1, 0])
    >>> calculate_distance(r1, r2)
    1
    """
    # This function calculates the distance between two points given as numpy arrays.
    d = rA - rB
    dist = np.linalg.norm(d)
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

"""Provide the primary functions."""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination. (Diego was here.)"
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def hello_world(with_attribution: bool = True):
    """
    Hello world.
    """
    quote = "Hello world!"
    if with_attribution:
        quote += "\n\t- Diego K."
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
