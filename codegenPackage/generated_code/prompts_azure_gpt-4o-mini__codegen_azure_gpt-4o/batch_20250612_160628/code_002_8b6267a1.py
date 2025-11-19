"""
Generated Code Metadata:
========================
Original URL: https://eveandevan.com
Prompt: Create a CSS stylesheet to style a product grid similar to the one found on the Evan Mens website for showcasing men's clothing.
Generated: DETERMINISTIC_8b6267a1b8916475
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Product Grid Stylesheet 
  Author: [Your Name]
  Description: Styles for a product grid showcasing men's clothing.
  Created: [Date]
*/

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: 'Arial', sans-serif;
  background-color: #f9f9f9;
  color: #333;
  line-height: 1.6;
}

/* Container for the Product Grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

/* Individual Product Card */
.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Hover Effect for Product Card */
.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

/* Product Image */
.product-card img {
  width: 100%;
  height: auto;
  display: block;
}

/* Product Details Section */
.product-details {
  padding: 15px;
  text-align: center;
}

/* Product Title */
.product-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}

/* Product Price */
.product-price {
  font-size: 1rem;
  color: #555;
  margin-bottom: 15px;
}

/* Add to Cart Button */
.add-to-cart-btn {
  display: inline-block;
  padding: 10px 20px;
  font-size: 0.9rem;
  font-weight: bold;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

/* Hover Effect for Add to Cart Button */
.add-to-cart-btn:hover {
  background-color: #0056b3;
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }

  .product-title {
    font-size: 1rem;
  }

  .product-price {
    font-size: 0.9rem;
  }

  .add-to-cart-btn {
    font-size: 0.8rem;
    padding: 8px 15px;
  }
}
```
