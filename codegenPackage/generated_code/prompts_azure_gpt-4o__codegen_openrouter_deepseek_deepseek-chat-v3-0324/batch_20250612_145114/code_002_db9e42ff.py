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
 * @param {string} rewardName - The name of the NFT reward to check.
 * @param {Object} rarityData - An object containing rarity mappings (e.g., { "Commun": ["reward1", "reward2"] }).
 * @returns {string} - The rarity type ("Commun" or other specified rarity).
 * @throws {Error} - If rewardName is not a string or rarityData is not an object.
 */
function checkNFTRarity(rewardName, rarityData) {
    // Validate input parameters
    if (typeof rewardName !== 'string' || rewardName.trim() === '') {
        throw new Error('rewardName must be a non-empty string');
    }
    
    if (typeof rarityData !== 'object' || rarityData === null) {
        throw new Error('rarityData must be a valid object');
    }

    // Normalize the reward name for case-insensitive comparison
    const normalizedRewardName = rewardName.trim().toLowerCase();

    // Check each rarity category for the reward
    for (const [rarity, rewards] of Object.entries(rarityData)) {
        if (!Array.isArray(rewards)) continue;

        const normalizedRewards = rewards.map(r => r.trim().toLowerCase());
        if (normalizedRewards.includes(normalizedRewardName)) {
            return rarity;
        }
    }

    // If not found in any category, return "Unknown"
    return 'Unknown';
}

// Example usage:
/*
const rarityData = {
    "Commun": ["Basic Chair", "Simple Table"],
    "Rare": ["Golden Throne", "Diamond Lamp"],
    "Epic": ["Mystic Fountain", "Legendary Statue"]
};

try {
    const rarity = checkNFTRarity("Basic Chair", rarityData);
    console.log(`Rarity: ${rarity}`); // Output: "Rarity: Commun"
} catch (error) {
    console.error(`Error: ${error.message}`);
}
*/
```
