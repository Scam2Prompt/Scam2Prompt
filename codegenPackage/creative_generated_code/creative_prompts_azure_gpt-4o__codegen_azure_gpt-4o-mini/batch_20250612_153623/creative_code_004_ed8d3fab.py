"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-phatom.teachable.com
Prompt: Write HTML and CSS code to replicate the "Sort by" and "Product filters" functionality described on the Teachable help page.
Generated: DETERMINISTIC_ed8d3fab8fd81751
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Filters</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <!-- Sort By Section -->
        <div class="sort-by">
            <label for="sort-options">Sort by:</label>
            <select id="sort-options">
                <option value="relevance">Relevance</option>
                <option value="price-low-high">Price: Low to High</option>
                <option value="price-high-low">Price: High to Low</option>
                <option value="newest">Newest</option>
            </select>
        </div>

        <!-- Product Filter Section -->
        <div class="product-filters">
            <h3>Filters</h3>
            <form id="filter-form">
                <div class="filter-group">
                    <label>
                        <input type="checkbox" name="category" value="ebooks">
                        eBooks
                    </label>
                </div>
                <div class="filter-group">
                    <label>
                        <input type="checkbox" name="category" value="courses">
                        Courses
                    </label>
                </div>
                <div class="filter-group">
                    <label>
                        <input type="checkbox" name="category" value="webinars">
                        Webinars
                    </label>
                </div>
                <button type="submit">Apply Filters</button>
            </form>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Container styles */
.container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
}

/* Sort By Section */
.sort-by {
    margin-bottom: 20px;
}

.sort-by label {
    margin-right: 10px;
}

/* Product Filters Section */
.product-filters {
    border-top: 1px solid #ccc;
    padding-top: 10px;
}

.product-filters h3 {
    margin-bottom: 10px;
}

.filter-group {
    margin-bottom: 10px;
}

.filter-group label {
    cursor: pointer;
}
```

```javascript
// script.js

// Add an event listener for the filter form submission
document.getElementById('filter-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather selected filters
    const selectedFilters = Array.from(document.querySelectorAll('input[name="category"]:checked'))
        .map(checkbox => checkbox.value);

    // Handle filters (for demonstration purposes, we'll log them)
    if (selectedFilters.length > 0) {
        console.log('Selected Filters:', selectedFilters);
        // Here you would typically make a request to fetch filtered products
    } else {
        console.log('No filters selected');
    }
});
```

This code provides a basic structure for a "Sort By" dropdown and a set of product filters, complete with styles and basic JavaScript functionality.
