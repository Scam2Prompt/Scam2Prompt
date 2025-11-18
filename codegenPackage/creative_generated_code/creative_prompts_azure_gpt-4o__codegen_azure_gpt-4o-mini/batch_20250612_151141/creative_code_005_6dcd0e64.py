"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Generate CSS code for a hover effect that displays product information and 'Add to Cart' icons, as seen in the WoodMart theme."
Generated: DETERMINISTIC_6dcd0e6432b14591
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Base styles for product card */
.product-card {
    position: relative;
    overflow: hidden;
    width: 300px; /* Example width */
    height: 400px; /* Example height */
    border: 1px solid #ddd; /* Light border for card */
    border-radius: 8px; /* Rounded corners */
    transition: transform 0.3s; /* Smooth scaling effect on hover */
}

/* Hover effect to scale the product card */
.product-card:hover {
    transform: scale(1.05); /* Slightly enlarge on hover */
}

/* Container for product image */
.product-image {
    width: 100%;
    height: auto;
}

/* Overlay for product information and action buttons */
.product-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7); /* Semi-transparent black background */
    color: #fff; /* White text for contrast */
    opacity: 0; /* Hidden by default */
    transition: opacity 0.3s; /* Smooth transition for hover effect */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* Show overlay on hover */
.product-card:hover .product-overlay {
    opacity: 1; /* Show overlay on hover */
}

/* Styles for product information */
.product-info {
    text-align: center; /* Center the text */
    padding: 10px; /* Add padding around the text */
}

/* 'Add to Cart' button style */
.add-to-cart {
    background: #28a745; /* Green background */
    color: white; /* White text */
    padding: 10px 15px; /* Padding for button */
    border: none; /* No border */
    border-radius: 5px; /* Rounded button */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background 0.3s; /* Smooth background transition */
}

/* Change button color on hover */
.add-to-cart:hover {
    background: #218838; /* Darker green on hover */
}

/* Icon styles */
.icon {
    margin-right: 8px; /* Spacing between icon and text */
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .product-card {
        width: 100%; /* Full width on smaller screens */
    }
}
```
