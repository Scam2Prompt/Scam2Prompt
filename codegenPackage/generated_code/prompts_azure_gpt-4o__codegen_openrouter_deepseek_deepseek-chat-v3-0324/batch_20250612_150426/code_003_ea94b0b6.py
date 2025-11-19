"""
Generated Code Metadata:
========================
Original URL: https://pulsemex.com
Prompt: Create a function in JavaScript using ethers.js to check the deflationary supply of $PLS tokens on the PulseChain network.
Generated: DETERMINISTIC_ea94b0b690904ebd
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const { ethers } = require('ethers');

/**
 * Checks the deflationary supply of $PLS tokens on PulseChain.
 * @param {string} rpcUrl - The RPC URL for the PulseChain network.
 * @param {string} plsTokenAddress - The contract address of the $PLS token.
 * @returns {Promise<{totalSupply: string, burnedSupply: string, circulatingSupply: string}>} An object containing supply metrics.
 * @throws Will throw an error if the RPC connection fails or contract call fails.
 */
async function checkPlsDeflationarySupply(rpcUrl, plsTokenAddress) {
    try {
        // Initialize provider and contract
        const provider = new ethers.providers.JsonRpcProvider(rpcUrl);
        const plsTokenAbi = [
            "function totalSupply() external view returns (uint256)",
            "function balanceOf(address account) external view returns (uint256)"
        ];
        const plsTokenContract = new ethers.Contract(plsTokenAddress, plsTokenAbi, provider);

        // Define burn address (common Ethereum burn address)
        const burnAddress = '0x000000000000000000000000000000000000dEaD';

        // Fetch supply data
        const totalSupply = await plsTokenContract.totalSupply();
        const burnedSupply = await plsTokenContract.balanceOf(burnAddress);

        // Calculate circulating supply
        const circulatingSupply = totalSupply.sub(burnedSupply);

        return {
            totalSupply: ethers.utils.formatUnits(totalSupply, 18),
            burnedSupply: ethers.utils.formatUnits(burnedSupply, 18),
            circulatingSupply: ethers.utils.formatUnits(circulatingSupply, 18)
        };
    } catch (error) {
        console.error('Error checking PLS supply:', error);
        throw new Error(`Failed to check PLS supply: ${error.message}`);
    }
}

module.exports = { checkPlsDeflationarySupply };
```
