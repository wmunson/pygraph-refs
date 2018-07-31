from flask import request, Blueprint, session, g, redirect, url_for, abort, render_template, flash

# from start import app
from app.models import Book, Author

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
	print(request.method)
	return render_template('index.html')
	# if request.method == 'GET':
		# return render_template('index.html')

@views.route('/add_book', methods=['POST'])
def add_book():
	title = request.form['title']
	author = request.form['author']
	tags = request.form['tags']

	if not title:
		abort(400, "Book must have title.")
	if not author:
		abort(400, "Book needs an Author.")
	if not tags:
		abort(400, "Book needs min. one tag.")

	Author(author).submit()
	Book(title, author).submit()

@views.route('/add_author', methods=["POST"])
def add_author():
	print('in author')
	name = request.form['name']
	print(name)
	if not name:
		print('error')
		abort(400, "Author requires name.")
	auth = Author(name)
	print(auth)
	return redirect('/')