"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://husdt-eth.top
Prompt: Provide examples of JavaScript code for querying Ethereum smart contracts in a DeFi context.
Generated: DETERMINISTIC_dd59c0604aa27b03
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ethers } = require("ethers");

// Define the contract ABI and address
const contractABI = [
    // Add the relevant ABI methods you need, for example:
    "function getReserveData(address asset) view returns (uint256 totalLiquidity, uint256 availableLiquidity, uint256 totalStableDebt, uint256 totalVariableDebt, uint256 liquidityRate, uint256 stableBorrowRate, uint256 variableBorrowRate, uint256 averageStableBorrowRate, uint256 liquidityIndex, uint256 variableBorrowIndex)",
    // Add other methods as needed
];

const contractAddress = "0xYourContractAddress"; // Replace with your DeFi contract address

// Initialize provider (Infura, Alchemy, or local node)
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");

// Initialize contract instance
const contract = new ethers.Contract(contractAddress, contractABI, provider);

/**
 * Fetch reserve data for a specific asset in the DeFi protocol.
 * @param {string} assetAddress - The address of the asset to query.
 * @returns {Promise<object>} - An object containing the reserve data.
 */
async function fetchReserveData(assetAddress) {
    try {
        // Call the smart contract function
        const reserveData = await contract.getReserveData(assetAddress);
        
        // Structure the response for clarity
        return {
            totalLiquidity: reserveData[0].toString(),
            availableLiquidity: reserveData[1].toString(),
            totalStableDebt: reserveData[2].toString(),
            totalVariableDebt: reserveData[3].toString(),
            liquidityRate: ethers.utils.formatUnits(reserveData[4], 27), // Adjust based on rate precision
            stableBorrowRate: ethers.utils.formatUnits(reserveData[5], 27),
            variableBorrowRate: ethers.utils.formatUnits(reserveData[6], 27),
            averageStableBorrowRate: ethers.utils.formatUnits(reserveData[7], 27),
            liquidityIndex: ethers.utils.formatUnits(reserveData[8], 27),
            variableBorrowIndex: ethers.utils.formatUnits(reserveData[9], 27),
        };
    } catch (error) {
        console.error("Error fetching reserve data:", error);
        throw new Error("Failed to fetch reserve data.");
    }
}

// Example usage
(async () => {
    const assetAddress = "0xYourAssetAddress"; // Replace with the asset address to query
    
    try {
        const reserveData = await fetchReserveData(assetAddress);
        console.log("Reserve Data:", reserveData);
    } catch (error) {
        console.error("Error in fetching or processing reserve data:", error);
    }
})();
```
