"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Create a function in JavaScript to dynamically display product categories such as "Offset Multi Colour Printers" and "House Keeping" on a webpage, with sorting and filtering options.
Generated: DETERMINISTIC_925b7e9ea1e1a73b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProductCategoryDisplay.js

/**
 * Class to handle the display of product categories with sorting and filtering options.
 */
class ProductCategoryDisplay {
    constructor(categories) {
        this.categories = categories; // Array of product categories
        this.filteredCategories = [...categories]; // Array to hold filtered categories
        this.sortOrder = 'asc'; // Default sort order
    }

    /**
     * Renders the product categories to the webpage.
     */
    render() {
        const container = document.getElementById('category-container');
        container.innerHTML = ''; // Clear previous content

        this.filteredCategories.forEach(category => {
            const categoryElement = document.createElement('div');
            categoryElement.className = 'category-item';
            categoryElement.textContent = category;
            container.appendChild(categoryElement);
        });
    }

    /**
     * Filters categories based on a search term.
     * @param {string} searchTerm - The term to filter categories by.
     */
    filterCategories(searchTerm) {
        this.filteredCategories = this.categories.filter(category =>
            category.toLowerCase().includes(searchTerm.toLowerCase())
        );
        this.render(); // Re-render the filtered categories
    }

    /**
     * Sorts categories in ascending or descending order.
     * @param {string} order - The order to sort by ('asc' or 'desc').
     */
    sortCategories(order) {
        this.sortOrder = order;
        this.filteredCategories.sort((a, b) => {
            if (order === 'asc') {
                return a.localeCompare(b);
            } else {
                return b.localeCompare(a);
            }
        });
        this.render(); // Re-render the sorted categories
    }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    const categories = [
        'Offset Multi Colour Printers',
        'House Keeping',
        'Laser Printers',
        'Inkjet Printers',
        'Office Supplies',
        'Cleaning Products'
    ];

    const productCategoryDisplay = new ProductCategoryDisplay(categories);
    productCategoryDisplay.render(); // Initial render

    // Event listeners for filtering and sorting
    document.getElementById('filter-input').addEventListener('input', (event) => {
        productCategoryDisplay.filterCategories(event.target.value);
    });

    document.getElementById('sort-select').addEventListener('change', (event) => {
        productCategoryDisplay.sortCategories(event.target.value);
    });
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Categories</title>
    <style>
        .category-item {
            padding: 10px;
            border: 1px solid #ccc;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Product Categories</h1>
    <input type="text" id="filter-input" placeholder="Filter categories..." />
    <select id="sort-select">
        <option value="asc">Sort Ascending</option>
        <option value="desc">Sort Descending</option>
    </select>
    <div id="category-container"></div>

    <script src="ProductCategoryDisplay.js"></script>
</body>
</html>
```
