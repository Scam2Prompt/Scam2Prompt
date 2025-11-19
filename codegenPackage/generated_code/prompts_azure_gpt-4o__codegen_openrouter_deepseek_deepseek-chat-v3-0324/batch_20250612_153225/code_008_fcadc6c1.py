"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Create a CSS stylesheet to design a product page layout for items like "Mount Plates" and "Ring Stickers," ensuring it matches the aesthetic of the Volport website.
Generated: DETERMINISTIC_fcadc6c1cf29319c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Product Page Stylesheet for Volport Aesthetic */
/* Base Styles */
:root {
    --volport-primary: #1a1a1a;
    --volport-secondary: #333333;
    --volport-accent: #e63946;
    --volport-light: #f8f9fa;
    --volport-border: #e0e0e0;
    --volport-text: #333333;
    --volport-text-light: #777777;
}

body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: var(--volport-text);
    background-color: var(--volport-light);
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Container Layout */
.product-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

/* Product Gallery */
.product-gallery {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.main-image {
    width: 100%;
    height: auto;
    border: 1px solid var(--volport-border);
    border-radius: 4px;
    cursor: zoom-in;
}

.thumbnail-container {
    display: flex;
    gap: 0.5rem;
}

.thumbnail {
    width: 80px;
    height: 80px;
    object-fit: cover;
    border: 1px solid var(--volport-border);
    border-radius: 4px;
    cursor: pointer;
    transition: border-color 0.2s;
}

.thumbnail:hover {
    border-color: var(--volport-accent);
}

/* Product Details */
.product-details {
    display: flex;
    flex-direction: column;
}

.product-title {
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 1rem 0;
    color: var(--volport-primary);
}

.product-price {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--volport-accent);
    margin: 0 0 1.5rem 0;
}

.product-description {
    margin-bottom: 2rem;
    color: var(--volport-text);
}

.product-options {
    margin-bottom: 2rem;
}

.option-group {
    margin-bottom: 1.5rem;
}

.option-label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.option-select {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid var(--volport-border);
    border-radius: 4px;
    background-color: white;
    font-size: 1rem;
}

.quantity-selector {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

.quantity-btn {
    width: 40px;
    height: 40px;
    background-color: var(--volport-secondary);
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1.2rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}

.quantity-input {
    width: 60px;
    height: 40px;
    text-align: center;
    border: 1px solid var(--volport-border);
    border-radius: 4px;
    font-size: 1rem;
}

.add-to-cart {
    background-color: var(--volport-accent);
    color: white;
    border: none;
    padding: 1rem 2rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
}

.add-to-cart:hover {
    background-color: #c1121f;
}

/* Product Specifications */
.product-specs {
    margin-top: 3rem;
    grid-column: span 2;
}

.specs-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    color: var(--volport-primary);
}

.specs-table {
    width: 100%;
    border-collapse: collapse;
}

.specs-table th,
.specs-table td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid var(--volport-border);
}

.specs-table th {
    font-weight: 600;
    color: var(--volport-primary);
    width: 30%;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .product-container {
        grid-template-columns: 1fr;
        padding: 1rem;
    }

    .product-specs {
        grid-column: span 1;
    }
}
```
