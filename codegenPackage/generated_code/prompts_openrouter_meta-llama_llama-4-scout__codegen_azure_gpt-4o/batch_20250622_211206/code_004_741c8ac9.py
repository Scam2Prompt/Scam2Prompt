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
        <nav class="main-menu">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#courses">Courses</a></li>
                <li><a href="#about">About</a></li>
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

            <label for="price-range">Price Range:</label>
            <select id="price-range" name="price-range">
                <option value="all">All</option>
                <option value="free">Free</option>
                <option value="paid">Paid</option>
            </select>

            <button type="submit">Apply Filters</button>
        </form>
    </section>

    <!-- Browse Products Section -->
    <section class="browse-products">
        <h2>Browse Courses</h2>
        <div class="product-grid">
            <!-- Example Course Card -->
            <div class="product-card">
                <h3>Introduction to Programming</h3>
                <p>Learn the basics of programming with this beginner-friendly course.</p>
                <button>View Details</button>
            </div>
            <div class="product-card">
                <h3>Web Design Fundamentals</h3>
                <p>Master the principles of web design and create stunning websites.</p>
                <button>View Details</button>
            </div>
            <div class="product-card">
                <h3>Digital Marketing 101</h3>
                <p>Understand the essentials of digital marketing and grow your business.</p>
                <button>View Details</button>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2023 Online Course Website. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    color: #333;
}

/* Header and Navigation */
header {
    background-color: #4CAF50;
    padding: 1rem 0;
    text-align: center;
}

.main-menu ul {
    list-style: none;
    display: flex;
    justify-content: center;
    gap: 1.5rem;
}

.main-menu a {
    text-decoration: none;
    color: white;
    font-weight: bold;
}

.main-menu a:hover {
    text-decoration: underline;
}

/* Filters Section */
.filters {
    background-color: #fff;
    padding: 2rem;
    margin: 1rem auto;
    max-width: 800px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.filters h2 {
    margin-bottom: 1rem;
}

.filters form {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.filters label {
    font-weight: bold;
}

.filters select, .filters button {
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.filters button {
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

.filters button:hover {
    background-color: #45a049;
}

/* Browse Products Section */
.browse-products {
    padding: 2rem;
    margin: 1rem auto;
    max-width: 1200px;
}

.browse-products h2 {
    margin-bottom: 1rem;
    text-align: center;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.product-card {
    background-color: #fff;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.product-card h3 {
    margin-bottom: 0.5rem;
}

.product-card p {
    margin-bottom: 1rem;
}

.product-card button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

.product-card button:hover {
    background-color: #45a049;
}

/* Footer */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #333;
    color: white;
}
```
