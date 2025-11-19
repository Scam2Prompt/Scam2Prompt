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
/* Product Page Stylesheet */
/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

body {
    background-color: #f9f9f9;
    color: #333;
    line-height: 1.6;
}

/* Container Styles */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Product Card Styles */
.product-card {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    overflow: hidden;
    margin: 20px 0;
    display: flex;
    flex-direction: column;
}

@media (min-width: 768px) {
    .product-card {
        flex-direction: row;
    }
}

/* Product Image Styles */
.product-image {
    width: 100%;
    height: auto;
    object-fit: cover;
}

@media (min-width: 768px) {
    .product-image {
        width: 50%;
        max-height: 500px;
    }
}

/* Product Info Styles */
.product-info {
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.product-title {
    font-size: 24px;
    font-weight: 700;
    color: #222;
}

.product-price {
    font-size: 28px;
    font-weight: 700;
    color: #2a5cff;
}

.product-old-price {
    font-size: 18px;
    color: #999;
    text-decoration: line-through;
    margin-left: 8px;
}

.product-description {
    color: #666;
    font-size: 16px;
    margin-bottom: 12px;
}

.product-features {
    list-style-type: none;
    margin: 16px 0;
}

.product-features li {
    padding: 8px 0;
    position: relative;
    padding-left: 28px;
}

.product-features li:before {
    content: "✓";
    color: #2a5cff;
    position: absolute;
    left: 0;
    font-weight: bold;
}

/* CTA Button Styles */
.cta-button {
    background-color: #2a5cff;
    color: white;
    border: none;
    padding: 14px 24px;
    font-size: 16px;
    font-weight: 600;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 12px;
    width: 100%;
}

.cta-button:hover {
    background-color: #1a4ae8;
}

/* Review Section Styles */
.reviews-section {
    margin-top: 40px;
    background: #fff;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.reviews-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 16px;
}

.review-card {
    padding: 16px 0;
    border-bottom: 1px solid #eee;
}

.review-author {
    font-weight: 600;
    margin-bottom: 8px;
}

.review-text {
    color: #555;
}

/* Responsive Adjustments */
@media (max-width: 767px) {
    .product-info {
        padding: 16px;
    }
    
    .product-title {
        font-size: 20px;
    }
    
    .product-price {
        font-size: 24px;
    }
}
```
