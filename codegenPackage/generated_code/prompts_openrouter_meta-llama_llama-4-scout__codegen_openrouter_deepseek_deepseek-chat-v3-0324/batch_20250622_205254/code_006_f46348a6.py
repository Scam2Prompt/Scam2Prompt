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
.product-card {
    width: 100%;
    max-width: 300px;
    border: 1px solid #e1e1e1;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
    background: #fff;
    margin: 0 auto;
    position: relative;
}

.product-card:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transform: translateY(-2px);
}

.product-image-container {
    position: relative;
    width: 100%;
    padding-top: 100%; /* 1:1 Aspect Ratio */
    overflow: hidden;
}

.product-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.product-card:hover .product-image {
    transform: scale(1.03);
}

.product-info {
    padding: 16px;
}

.product-title {
    font-size: 16px;
    font-weight: 600;
    color: #333;
    margin: 0 0 8px 0;
    line-height: 1.3;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.product-price {
    font-size: 18px;
    font-weight: 700;
    color: #000;
    margin: 0 0 8px 0;
}

.product-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    color: #666;
}

.product-rating {
    display: flex;
    align-items: center;
}

.product-rating svg {
    fill: #ffc107;
    margin-right: 4px;
}

.product-actions {
    display: flex;
    justify-content: space-between;
    margin-top: 12px;
}

.add-to-cart-btn {
    background: #4CAF50;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
    transition: background 0.2s ease;
    flex-grow: 1;
}

.add-to-cart-btn:hover {
    background: #3d8b40;
}

.wishlist-btn {
    background: transparent;
    border: 1px solid #e1e1e1;
    border-radius: 4px;
    padding: 8px;
    margin-left: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.wishlist-btn:hover {
    background: #f5f5f5;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .product-card {
        max-width: 100%;
    }
    
    .product-title {
        white-space: normal;
    }
}
```
