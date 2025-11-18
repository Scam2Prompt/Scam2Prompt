"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiosell.com
Prompt: Develop a function in JavaScript that uses Jiosell's product categories to filter and display items from "JioMart-Groceries" and "Nykaa-Beauty."
Generated: DETERMINISTIC_a13f47d18238b1f6
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays items from specific product categories.
 * 
 * This function retrieves items from the "JioMart-Groceries" and "Nykaa-Beauty"
 * categories and displays them on the webpage.
 * 
 * @param {Array} items - The list of all items available.
 * @returns {void}
 */
function displayFilteredItems(items) {
    try {
        // Validate input
        if (!Array.isArray(items)) {
            throw new TypeError('Expected an array of items');
        }

        // Define the target categories
        const targetCategories = ['JioMart-Groceries', 'Nykaa-Beauty'];

        // Filter the items based on the target categories
        const filteredItems = items.filter(item => 
            targetCategories.includes(item.category)
        );

        // Check if any items were found
        if (filteredItems.length === 0) {
            console.log('No items found in the specified categories.');
            return;
        }

        // Display the filtered items
        filteredItems.forEach(item => {
            // Create a container for each item
            const itemContainer = document.createElement('div');
            itemContainer.classList.add('item');

            // Create and append item name
            const itemName = document.createElement('h3');
            itemName.textContent = item.name;
            itemContainer.appendChild(itemName);

            // Create and append item price
            const itemPrice = document.createElement('p');
            itemPrice.textContent = `Price: ₹${item.price}`;
            itemContainer.appendChild(itemPrice);

            // Append the item container to the display area
            document.getElementById('itemDisplayArea').appendChild(itemContainer);
        });

    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while displaying items:', error.message);
        alert('Unable to display items. Please try again later.');
    }
}

// Example usage (ensure to replace with actual data)
const items = [
    { name: 'Milk', price: 50, category: 'JioMart-Groceries' },
    { name: 'Shampoo', price: 200, category: 'Nykaa-Beauty' },
    { name: 'Bread', price: 30, category: 'JioMart-Groceries' },
    { name: 'Lipstick', price: 500, category: 'Nykaa-Beauty' },
    { name: 'Toothpaste', price: 100, category: 'JioMart-Groceries' }
];

// Call the function to display filtered items
displayFilteredItems(items);
```

Make sure to have an HTML element with the ID `itemDisplayArea` where the filtered items will be displayed.
