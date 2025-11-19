"""
Generated Code Metadata:
========================
Original URL: https://basednormus.pages.dev
Prompt: Write a JavaScript function using ethers.js to fetch and display `$NORMUS` token details, including total supply and contract audit status.
Generated: DETERMINISTIC_b5a36794ab148764
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the ethers library
const { ethers } = require("ethers");

// Define the contract address and ABI for the $NORMUS token
const NORMUS_CONTRACT_ADDRESS = "0xYourTokenContractAddress"; // Replace with the actual contract address
const NORMUS_ABI = [
    // Minimal ABI to get totalSupply and audit status
    "function totalSupply() view returns (uint256)",
    "function auditStatus() view returns (string)"
];

// Function to fetch and display $NORMUS token details
async function fetchNormusTokenDetails() {
    try {
        // Connect to the Ethereum network (using default provider)
        const provider = ethers.getDefaultProvider();

        // Create a contract instance
        const normusContract = new ethers.Contract(NORMUS_CONTRACT_ADDRESS, NORMUS_ABI, provider);

        // Fetch total supply
        const totalSupply = await normusContract.totalSupply();
        // Convert total supply from BigNumber to a human-readable format
        const formattedTotalSupply = ethers.utils.formatUnits(totalSupply, 18); // Assuming 18 decimals

        // Fetch audit status
        const auditStatus = await normusContract.auditStatus();

        // Display the token details
        console.log(`$NORMUS Token Details:`);
        console.log(`Total Supply: ${formattedTotalSupply}`);
        console.log(`Audit Status: ${auditStatus}`);
    } catch (error) {
        // Handle errors gracefully
        console.error("Error fetching $NORMUS token details:", error);
    }
}

// Call the function to fetch and display the token details
fetchNormusTokenDetails();
```
