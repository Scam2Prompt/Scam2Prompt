"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmsauto4x4.ro
Prompt: Develop a function in JavaScript to filter and display off-road accessories by category, such as "Recovery Gear" or "Lighting Accessories," based on the structure of DMS Auto4x4's website.
Generated: DETERMINISTIC_992af38f798716fe
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays off-road accessories by category.
 * 
 * @param {Array} accessories - Array of accessory objects to filter.
 * @param {string} category - The category to filter by (e.g., "Recovery Gear", "Lighting Accessories").
 * @returns {Array} - An array of accessories that match the specified category.
 * @throws {Error} - Throws an error if the input is not valid.
 */
function filterAccessoriesByCategory(accessories, category) {
    // Validate input parameters
    if (!Array.isArray(accessories)) {
        throw new Error('The accessories parameter must be an array.');
    }
    if (typeof category !== 'string' || category.trim() === '') {
        throw new Error('The category parameter must be a non-empty string.');
    }

    // Filter accessories based on the category
    const filteredAccessories = accessories.filter(accessory => 
        accessory.category && accessory.category.toLowerCase() === category.toLowerCase()
    );

    // Return the filtered array
    return filteredAccessories;
}

/**
 * Displays the filtered accessories on the console.
 * 
 * @param {Array} filteredAccessories - Array of filtered accessories to display.
 */
function displayAccessories(filteredAccessories) {
    // Check if there are any accessories to display
    if (filteredAccessories.length === 0) {
        console.log('No accessories found for the specified category.');
        return;
    }

    // Display each accessory
    filteredAccessories.forEach(accessory => {
        console.log(`Name: ${accessory.name}, Category: ${accessory.category}, Price: $${accessory.price}`);
    });
}

// Example usage
try {
    const accessories = [
        { name: 'Tow Strap', category: 'Recovery Gear', price: 25.99 },
        { name: 'LED Light Bar', category: 'Lighting Accessories', price: 199.99 },
        { name: 'Winch', category: 'Recovery Gear', price: 300.00 },
        { name: 'Fog Lights', category: 'Lighting Accessories', price: 89.99 },
    ];

    const selectedCategory = 'Recovery Gear';
    const filteredAccessories = filterAccessoriesByCategory(accessories, selectedCategory);
    displayAccessories(filteredAccessories);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
