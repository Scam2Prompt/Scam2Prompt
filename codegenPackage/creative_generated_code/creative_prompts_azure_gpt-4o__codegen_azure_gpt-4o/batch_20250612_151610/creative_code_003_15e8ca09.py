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
/**
 * Script to filter and display machinery parts inventory based on brand and quality certification.
 * Author: [Your Name]
 * Date: [Today's Date]
 * Description: This script filters machinery parts inventory based on user-defined criteria
 * and displays the filtered result. It uses best practices and includes error handling.
 */

// Sample inventory data (can be replaced with an actual database or API response)
const inventory = [
    { id: 1, name: "Engine Block", brand: "CATERPILLAR", certification: "ISO 9001" },
    { id: 2, name: "Hydraulic Pump", brand: "JOHN DEERE", certification: "CE" },
    { id: 3, name: "Gearbox", brand: "CATERPILLAR", certification: "ISO 9001" },
    { id: 4, name: "Turbocharger", brand: "KOMATSU", certification: "ISO 14001" },
    { id: 5, name: "Fuel Injector", brand: "JOHN DEERE", certification: "ISO 9001" }
];

/**
 * Filters the inventory based on brand and certification criteria.
 * @param {Array} inventory - The array of machinery parts.
 * @param {string} brand - The brand to filter by (e.g., 'CATERPILLAR', 'JOHN DEERE').
 * @param {string} certification - The certification to filter by (e.g., 'ISO 9001').
 * @returns {Array} - The filtered list of machinery parts.
 */
function filterInventory(inventory, brand, certification) {
    try {
        // Validate input types
        if (!Array.isArray(inventory)) {
            throw new Error("Invalid inventory data. Expected an array.");
        }
        if (typeof brand !== "string" || typeof certification !== "string") {
            throw new Error("Invalid brand or certification. Both must be strings.");
        }

        // Filter inventory based on the criteria
        const filteredParts = inventory.filter(
            (part) => part.brand === brand && part.certification === certification
        );

        return filteredParts;
    } catch (error) {
        console.error("Error filtering inventory:", error.message);
        return [];
    }
}

/**
 * Displays the filtered inventory parts in a readable format.
 * @param {Array} parts - The array of machinery parts to display.
 */
function displayParts(parts) {
    if (parts.length === 0) {
        console.log("No matching parts found.");
        return;
    }

    console.log("Filtered Machinery Parts:");
    parts.forEach((part) => {
        console.log(`- ID: ${part.id}, Name: ${part.name}, Brand: ${part.brand}, Certification: ${part.certification}`);
    });
}

// Example usage:
const brand = "CATERPILLAR";
const certification = "ISO 9001";

// Filter inventory based on criteria
const filteredParts = filterInventory(inventory, brand, certification);

// Display the filtered inventory
displayParts(filteredParts);
```
