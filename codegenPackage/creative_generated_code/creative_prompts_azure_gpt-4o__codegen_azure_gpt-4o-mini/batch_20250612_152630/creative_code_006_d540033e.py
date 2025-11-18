"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catgirlwhitelist.pages.dev
Prompt: Write a function in JavaScript that calculates the rarity of a Catgirl NFT based on the drop rates provided and displays the rarity category (e.g., COMMON, RARE, EPIC).
Generated: DETERMINISTIC_d540033ea5205330
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to determine the rarity of a Catgirl NFT based on drop rates.
 * 
 * @param {number} dropRate - The drop rate of the NFT (in percentage).
 * @returns {string} - The rarity category of the NFT.
 * @throws {Error} - Throws an error if the dropRate is not a number or is out of the expected range (0-100).
 */
function calculateRarity(dropRate) {
    // Validate input
    if (typeof dropRate !== 'number' || dropRate < 0 || dropRate > 100) {
        throw new Error('Invalid drop rate. It must be a number between 0 and 100.');
    }

    // Determine rarity category based on drop rate
    if (dropRate <= 50) {
        return 'COMMON';
    } else if (dropRate <= 80) {
        return 'RARE';
    } else if (dropRate <= 95) {
        return 'EPIC';
    } else {
        return 'LEGENDARY';
    }
}

// Example usage:
try {
    const dropRate = 75; // Replace with actual drop rate
    const rarity = calculateRarity(dropRate);
    console.log(`The rarity of the Catgirl NFT is: ${rarity}`);
} catch (error) {
    console.error(error.message);
}
```
