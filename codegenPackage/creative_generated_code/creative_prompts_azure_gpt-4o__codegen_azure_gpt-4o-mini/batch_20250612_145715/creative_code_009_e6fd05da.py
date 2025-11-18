"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minkycoin.pages.dev
Prompt: Write a program using ethers.js to query $MINKY token details, including its supply and tax rate, and display the information in a user-friendly format.
Generated: DETERMINISTIC_e6fd05dad50d84d0
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries from ethers.js
const { ethers } = require("ethers");

// Constants for the MINKY Token contract
const TOKEN_ADDRESS = "0xYourTokenAddress"; // Replace with the actual MINKY token contract address
const ABI = [
  // Minimal ABI to get the total supply and tax rate (replace with actual ABI if necessary)
  "function totalSupply() view returns (uint256)",
  "function taxRate() view returns (uint256)"
];

// Function to fetch MINKY token details
async function fetchMinkyTokenDetails() {
  try {
    // Connect to the Ethereum network (e.g., using Infura or Alchemy)
    const provider = new ethers.providers.InfuraProvider("mainnet", "your_infura_project_id"); // Replace with your Infura project ID

    // Create a contract instance
    const tokenContract = new ethers.Contract(TOKEN_ADDRESS, ABI, provider);

    // Fetch total supply
    const totalSupply = await tokenContract.totalSupply();
    // Fetch tax rate
    const taxRate = await tokenContract.taxRate();

    // Convert big numbers to human-readable format
    const formattedSupply = ethers.utils.formatUnits(totalSupply, 18); // Assuming the token has 18 decimals
    const formattedTaxRate = ethers.utils.formatUnits(taxRate, 2); // Assuming tax rate is in basis points

    // Display the token details in a user-friendly format
    console.log("MINKY Token Details:");
    console.log(`Total Supply: ${formattedSupply} MINKY`);
    console.log(`Tax Rate: ${formattedTaxRate} %`);
  } catch (error) {
    // Handle and log errors appropriately
    console.error("Error fetching MINKY token details:", error);
  }
}

// Execute the function to fetch and display token details
fetchMinkyTokenDetails();
```
