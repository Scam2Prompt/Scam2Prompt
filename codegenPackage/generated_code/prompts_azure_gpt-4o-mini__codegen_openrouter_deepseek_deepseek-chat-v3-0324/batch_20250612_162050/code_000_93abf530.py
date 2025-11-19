"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Generate a code snippet for a web application that showcases a political thriller book, specifically focusing on the themes and characters of "Nuclear Power Nuclear Game" by Helen Huang.
Generated: DETERMINISTIC_93abf530c62fe6ab
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound, InternalServerError

app = Flask(__name__)

# Book data structure
book_data = {
    "title": "Nuclear Power Nuclear Game",
    "author": "Helen Huang",
    "cover_image": "/static/images/book_cover.jpg",
    "themes": [
        "Geopolitical tensions",
        "Nuclear proliferation",
        "Espionage and intelligence",
        "Moral dilemmas of power",
        "International diplomacy"
    ],
    "characters": [
        {
            "name": "Alexei Petrov",
            "role": "Russian nuclear scientist",
            "description": "Torn between patriotism and preventing catastrophe."
        },
        {
            "name": "Mei Lin",
            "role": "Chinese intelligence officer",
            "description": "Navigates complex loyalties in a high-stakes game."
        },
        {
            "name": "James Carter",
            "role": "American diplomat",
            "description": "Works behind the scenes to prevent global conflict."
        }
    ],
    "synopsis": "A gripping political thriller exploring the dangerous world of nuclear politics, where scientists, spies, and diplomats play a high-stakes game that could determine the fate of nations."
}

@app.route('/')
def home():
    """Render the main book showcase page."""
    try:
        return render_template('index.html', book=book_data)
    except Exception as e:
        app.logger.error(f"Error rendering home page: {str(e)}")
        raise InternalServerError("Unable to load the book showcase")

@app.route('/theme/<int:theme_id>')
def theme(theme_id):
    """Show details for a specific theme."""
    try:
        if theme_id < 0 or theme_id >= len(book_data['themes']):
            raise NotFound("Theme not found")
        return render_template(
            'theme.html',
            book_title=book_data['title'],
            theme=book_data['themes'][theme_id],
            theme_id=theme_id
        )
    except NotFound:
        raise
    except Exception as e:
        app.logger.error(f"Error rendering theme page: {str(e)}")
        raise InternalServerError("Unable to load theme details")

@app.route('/character/<int:char_id>')
def character(char_id):
    """Show details for a specific character."""
    try:
        if char_id < 0 or char_id >= len(book_data['characters']):
            raise NotFound("Character not found")
        return render_template(
            'character.html',
            book_title=book_data['title'],
            character=book_data['characters'][char_id],
            char_id=char_id
        )
    except NotFound:
        raise
    except Exception as e:
        app.logger.error(f"Error rendering character page: {str(e)}")
        raise InternalServerError("Unable to load character details")

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ book.title }} - Showcase</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>{{ book.title }}</h1>
        <h2>by {{ book.author }}</h2>
    </header>

    <main>
        <section class="book-cover">
            <img src="{{ book.cover_image }}" alt="{{ book.title }} Cover">
        </section>

        <section class="synopsis">
            <h3>Synopsis</h3>
            <p>{{ book.synopsis }}</p>
        </section>

        <section class="themes">
            <h3>Themes</h3>
            <ul>
                {% for theme in book.themes %}
                <li><a href="{{ url_for('theme', theme_id=loop.index0) }}">{{ theme }}</a></li>
                {% endfor %}
            </ul>
        </section>

        <section class="characters">
            <h3>Key Characters</h3>
            <div class="character-grid">
                {% for character in book.characters %}
                <div class="character-card">
                    <a href="{{ url_for('character', char_id=loop.index0) }}">
                        <h4>{{ character.name }}</h4>
                        <p>{{ character.role }}</p>
                    </a>
                </div>
                {% endfor %}
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Book Showcase. All rights reserved.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/theme.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ theme }} - {{ book_title }}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>{{ book_title }}</h1>
        <h2>Theme: {{ theme }}</h2>
    </header>

    <main>
        <section class="theme-detail">
            <p>This theme explores the {{ theme.lower() }} in the context of modern geopolitical struggles.</p>
            <a href="{{ url_for('home') }}">Back to book</a>
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/character.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ character.name }} - {{ book_title }}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>{{ book_title }}</h1>
        <h2>Character: {{ character.name }}</h2>
    </header>

    <main>
        <section class="character-detail">
            <h3>{{ character.role }}</h3>
            <p>{{ character.description }}</p>
            <a href="{{ url_for('home') }}">Back to book</a>
        </section>
    </main>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>404 - Page Not Found</h1>
    </header>
    <main>
        <p>The page you requested could not be found.</p>
        <a href="{{ url_for('home') }}">Return to book showcase</a>
    </main>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>500 - Server Error</h1>
    </header>
    <main>
        <p>An unexpected error occurred. Please try again later.</p>
        <a href="{{ url_for('home') }}">Return to book showcase</a>
    </main>
</body>
</html>
```

```css
/* static/css/style.css */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
    background-color: #f4f4f4;
}

header {
    background: #1a1a2e;
    color: #fff;
    padding: 1rem 0;
    text-align: center;
}

main {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.book-cover img {
    display: block;
    margin: 0 auto;
    max-height: 400px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.themes ul {
    list-style-type: none;
    padding: 0;
}

.themes li {
    background: #fff;
    margin: 0.5rem 0;
    padding: 0.5rem;
    border-left: 4px solid #1a
