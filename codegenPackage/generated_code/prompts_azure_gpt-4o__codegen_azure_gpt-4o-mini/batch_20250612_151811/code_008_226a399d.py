"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Develop a feature in JavaScript that allows users to filter menu items by category (e.g., pasta, pizza, ravioli) on a restaurant website, inspired by RAVIOLI HOUSE's menu structure.
Generated: DETERMINISTIC_226a399d3023eb51
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Menu filtering feature for a restaurant website
// Inspired by RAVIOLI HOUSE's menu structure

// Sample menu data
const menuItems = [
    { id: 1, name: 'Spaghetti Carbonara', category: 'pasta' },
    { id: 2, name: 'Margherita Pizza', category: 'pizza' },
    { id: 3, name: 'Ravioli di Ricotta', category: 'ravioli' },
    { id: 4, name: 'Fettuccine Alfredo', category: 'pasta' },
    { id: 5, name: 'Pepperoni Pizza', category: 'pizza' },
    { id: 6, name: 'Ravioli al Pomodoro', category: 'ravioli' },
];

// Function to filter menu items by category
/**
 * Filters menu items based on the selected category.
 * @param {string} category - The category to filter by (e.g., 'pasta', 'pizza', 'ravioli').
 * @returns {Array} - An array of filtered menu items.
 */
function filterMenuItems(category) {
    // Validate input
    if (typeof category !== 'string') {
        console.error('Invalid category type. Expected a string.');
        return [];
    }

    // Filter menu items by the specified category
    const filteredItems = menuItems.filter(item => item.category === category);

    // Return filtered items or a message if none found
    return filteredItems.length > 0 ? filteredItems : `No items found in the category: ${category}`;
}

// Function to display menu items
/**
 * Displays the menu items in the console.
 * @param {Array} items - The array of menu items to display.
 */
function displayMenuItems(items) {
    if (Array.isArray(items) && items.length > 0) {
        console.log('Menu Items:');
        items.forEach(item => {
            console.log(`- ${item.name} (${item.category})`);
        });
    } else {
        console.log(items); // Display the message if no items found
    }
}

// Example usage
const selectedCategory = 'pasta'; // Change this to filter by different categories
const filteredItems = filterMenuItems(selectedCategory);
displayMenuItems(filteredItems);
```
