import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math

import special_graphs

class Graph():
	"""A base class for all graphs in the module."""
	graph_colors = iter(['#C74440', '#2D70B3', '#388C46', '#6042A5'])
	drawn_graph_legends = []

	def __init__(self, x_values, y_values, **coord_kwargs):
		"""Initialize the graph color, the graph domain and its image."""
		self.color = next(Graph.graph_colors, 'black')
		self.domain = x_values
		self.image = y_values

		# Set its label for use in the legend.
		self.label = len(Graph.drawn_graph_legends) + 1

		# Set coordinate system configuration details.
		Graph.coord_kwargs = coord_kwargs
		try:
			if Graph.coord_kwargs['cs']:
				Graph.cs = special_graphs.CoordinateSystem()
		except KeyError:
			pass
		else:
			self.set_coordinate_system_details()

	@classmethod
	def set_coordinate_system_details(cls):
		"""Called in the constructor function to determine 
		coordinate system's length and if it will be used or not."""
		try:
			cls.cs.axis = list(range(-Graph.coord_kwargs['cs_length'], 
				Graph.coord_kwargs['cs_length'] + 1))
		except KeyError:
			cls.cs.axis = list(range(-10000, 10000))
		finally:
			cls.cs.draw_coordinate_system()

	def draw(self):
		"""Draw the graph and add it to drawn graphs."""
		Graph.drawn_graph_legends.append(mlines.Line2D([], [], 
			color=self.color, label='Graph ' + str(self.label)))

		plt.scatter(self.domain, self.image, c=self.color, s=5)

	@classmethod
	def show_graphs(cls):
		"""Makes all drawn graphs visible."""
		plt.axis([-Graph.cs.axis, Graph.cs.axis, -Graph.cs.axis, Graph.cs.axis])

		plt.legend(loc='lower left', handles=Graph.drawn_graph_legends)
		plt.subplots_adjust(left=0.3, bottom=0.12, right=0.7, 
			top=0.88, wspace=0, hspace=0)
		plt.show()


class TrigGraph(Graph):
	"""A base class for trigonometric function graphs."""

	def __init__(self, min_degrees=0, max_degrees=360):
		pass


if __name__ == '__main__':
	g = Graph(list(range(100)), list(range(100)), cs=True, cs_length=100)
	g2 = Graph(list(range(-100, 0)), list(range(-100, 0)))

	g.draw()
	g2.draw()
	Graph.show_graphs()