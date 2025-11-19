"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Suggest a CSS styling approach to create a responsive product grid layout similar to the one used on this webpage to display products like XÍCARA DE CHÁ PEARL 180ML.
Generated: DETERMINISTIC_f3be4324e8709c08
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Responsive Product Grid Layout */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  color: #333;
  line-height: 1.6;
}

/* Container for the Product Grid */
.product-grid {
  display: grid;
  gap: 1.5rem; /* Space between grid items */
  padding: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* Responsive columns */
}

/* Individual Product Card */
.product-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Hover Effect for Product Card */
.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

/* Product Image */
.product-card img {
  width: 100%;
  height: auto;
  display: block;
}

/* Product Details */
.product-details {
  padding: 1rem;
  text-align: center;
}

/* Product Title */
.product-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

/* Product Price */
.product-price {
  font-size: 1rem;
  color: #007b5e; /* Accent color for price */
  margin-bottom: 0.5rem;
}

/* Add to Cart Button */
.add-to-cart {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #007b5e;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  font-size: 0.9rem;
  transition: background-color 0.3s ease;
}

.add-to-cart:hover {
  background-color: #005f46;
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* Adjust for smaller screens */
  }
}

@media (max-width: 480px) {
  .product-title {
    font-size: 1rem; /* Adjust font size for smaller screens */
  }

  .add-to-cart {
    font-size: 0.8rem; /* Adjust button size for smaller screens */
  }
}
```
