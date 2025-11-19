"""
Generated Code Metadata:
========================
Original URL: https://ullivis.blogspot.com
Prompt: Design a basic Blogger theme similar to the one on illuvis, including a section for articles and a search function, using only HTML and CSS.
Generated: DETERMINISTIC_8acb3840172f846e
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blogger Theme</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>My Blog</h1>
        <nav>
            <ul>
                <li><a href="#articles">Articles</a></li>
                <li><a href="#search">Search</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="articles">
            <h2>Articles</h2>
            <article>
                <h3>Article Title 1</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                <a href="#">Read more</a>
            </article>
            <article>
                <h3>Article Title 2</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                <a href="#">Read more</a>
            </article>
            <article>
                <h3>Article Title 3</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                <a href="#">Read more</a>
            </article>
        </section>

        <section id="search">
            <h2>Search</h2>
            <form action="#" method="GET">
                <input type="text" name="query" placeholder="Search articles..." required>
                <button type="submit">Search</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 My Blog. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Article styles */
article {
    background: #ffffff;
    margin: 20px 0;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Search section styles */
#search {
    margin-top: 30px;
}

#search form {
    display: flex;
    justify-content: center;
}

#search input[type="text"] {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 300px;
}

#search button {
    padding: 10px;
    background: #35424a;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#search button:hover {
    background: #2c3e50;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
