from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith goes the the homepage and accidentally tries to submit
		# a empty list item, she hits enter on the empty input box

		# The homepage refreshes and there is an error message saying that
		# the list items cannot be blank

		# she tries again with some text for the item, which now works

		# she now decides to submit a second blnk list item

		# she receives  a similar warning onthe list page

		# and she can correct it by filling some text in

		self.fail('write me')
	