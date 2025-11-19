"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Write a CSS code snippet to style a product card component, similar to those on Poly-Market, with a responsive design and hover effects, for a product like "Drohmo R25 polcos szekrény".
Generated: DETERMINISTIC_f46348a6c67adcc2
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Product Card Component Styles */

/* Base Styles */
.product-card {
  display: flex;
  flex-direction: column;
  width: 300px;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}

/* Image Styles */
.product-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

/* Content Styles */
.product-card-content {
  padding: 20px;
}

.product-card-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.product-card-description {
  font-size: 14px;
  color: #666;
  margin-bottom: 20px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-card {
    width: 100%;
    margin: 10px 0;
  }
}

/* Additional Styles for Product: Drohmo R25 polcos szekrény */
.product-card-drohmo-r25 {
  background-color: #f9f9f9;
}

.product-card-drohmo-r25 .product-card-title {
  color: #333;
}

.product-card-drohmo-r25 .product-card-description {
  color: #666;
}

/* Hover Effects */
.product-card:hover .product-card-title {
  color: #337ab7;
}

.product-card:hover .product-card-description {
  color: #23527c;
}
```
