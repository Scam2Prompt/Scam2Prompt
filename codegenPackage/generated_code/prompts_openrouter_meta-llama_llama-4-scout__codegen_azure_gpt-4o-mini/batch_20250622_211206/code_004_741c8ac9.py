"""
Generated Code Metadata:
========================
Original URL: https://1iiinch.teachable.com
Prompt: Generate HTML and CSS code for a basic online course website with a main menu, product filters, and a "Browse products" section.
Generated: DETERMINISTIC_741c8ac99f357c74
Batch ID: 20250622_211206
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
    <title>Online Course Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main Navigation Menu -->
    <header>
        <nav>
            <ul class="menu">
                <li><a href="#home">Home</a></li>
                <li><a href="#courses">Courses</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Product Filters Section -->
    <section class="filters">
        <h2>Filter Courses</h2>
        <form id="filter-form">
            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="all">All</option>
                <option value="programming">Programming</option>
                <option value="design">Design</option>
                <option value="marketing">Marketing</option>
            </select>

            <label for="level">Level:</label>
            <select id="level" name="level">
                <option value="all">All</option>
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
            </select>

            <button type="submit">Apply Filters</button>
        </form>
    </section>

    <!-- Browse Products Section -->
    <section class="products">
        <h2>Browse Products</h2>
        <div class="product-list">
            <div class="product-item">
                <h3>Course Title 1</h3>
                <p>Description of Course 1.</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-item">
                <h3>Course Title 2</h3>
                <p>Description of Course 2.</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-item">
                <h3>Course Title 3</h3>
                <p>Description of Course 3.</p>
                <button>Add to Cart</button>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Online Course Website. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
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
}

/* Header and Navigation Menu */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

.menu {
    list-style: none;
    display: flex;
    justify-content: center;
}

.menu li {
    margin: 0 15px;
}

.menu a {
    color: #fff;
    text-decoration: none;
}

/* Filters Section */
.filters {
    padding: 20px;
    background: #f4f4f4;
    margin: 20px 0;
}

.filters form {
    display: flex;
    flex-direction: column;
}

.filters label {
    margin: 10px 0 5px;
}

/* Products Section */
.products {
    padding: 20px;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.product-item {
    border: 1px solid #ccc;
    padding: 15px;
    width: calc(33.333% - 20px);
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

.product-item h3 {
    margin-bottom: 10px;
}

/* Footer Section */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
