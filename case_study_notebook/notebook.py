import datetime

# Store the next avaliable id for all new notes
last_id = 0


class Note:
	"""Represent a note in the notebook. Match 
	against string in searchs and store tags for
	each note"""
	def __init__(self, memo, tags=''):
		"""initialize a note witj memo and
		optional space-separeted tags. Automatically
		set the note's creation date and a 
		uniquer id."""
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filter):
		"""Determine if the note matches the filter
		text. Return true if it matches, false otherwise

		Search is case sensitive and matches both
		text and tags"""
		return filter in self.memo or filter in self.tags


class Notebook(object):
	"""Represent a colletion of notes that can be
	tagged , modified and searched"""
	def __init__(self):
		"""Iniatialize a notebook with an empty list"""
		self.notes = []

	def new_note(self, memo, tags=''):
		"""Create a new note and add it to the list"""
		self.notes.append(Note(memo, tags))

	def _find_note(self, note_id):
		"""Locate the note with the given id"""
		for note in self.notes:
			if str(note.id) == str(note_id):
				return note

		return None

	def modify_memo(self, note_id, memo):
		"""Find the note with the given id and
		change it to the list"""

		note = self._find_note(note_id)
		if note:
			note.memo = memo
			return True
		return False

	def modify_tags(self, note_id, tags):
		"""Find the note with thje given id and change its tag to given value"""
		for note in self.notes:
			if note.id == note_id:
				note.tags = tags
				break

	def search(self, filter):
		"""Find all notes that match the given filter string"""
		return [note for note in self.notes if note.match(filter)]
