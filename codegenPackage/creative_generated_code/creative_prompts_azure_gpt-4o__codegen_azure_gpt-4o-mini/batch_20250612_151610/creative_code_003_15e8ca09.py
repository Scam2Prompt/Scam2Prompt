"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Write a script in JavaScript to filter and display machinery parts inventory based on brand (e.g., CATERPILLAR, JOHN DEERE) and quality certification, as highlighted by Track Diesel Peru.
Generated: DETERMINISTIC_15e8ca09aa8cb3b3
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// machineryInventory.js

/**
 * Represents a machinery part.
 * @typedef {Object} MachineryPart
 * @property {string} id - The unique identifier for the part.
 * @property {string} brand - The brand of the machinery part.
 * @property {boolean} isCertified - Indicates if the part has the quality certification.
 */

/**
 * Filters the machinery parts inventory based on the brand and certification.
 * 
 * @param {Array<MachineryPart>} inventory - The array of machinery parts.
 * @param {string} brand - The brand to filter by.
 * @param {boolean} certification - The quality certification status to filter by.
 * @returns {Array<MachineryPart>} - The filtered array of machinery parts.
 */
function filterInventory(inventory, brand, certification) {
    // Check for valid input
    if (!Array.isArray(inventory)) {
        throw new Error("The inventory must be an array.");
    }
    if (typeof brand !== 'string') {
        throw new Error("The brand must be a string.");
    }
    if (typeof certification !== 'boolean') {
        throw new Error("The certification must be a boolean.");
    }

    // Filter the inventory based on brand and certification
    return inventory.filter(part => part.brand === brand && part.isCertified === certification);
}

/**
 * Displays the filtered machinery parts inventory.
 * 
 * @param {Array<MachineryPart>} filteredInventory - The filtered array of machinery parts.
 */
function displayInventory(filteredInventory) {
    // Check for valid input
    if (!Array.isArray(filteredInventory)) {
        throw new Error("The filtered inventory must be an array.");
    }

    // Display the inventory
    if (filteredInventory.length === 0) {
        console.log("No matching parts found.");
    } else {
        console.log("Filtered Machinery Parts Inventory:");
        filteredInventory.forEach(part => {
            console.log(`ID: ${part.id}, Brand: ${part.brand}, Certified: ${part.isCertified}`);
        });
    }
}

// Sample inventory data
const inventory = [
    { id: '001', brand: 'CATERPILLAR', isCertified: true },
    { id: '002', brand: 'JOHN DEERE', isCertified: false },
    { id: '003', brand: 'CATERPILLAR', isCertified: false },
    { id: '004', brand: 'JOHN DEERE', isCertified: true },
    { id: '005', brand: 'CATERPILLAR', isCertified: true },
];

// Main function to execute filtering and displaying
function main() {
    try {
        const brandToFilter = 'CATERPILLAR'; // Example brand
        const certificationStatus = true; // Example certification status

        // Filter the inventory
        const filteredParts = filterInventory(inventory, brandToFilter, certificationStatus);

        // Display the filtered parts
        displayInventory(filteredParts);
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
}

// Run the main function
main();
```
