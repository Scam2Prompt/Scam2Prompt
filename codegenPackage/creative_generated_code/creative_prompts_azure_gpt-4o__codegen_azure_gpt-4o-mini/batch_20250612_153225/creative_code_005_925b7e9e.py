"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Create a function in JavaScript to dynamically display product categories such as "Offset Multi Colour Printers" and "House Keeping" on a webpage, with sorting and filtering options.
Generated: DETERMINISTIC_925b7e9ea1e1a73b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Sample data representing product categories
const productCategories = [
    "Offset Multi Colour Printers",
    "House Keeping",
    "Digital Printers",
    "Office Supplies",
    "Cleaning Supplies",
    "Stationery"
];

/**
 * Function to create and display product categories on the webpage
 * @param {Array} categories - An array of category names to display
 */
function displayCategories(categories) {
    // Get the category display element
    const categoryDisplay = document.getElementById('category-display');
    categoryDisplay.innerHTML = ''; // Clear existing categories

    // Create and append category elements
    categories.forEach(category => {
        const categoryElement = document.createElement('div');
        categoryElement.className = 'category-item';
        categoryElement.textContent = category;
        categoryDisplay.appendChild(categoryElement);
    });
}

/**
 * Function to sort categories based on the given criteria
 * @param {Array} categories - An array of category names to sort
 * @param {string} order - The order to sort categories ('asc' or 'desc')
 * @returns {Array} - Sorted array of categories
 */
function sortCategories(categories, order) {
    if (!Array.isArray(categories)) {
        throw new TypeError('Expected an array of categories');
    }

    return categories.sort((a, b) => {
        return order === 'asc' ? a.localeCompare(b) : b.localeCompare(a);
    });
}

/**
 * Function to filter categories based on the search term
 * @param {Array} categories - An array of category names to filter
 * @param {string} searchTerm - The term to filter categories by
 * @returns {Array} - Filtered array of categories
 */
function filterCategories(categories, searchTerm) {
    if (!Array.isArray(categories)) {
        throw new TypeError('Expected an array of categories');
    }
    
    return categories.filter(category => 
        category.toLowerCase().includes(searchTerm.toLowerCase())
    );
}

// Event listener for sorting and filtering input
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search-input');
    const sortSelect = document.getElementById('sort-select');

    // Display initial categories
    displayCategories(productCategories);

    // Handle search input
    searchInput.addEventListener('input', () => {
        const filteredCategories = filterCategories(productCategories, searchInput.value);
        displayCategories(filteredCategories);
    });

    // Handle sorting
    sortSelect.addEventListener('change', () => {
        const sortedCategories = sortCategories(productCategories, sortSelect.value);
        displayCategories(sortedCategories);
    });
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Categories</title>
    <style>
        .category-item {
            padding: 5px;
            border: 1px solid #ccc;
            margin: 5px;
        }
    </style>
</head>
<body>
    <h1>Product Categories</h1>
    <input type="text" id="search-input" placeholder="Search categories..." />
    <select id="sort-select">
        <option value="asc">Sort Ascending</option>
        <option value="desc">Sort Descending</option>
    </select>
    <div id="category-display"></div>

    <script src="path/to/your/javascript.js"></script>
</body>
</html>
```
