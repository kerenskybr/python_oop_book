from urllib.request import urlopen

class WebPage:
	def __init__(self, url):
		self.url = url
		self._content = None

	# crating a custom getter to cache previous retrieved data
	# as a private atribute on our object to avoid much calculation
	@property
	def content(self):
		if not self._content:
			print("Retrieving new page...(not cached)")
			self._content = urlopen(self.url).read()
		return self._content
	