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
 * Function to calculate the rarity category of a Catgirl NFT based on drop rates.
 * @param {number} dropRate - The drop rate percentage for the NFT (0-100).
 * @returns {string} - The rarity category of the NFT ("COMMON", "RARE", "EPIC").
 * @throws {Error} - Throws an error if the dropRate is invalid or out of range.
 */
function calculateCatgirlNftRarity(dropRate) {
  // Validate the input to ensure dropRate is a number within the range of 0-100
  if (typeof dropRate !== 'number' || dropRate < 0 || dropRate > 100) {
    throw new Error('Invalid dropRate. It must be a number between 0 and 100.');
  }

  // Determine the rarity category based on the drop rate
  if (dropRate > 50) {
    return 'COMMON'; // Most frequent category
  } else if (dropRate > 20) {
    return 'RARE'; // Moderate rarity category
  } else {
    return 'EPIC'; // Least frequent category
  }
}

// Example Usage:
try {
  const rarity = calculateCatgirlNftRarity(15); // Replace with actual drop rate
  console.log(`The rarity of the Catgirl NFT is: ${rarity}`); // Outputs: The rarity of the Catgirl NFT is: EPIC
} catch (error) {
  console.error(error.message); // Handle invalid input gracefully
}
```
