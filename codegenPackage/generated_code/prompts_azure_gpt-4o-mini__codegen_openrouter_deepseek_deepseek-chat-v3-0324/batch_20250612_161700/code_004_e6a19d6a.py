"""
Generated Code Metadata:
========================
Original URL: https://delourier.com
Prompt: Write a CSS style for a product gallery showcasing chainmail dresses, ensuring it emphasizes the sleek silhouette of the garments made from premium materials.
Generated: DETERMINISTIC_e6a19d6a09959528
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Product Gallery Styles for Chainmail Dresses */
.product-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    padding: 2rem;
    background-color: #f8f8f8;
    max-width: 1200px;
    margin: 0 auto;
}

.product-item {
    position: relative;
    overflow: hidden;
    border-radius: 4px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    background: white;
}

.product-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.product-image {
    width: 100%;
    height: 400px;
    object-fit: cover;
    object-position: center;
    display: block;
    background: linear-gradient(to bottom, #e0e0e0, #f5f5f5);
}

.product-details {
    padding: 1.5rem;
    text-align: center;
}

.product-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #333;
}

.product-material {
    font-size: 0.9rem;
    color: #666;
    font-style: italic;
    margin-bottom: 0.5rem;
}

.product-price {
    font-size: 1.1rem;
    font-weight: 700;
    color: #222;
}

/* Highlight premium materials and sleek silhouette */
.product-item::after {
    content: "Premium Materials";
    position: absolute;
    top: 1rem;
    right: 1rem;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 0.3rem 0.6rem;
    border-radius: 3px;
    font-size: 0.8rem;
    font-weight: 500;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .product-gallery {
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 1.5rem;
        padding: 1.5rem;
    }
    
    .product-image {
        height: 350px;
    }
}

@media (max-width: 480px) {
    .product-gallery {
        grid-template-columns: 1fr;
    }
}
```
