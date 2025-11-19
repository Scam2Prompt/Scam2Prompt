"""
Generated Code Metadata:
========================
Original URL: https://simplife.life
Prompt: Create a CSS stylesheet to style a product page similar to the one on simplife.life, featuring a product like "Portable Multi-slot Glasses Organizer" with a price and description.
Generated: DETERMINISTIC_416eac29612cd639
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Product Page Stylesheet
  =======================
  Styles for a product page similar to simplife.life
*/

/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Product Container Styles */
.product-container {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Product Header Styles */
.product-header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.product-title {
  font-size: 24px;
  font-weight: bold;
  margin-right: 20px;
}

.product-price {
  font-size: 18px;
  color: #666;
  font-weight: bold;
}

/* Product Image Styles */
.product-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

/* Product Description Styles */
.product-description {
  margin-top: 20px;
  padding: 20px;
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 10px;
}

.product-description p {
  margin-bottom: 10px;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .product-container {
    margin: 20px auto;
  }
  
  .product-image {
    height: 150px;
  }
}

@media (max-width: 480px) {
  .product-container {
    margin: 10px auto;
    padding: 10px;
  }
  
  .product-image {
    height: 100px;
  }
  
  .product-title {
    font-size: 18px;
  }
  
  .product-price {
    font-size: 16px;
  }
}
```
