"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedonpepe.pages.dev
Prompt: Write a JavaScript function using ethers.js to connect to the BASE chain and retrieve the total supply of Based $PEPE tokens (`420,690,000,000,000`) from its contract address.
Generated: DETERMINISTIC_542cc7742039de05
Batch ID: 20250612_151343
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.base.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require('ethers');

/**
 * Connects to the BASE chain and retrieves the total supply of Based $PEPE tokens.
 * 
 * @async
 * @function getBasedPepeTotalSupply
 * @param {string} rpcUrl - The RPC URL of the BASE chain.
 * @param {string} contractAddress - The Based $PEPE token contract address.
 * @returns {Promise<string>} - Total supply of Based $PEPE tokens as a string.
 * @throws {Error} - Throws an error if connection fails or data retrieval encounters an issue.
 */
async function getBasedPepeTotalSupply(rpcUrl, contractAddress) {
    try {
        // Connect to the Base chain using the provided RPC URL
        const provider = new ethers.JsonRpcProvider(rpcUrl);

        // ABI for ERC20 token standard (simplified to include the 'totalSupply' function)
        const erc20ABI = [
            "function totalSupply() view returns (uint256)"
        ];

        // Create a contract instance for the Based $PEPE token
        const basedPepeContract = new ethers.Contract(contractAddress, erc20ABI, provider);

        // Retrieve the total supply from the contract
        const totalSupply = await basedPepeContract.totalSupply();

        // Convert the total supply from BigNumber to string and return it
        return totalSupply.toString();
    } catch (error) {
        // Log the error and rethrow it for proper error handling upstream
        console.error("Error while fetching total supply:", error);
        throw new Error("Failed to fetch Based $PEPE total supply.");
    }
}

// Example Usage:
// Replace `rpcUrl` and `contractAddress` with actual values.
const rpcUrl = "https://mainnet.base.org"; // Replace with BASE chain RPC URL
const contractAddress = "0xYourBasedPepeTokenContractAddressHere"; // Replace with Based $PEPE contract address

getBasedPepeTotalSupply(rpcUrl, contractAddress)
    .then(totalSupply => {
        console.log("Total Supply of Based $PEPE:", totalSupply);
    })
    .catch(error => {
        console.error("Error:", error.message);
    });

```
