"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Create a JavaScript function that calculates the total mint price for adopting multiple KevinLand NFTs, given the mint price of 0.03 Ξ per NFT.
Generated: DETERMINISTIC_5fdbbba4025eca5c
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total mint price for adopting multiple KevinLand NFTs.
 * 
 * @param {number} quantity - The number of NFTs to mint.
 * @returns {number} - The total mint price in Ξ.
 * @throws {Error} - Throws an error if the quantity is not a positive integer.
 */
function calculateTotalMintPrice(quantity) {
    const MINT_PRICE_PER_NFT = 0.03; // Mint price per NFT in Ξ

    // Validate input
    if (typeof quantity !== 'number' || quantity <= 0 || !Number.isInteger(quantity)) {
        throw new Error("Quantity must be a positive integer.");
    }

    // Calculate total mint price
    const totalMintPrice = quantity * MINT_PRICE_PER_NFT;

    return totalMintPrice;
}

// Example usage:
try {
    const nftQuantity = 5; // Number of NFTs to mint
    const totalCost = calculateTotalMintPrice(nftQuantity);
    console.log(`Total mint price for ${nftQuantity} NFTs is: ${totalCost} Ξ`);
} catch (error) {
    console.error(error.message);
}
```
