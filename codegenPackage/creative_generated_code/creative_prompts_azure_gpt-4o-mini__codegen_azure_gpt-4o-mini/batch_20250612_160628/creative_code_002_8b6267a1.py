"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveandevan.com
Prompt: Create a CSS stylesheet to style a product grid similar to the one found on the Evan Mens website for showcasing men's clothing.
Generated: DETERMINISTIC_8b6267a1b8916475
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Global styles */
body {
    font-family: Arial, sans-serif; /* Sets the font for the body */
    margin: 0; /* Resets default margin */
    padding: 0; /* Resets default padding */
    background-color: #f4f4f4; /* Light background color for the entire page */
}

/* Container for the product grid */
.product-grid {
    display: grid; /* Uses CSS Grid layout */
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* Responsive columns */
    gap: 20px; /* Space between grid items */
    padding: 20px; /* Padding around the grid */
}

/* Individual product item */
.product-item {
    background-color: #ffffff; /* White background for each product item */
    border: 1px solid #dddddd; /* Light grey border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Hides overflow content */
    transition: transform 0.3s, box-shadow 0.3s; /* Smooth transition for hover effects */
}

/* Hover effect for product items */
.product-item:hover {
    transform: translateY(-5px); /* Lifts the item on hover */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Adds shadow on hover */
}

/* Product image styling */
.product-item img {
    width: 100%; /* Makes image responsive */
    height: auto; /* Maintains aspect ratio */
}

/* Product title styling */
.product-title {
    font-size: 1.2em; /* Font size for product title */
    margin: 10px; /* Margin around title */
    color: #333; /* Dark text color */
}

/* Product price styling */
.product-price {
    font-size: 1.1em; /* Font size for product price */
    margin: 10px; /* Margin around price */
    color: #e67e22; /* Orange color for price */
}

/* Button styling */
.product-button {
    display: block; /* Makes the button fill the width */
    background-color: #3498db; /* Blue background for button */
    color: white; /* White text color */
    padding: 10px; /* Padding inside the button */
    text-align: center; /* Center text in button */
    text-decoration: none; /* Removes underline from link */
    border: none; /* Removes border */
    border-radius: 5px; /* Rounded corners for button */
    margin: 10px; /* Margin around button */
    transition: background-color 0.3s; /* Smooth transition for hover effect */
}

/* Button hover effect */
.product-button:hover {
    background-color: #2980b9; /* Darker blue on hover */
}

/* Responsive adjustments */
@media (max-width: 600px) {
    .product-grid {
        grid-template-columns: 1fr; /* Stacks items in a single column on small screens */
    }
}
```
