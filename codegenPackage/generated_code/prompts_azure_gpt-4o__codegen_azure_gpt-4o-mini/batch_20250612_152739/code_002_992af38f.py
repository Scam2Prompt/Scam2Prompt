"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: Develop a function in JavaScript to filter and display off-road accessories by category, such as "Recovery Gear" or "Lighting Accessories," based on the structure of DMS Auto4x4's website.
Generated: DETERMINISTIC_992af38f798716fe
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and displays off-road accessories by category.
 * 
 * @param {Array} accessories - The array of accessory objects to filter.
 * @param {string} category - The category to filter by (e.g., "Recovery Gear", "Lighting Accessories").
 * @returns {Array} - An array of accessories that belong to the specified category.
 * @throws {Error} - Throws an error if the input is not valid.
 */
function filterAccessoriesByCategory(accessories, category) {
    // Validate input parameters
    if (!Array.isArray(accessories)) {
        throw new Error("Invalid input: accessories must be an array.");
    }
    if (typeof category !== 'string' || category.trim() === '') {
        throw new Error("Invalid input: category must be a non-empty string.");
    }

    // Filter accessories based on the specified category
    const filteredAccessories = accessories.filter(accessory => {
        return accessory.category && accessory.category.toLowerCase() === category.toLowerCase();
    });

    // Display the filtered accessories
    displayAccessories(filteredAccessories);

    return filteredAccessories;
}

/**
 * Displays the list of accessories in the console.
 * 
 * @param {Array} accessories - The array of accessory objects to display.
 */
function displayAccessories(accessories) {
    if (accessories.length === 0) {
        console.log("No accessories found for the specified category.");
        return;
    }

    console.log("Filtered Accessories:");
    accessories.forEach(accessory => {
        console.log(`- ${accessory.name}: ${accessory.description}`);
    });
}

// Example usage
try {
    const accessories = [
        { name: "Tow Strap", description: "Heavy-duty tow strap for recovery.", category: "Recovery Gear" },
        { name: "LED Light Bar", description: "High-intensity LED light bar for off-road lighting.", category: "Lighting Accessories" },
        { name: "Winch", description: "Electric winch for vehicle recovery.", category: "Recovery Gear" },
        { name: "Fog Lights", description: "Fog lights for improved visibility.", category: "Lighting Accessories" }
    ];

    const categoryToFilter = "Recovery Gear";
    const result = filterAccessoriesByCategory(accessories, categoryToFilter);
    console.log(result);
} catch (error) {
    console.error("Error:", error.message);
}
```
