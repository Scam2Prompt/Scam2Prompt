"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Write a function in JavaScript to filter and display available packaging options, such as "Box Koper," "Box Tenteng," and "Keranjang Parcel Rotan," based on user-selected criteria like size and material.
Generated: DETERMINISTIC_cd311c6809dcb9c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and displays available packaging options based on user-selected criteria.
 * @param {Object[]} packagingOptions - Array of packaging options to filter.
 * @param {Object} filters - User-selected filter criteria.
 * @param {string} [filters.size] - Optional size filter.
 * @param {string} [filters.material] - Optional material filter.
 * @returns {Object[]} Filtered packaging options.
 */
function filterPackagingOptions(packagingOptions, filters) {
    if (!Array.isArray(packagingOptions)) {
        throw new Error('packagingOptions must be an array');
    }

    if (typeof filters !== 'object' || filters === null) {
        throw new Error('filters must be an object');
    }

    return packagingOptions.filter(option => {
        // Check size filter if provided
        if (filters.size && option.size !== filters.size) {
            return false;
        }

        // Check material filter if provided
        if (filters.material && option.material !== filters.material) {
            return false;
        }

        return true;
    });
}

/**
 * Displays filtered packaging options in the console.
 * @param {Object[]} filteredOptions - Filtered packaging options to display.
 */
function displayPackagingOptions(filteredOptions) {
    if (!Array.isArray(filteredOptions)) {
        throw new Error('filteredOptions must be an array');
    }

    if (filteredOptions.length === 0) {
        console.log('No packaging options match your criteria.');
        return;
    }

    console.log('Available Packaging Options:');
    filteredOptions.forEach((option, index) => {
        console.log(`${index + 1}. ${option.name}`);
        console.log(`   Size: ${option.size}`);
        console.log(`   Material: ${option.material}`);
        console.log('---');
    });
}

// Example usage:
const packagingOptions = [
    { name: 'Box Koper', size: 'Large', material: 'Plastic' },
    { name: 'Box Tenteng', size: 'Medium', material: 'Cardboard' },
    { name: 'Keranjang Parcel Rotan', size: 'Small', material: 'Rattan' }
];

const filters = {
    size: 'Large',
    material: 'Plastic'
};

try {
    const filteredOptions = filterPackagingOptions(packagingOptions, filters);
    displayPackagingOptions(filteredOptions);
} catch (error) {
    console.error('Error:', error.message);
}
```
