"""
Generated Code Metadata:
========================
Original URL: https://www.bicho.se
Prompt: Generate a simple web page using HTML and CSS that showcases Jenny Bicho's books and David Bicho's photography work.
Generated: DETERMINISTIC_0acb4a28ae92d572
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jenny Bicho's Books and David Bicho's Photography</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Jenny Bicho's Books and David Bicho's Photography</h1>
        <nav>
            <ul>
                <li><a href="#books">Jenny's Books</a></li>
                <li><a href="#photography">David's Photography</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="books">
            <h2>Jenny Bicho's Books</h2>
            <div class="book-grid">
                <div class="book">
                    <img src="book1-cover.jpg" alt="Book 1 Cover">
                    <h3>Book 1 Title</h3>
                    <p>Book 1 Description</p>
                </div>
                <div class="book">
                    <img src="book2-cover.jpg" alt="Book 2 Cover">
                    <h3>Book 2 Title</h3>
                    <p>Book 2 Description</p>
                </div>
                <!-- Add more books here -->
            </div>
        </section>
        <section id="photography">
            <h2>David Bicho's Photography</h2>
            <div class="photo-grid">
                <div class="photo">
                    <img src="photo1.jpg" alt="Photo 1">
                    <p>Photo 1 Description</p>
                </div>
                <div class="photo">
                    <img src="photo2.jpg" alt="Photo 2">
                    <p>Photo 2 Description</p>
                </div>
                <!-- Add more photos here -->
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Jenny Bicho and David Bicho</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

.book-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.book {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.book img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

.photo-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.photo {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.photo img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
