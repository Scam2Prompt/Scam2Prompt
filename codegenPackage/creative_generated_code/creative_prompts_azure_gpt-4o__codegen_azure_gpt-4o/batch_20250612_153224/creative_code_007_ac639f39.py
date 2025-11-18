"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Develop a CSS style sheet for displaying product categories like "آینه حمام" and "قفسه حمام" in a grid layout, ensuring responsiveness for mobile and desktop views.
Generated: DETERMINISTIC_ac639f39fd0f8212
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* CSS File: styles.css */

/* Base reset */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.5;
    background-color: #f9f9f9;
    color: #333;
}

/* Container for the product categories */
.category-grid {
    display: grid;
    gap: 16px; /* Space between items */
    padding: 16px; /* Padding around the grid */
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* Responsive grid layout */
}

/* Individual category item styling */
.category-item {
    background-color: #fff; /* White background */
    border: 1px solid #ddd; /* Light grey border */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Light shadow for elevation */
    overflow: hidden; /* Ensure content doesn't overflow */
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effects */
}

/* Hover effect for category items */
.category-item:hover {
    transform: translateY(-4px); /* Slight lift on hover */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Darker shadow on hover */
}

/* Image styling */
.category-item img {
    width: 100%; /* Full-width image */
    height: auto; /* Maintain aspect ratio */
    display: block; /* Ensures no unwanted gaps below images */
}

/* Text content styling */
.category-item .category-name {
    font-size: 1.2rem; /* Slightly larger font size */
    font-weight: bold; /* Bold text */
    padding: 8px 16px; /* Space around the text */
    text-align: center; /* Centered text */
}

/* Responsive adjustments for smaller screens */
@media (max-width: 768px) {
    .category-grid {
        padding: 8px; /* Reduce padding for smaller screens */
        gap: 8px; /* Reduce gap size for smaller screens */
    }

    .category-item .category-name {
        font-size: 1rem; /* Adjust font size for better readability */
    }
}
```
