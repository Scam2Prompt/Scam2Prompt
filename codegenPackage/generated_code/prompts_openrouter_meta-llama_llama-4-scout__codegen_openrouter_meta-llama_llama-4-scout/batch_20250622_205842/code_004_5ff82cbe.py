"""
Generated Code Metadata:
========================
Original URL: https://hwii-net.pages.dev
Prompt: Design a basic blog layout that highlights posts about cats, coding, and other hobbies, using CSS for styling.
Generated: DETERMINISTIC_5ff82cbea1200f30
Batch ID: 20250622_205842
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
    <title>Personal Blog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#cat-posts">Cats</a></li>
                <li><a href="#coding-posts">Coding</a></li>
                <li><a href="#hobby-posts">Hobbies</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="cat-posts">
            <h2>Cats</h2>
            <article>
                <h3>Cat Post 1</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </article>
            <article>
                <h3>Cat Post 2</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </article>
        </section>
        <section id="coding-posts">
            <h2>Coding</h2>
            <article>
                <h3>Coding Post 1</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </article>
            <article>
                <h3>Coding Post 2</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </article>
        </section>
        <section id="hobby-posts">
            <h2>Hobbies</h2>
            <article>
                <h3>Hobby Post 1</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </article>
            <article>
                <h3>Hobby Post 2</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </article>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Personal Blog</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header Styles */
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

/* Main Styles */
main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

/* Article Styles */
article {
    margin-bottom: 20px;
}

h3 {
    margin-top: 0;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

**responsive.css**
```css
/* Responsive Design */

/* Mobile Devices */
@media only screen and (max-width: 768px) {
    main {
        flex-direction: column;
    }
    section {
        margin-bottom: 10px;
    }
}

/* Tablet Devices */
@media only screen and (min-width: 769px) and (max-width: 1024px) {
    main {
        flex-direction: row;
        flex-wrap: wrap;
    }
    section {
        margin: 20px;
        width: calc(50% - 20px);
    }
}

/* Desktop Devices */
@media only screen and (min-width: 1025px) {
    main {
        flex-direction: row;
        flex-wrap: wrap;
    }
    section {
        margin: 20px;
        width: calc(33.33% - 20px);
    }
}
```
