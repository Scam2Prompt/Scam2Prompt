"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Write HTML and CSS code to design a product page for Belts Mania that highlights "Custom Championship Belts" with sections for trending belts, new arrivals, and customer reviews.
Generated: DETERMINISTIC_212d5a5ad22e8092
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Belts Mania - Custom Championship Belts</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Trending</a></li>
                <li><a href="#">New Arrivals</a></li>
                <li><a href="#">Reviews</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Custom Championship Belts</h1>
        <p>Design your own championship belt with Belts Mania</p>
        <button>Explore Now</button>
    </section>

    <!-- Trending Section -->
    <section class="trending">
        <h2>Trending Belts</h2>
        <div class="belt-grid">
            <div class="belt-card">
                <img src="belt1.jpg" alt="Belt 1">
                <h3>Belt 1</h3>
                <p>$99.99</p>
            </div>
            <div class="belt-card">
                <img src="belt2.jpg" alt="Belt 2">
                <h3>Belt 2</h3>
                <p>$149.99</p>
            </div>
            <div class="belt-card">
                <img src="belt3.jpg" alt="Belt 3">
                <h3>Belt 3</h3>
                <p>$199.99</p>
            </div>
        </div>
    </section>

    <!-- New Arrivals Section -->
    <section class="new-arrivals">
        <h2>New Arrivals</h2>
        <div class="belt-grid">
            <div class="belt-card">
                <img src="new-belt1.jpg" alt="New Belt 1">
                <h3>New Belt 1</h3>
                <p>$79.99</p>
            </div>
            <div class="belt-card">
                <img src="new-belt2.jpg" alt="New Belt 2">
                <h3>New Belt 2</h3>
                <p>$129.99</p>
            </div>
            <div class="belt-card">
                <img src="new-belt3.jpg" alt="New Belt 3">
                <h3>New Belt 3</h3>
                <p>$179.99</p>
            </div>
        </div>
    </section>

    <!-- Customer Reviews Section -->
    <section class="customer-reviews">
        <h2>What Our Customers Say</h2>
        <div class="review-grid">
            <div class="review-card">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <h3>John Doe</h3>
            </div>
            <div class="review-card">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <h3>Jane Doe</h3>
            </div>
            <div class="review-card">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <h3>Bob Smith</h3>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Belts Mania. All rights reserved.</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header Styles */
header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Styles */
.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

/* Trending Styles */
.trending {
    padding: 2em;
}

.trending h2 {
    font-size: 36px;
    margin-bottom: 10px;
}

.belt-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.belt-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.belt-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.belt-card h3 {
    font-size: 18px;
    margin-bottom: 5px;
}

/* New Arrivals Styles */
.new-arrivals {
    padding: 2em;
}

.new-arrivals h2 {
    font-size: 36px;
    margin-bottom: 10px;
}

/* Customer Reviews Styles */
.customer-reviews {
    padding: 2em;
}

.customer-reviews h2 {
    font-size: 36px;
    margin-bottom: 10px;
}

.review-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.review-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.review-card p {
    font-size: 14px;
    margin-bottom: 10px;
}

.review-card h3 {
    font-size: 18px;
    margin-bottom: 5px;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
