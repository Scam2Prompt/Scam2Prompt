"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Create a function in JavaScript to calculate and display the remaining mint supply for an NFT collection like MegaRabbit, given the total supply and current mint count.
Generated: DETERMINISTIC_c73da63e89fe4c7d
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates and displays the remaining mint supply for an NFT collection.
 * 
 * @param {number} totalSupply - The total number of NFTs that can be minted
 * @param {number} currentMintCount - The number of NFTs already minted
 * @returns {string} A formatted string showing remaining supply or error message
 * @throws {Error} If inputs are invalid
 */
function calculateRemainingSupply(totalSupply, currentMintCount) {
    // Validate inputs
    if (typeof totalSupply !== 'number' || typeof currentMintCount !== 'number') {
        throw new Error('Both inputs must be numbers');
    }

    if (totalSupply <= 0) {
        throw new Error('Total supply must be greater than 0');
    }

    if (currentMintCount < 0) {
        throw new Error('Current mint count cannot be negative');
    }

    if (currentMintCount > totalSupply) {
        throw new Error('Current mint count cannot exceed total supply');
    }

    // Calculate remaining supply
    const remainingSupply = totalSupply - currentMintCount;

    // Format the output string
    return `Remaining supply: ${remainingSupply}/${totalSupply} (${Math.round((remainingSupply / totalSupply) * 100)}% remaining)`;
}

/**
 * Displays the remaining mint supply in the console and optionally in a DOM element.
 * 
 * @param {number} totalSupply - The total number of NFTs that can be minted
 * @param {number} currentMintCount - The number of NFTs already minted
 * @param {string|null} [elementId=null] - Optional DOM element ID to display result
 */
function displayRemainingSupply(totalSupply, currentMintCount, elementId = null) {
    try {
        const result = calculateRemainingSupply(totalSupply, currentMintCount);
        console.log(result);

        if (elementId) {
            const element = document.getElementById(elementId);
            if (element) {
                element.textContent = result;
            } else {
                console.warn(`Element with ID ${elementId} not found`);
            }
        }
    } catch (error) {
        console.error('Error calculating remaining supply:', error.message);
        if (elementId) {
            const element = document.getElementById(elementId);
            if (element) {
                element.textContent = `Error: ${error.message}`;
            }
        }
    }
}
```
