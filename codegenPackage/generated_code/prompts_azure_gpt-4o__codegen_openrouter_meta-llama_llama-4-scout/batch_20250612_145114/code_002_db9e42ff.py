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
 * @param {string} rarityCode - The rarity code of the NFT reward.
 * @returns {string} The rarity type of the NFT reward.
 */
function getHabboNftRarity(rarityCode) {
    // Define a dictionary to map rarity codes to their respective types
    const rarityTypes = {
        "common": "Commun",
        "uncommon": "Peu commun",
        "rare": "Rare",
        "veryrare": "Très rare",
        "legendary": "Légendaire"
    };

    try {
        // Check if the rarity code is valid
        if (!(rarityCode in rarityTypes)) {
            throw new Error(`Invalid rarity code: ${rarityCode}`);
        }

        // Return the rarity type
        return rarityTypes[rarityCode];
    } catch (error) {
        // Log the error and return a default message
        console.error(`Error checking NFT rarity: ${error.message}`);
        return "Unknown rarity";
    }
}

// Example usage:
function main() {
    const rarityCode = "common";
    const rarityType = getHabboNftRarity(rarityCode);
    console.log(`The NFT reward with rarity code '${rarityCode}' is ${rarityType}.`);
}

main();
```
