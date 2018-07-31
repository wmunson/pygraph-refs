from py2neo import Graph, Node, Relationship

graph = Graph(password='admin')

class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = Author(author).find()
		self.submit()

	def find(self):
		book = graph.match_one('Book', 'title', self.title)
		return book

	def submit(self, categories):
		if not self.find():
			book = Node('Book', title=self.title, author=self.author)
			graph.create(book)
			categories = [x.strip() for x in categories.lower().split(',')]
			for t in set(categories):
				tag = graph.merge_one('Category','name',t)
				rel = Relationship(tag,'TAGGED', book)
				graph.create(rel)
			# author = Author(self.author).find()
			auth_rel = Relationship(self.author, 'WROTE', book)
			graph.create(auth_rel)
			return True
		else:
			return False


	# def add_book_reference(self, Book):
	# 	if not Book.find():
	# 		book = Node('Book', title=Book.title, year=Book.year)
	# 		graph.create(book)
	# 	book = graph.find_one('Book','title', Book.title, 'year', Book.year)	
	# 	rel = Relationship(self, 'REFERENCED', book)
	# 	graph.createe(rel)
	# 	return True



class Author:

	def __init__(self, name):
		self.name = name
		self.submit()

	def find(self):
		name =  self.name
		author = graph.match_one('Author', 'name', name)
		return author

	# def find(self):
	# 	author = graph.match_one('Author', 'name', self.name)
	# 	if not author:
	# 		self.submit()
	# 		author = graph.match_one('Author', 'name', self.name)
	# 	return author

	def submit(self):
		if not self.find():
			author = Node('Author', name=self.name)
			grpah.create(author)
			return True
		else:
			return False
