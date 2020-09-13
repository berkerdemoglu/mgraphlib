####################################
############ EXCEPTIONS ############
####################################

class Error(Exception):
	"""A base class for all errors in the module."""
	pass

class EquationError(Error):
	"""The error raised when an invalid equation is provided."""
	def __init__(self, invalid_equation):
		"""Print a message informing what was wrong with the equation."""
		message = "Invalid equation: '{}'".format(invalid_equation)
		super().__init__()


####################################
########## EQUATIONPARSER ##########
####################################

class EquationParser():
	"""A class that parses mathematical equations."""

	def __init__(self, equation):
		"""Initialize an equation parser with an equation."""
		self.equation = equation

		# Set the list of operators.
		self.operators = ('+', '-', '/', '^')

	def parse_equation(self):
		"""Parses the equation and returns a lambda function."""
		self.equation = self.equation.replace(' ', '')
		switcher = {
			'+': '+',
			'-': '-',
			'/': '/',
			'^': '**'
		}

		for char in self.equation:
			if char in self.operators:
				self.equation = self.equation.replace(char, switcher[char])

		self.f = lambda x: eval(self.equation)
		return self.f

	def create_image(self, domain):
		"""Creates and returns the image set of a domain."""
		image = list(map(self.f, domain))
		return image


ep = EquationParser('print("bruh")')
# x^2+6x+8
ep.parse_equation()
ep.f(5)