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

/* General Sidebar Styles */
.sidebar {
    width: 300px;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    font-family: Arial, sans-serif;
}

/* Heading */
.sidebar h2 {
    font-size: 1.5em;
    margin-bottom: 20px;
    color: #333;
}

/* Filter Section */
.filter-category {
    margin-bottom: 30px;
}

.filter-category h3 {
    font-size: 1.2em;
    margin-bottom: 10px;
    color: #555;
}

.filter-category ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.filter-category ul li {
    margin-bottom: 10px;
}

.filter-category ul li label {
    display: flex;
    align-items: center;
    cursor: pointer;
}

.filter-category ul li input[type="checkbox"] {
    margin-right: 10px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .sidebar {
        width: 100%;
        padding: 15px;
        box-shadow: none; /* Simplify for mobile */
    }

    .sidebar h2 {
        font-size: 1.3em;
    }

    .filter-category h3 {
        font-size: 1em;
    }
}

/* Accessibility Enhancements */
.sidebar h2, .filter-category h3 {
    font-weight: bold;
}

.sidebar label {
    font-size: 0.9em;
    color: #666;
}

.sidebar label:hover {
    color: #000;
}
```
