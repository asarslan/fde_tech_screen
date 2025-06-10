import math 

def sort(width, height, length, mass):
    """
    Returns:
        'STANDARD' if not bulky and not heavy
        'SPECIAL' if bulky or heavy
        'REJECTED' if both bulky and heavy

    Raises:
        TypeError: If any input is not numeric
        ValueError: If any input is non-positive
    """
    
    # Validate types
    if not all(isinstance(x, (int, float)) for x in (width, height, length, mass)):
        raise TypeError

    # Validate positive, non-zero values
    if any(x <= 0 for x in (width, height, length, mass)):
        raise ValueError

    dimensions = (width, height, length)
    is_bulky = math.prod(dimensions) >= 1000000 or max(dimensions) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return 'REJECTED'
    elif is_bulky or is_heavy:
        return 'SPECIAL'
    return 'STANDARD'