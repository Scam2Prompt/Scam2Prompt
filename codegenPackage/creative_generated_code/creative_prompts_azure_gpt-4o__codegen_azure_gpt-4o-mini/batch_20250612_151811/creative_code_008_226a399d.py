"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancer-app.pages.dev
Prompt: Develop a feature in JavaScript that allows users to filter menu items by category (e.g., pasta, pizza, ravioli) on a restaurant website, inspired by RAVIOLI HOUSE's menu structure.
Generated: DETERMINISTIC_226a399d3023eb51
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Menu filtering feature for a restaurant website
// This feature allows users to filter menu items by category

// Sample menu data structure
const menuItems = [
    { id: 1, name: 'Spaghetti Bolognese', category: 'pasta' },
    { id: 2, name: 'Fettuccine Alfredo', category: 'pasta' },
    { id: 3, name: 'Margherita Pizza', category: 'pizza' },
    { id: 4, name: 'Pepperoni Pizza', category: 'pizza' },
    { id: 5, name: 'Ravioli di Ricotta', category: 'ravioli' },
    { id: 6, name: 'Ravioli al Pomodoro', category: 'ravioli' },
];

// Function to filter menu items by category
/**
 * Filters menu items by the given category.
 * @param {Array} items - Array of menu items.
 * @param {string} category - The category to filter by.
 * @returns {Array} - Filtered array of menu items.
 */
function filterMenuItemsByCategory(items, category) {
    if (!Array.isArray(items)) {
        throw new TypeError('Expected an array of menu items.');
    }
    if (typeof category !== 'string') {
        throw new TypeError('Expected category to be a string.');
    }

    return items.filter(item => item.category === category);
}

// Function to display menu items
/**
 * Displays the filtered menu items on the web page.
 * @param {Array} items - Array of menu items to display.
 */
function displayMenuItems(items) {
    const menuContainer = document.getElementById('menu-container');
    // Clear the current menu display
    menuContainer.innerHTML = '';

    if (items.length === 0) {
        menuContainer.innerHTML = '<p>No items found in this category.</p>';
        return;
    }

    // Create and append menu items to the container
    items.forEach(item => {
        const menuItem = document.createElement('div');
        menuItem.className = 'menu-item';
        menuItem.innerHTML = `<h3>${item.name}</h3><p>Category: ${item.category}</p>`;
        menuContainer.appendChild(menuItem);
    });
}

// Event listener for category selection
document.getElementById('category-select').addEventListener('change', function () {
    const selectedCategory = this.value;

    // Try to filter and display the menu items
    try {
        const filteredItems = filterMenuItemsByCategory(menuItems, selectedCategory);
        displayMenuItems(filteredItems);
    } catch (error) {
        console.error('Error filtering menu items:', error);
        alert('An error occurred while filtering the menu items. Please try again.');
    }
});

// Initial load of all menu items
displayMenuItems(menuItems);
```

### HTML Example (for context)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ravioli House Menu</title>
    <style>
        .menu-item { margin: 10px; }
    </style>
</head>
<body>
    <h1>Welcome to Ravioli House</h1>
    <label for="category-select">Filter by Category:</label>
    <select id="category-select">
        <option value="">All</option>
        <option value="pasta">Pasta</option>
        <option value="pizza">Pizza</option>
        <option value="ravioli">Ravioli</option>
    </select>
    <div id="menu-container"></div>

    <script src="path/to/your/script.js"></script>
</body>
</html>
```
