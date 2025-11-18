"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Create an HTML and CSS template for a furniture e-commerce website homepage, including sections for "Shop Collection," "Explore Our Furniture Range," and "Contact Us," inspired by Navkar Furniture's layout.
Generated: DETERMINISTIC_609c2f638d39a5af
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navkar Furniture - Home</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Navkar Furniture</h1>
        <nav>
            <ul>
                <li><a href="#shop-collection">Shop Collection</a></li>
                <li><a href="#explore-range">Explore Our Furniture Range</a></li>
                <li><a href="#contact-us">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="shop-collection" class="section">
            <h2>Shop Collection</h2>
            <div class="collection-grid">
                <div class="collection-item">Living Room</div>
                <div class="collection-item">Bedroom</div>
                <div class="collection-item">Dining Room</div>
                <div class="collection-item">Office</div>
            </div>
        </section>

        <section id="explore-range" class="section">
            <h2>Explore Our Furniture Range</h2>
            <div class="furniture-range">
                <div class="furniture-item">Sofas</div>
                <div class="furniture-item">Chairs</div>
                <div class="furniture-item">Tables</div>
                <div class="furniture-item">Storage</div>
            </div>
        </section>

        <section id="contact-us" class="section">
            <h2>Contact Us</h2>
            <p>If you have any questions, feel free to reach out!</p>
            <form id="contact-form" action="/submit" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Navkar Furniture. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for browser styling */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

header nav ul {
    list-style: none;
}

header nav ul li {
    display: inline;
    margin: 0 15px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section styles */
.section {
    padding: 20px;
    margin: 20px;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Collection grid styles */
.collection-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 10px;
}

.collection-item, .furniture-item {
    background: #e2e2e2;
    padding: 20px;
    text-align: center;
    border-radius: 5px;
}

/* Contact form styles */
#contact-form {
    display: flex;
    flex-direction: column;
}

#contact-form label {
    margin: 10px 0 5px;
}

#contact-form input, 
#contact-form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#contact-form button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#contact-form button:hover {
    background: #555;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```
