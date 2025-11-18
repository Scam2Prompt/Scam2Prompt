"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-crypto.yivesites.com
Prompt: Write HTML and CSS code to design a responsive product listing page that matches the layout and branding style of the Apelbet website.
Generated: DETERMINISTIC_8017431c57456509
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Listing - Apelbet</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <h1>Apelbet Products</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="product-list">
            <article class="product-card">
                <img src="product1.jpg" alt="Product 1" />
                <h2 class="product-name">Product 1</h2>
                <p class="product-price">$29.99</p>
                <button class="add-to-cart">Add to Cart</button>
            </article>

            <article class="product-card">
                <img src="product2.jpg" alt="Product 2" />
                <h2 class="product-name">Product 2</h2>
                <p class="product-price">$39.99</p>
                <button class="add-to-cart">Add to Cart</button>
            </article>

            <article class="product-card">
                <img src="product3.jpg" alt="Product 3" />
                <h2 class="product-name">Product 3</h2>
                <p class="product-price">$49.99</p>
                <button class="add-to-cart">Add to Cart</button>
            </article>

            <!-- Add more product cards as needed -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Apelbet. All Rights Reserved.</p>
    </footer>

</body>

</html>
```

```css
/* styles.css */

/* Reset default browser styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    color: #333;
}

/* Header styling */
header {
    background: #007bff;
    color: white;
    padding: 20px;
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
    color: white;
    text-decoration: none;
}

/* Main styling */
main {
    padding: 20px;
}

/* Product list styling */
.product-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

/* Product card styling */
.product-card {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 15px;
    padding: 15px;
    text-align: center;
    width: 200px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

.product-card:hover {
    transform: scale(1.05);
}

.product-name {
    font-size: 1.2em;
    margin: 10px 0;
}

.product-price {
    color: #28a745;
    font-size: 1.1em;
}

/* Button styling */
.add-to-cart {
    background-color: #007bff;
    border: none;
    color: white;
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.add-to-cart:hover {
    background-color: #0056b3;
}

/* Footer styling */
footer {
    text-align: center;
    margin-top: 20px;
    padding: 10px;
    background: #007bff;
    color: white;
}

/* Responsive styles */
@media (max-width: 600px) {
    .product-list {
        flex-direction: column;
        align-items: center;
    }

    .product-card {
        width: 90%;
    }
}
```
