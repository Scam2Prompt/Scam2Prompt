"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Generate a JavaScript function to dynamically filter Travis Scott merchandise by category (e.g., hoodies, t-shirts, sweatshirts) on an e-commerce website.
Generated: DETERMINISTIC_576885539123d2fa
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters Travis Scott merchandise based on the selected category.
 * Updates the displayed merchandise items accordingly.
 * 
 * @param {string} category - The category to filter the merchandise by (e.g., 'hoodies', 't-shirts', 'sweatshirts').
 * @throws {Error} Throws an error if the category is not valid or if merchandise data is not available.
 */
function filterMerchandiseByCategory(category) {
    // Define valid categories for filtering
    const validCategories = ['hoodies', 't-shirts', 'sweatshirts'];
    
    // Validate the category input
    if (!validCategories.includes(category)) {
        throw new Error(`Invalid category: ${category}. Valid categories are: ${validCategories.join(', ')}`);
    }

    // Get the merchandise items (this could be fetched from an API or defined in a data structure)
    const merchandiseItems = [
        { id: 1, name: 'Travis Scott Hoodie', category: 'hoodies' },
        { id: 2, name: 'Travis Scott T-Shirt', category: 't-shirts' },
        { id: 3, name: 'Travis Scott Sweatshirt', category: 'sweatshirts' },
        { id: 4, name: 'Travis Scott Hoodie 2', category: 'hoodies' },
        { id: 5, name: 'Travis Scott T-Shirt 2', category: 't-shirts' }
    ];

    // Find the merchandise items that match the selected category
    const filteredItems = merchandiseItems.filter(item => item.category === category);

    // Update the display with the filtered items
    updateDisplay(filteredItems);
}

/**
 * Updates the merchandise display with the filtered items.
 * 
 * @param {Array} items - The array of merchandise items to be displayed.
 */
function updateDisplay(items) {
    // Get the merchandise display container element
    const displayContainer = document.getElementById('merchandise-display');

    // Clear the current display
    displayContainer.innerHTML = '';

    // Check if there are items to display
    if (items.length === 0) {
        displayContainer.innerHTML = '<p>No items found in this category.</p>';
        return;
    }

    // Create and append the filtered items to the display
    items.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'merch-item';
        itemElement.innerHTML = `<h3>${item.name}</h3>`;
        displayContainer.appendChild(itemElement);
    });
}

// Event listener for category selection (assuming there is a select element for categories)
document.getElementById('category-select').addEventListener('change', (event) => {
    try {
        filterMerchandiseByCategory(event.target.value);
    } catch (error) {
        console.error(error.message);
        alert(error.message); // Alert the user in case of error
    }
});
```
