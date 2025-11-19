"""
Generated Code Metadata:
========================
Original URL: https://magahat-3gz.pages.dev
Prompt: Write a JavaScript function that calculates the total fees for minting a token in the MAGA•THE•DONALD•TRUMP collection based on the provided fee structure and mint count.
Generated: DETERMINISTIC_e8706e19495367e4
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total fees for minting a token in the MAGA•THE•DONALD•TRUMP collection.
 * 
 * Fee Structure:
 * - First 100 mints: 0.01 ETH each
 * - Next 400 mints (101-500): 0.02 ETH each
 * - Next 500 mints (501-1000): 0.03 ETH each
 * - Mints beyond 1000: 0.05 ETH each
 * 
 * @param {number} mintCount - The current number of tokens minted (must be a non-negative integer)
 * @returns {number} Total fee in ETH for minting the next token
 * @throws {Error} If mintCount is not a non-negative integer
 */
function calculateMintingFee(mintCount) {
    // Validate input
    if (!Number.isInteger(mintCount) || mintCount < 0) {
        throw new Error('mintCount must be a non-negative integer');
    }

    let fee;
    
    if (mintCount < 100) {
        fee = 0.01;
    } else if (mintCount < 500) {
        fee = 0.02;
    } else if (mintCount < 1000) {
        fee = 0.03;
    } else {
        fee = 0.05;
    }
    
    return fee;
}

/**
 * Calculates the total fees for minting multiple tokens in the MAGA•THE•DONALD•TRUMP collection.
 * 
 * @param {number} currentMintCount - The current number of tokens minted before this batch
 * @param {number} quantity - Number of tokens to mint in this batch (must be positive integer)
 * @returns {number} Total fee in ETH for minting all tokens in the batch
 * @throws {Error} If inputs are invalid
 */
function calculateBatchMintingFee(currentMintCount, quantity) {
    // Validate inputs
    if (!Number.isInteger(currentMintCount) || currentMintCount < 0) {
        throw new Error('currentMintCount must be a non-negative integer');
    }
    if (!Number.isInteger(quantity) || quantity <= 0) {
        throw new Error('quantity must be a positive integer');
    }

    let totalFee = 0;
    let remaining = quantity;
    let currentTier = currentMintCount;

    while (remaining > 0) {
        const tierThreshold = currentTier < 100 ? 100 : 
                             currentTier < 500 ? 500 : 
                             currentTier < 1000 ? 1000 : Infinity;
        
        const availableInTier = tierThreshold - currentTier;
        const mintsInThisTier = Math.min(remaining, availableInTier);
        
        totalFee += mintsInThisTier * calculateMintingFee(currentTier);
        remaining -= mintsInThisTier;
        currentTier += mintsInThisTier;
    }

    return totalFee;
}
```
