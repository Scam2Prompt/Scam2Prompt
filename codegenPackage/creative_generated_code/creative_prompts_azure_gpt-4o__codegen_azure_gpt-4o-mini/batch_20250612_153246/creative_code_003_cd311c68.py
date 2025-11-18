"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Write a function in JavaScript to filter and display available packaging options, such as "Box Koper," "Box Tenteng," and "Keranjang Parcel Rotan," based on user-selected criteria like size and material.
Generated: DETERMINISTIC_cd311c6809dcb9c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays available packaging options based on user-selected criteria.
 * 
 * @param {Array} options - List of packaging options.
 * @param {Object} criteria - Criteria for filtering the options.
 * @param {string} criteria.size - The size to filter by (e.g., "small", "medium", "large").
 * @param {string} criteria.material - The material to filter by (e.g., "cardboard", "plastic", "woven").
 * @returns {Array} - An array of filtered packaging options.
 */
function filterPackagingOptions(options, criteria) {
    // Validate input parameters
    if (!Array.isArray(options)) {
        throw new Error("Invalid options: expected an array.");
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error("Invalid criteria: expected an object.");
    }

    // Destructure criteria for size and material
    const { size, material } = criteria;

    // Filter options based on criteria
    const filteredOptions = options.filter(option => {
        const sizeMatch = size ? option.size === size : true;
        const materialMatch = material ? option.material === material : true;
        return sizeMatch && materialMatch;
    });

    // Display filtered options
    displayFilteredOptions(filteredOptions);

    return filteredOptions;
}

/**
 * Displays the filtered packaging options in the console.
 * 
 * @param {Array} options - The filtered packaging options to display.
 */
function displayFilteredOptions(options) {
    if (options.length === 0) {
        console.log("No packaging options available for the selected criteria.");
    } else {
        console.log("Available Packaging Options:");
        options.forEach(option => {
            console.log(`- ${option.name} (Size: ${option.size}, Material: ${option.material})`);
        });
    }
}

// Example usage
try {
    const packagingOptions = [
        { name: "Box Koper", size: "medium", material: "cardboard" },
        { name: "Box Tenteng", size: "large", material: "plastic" },
        { name: "Keranjang Parcel Rotan", size: "small", material: "woven" },
        { name: "Box Kecil", size: "small", material: "cardboard" }
    ];

    const criteria = {
        size: "small", // Change size as needed
        material: "woven" // Change material as needed
    };

    filterPackagingOptions(packagingOptions, criteria);
} catch (error) {
    console.error("Error:", error.message);
}
```
