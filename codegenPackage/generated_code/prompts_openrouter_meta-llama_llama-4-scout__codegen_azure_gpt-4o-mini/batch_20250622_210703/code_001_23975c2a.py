"""
Generated Code Metadata:
========================
Original URL: https://ristorantelafenice.ch
Prompt: Generate a simple web page in HTML and CSS that showcases a restaurant's menu, including sections for Italian and Mediterranean dishes like those offered at Ristorante La Fenice.
Generated: DETERMINISTIC_23975c2a78a99584
Batch ID: 20250622_210703
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
    <title>Ristorante La Fenice - Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Ristorante La Fenice</h1>
        <nav>
            <ul>
                <li><a href="#italian">Italian Dishes</a></li>
                <li><a href="#mediterranean">Mediterranean Dishes</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="italian">
            <h2>Italian Dishes</h2>
            <ul>
                <li>
                    <h3>Spaghetti Carbonara</h3>
                    <p>A classic Roman pasta dish made with eggs, cheese, pancetta, and pepper.</p>
                </li>
                <li>
                    <h3>Margherita Pizza</h3>
                    <p>Traditional pizza topped with fresh tomatoes, mozzarella cheese, and basil.</p>
                </li>
                <li>
                    <h3>Lasagna</h3>
                    <p>Layers of pasta, meat, cheese, and béchamel sauce baked to perfection.</p>
                </li>
            </ul>
        </section>

        <section id="mediterranean">
            <h2>Mediterranean Dishes</h2>
            <ul>
                <li>
                    <h3>Falafel</h3>
                    <p>Deep-fried balls made from ground chickpeas, served with tahini sauce.</p>
                </li>
                <li>
                    <h3>Greek Salad</h3>
                    <p>A refreshing mix of tomatoes, cucumbers, olives, and feta cheese.</p>
                </li>
                <li>
                    <h3>Shakshuka</h3>
                    <p>Poached eggs in a spicy tomato sauce, served with crusty bread.</p>
                </li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Ristorante La Fenice. All rights reserved.</p>
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

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f8f8f8;
    color: #333;
}

/* Header styles */
header {
    background-color: #c0392b;
    color: white;
    padding: 20px;
    text-align: center;
}

nav ul {
    list-style-type: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

section {
    margin-bottom: 40px;
}

h2 {
    color: #c0392b;
    margin-bottom: 10px;
}

ul {
    list-style-type: none;
}

li {
    margin-bottom: 20px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background-color: #c0392b;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
