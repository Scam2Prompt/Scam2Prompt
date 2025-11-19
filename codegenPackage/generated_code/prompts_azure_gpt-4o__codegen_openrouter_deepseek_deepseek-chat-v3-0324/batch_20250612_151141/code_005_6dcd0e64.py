"""
Generated Code Metadata:
========================
Original URL: https://flashusdtgenerator.com
Prompt: "Generate CSS code for a hover effect that displays product information and 'Add to Cart' icons, as seen in the WoodMart theme."
Generated: DETERMINISTIC_6dcd0e6432b14591
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Product Card Container */
.product-card {
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

/* Product Image Container */
.product-image-container {
  position: relative;
}

/* Hover Overlay */
.product-hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  opacity: 0;
  transition: opacity 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* Product Info on Hover */
.product-hover-info {
  color: #fff;
  text-align: center;
  padding: 15px;
  transform: translateY(20px);
  transition: transform 0.3s ease;
  opacity: 0;
}

/* Quick Actions (Add to Cart, etc.) */
.product-quick-actions {
  display: flex;
  gap: 10px;
  margin-top: 15px;
  transform: translateY(20px);
  transition: transform 0.3s ease;
  opacity: 0;
}

/* Quick Action Buttons */
.quick-action-btn {
  width: 40px;
  height: 40px;
  background: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #333;
  cursor: pointer;
  transition: all 0.2s ease;
}

.quick-action-btn:hover {
  background: #4CAF50;
  color: #fff;
}

/* Add to Cart Button */
.add-to-cart-btn {
  background: #4CAF50;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 30px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
}

.add-to-cart-btn:hover {
  background: #3e8e41;
}

/* Hover Effects */
.product-card:hover .product-hover-overlay {
  opacity: 1;
}

.product-card:hover .product-hover-info,
.product-card:hover .product-quick-actions {
  transform: translateY(0);
  opacity: 1;
  transition-delay: 0.1s;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .product-quick-actions {
    flex-direction: column;
    gap: 5px;
  }
  
  .quick-action-btn {
    width: 35px;
    height: 35px;
  }
}
```
