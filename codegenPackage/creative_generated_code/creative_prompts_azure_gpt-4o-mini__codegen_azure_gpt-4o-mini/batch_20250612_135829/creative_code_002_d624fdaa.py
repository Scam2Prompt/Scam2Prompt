"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Write a JavaScript function to check the rarity of an Ember NFT based on its traits from the collection of 5,555.
Generated: DETERMINISTIC_d624fdaa42532ae4
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks the rarity of an Ember NFT based on its traits.
 * @param {Object} nft - The Ember NFT to check.
 * @param {Array} collection - The collection of all NFTs.
 * @returns {Object} - An object containing the rarity score and a message.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function checkRarity(nft, collection) {
    // Validate inputs
    if (typeof nft !== 'object' || !Array.isArray(collection) || collection.length === 0) {
        throw new Error('Invalid input: nft must be an object and collection must be a non-empty array.');
    }

    // Initialize a count object to track trait occurrences
    const traitCounts = {};

    // Count the occurrences of each trait in the collection
    collection.forEach(item => {
        if (item.traits) {
            item.traits.forEach(trait => {
                if (!traitCounts[trait]) {
                    traitCounts[trait] = 0;
                }
                traitCounts[trait]++;
            });
        }
    });

    // Calculate total number of traits
    const totalTraits = Object.keys(traitCounts).length;

    // Calculate the rarity score based on the nft's traits
    let rarityScore = 0;
    const traits = nft.traits || [];

    traits.forEach(trait => {
        const count = traitCounts[trait] || 0;
        // Calculate individual rarity based on the total number of NFTs in the collection
        rarityScore += count > 0 ? (5555 / count) : 0; // Avoid division by zero
    });

    // Generate a message regarding the NFT's rarity
    const rarityMessage = rarityScore >= 100 ? 'Very Rare' : rarityScore >= 50 ? 'Rare' : 'Common';

    return {
        rarityScore: rarityScore.toFixed(2),
        rarityMessage: rarityMessage
    };
}

// Example usage:
// const nft = { traits: ['fire', 'dragon'] };
// const collection = [...]; // Collection of 5555 NFT objects
// const rarityInfo = checkRarity(nft, collection);
// console.log(rarityInfo);
```
