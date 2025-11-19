"""
Generated Code Metadata:
========================
Original URL: https://olhaoshu.com
Prompt: Develop a CSS snippet to style a product display section for an online shop, inspired by the premium design aesthetic of Olha Oshu's website.
Generated: DETERMINISTIC_28ac40794372e5c0
Batch ID: 20250612_160454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Product Display Section Styles */

/* Container Styles */
.product-display {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

/* Product Card Styles */
.product-card {
  margin: 20px;
  width: calc(33.33% - 40px);
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}

/* Product Image Styles */
.product-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

/* Product Information Styles */
.product-info {
  padding: 20px;
}

.product-info h2 {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.product-info p {
  font-size: 14px;
  color: #666;
  margin-bottom: 20px;
}

.product-info .price {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.product-info .cta {
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 14px;
  cursor: pointer;
  border-radius: 5px;
}

.product-info .cta:hover {
  background-color: #444;
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-card {
    width: calc(50% - 40px);
  }
}

@media (max-width: 480px) {
  .product-card {
    width: 100%;
    margin: 10px 0;
  }
  
  .product-display {
    padding: 20px;
  }
}
```
