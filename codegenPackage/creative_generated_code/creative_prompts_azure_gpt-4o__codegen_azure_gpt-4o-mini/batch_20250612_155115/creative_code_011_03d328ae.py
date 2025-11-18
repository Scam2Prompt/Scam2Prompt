"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Create a CSS stylesheet to style a product filter sidebar with categories for colors, sizes, and retailers, ensuring responsive design for mobile and desktop views.
Generated: DETERMINISTIC_03d328ae7293d2e0
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Product Filter Sidebar Stylesheet */

/* Base styles for the sidebar container */
.sidebar {
    width: 250px; /* Fixed width for desktop */
    padding: 20px; /* Padding for inner content */
    background-color: #f9f9f9; /* Light background */
    border-right: 1px solid #ddd; /* Border for separation */
}

/* Responsive adjustments for mobile view */
@media (max-width: 768px) {
    .sidebar {
        width: 100%; /* Full width on mobile */
        border-right: none; /* Remove border */
        border-bottom: 1px solid #ddd; /* Add bottom border for separation */
    }
}

/* Category title styles */
.sidebar h2 {
    font-size: 1.5em; /* Larger font size for titles */
    margin-bottom: 15px; /* Space below title */
}

/* List styles for categories */
.sidebar ul {
    list-style-type: none; /* Remove default list styles */
    padding: 0; /* Remove default padding */
}

/* Individual category item styles */
.sidebar li {
    margin: 10px 0; /* Space between items */
}

/* Checkbox styles for filters */
.sidebar input[type="checkbox"] {
    margin-right: 10px; /* Space between checkbox and label */
}

/* Hover effect for category items */
.sidebar li:hover {
    background-color: #eaeaea; /* Light background on hover */
    cursor: pointer; /* Pointer cursor for hover */
}

/* Active filter styles */
.sidebar .active {
    font-weight: bold; /* Bold text for active filters */
    color: #007bff; /* Primary color for active state */
}

/* Footer styles for sidebar */
.sidebar .footer {
    margin-top: 20px; /* Space above footer */
    text-align: center; /* Centered text */
    font-size: 0.9em; /* Smaller font for footer */
    color: #777; /* Gray color for footer text */
}

/* Responsive footer adjustments */
@media (max-width: 768px) {
    .sidebar .footer {
        font-size: 0.8em; /* Smaller text on mobile */
    }
}
```
