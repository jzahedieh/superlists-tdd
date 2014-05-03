from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edith goes the the homepage and accidentally tries to submit
		# a empty list item, she hits enter on the empty input box
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# The homepage refreshes and there is an error message saying that
		# the list items cannot be blank
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# she tries again with some text for the item, which now works
		self.browser.find_element_by_id('id_new_item').send_keys('By milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# she now decides to submit a second blank list item
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# she receives  a similar warning on the list page
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# and she can correct it by filling some text in
		self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')

	