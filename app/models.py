from py2neo import Graph, Node, Relationship

graph = Graph()

class Book:
	def __init__(self, title):
		self.title = title

	def find(self):
		book = graph.find_one('Book', 'title', self.title)
		return book

	def submit(self, categories):
		if not self.find():
			book = Node('Book', title=self.title)
			graph.create(book)
			categories = [x.strip() for x in categories.lower().split(',')]
			for t in set(categories):
				tag = graph.merge_one('Category','name',t)
				rel = Relationship(tag,'TAGGED')
			return True
		else:
			return False

# Think about if each book submission needs references in order to submit, or if refs can be added later?
