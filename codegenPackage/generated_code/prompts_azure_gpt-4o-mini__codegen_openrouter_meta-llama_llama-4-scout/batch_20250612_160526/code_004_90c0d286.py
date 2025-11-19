"""
Generated Code Metadata:
========================
Original URL: https://andreeabalogh.com
Prompt: Design a simple web application that showcases Andreea Balogh's recommendations for books and movies, using Flask or Django.
Generated: DETERMINISTIC_90c0d2865c4181ed
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Simple Web Application using Flask**

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define models for books and movies
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.director}')"


# Create the database tables
with app.app_context():
    db.create_all()


# Home route
@app.route('/')
def home():
    books = Book.query.all()
    movies = Movie.query.all()
    return render_template('home.html', books=books, movies=movies)


# Add book route
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        description = request.form['description']
        new_book = Book(title=title, author=author, description=description)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_book.html')


# Add movie route
@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        director = request.form['director']
        description = request.form['description']
        new_movie = Movie(title=title, director=director, description=description)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_movie.html')


# Edit book route
@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.description = request.form['description']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_book.html', book=book)


# Edit movie route
@app.route('/edit_movie/<int:movie_id>', methods=['GET', 'POST'])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.director = request.form['director']
        movie.description = request.form['description']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_movie.html', movie=movie)


# Delete book route
@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


# Delete movie route
@app.route('/delete_movie/<int:movie_id>')
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/home.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andreea Balogh's Recommendations</title>
</head>
<body>
    <h1>Andreea Balogh's Recommendations</h1>
    <h2>Books:</h2>
    <ul>
    {% for book in books %}
        <li>{{ book.title }} by {{ book.author }} - {{ book.description }}
            <a href="{{ url_for('edit_book', book_id=book.id) }}">Edit</a>
            <a href="{{ url_for('delete_book', book_id=book.id) }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_book') }}">Add a new book</a></p>
    <h2>Movies:</h2>
    <ul>
    {% for movie in movies %}
        <li>{{ movie.title }} by {{ movie.director }} - {{ movie.description }}
            <a href="{{ url_for('edit_movie', movie_id=movie.id) }}">Edit</a>
            <a href="{{ url_for('delete_movie', movie_id=movie.id) }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_movie') }}">Add a new movie</a></p>
</body>
</html>
```

```html
<!-- templates/add_book.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a new book</title>
</head>
<body>
    <h1>Add a new book</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="author">Author:</label>
        <input type="text" id="author" name="author"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Add book">
    </form>
</body>
</html>
```

```html
<!-- templates/add_movie.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a new movie</title>
</head>
<body>
    <h1>Add a new movie</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="director">Director:</label>
        <input type="text" id="director" name="director"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Add movie">
    </form>
</body>
</html>
```

```html
<!-- templates/edit_book.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit book</title>
</head>
<body>
    <h1>Edit book</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" value="{{ book.title }}"><br><br>
        <label for="author">Author:</label>
        <input type="text" id="author" name="author" value="{{ book.author }}"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description">{{ book.description }}</textarea><br><br>
        <input type="submit" value="Save changes">
    </form>
</body>
</html>
```

```html
<!-- templates/edit_movie.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit movie</title>
</head>
<body>
    <h1>Edit movie</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" value="{{ movie.title }}"><br><br>
        <label for="director">Director:</label>
        <input type="text" id="director" name="director" value="{{ movie.director }}"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description">{{ movie.description }}</textarea><br><br>
        <input type="submit" value="Save changes">
    </form>
</body>
</html>
```
