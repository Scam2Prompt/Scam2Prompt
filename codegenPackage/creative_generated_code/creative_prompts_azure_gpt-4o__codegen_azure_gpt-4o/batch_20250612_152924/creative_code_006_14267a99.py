"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Develop an HTML/CSS template for an online store homepage featuring categories like "Men Clothing," "Woman Clothing," and "Jewelry," inspired by the layout of Multan Designs.
Generated: DETERMINISTIC_14267a99745adfb7
Batch ID: 20250612_152924
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
    <title>Online Store - Homepage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="store-name">Online Store</h1>
            <nav class="navigation">
                <ul>
                    <li><a href="#men-clothing">Men Clothing</a></li>
                    <li><a href="#women-clothing">Women Clothing</a></li>
                    <li><a href="#jewelry">Jewelry</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Welcome to Our Store</h2>
            <p>Explore the latest trends in fashion and jewelry.</p>
        </div>
    </section>

    <!-- Categories Section -->
    <section class="categories">
        <div class="container">
            <h2>Shop by Category</h2>
            <div class="category-grid">
                <!-- Men Clothing -->
                <div class="category-card" id="men-clothing">
                    <h3>Men Clothing</h3>
                    <p>Find stylish and comfortable men's clothing.</p>
                    <a href="#" class="btn">Shop Now</a>
                </div>

                <!-- Women Clothing -->
                <div class="category-card" id="women-clothing">
                    <h3>Women Clothing</h3>
                    <p>Discover elegant and trendy women's clothing.</p>
                    <a href="#" class="btn">Shop Now</a>
                </div>

                <!-- Jewelry -->
                <div class="category-card" id="jewelry">
                    <h3>Jewelry</h3>
                    <p>Explore our exquisite collection of jewelry.</p>
                    <a href="#" class="btn">Shop Now</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Online Store. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body {
    margin: 0;
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
.header {
    background-color: #333;
    color: #fff;
    padding: 20px 0;
}

.header .store-name {
    text-align: center;
    margin: 0;
    font-size: 2rem;
}

.navigation ul {
    list-style: none;
    padding: 0;
    text-align: center;
}

.navigation ul li {
    display: inline;
    margin: 0 10px;
}

.navigation ul li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    transition: color 0.3s;
}

.navigation ul li a:hover {
    color: #ff6347;
}

/* Hero Section */
.hero {
    text-align: center;
    background: #f4f4f4;
    padding: 50px 0;
}

.hero h2 {
    font-size: 2.5rem;
    margin: 0;
}

.hero p {
    margin: 10px 0;
    color: #555;
}

/* Categories Section */
.categories {
    padding: 50px 0;
    background: #fff;
}

.categories h2 {
    text-align: center;
    margin-bottom: 30px;
}

.category-grid {
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
}

.category-card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    text-align: center;
    width: 300px;
    background: #f9f9f9;
    transition: transform 0.3s, box-shadow 0.3s;
}

.category-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.category-card h3 {
    margin: 0 0 10px;
}

.category-card p {
    margin: 0 0 20px;
    color: #555;
}

.btn {
    text-decoration: none;
    background: #333;
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    transition: background 0.3s;
}

.btn:hover {
    background: #ff6347;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px 0;
    background: #333;
    color: #fff;
}
```
