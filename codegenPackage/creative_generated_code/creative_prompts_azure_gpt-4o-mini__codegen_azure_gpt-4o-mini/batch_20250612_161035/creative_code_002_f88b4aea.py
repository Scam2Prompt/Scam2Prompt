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
 * The function counts the number of unique characters in each category: aliens, apes, and zombies.
 *
 * @param {Array} tpunks - An array of collectible character objects from the TPUNKS collection.
 * Each object should have a 'type' property indicating the category: 'alien', 'ape', or 'zombie'.
 * @returns {Object} An object with counts of unique characters in each category.
 * @throws {Error} Throws an error if input is not an array or if the array is empty.
 */
function displayUniqueCollectibles(tpunks) {
    // Validate input
    if (!Array.isArray(tpunks)) {
        throw new Error('Input must be an array');
    }
    if (tpunks.length === 0) {
        throw new Error('Input array cannot be empty');
    }

    // Initialize counters for each category
    const counts = {
        aliens: new Set(),
        apes: new Set(),
        zombies: new Set()
    };

    // Iterate through the TPUNKS collection to count unique characters
    tpunks.forEach(character => {
        const { type } = character;

        // Check if the type is valid and add to the appropriate set
        if (type === 'alien') {
            counts.aliens.add(character);
        } else if (type === 'ape') {
            counts.apes.add(character);
        } else if (type === 'zombie') {
            counts.zombies.add(character);
        } else {
            console.warn(`Unknown character type: ${type}`);
        }
    });

    // Return the counts as an object with the size of each set
    return {
        aliens: counts.aliens.size,
        apes: counts.apes.size,
        zombies: counts.zombies.size
    };
}

// Example usage:
try {
    const tpunksCollection = [
        { type: 'alien', name: 'Alien One' },
        { type: 'ape', name: 'Ape One' },
        { type: 'zombie', name: 'Zombie One' },
        { type: 'alien', name: 'Alien Two' },
        { type: 'ape', name: 'Ape One' }, // Duplicate
    ];

    const uniqueCounts = displayUniqueCollectibles(tpunksCollection);
    console.log(uniqueCounts); // { aliens: 2, apes: 1, zombies: 1 }
} catch (error) {
    console.error(error.message);
}
```
