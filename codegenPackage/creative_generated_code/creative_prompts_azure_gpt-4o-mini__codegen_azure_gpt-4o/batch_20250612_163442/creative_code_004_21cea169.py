"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blacksabbathmerch.com
Prompt: Construct a CSS stylesheet that styles a product listing for Black Sabbath merch, focusing on t-shirts and hoodies, to enhance user experience.
Generated: DETERMINISTIC_21cea16986b06c3a
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Black Sabbath Merch Product Listing Stylesheet */
/* This stylesheet enhances the user experience for t-shirts and hoodies */

/* Global styles for consistent design */
body {
    font-family: 'Arial', sans-serif;
    background-color: #121212; /* Dark background for a metal aesthetic */
    color: #f5f5f5; /* Light text for readability */
    margin: 0;
    padding: 0;
}

/* Container for the product listing */
.product-listing {
    display: flex;
    flex-wrap: wrap; /* Ensure responsive layout with wrapping rows */
    justify-content: center;
    gap: 20px; /* Add space between products */
    padding: 20px;
}

/* Individual product card */
.product-card {
    background-color: #1c1c1c; /* Slightly lighter background for product cards */
    border: 1px solid #444; /* Subtle border for definition */
    border-radius: 8px; /* Smooth corners */
    width: 300px;
    text-align: center; /* Center content inside cards */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Add depth with a shadow */
    transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth hover effects */
}

/* Hover effect for product cards */
.product-card:hover {
    transform: translateY(-10px); /* Slight lift on hover */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5); /* Enhance shadow on hover */
}

/* Product image */
.product-card img {
    max-width: 100%; /* Ensure image fits within card */
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

/* Product title */
.product-card h2 {
    font-size: 1.5em;
    margin: 10px 0;
    color: #fff; /* High contrast text */
}

/* Product price */
.product-card .price {
    font-size: 1.2em;
    color: #ff9800; /* Highlight price with orange */
    margin: 10px 0;
}

/* Add to cart button */
.product-card .add-to-cart {
    display: inline-block;
    background-color: #ff9800; /* Standout orange button */
    color: #121212; /* Dark text for contrast on button */
    padding: 10px 20px;
    margin: 15px 0;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    text-transform: uppercase; /* Make text all uppercase */
    transition: background-color 0.2s ease, color 0.2s ease; /* Smooth color transitions */
}

/* Hover effect for add-to-cart button */
.product-card .add-to-cart:hover {
    background-color: #e68900; /* Slightly darker orange on hover */
    color: #f5f5f5; /* Light text on hover */
}

/* Responsive styles */
@media (max-width: 768px) {
    .product-card {
        width: 100%; /* Make cards full-width on smaller screens */
    }
}
```
