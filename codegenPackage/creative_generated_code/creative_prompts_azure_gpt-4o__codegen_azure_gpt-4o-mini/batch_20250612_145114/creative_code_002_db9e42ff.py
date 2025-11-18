"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Create a function in JavaScript to check the rarity of an NFT reward on the Habbo platform and display whether it is "Commun" or another rarity type, as described on the webpage.
Generated: DETERMINISTIC_db9e42ffc464dff9
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks the rarity of an NFT reward on the Habbo platform.
 * 
 * @param {string} rarity - The rarity string of the NFT reward.
 * @returns {string} - Returns "Commun" if the rarity is "Commun", otherwise returns the rarity type.
 * @throws {Error} - Throws an error if the rarity parameter is not a valid string.
 */
function checkNftRarity(rarity) {
    // Validate input
    if (typeof rarity !== 'string') {
        throw new Error('Invalid input: rarity must be a string');
    }
    
    // Normalize the rarity input to handle case sensitivity
    const normalizedRarity = rarity.trim().toLowerCase();

    // Check rarity type and return appropriate value
    if (normalizedRarity === 'commun') {
        return 'Commun';
    } else {
        return normalizedRarity.charAt(0).toUpperCase() + normalizedRarity.slice(1);
    }
}

// Example usage
try {
    const nftRarity = 'Commun'; // Change this value to test different rarities
    const rarityStatus = checkNftRarity(nftRarity);
    console.log(`The NFT rarity is: ${rarityStatus}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
