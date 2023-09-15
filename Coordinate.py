import math


class Coordinate:
    """Sinus coordinate
        Arguments:
            value {integer, float} -- passes as integer or float

        Keyword Arguments: None
	    Raises: None

        Returns:
            [float] -- returns coordinats of sinus
    """
    def sin(self, value):
        return math.sin((22 / 7) / 180 * value)


    """Cosinus coordinate
        Arguments:
            value {integer, float} -- passes as integer or float

        Keyword Arguments: None
	    Raises: None

        Returns:
            [float] -- returns coordinats of cosinus
    """
    def cos(self, value):
        return math.cos((22 / 7) / 180 * value)