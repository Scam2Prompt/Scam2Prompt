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

/* Container for the product card */
.product-card {
    background-color: #ffffff; /* White background for the card */
    border: 1px solid #e0e0e0; /* Light gray border */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    overflow: hidden; /* Prevents overflow of child elements */
    transition: transform 0.3s ease; /* Smooth transition for hover effect */
    max-width: 300px; /* Maximum width of the card */
    margin: 20px; /* Margin around the card */
}

/* Image styling */
.product-card img {
    width: 100%; /* Full width image */
    height: auto; /* Maintain aspect ratio */
}

/* Product title styling */
.product-card .product-title {
    font-size: 1.5em; /* Larger font size for title */
    font-weight: bold; /* Bold text */
    margin: 15px; /* Margin around the title */
    color: #333; /* Dark gray color for text */
}

/* Product description styling */
.product-card .product-description {
    font-size: 1em; /* Standard font size for description */
    color: #666; /* Medium gray color for text */
    margin: 0 15px 15px; /* Margin around the description */
}

/* Price styling */
.product-card .product-price {
    font-size: 1.2em; /* Slightly larger font size for price */
    color: #e91e63; /* Pink color for price */
    margin: 0 15px 15px; /* Margin around the price */
}

/* Hover effect for the product card */
.product-card:hover {
    transform: scale(1.05); /* Slightly enlarge the card on hover */
}

/* Responsive design */
@media (max-width: 768px) {
    .product-card {
        max-width: 100%; /* Full width on smaller screens */
        margin: 10px; /* Reduced margin on smaller screens */
    }
}
```
