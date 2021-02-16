# Notice the use of a build in method "list"
class ContactList(list):
	def search(self, name):
		"""Return all contacts that contain the 
		search values in their name"""	
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts

class Contact:
	all_contacts = ContactList()
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contacts.append(self)

class Supplier(Contact):
	def order(self, order):
		print("If this were a real system we would send "
		"'{}' order to '{}'".format(order, self.name))

# Overriting a method
class Friend(Contact):
	def __init__(self, name, email, phone):
		# Super will firs fire Contact class
		# and them whe have a new field (phone)
		# This avoid the redundanci of name and email
		super().__init__(name, email)
		self.phone = phone