"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnu.co.id
Prompt: Generate a code snippet to create an e-commerce product page for herbal supplements similar to those offered by Habbasyi Niaga Utama, focusing on Habbatussauda and its health benefits.
Generated: DETERMINISTIC_42368111f533e57f
Batch ID: 20250612_164000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Shop high-quality herbal supplements like Habbatussauda to improve your health and wellness.">
  <title>Habbatussauda Herbal Supplement - Product Page</title>
  <!-- External CSS for styling -->
  <link rel="stylesheet" href="styles.css">
  <!-- Font and icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
  <header>
    <nav>
      <div class="logo">
        <a href="/">Herbal Supplements</a>
      </div>
      <ul class="nav-links">
        <li><a href="/products">Products</a></li>
        <li><a href="/about">About Us</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section class="product-section">
      <div class="product-image">
        <!-- Placeholder for product image -->
        <img src="images/habbatussauda.jpg" alt="Habbatussauda Herbal Supplement" />
      </div>
      <div class="product-details">
        <h1>Habbatussauda Herbal Supplement</h1>
        <p><strong>Price:</strong> $15.99</p>
        <p><strong>Benefits:</strong> Known for its various health benefits including boosting immunity, improving digestion, and supporting overall wellness.</p>
        <p>Our Habbatussauda is made from high-quality black seed oil, ensuring purity and efficacy.</p>
        <button id="addToCartButton">Add to Cart</button>
      </div>
    </section>

    <section class="product-description">
      <h2>Why Choose Habbatussauda?</h2>
      <p>Habbatussauda, also known as black seed oil, has been used for centuries as a natural remedy for a variety of ailments. Rich in antioxidants and essential fatty acids, it provides powerful benefits for the body and mind.</p>
      <ul>
        <li>Supports immune system health</li>
        <li>Helps maintain heart health</li>
        <li>Promotes healthy skin and digestion</li>
      </ul>
    </section>

    <section class="reviews">
      <h2>Customer Reviews</h2>
      <div class="review">
        <p><strong>John Doe:</strong> "This supplement has significantly improved my energy levels. Highly recommend it!"</p>
      </div>
      <div class="review">
        <p><strong>Jane Smith:</strong> "I've been using this product for a month, and I can already feel the difference in my overall health."</p>
      </div>
    </section>
  </main>

  <footer>
    <div class="footer-content">
      <p>&copy; 2023 Herbal Supplements. All rights reserved.</p>
      <ul class="footer-links">
        <li><a href="/terms">Terms of Service</a></li>
        <li><a href="/privacy">Privacy Policy</a></li>
      </ul>
    </div>
  </footer>

  <!-- External JavaScript -->
  <script src="scripts.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset and Base Styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f8f8f8;
  color: #333;
}

header {
  background: #4caf50;
  color: #fff;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header .logo {
  font-size: 1.5rem;
}

header .nav-links {
  list-style: none;
  display: flex;
}

header .nav-links li {
  margin-left: 1rem;
}

header .nav-links a {
  color: #fff;
  text-decoration: none;
}

.product-section {
  display: flex;
  padding: 2rem;
  background: #fff;
}

.product-image img {
  max-width: 100%;
  height: auto;
}

.product-details {
  margin-left: 2rem;
}

.product-details button {
  background: #4caf50;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

.product-details button:hover {
  background: #45a049;
}

.product-description {
  padding: 2rem;
  background: #f4f4f4;
}

.reviews {
  padding: 2rem;
  background: #fff;
}

footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 1rem;
}

.footer-links {
  list-style: none;
  display: flex;
  justify-content: center;
  padding: 0;
}

.footer-links li {
  margin: 0 1rem;
}

.footer-links a {
  color: #fff;
  text-decoration: none;
}
```

```javascript
// scripts.js

// Handling "Add to Cart" button click
document.getElementById("addToCartButton").addEventListener("click", function() {
  try {
    alert("Product added to cart successfully!");
    // Simulate adding product to cart (e.g., update cart details in a database or on the backend)
    // This can be extended with AJAX or API calls to handle cart functionality.
  } catch (error) {
    console.error("Error adding product to cart:", error);
    alert("An error occurred while adding the product to the cart. Please try again.");
  }
});
```
