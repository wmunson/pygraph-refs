from flask import request, session, g, redirect, url_for, abort, render_template, flash

from app import app
from models import Book

@app.route('/add_book', methods=['POST'])
def add_book():
	title = request.form['title']
	tags = request.form['tags']

	if not title:
		abort(400, "Book must have title.")
	if not tags:
		abort(400, "Book needs min. one tag.")

	Book(title).submit()