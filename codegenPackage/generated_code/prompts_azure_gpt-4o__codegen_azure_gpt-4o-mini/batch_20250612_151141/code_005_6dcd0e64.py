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
/* Base styles for product card */
.product-card {
    position: relative; /* Positioning for absolute elements */
    overflow: hidden; /* Hide overflow for hover effect */
    border: 1px solid #e1e1e1; /* Light border for product card */
    border-radius: 8px; /* Rounded corners */
    transition: transform 0.3s ease; /* Smooth scaling effect */
}

/* Scale effect on hover */
.product-card:hover {
    transform: scale(1.05); /* Slightly enlarge the card */
}

/* Overlay for product information */
.product-info-overlay {
    position: absolute; /* Position overlay over the product */
    top: 0; /* Align to the top */
    left: 0; /* Align to the left */
    right: 0; /* Stretch to the right */
    bottom: 0; /* Stretch to the bottom */
    background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
    color: #fff; /* White text color */
    display: flex; /* Flexbox for centering content */
    flex-direction: column; /* Stack items vertically */
    justify-content: center; /* Center items vertically */
    align-items: center; /* Center items horizontally */
    opacity: 0; /* Initially hidden */
    transition: opacity 0.3s ease; /* Smooth fade-in effect */
}

/* Show overlay on hover */
.product-card:hover .product-info-overlay {
    opacity: 1; /* Show overlay */
}

/* Add to Cart button styles */
.add-to-cart {
    background-color: #ff6f61; /* Button background color */
    color: #fff; /* Button text color */
    padding: 10px 20px; /* Button padding */
    border: none; /* No border */
    border-radius: 5px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background-color 0.3s ease; /* Smooth background color change */
}

/* Change button color on hover */
.add-to-cart:hover {
    background-color: #ff4c3b; /* Darker shade on hover */
}

/* Product title styles */
.product-title {
    font-size: 1.2em; /* Font size for product title */
    margin: 10px 0; /* Margin for spacing */
    text-align: center; /* Center text */
}

/* Product price styles */
.product-price {
    font-size: 1em; /* Font size for product price */
    margin: 5px 0; /* Margin for spacing */
    text-align: center; /* Center text */
}
```
