"""
Generated Code Metadata:
========================
Original URL: https://zerion.shop
Prompt: Develop a CSS style for a product page that showcases items like the Milegua leather jacket and winter jacket, emphasizing unique design elements and user experience.
Generated: DETERMINISTIC_8db7d1ec91126389
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Product Page Stylesheet */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: 'Arial', sans-serif;
  background-color: #f9f9f9; /* Light background for better readability */
  color: #333; /* Neutral text color */
  line-height: 1.6;
}

/* Container for the product page */
.product-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Header Section */
.header {
  text-align: center;
  padding: 20px 0;
  background-color: #222; /* Dark background for contrast */
  color: #fff; /* White text for readability */
}

.header h1 {
  font-size: 2.5rem;
  font-weight: bold;
}

/* Product Grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 30px;
}

/* Individual Product Card */
.product-card {
  background-color: #fff;
  border: 1px solid #ddd; /* Subtle border for separation */
  border-radius: 8px; /* Rounded corners for modern design */
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effect */
}

.product-card:hover {
  transform: translateY(-5px); /* Lift effect on hover */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Shadow effect */
}

/* Product Image */
.product-card img {
  width: 100%;
  height: auto;
  display: block;
}

/* Product Details */
.product-details {
  padding: 15px;
}

.product-details h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #222; /* Darker text for emphasis */
}

.product-details p {
  font-size: 1rem;
  color: #666; /* Subtle text for descriptions */
  margin-bottom: 15px;
}

/* Price Styling */
.product-price {
  font-size: 1.2rem;
  font-weight: bold;
  color: #e63946; /* Highlight price in red */
}

/* Add to Cart Button */
.add-to-cart {
  display: inline-block;
  text-align: center;
  padding: 10px 20px;
  background-color: #2a9d8f; /* Greenish color for CTA */
  color: #fff; /* White text for contrast */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.add-to-cart:hover {
  background-color: #21867a; /* Darker shade on hover */
}

/* Responsive Design */
@media (max-width: 768px) {
  .header h1 {
    font-size: 2rem;
  }

  .product-details h2 {
    font-size: 1.3rem;
  }

  .product-price {
    font-size: 1.1rem;
  }

  .add-to-cart {
    font-size: 0.9rem;
  }
}
```
