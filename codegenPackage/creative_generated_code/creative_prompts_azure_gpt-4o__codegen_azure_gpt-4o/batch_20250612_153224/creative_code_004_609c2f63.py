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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Furniture E-commerce Website">
  <title>Furniture E-commerce</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Furniture Store</h1>
      <nav class="navigation">
        <ul>
          <li><a href="#shop-collection">Shop Collection</a></li>
          <li><a href="#explore-range">Explore Range</a></li>
          <li><a href="#contact-us">Contact Us</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <h2>Welcome to Furniture Store</h2>
      <p>Discover quality furniture crafted for your comfort and style.</p>
      <a href="#shop-collection" class="btn">Shop Now</a>
    </div>
  </section>

  <!-- Shop Collection Section -->
  <section id="shop-collection" class="shop-collection">
    <div class="container">
      <h2>Shop Collection</h2>
      <div class="collection-grid">
        <div class="collection-item">
          <img src="chair.jpg" alt="Chair">
          <h3>Modern Chair</h3>
          <p>$120</p>
        </div>
        <div class="collection-item">
          <img src="table.jpg" alt="Table">
          <h3>Dining Table</h3>
          <p>$250</p>
        </div>
        <div class="collection-item">
          <img src="sofa.jpg" alt="Sofa">
          <h3>Classic Sofa</h3>
          <p>$420</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Explore Range Section -->
  <section id="explore-range" class="explore-range">
    <div class="container">
      <h2>Explore Our Furniture Range</h2>
      <p>Browse through our extensive catalog of premium furniture for every room in your house.</p>
      <a href="#shop-collection" class="btn">View All Products</a>
    </div>
  </section>

  <!-- Contact Us Section -->
  <section id="contact-us" class="contact-us">
    <div class="container">
      <h2>Contact Us</h2>
      <p>Have questions? Reach out to us!</p>
      <form class="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
        <button type="submit" class="btn">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Furniture Store. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.6;
}

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
  text-align: center;
}

.header .logo {
  font-size: 1.8em;
}

.header .navigation ul {
  list-style: none;
  padding: 0;
}

.header .navigation ul li {
  display: inline-block;
  margin: 0 15px;
}

.header .navigation ul li a {
  color: #fff;
  text-decoration: none;
}

/* Hero Section */
.hero {
  background-color: #f4f4f4;
  text-align: center;
  padding: 50px 0;
}

.hero h2 {
  font-size: 2.5em;
}

.hero p {
  margin: 20px 0;
}

.hero .btn {
  display: inline-block;
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
}

/* Shop Collection */
.shop-collection {
  padding: 50px 0;
  text-align: center;
}

.shop-collection h2 {
  font-size: 2em;
}

.collection-grid {
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.collection-item {
  border: 1px solid #ddd;
  padding: 15px;
}

.collection-item img {
  width: 100%;
  height: auto;
}

.collection-item h3 {
  margin: 10px 0 5px;
}

/* Explore Range */
.explore-range {
  background-color: #f9f9f9;
  padding: 50px 0;
  text-align: center;
}

.explore-range h2 {
  font-size: 2em;
}

.explore-range p {
  margin: 20px 0;
}

.explore-range .btn {
  display: inline-block;
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
}

/* Contact Us */
.contact-us {
  padding: 50px 0;
  text-align: center;
}

.contact-us h2 {
  font-size: 2em;
}

.contact-us form {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  text-align: left;
}

.contact-us form label {
  display: block;
  margin: 10px 0 5px;
}

.contact-us form input,
.contact-us form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.contact-us form .btn {
  display: inline-block;
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
}

/* Footer */
.footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px 0;
}
```
