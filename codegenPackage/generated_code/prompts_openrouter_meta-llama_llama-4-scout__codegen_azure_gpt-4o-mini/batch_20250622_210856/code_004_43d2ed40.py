"""
Generated Code Metadata:
========================
Original URL: https://flare-staking-indol.vercel.app
Prompt: Develop a function in JavaScript that calculates the airdrop of LFNTY tokens to NFT holders, given the total supply of tokens and the number of NFT holders.
Generated: DETERMINISTIC_43d2ed4043f1adc0
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the airdrop amount of LFNTY tokens for each NFT holder.
 * 
 * @param {number} totalSupply - The total supply of LFNTY tokens available for airdrop.
 * @param {number} nftHolders - The number of NFT holders eligible for the airdrop.
 * @returns {number} - The amount of LFNTY tokens each NFT holder will receive.
 * @throws {Error} - Throws an error if totalSupply or nftHolders are not valid positive numbers.
 */
function calculateAirdrop(totalSupply, nftHolders) {
    // Validate input parameters
    if (typeof totalSupply !== 'number' || typeof nftHolders !== 'number') {
        throw new Error('Both totalSupply and nftHolders must be numbers.');
    }
    if (totalSupply < 0) {
        throw new Error('totalSupply must be a non-negative number.');
    }
    if (nftHolders <= 0) {
        throw new Error('nftHolders must be a positive number greater than zero.');
    }

    // Calculate the airdrop amount per NFT holder
    const airdropPerHolder = totalSupply / nftHolders;

    // Return the calculated airdrop amount
    return airdropPerHolder;
}

// Example usage
try {
    const totalSupply = 1000000; // Total LFNTY tokens
    const nftHolders = 100; // Number of NFT holders
    const airdropAmount = calculateAirdrop(totalSupply, nftHolders);
    console.log(`Each NFT holder will receive: ${airdropAmount} LFNTY tokens.`);
} catch (error) {
    console.error(`Error calculating airdrop: ${error.message}`);
}
```
