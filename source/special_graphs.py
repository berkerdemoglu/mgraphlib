import matplotlib.pyplot as plt
from math import sqrt

class CoordinateSystem():
	"""A class that represents the coordinate system."""

	def __init__(self):
		"""Initialize a coordinate system's axes' length and color."""
		self.axis = [1]
		self.color = 'black'

	def draw_coordinate_system(self):
		"""Draw the coordinate system."""
		plt.plot(self.axis, [0 for i in range(len(self.axis))], 
			c=self.color, linewidth=2)
		plt.plot([0 for i in range(len(self.axis))], self.axis, 
			c=self.color, linewidth=2)


class UnitCircle():
	"""A class for the unit circle."""

	def __init__(self, color='black'):
		"""Initialize the unit circle."""
		self.color = color

		# Define the unit circle equation and the domain and its image.
		f = lambda x: sqrt(1 - pow(x, 2))
		self.domain = tuple([x/10000 for x in range(-10000, 10001)])
		self.image_positive_y = tuple(map(f, self.domain))
		self.image_negative_y = tuple([-y for y in self.image_positive_y])

	def draw_unit_circle(self):
		"""Draw the unit circle."""
		plt.scatter(self.domain, self.image_positive_y, c=self.color, s=8)
		plt.scatter(self.domain, self.image_negative_y, c=self.color, s=8)