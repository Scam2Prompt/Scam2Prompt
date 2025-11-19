"""
Generated Code Metadata:
========================
Original URL: https://www.navkarfurniture.com
Prompt: Create an HTML and CSS template for a furniture e-commerce website homepage, including sections for "Shop Collection," "Explore Our Furniture Range," and "Contact Us," inspired by Navkar Furniture's layout.
Generated: DETERMINISTIC_609c2f638d39a5af
Batch ID: 20250612_153224
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
        <section id="shop-collection">
            <h2>Shop Collection</h2>
            <div class="collection-items">
                <div class="item">
                    <img src="images/sofa.jpg" alt="Sofa">
                    <h3>Elegant Sofa</h3>
                    <p>Comfortable and stylish sofa for your living room.</p>
                    <button>Add to Cart</button>
                </div>
                <div class="item">
                    <img src="images/table.jpg" alt="Dining Table">
                    <h3>Dining Table</h3>
                    <p>Beautiful dining table for family gatherings.</p>
                    <button>Add to Cart</button>
                </div>
                <div class="item">
                    <img src="images/chair.jpg" alt="Chair">
                    <h3>Office Chair</h3>
                    <p>Ergonomic chair for your workspace.</p>
                    <button>Add to Cart</button>
                </div>
            </div>
        </section>

        <section id="explore-range">
            <h2>Explore Our Furniture Range</h2>
            <p>Discover a wide variety of furniture that suits your style and needs. From modern to classic designs, we have something for everyone.</p>
            <div class="range-items">
                <div class="item">
                    <img src="images/bed.jpg" alt="Bed">
                    <h3>Luxury Bed</h3>
                </div>
                <div class="item">
                    <img src="images/cabinet.jpg" alt="Cabinet">
                    <h3>Storage Cabinet</h3>
                </div>
                <div class="item">
                    <img src="images/bookshelf.jpg" alt="Bookshelf">
                    <h3>Bookshelf</h3>
                </div>
            </div>
        </section>

        <section id="contact-us">
            <h2>Contact Us</h2>
            <p>If you have any questions or need assistance, feel free to reach out to us!</p>
            <form action="submit_contact.php" method="POST">
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
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
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
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 40px;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.collection-items, .range-items {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

.item {
    text-align: center;
    margin: 10px;
    flex: 1 1 30%; /* Responsive item sizing */
}

.item img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
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
