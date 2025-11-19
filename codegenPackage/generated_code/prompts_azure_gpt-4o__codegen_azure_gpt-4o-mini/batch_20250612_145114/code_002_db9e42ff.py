"""
Generated Code Metadata:
========================
Original URL: https://fr.habbometa.com
Prompt: Create a function in JavaScript to check the rarity of an NFT reward on the Habbo platform and display whether it is "Commun" or another rarity type, as described on the webpage.
Generated: DETERMINISTIC_db9e42ffc464dff9
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks the rarity of an NFT reward on the Habbo platform.
 * 
 * @param {string} rarity - The rarity string to check.
 * @returns {string} - Returns "Commun" if the rarity is "Commun", otherwise returns the rarity type.
 * @throws {Error} - Throws an error if the input is not a string or is empty.
 */
function checkNFTRarity(rarity) {
    // Validate input
    if (typeof rarity !== 'string' || rarity.trim() === '') {
        throw new Error('Invalid input: rarity must be a non-empty string.');
    }

    // Normalize the rarity string to handle case sensitivity
    const normalizedRarity = rarity.trim().toLowerCase();

    // Check for rarity type
    if (normalizedRarity === 'commun') {
        return 'Commun';
    } else {
        return `Rarity type: ${rarity}`;
    }
}

// Example usage
try {
    const rarityInput = 'Commun'; // Replace with actual input
    const result = checkNFTRarity(rarityInput);
    console.log(result); // Output the result
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
