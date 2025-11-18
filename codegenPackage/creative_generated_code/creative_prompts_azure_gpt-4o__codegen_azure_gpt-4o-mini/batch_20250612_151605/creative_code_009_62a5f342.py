"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Generate HTML and CSS code to design a product listing page for an e-commerce site like "Poly-Market.hu," ensuring responsiveness and category-based filtering.
Generated: DETERMINISTIC_62a5f342bf5b7bf6
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poly-Market - Terméklistázó</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <header>
        <h1>Poly-Market</h1>
        <nav>
            <ul>
                <li><a href="#category1">Kategória 1</a></li>
                <li><a href="#category2">Kategória 2</a></li>
                <li><a href="#category3">Kategória 3</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <aside>
            <h2>Kategória Szűrés</h2>
            <ul>
                <li><input type="checkbox" id="cat1" checked> <label for="cat1">Kategória 1</label></li>
                <li><input type="checkbox" id="cat2" checked> <label for="cat2">Kategória 2</label></li>
                <li><input type="checkbox" id="cat3" checked> <label for="cat3">Kategória 3</label></li>
            </ul>
        </aside>

        <section class="product-list">
            <article class="product-item">
                <img src="product1.jpg" alt="Termék 1">
                <h3>Termék 1</h3>
                <p>Leírás a termékről.</p>
                <span class="price">3,000 Ft</span>
                <button class="add-to-cart">Kosárba</button>
            </article>

            <article class="product-item">
                <img src="product2.jpg" alt="Termék 2">
                <h3>Termék 2</h3>
                <p>Leírás a termékről.</p>
                <span class="price">4,500 Ft</span>
                <button class="add-to-cart">Kosárba</button>
            </article>

            <!-- Add more product items as needed -->

        </section>
    </main>

    <footer>
        <p>&copy; 2023 Poly-Market. Minden jog fenntartva.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset default margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styles */
header {
    background-color: #007BFF;
    color: white;
    padding: 1rem;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 1rem;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

/* Main layout */
main {
    display: flex;
    padding: 1rem;
}

/* Sidebar for filtering categories */
aside {
    width: 25%;
    padding: 1rem;
    border-right: 1px solid #ccc;
}

aside h2 {
    margin-bottom: 1rem;
}

/* Product listing section */
.product-list {
    width: 75%;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
    padding: 1rem;
}

.product-item {
    border: 1px solid #ccc;
    padding: 1rem;
    text-align: center;
    transition: transform 0.2s;
}

.product-item:hover {
    transform: scale(1.05);
}

.product-item img {
    max-width: 100%;
    height: auto;
}

.price {
    display: block;
    font-weight: bold;
    margin: 0.5rem 0;
}

/* Button styles */
.add-to-cart {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
}

.add-to-cart:hover {
    background-color: #218838;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #f8f9fa;
    position: relative;
    bottom: 0;
    width: 100%;
}

/* Responsive styles */
@media (max-width: 768px) {
    main {
        flex-direction: column;
    }

    aside {
        width: 100%;
    }

    .product-list {
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
}
```
