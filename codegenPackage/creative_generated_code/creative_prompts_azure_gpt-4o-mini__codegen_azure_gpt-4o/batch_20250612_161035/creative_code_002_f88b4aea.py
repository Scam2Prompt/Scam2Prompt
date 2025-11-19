"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpunksxyz.pages.dev
Prompt: Create a JavaScript function that displays the unique collectible characters from the TPUNKS collection, including the number of aliens, apes, and zombies.
Generated: DETERMINISTIC_f88b4aea5f5e2dad
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display unique collectible characters from the TPUNKS collection.
 * This function calculates and displays the total number of aliens, apes, and zombies.
 * @param {Array} collection - Array of TPUNKS collectibles.
 * @returns {Object} Summary of unique characters and their counts.
 */
function getTPUNKSCharacterSummary(collection) {
    // Validate input
    if (!Array.isArray(collection)) {
        throw new Error("Invalid input: collection must be an array.");
    }

    // Initialize counters for each type of collectible
    const characterCounts = {
        aliens: 0,
        apes: 0,
        zombies: 0
    };

    // Track unique collectible IDs
    const uniqueIDs = new Set();

    // Process each collectible in the collection
    collection.forEach(item => {
        // Validate item structure
        if (!item || typeof item !== 'object' || !item.id || !item.type) {
            console.warn("Skipping invalid item in collection:", item);
            return;
        }

        // Check for uniqueness
        if (!uniqueIDs.has(item.id)) {
            uniqueIDs.add(item.id);

            // Increment the appropriate counter based on type
            switch (item.type.toLowerCase()) {
                case 'alien':
                    characterCounts.aliens++;
                    break;
                case 'ape':
                    characterCounts.apes++;
                    break;
                case 'zombie':
                    characterCounts.zombies++;
                    break;
                default:
                    console.warn("Unknown type detected: ", item.type);
            }
        }
    });

    // Display summary
    console.log("TPUNKS Character Summary:");
    console.log("Aliens:", characterCounts.aliens);
    console.log("Apes:", characterCounts.apes);
    console.log("Zombies:", characterCounts.zombies);

    // Return the summary object
    return characterCounts;
}

// Example usage
const tpunksCollection = [
    { id: 1, type: 'alien' },
    { id: 2, type: 'ape' },
    { id: 3, type: 'zombie' },
    { id: 4, type: 'alien' },
    { id: 5, type: 'ape' },
    { id: 1, type: 'alien' } // Duplicate ID
];

try {
    const summary = getTPUNKSCharacterSummary(tpunksCollection);
    console.log("Summary result:", summary);
} catch (error) {
    console.error("Error:", error.message);
}
```
