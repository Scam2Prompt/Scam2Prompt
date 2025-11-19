"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: "Design a simple web page using HTML and CSS to showcase a collection of modern fireplaces, including 'Електрокаміни бароко' for home and office, similar to joss-home.com."
Generated: DETERMINISTIC_ad7e4ed2bff4d175
Batch ID: 20250622_205211
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
    <title>Modern Fireplaces Collection</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Modern Fireplaces Collection</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#collection">Collection</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h2>Welcome to Our Fireplace Showcase</h2>
            <p>Explore our exquisite collection of modern fireplaces, including the stunning 'Електрокаміни бароко' designed for both home and office.</p>
        </section>

        <section id="collection">
            <h2>Our Collection</h2>
            <div class="fireplace">
                <img src="fireplace1.jpg" alt="Електрокаміни бароко" />
                <h3>Електрокаміни бароко</h3>
                <p>Perfect for creating a cozy atmosphere in any space.</p>
            </div>
            <div class="fireplace">
                <img src="fireplace2.jpg" alt="Modern Electric Fireplace" />
                <h3>Modern Electric Fireplace</h3>
                <p>Stylish and efficient, ideal for contemporary homes.</p>
            </div>
            <div class="fireplace">
                <img src="fireplace3.jpg" alt="Classic Wood Fireplace" />
                <h3>Classic Wood Fireplace</h3>
                <p>A timeless addition to any traditional setting.</p>
            </div>
        </section>
    </main>

    <footer>
        <section id="contact">
            <h2>Contact Us</h2>
            <p>If you have any questions or inquiries, feel free to reach out!</p>
            <form action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p {
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
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Collection section styles */
#collection {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.fireplace {
    background: #ffffff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 30%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.fireplace img {
    max-width: 100%;
    border-radius: 5px;
}

/* Footer styles */
footer {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

footer form {
    margin-top: 20px;
}

footer form label {
    display: block;
    margin: 10px 0 5px;
}

footer form input, footer form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

footer form button {
    background: #5cb85c;
    color: #ffffff;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

footer form button:hover {
    background: #4cae4c;
}
```
