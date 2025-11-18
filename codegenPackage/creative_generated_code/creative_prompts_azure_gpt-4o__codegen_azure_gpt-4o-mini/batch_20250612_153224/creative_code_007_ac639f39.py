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
/* CSS Style Sheet for Product Categories */
body {
    margin: 0;
    font-family: Arial, sans-serif; /* Use a clean sans-serif font */
}

/* Container for the product categories */
.category-container {
    display: grid; /* Use grid layout */
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* Responsive columns */
    gap: 16px; /* Spacing between grid items */
    padding: 20px; /* Padding around the grid */
}

/* Individual category item styling */
.category-item {
    background-color: #f8f9fa; /* Light background color */
    border: 1px solid #ced4da; /* Light border */
    border-radius: 8px; /* Rounded corners */
    padding: 16px; /* Padding within each item */
    text-align: center; /* Center text */
    transition: transform 0.2s; /* Smooth transformation */
}

/* Hover effect for category items */
.category-item:hover {
    transform: scale(1.05); /* Scale item slightly on hover */
}

/* Title styling for category items */
.category-title {
    font-size: 1.2em; /* Larger font size for titles */
    color: #343a40; /* Dark gray color for text */
    margin: 0; /* Remove default margin */
}

/* Responsive media query for larger screens */
@media (min-width: 768px) {
    .category-container {
        padding: 40px; /* Increased padding for larger screens */
    }
}

/* Responsive media query for smaller screens */
@media (max-width: 767px) {
    .category-item {
        padding: 12px; /* Reduced padding for smaller screens */
    }

    .category-title {
        font-size: 1em; /* Smaller font size for titles */
    }
}
```
