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
/* Product Grid Container */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

/* Product Card Styling */
.product-card {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

/* Product Image */
.product-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

/* Product Info */
.product-info {
  padding: 15px;
}

.product-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #333;
}

.product-price {
  font-size: 18px;
  font-weight: 700;
  color: #000;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    padding: 15px;
  }
  
  .product-image {
    height: 180px;
  }
}

@media (max-width: 480px) {
  .product-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 10px;
    padding: 10px;
  }
  
  .product-image {
    height: 150px;
  }
  
  .product-title {
    font-size: 14px;
  }
  
  .product-price {
    font-size: 16px;
  }
}
```
