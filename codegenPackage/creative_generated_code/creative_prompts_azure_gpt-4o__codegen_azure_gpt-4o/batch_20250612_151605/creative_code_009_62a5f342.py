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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Listing - Poly-Market</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="brand">Poly-Market</div>
            <ul class="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="filter-section">
            <form id="filter-form">
                <label for="category">Filter by Category:</label>
                <select id="category" name="category">
                    <option value="all">All</option>
                    <option value="electronics">Electronics</option>
                    <option value="fashion">Fashion</option>
                    <option value="home-appliances">Home Appliances</option>
                </select>
            </form>
        </section>
        <section class="product-list">
            <!-- Example Product Cards -->
            <div class="product-card" data-category="electronics">
                <img src="product1.jpg" alt="Product 1">
                <h3>Smartphone</h3>
                <p>$599</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-card" data-category="fashion">
                <img src="product2.jpg" alt="Product 2">
                <h3>Men's Jacket</h3>
                <p>$79</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-card" data-category="home-appliances">
                <img src="product3.jpg" alt="Product 3">
                <h3>Microwave Oven</h3>
                <p>$99</p>
                <button>Add to Cart</button>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Poly-Market. All Rights Reserved.</p>
    </footer>
    <script>
        // JavaScript for filtering products based on selected category
        document.getElementById('category').addEventListener('change', function() {
            const selectedCategory = this.value;
            const productCards = document.querySelectorAll('.product-card');

            productCards.forEach(card => {
                if (selectedCategory === 'all' || card.dataset.category === selectedCategory) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Navbar Styling */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    color: #fff;
    padding: 1rem;
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 1rem;
}

.nav-links a {
    text-decoration: none;
    color: #fff;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #f0a500;
}

/* Filter Section */
.filter-section {
    padding: 1rem;
    background-color: #f8f8f8;
}

#filter-form {
    display: flex;
    gap: 0.5rem;
    align-items: center;
}

/* Product List */
.product-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    padding: 1rem;
}

.product-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
    background-color: #fff;
    transition: transform 0.2s, box-shadow 0.2s;
}

.product-card img {
    max-width: 100%;
    height: auto;
    border-radius: 8px 8px 0 0;
}

.product-card h3 {
    margin-top: 0.5rem;
    font-size: 1.2rem;
}

.product-card p {
    margin-top: 0.5rem;
    font-weight: bold;
    color: #333;
}

.product-card button {
    margin-top: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: #f0a500;
    border: none;
    color: #fff;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.product-card button:hover {
    background-color: #cf8500;
}

.product-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Footer Styling */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #333;
    color: #fff;
}
```
