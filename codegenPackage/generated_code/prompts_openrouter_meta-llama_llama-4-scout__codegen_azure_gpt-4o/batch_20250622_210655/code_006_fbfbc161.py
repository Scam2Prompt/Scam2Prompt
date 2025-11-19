"""
Generated Code Metadata:
========================
Original URL: https://iyitixobond.com
Prompt: Create a simple e-commerce website using HTML, CSS, and JavaScript to showcase and sell stone care products, similar to iyitixobond.com.
Generated: DETERMINISTIC_fbfbc161cd1d7d2b
Batch ID: 20250622_210655
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
  <title>Stone Care Products</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Stone Care Products</h1>
      <nav>
        <ul>
          <li><a href="#products">Products</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <!-- Products Section -->
    <section id="products" class="container">
      <h2>Our Products</h2>
      <div class="product-list">
        <!-- Product Item -->
        <div class="product-item">
          <img src="images/product1.jpg" alt="Product 1">
          <h3>Stone Cleaner</h3>
          <p>Price: $19.99</p>
          <button class="add-to-cart" data-product="Stone Cleaner" data-price="19.99">Add to Cart</button>
        </div>
        <!-- Product Item -->
        <div class="product-item">
          <img src="images/product2.jpg" alt="Product 2">
          <h3>Stone Sealer</h3>
          <p>Price: $29.99</p>
          <button class="add-to-cart" data-product="Stone Sealer" data-price="29.99">Add to Cart</button>
        </div>
        <!-- Product Item -->
        <div class="product-item">
          <img src="images/product3.jpg" alt="Product 3">
          <h3>Stone Polish</h3>
          <p>Price: $24.99</p>
          <button class="add-to-cart" data-product="Stone Polish" data-price="24.99">Add to Cart</button>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="container">
      <h2>About Us</h2>
      <p>We provide high-quality stone care products to help you maintain and protect your stone surfaces.</p>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="container">
      <h2>Contact Us</h2>
      <form id="contact-form">
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

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <p>&copy; 2023 Stone Care Products. All rights reserved.</p>
    </div>
  </footer>

  <!-- JavaScript -->
  <script src="script.js"></script>
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

/* Header Styles */
header {
  background: #333;
  color: #fff;
  padding: 1rem 0;
}

header h1 {
  text-align: center;
}

header nav ul {
  list-style: none;
  text-align: center;
  padding: 0;
}

header nav ul li {
  display: inline;
  margin: 0 10px;
}

header nav ul li a {
  color: #fff;
  text-decoration: none;
}

/* Products Section */
.product-list {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

.product-item {
  border: 1px solid #ddd;
  padding: 1rem;
  text-align: center;
  width: 300px;
}

.product-item img {
  max-width: 100%;
  height: auto;
}

.add-to-cart {
  background: #28a745;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

.add-to-cart:hover {
  background: #218838;
}

/* About Section */
#about {
  margin: 2rem 0;
  text-align: center;
}

/* Contact Section */
#contact-form {
  max-width: 600px;
  margin: 0 auto;
}

#contact-form label {
  display: block;
  margin: 0.5rem 0 0.2rem;
}

#contact-form input,
#contact-form textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
}

#contact-form button {
  background: #007bff;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

#contact-form button:hover {
  background: #0056b3;
}

/* Footer Styles */
footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```

```javascript
// script.js

// Handle "Add to Cart" button clicks
document.addEventListener('DOMContentLoaded', () => {
  const cart = [];

  // Add event listeners to all "Add to Cart" buttons
  const addToCartButtons = document.querySelectorAll('.add-to-cart');
  addToCartButtons.forEach(button => {
    button.addEventListener('click', () => {
      const productName = button.getAttribute('data-product');
      const productPrice = parseFloat(button.getAttribute('data-price'));

      // Add product to cart
      cart.push({ name: productName, price: productPrice });

      // Display confirmation
      alert(`${productName} has been added to your cart.`);
      console.log('Cart:', cart); // For debugging purposes
    });
  });

  // Handle contact form submission
  const contactForm = document.getElementById('contact-form');
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Basic validation
    if (!name || !email || !message) {
      alert('Please fill out all fields.');
      return;
    }

    // Simulate form submission
    alert('Thank you for your message! We will get back to you soon.');
    contactForm.reset();
  });
});
```
