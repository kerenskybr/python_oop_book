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

####################
# From here, multiple inheritance

class MailSender:
	def send_mail(self, message):
		print("Sending email to " + self.email)
		# Logic goes here

# Inheriting from Contact and MailSender
#BUT, we could also do:
# A standalone function to send email and just call it
# Create the method send email inside Contact, or
#EmailableContact itself
class EmailableContact(Contact, MailSender):
	pass

class AddressHolder:
	def __init__(self, street, city, state, code):
		self.street = street
		self.city = city
		self.state = state
		self.code = code