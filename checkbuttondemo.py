"""

Program: checkbuttondemo.py
Author: Narvar 11/15/2021

*** Note: the file breezypythongui.py Must be in the same directory as this file for the application to work***

***This module studies and plays the game of craps.
Refactors code from case study so that the user
can have the Player object roll the dice and view
the result.***

"""

from breezypythongui import EasyFrame

class CheckButtonDemo(EasyFrame):
	"""Allows the user to place a resturant order from a set of options."""


		


	def __init__(self):
		"""Sets up the window and widgets."""
		EasyFrame.__init__(self, title ="Check Button Demo")

		#Add four check buttons 
		self.chickCB = self.addCheckbutton(text = "Chicken", row = 0, column = 0)
		self.taterCB = self.addCheckbutton(text = "French Fries", row = 0, column = 1)
		self.beanCB = self.addCheckbutton(text = "Green Beans", row = 1, column = 0)
		self.sauceCB = self.addCheckbutton(text = "Applesauce", row = 1, column = 1)

		#Add the comand button
		self.addButton(text = "Place order", row = 2, column = 0, columnspan = 2, command = self.placeOrder)
	# Event handling event	
	def placeOrder(self):
		"""Display a message bex with order information."""
		message = ""
		if self.chickCB.isChecked():
			message += "Chicken\n\n"
		if self.taterCB.isChecked():
			message += "French Fries\n\n"
		if self.beanCB.isChecked():
			message += "Green Beans\n\n"
		if self.sauceCB.isChecked():
			message += "Applesauce\n"
		if message == "": message = "No food ordered!"
		self.messageBox(title = "Customer Order", message = message)
		
		
# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	CheckButtonDemo().mainloop()

# global call to trigger main() function
if __name__ == "__main__":
	main()