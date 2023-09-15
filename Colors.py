class Colors:
	def __init__(self):
		pass


	"""Rainbow colors 
 	   	Arguments:
 	        value {Integer} -- Color manipulation

		Keyword Arguments: None
		Raises: None

    	Returns:
        	[Tupel] -- returns tupel of color range RGB
	"""
	def color(self, value = 0):
		value = (value - (round(value / 360) + (((value / 360) > round(value / 360)) * 1) - 1) * 360)
		red = (((int(value >= 0) == int(120 >= value)) or (int(value >= 300) == int(360 >= value))) * 255) + (((int(value >= 60) == int(120 >= value)) * ((60 - value) * (255 / 60)))) + ((int(value > 240) == int(300 > value)) * ((value - 240) * (255 / 60)))
		green = (((int(value >= 0) == int(60 >= value)) * ((value) * (255 / 60)))) + ((int(value > 60) == int(240 >= value)) * 255) + ((int(value >= 180) == int(240 >= value)) * ((180 - value) * (255 / 60)))
		blue = (((int(value >= 120) == int(180 >= value)) * ((value - 120) * (255 / 60)))) + (((int(value > 180) == int(360 > value)) * 255)) + ((((int(value > 300) == int(360 > value)) * (300 - value) * (255 / 60))))
		return (red, green, blue)


	"""Default colors
		Arguments:
			red {Integer} -- red color
			green {Integer} -- green color
			blue {Integer} -- blue color
			
		Keyword Argments: None
		Raises: None

		Retruns:
			[Tuple] -- return default value
	"""
	def defaultColors(self, red = 0, green = 0, blue = 0):
		return (red, green, blue)