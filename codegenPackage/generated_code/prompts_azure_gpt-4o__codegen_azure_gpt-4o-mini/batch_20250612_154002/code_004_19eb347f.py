"""
Generated Code Metadata:
========================
Original URL: https://onc185.vip
Prompt: Write a script using ethers.js to fetch real-time data from an Ethereum-based DeFi platform.
Generated: DETERMINISTIC_19eb347fc7f48791
Batch ID: 20250612_154002
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

// Define the provider to connect to the Ethereum network
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");

// Define the contract address and ABI for the DeFi platform
const contractAddress = "0xYourDeFiContractAddress"; // Replace with the actual contract address
const contractABI = [
    // Replace with the actual ABI of the contract
    "function getReserveData() view returns (uint256 totalLiquidity, uint256 availableLiquidity, uint256 totalBorrows, uint256 totalFees, uint256 interestRate, uint256 lastUpdateTimestamp)"
];

// Create a contract instance
const contract = new ethers.Contract(contractAddress, contractABI, provider);

// Function to fetch real-time data from the DeFi platform
async function fetchDeFiData() {
    try {
        // Call the contract function to get reserve data
        const reserveData = await contract.getReserveData();

        // Destructure the returned data
        const [
            totalLiquidity,
            availableLiquidity,
            totalBorrows,
            totalFees,
            interestRate,
            lastUpdateTimestamp
        ] = reserveData;

        // Log the fetched data
        console.log("DeFi Platform Data:");
        console.log(`Total Liquidity: ${ethers.utils.formatEther(totalLiquidity)} ETH`);
        console.log(`Available Liquidity: ${ethers.utils.formatEther(availableLiquidity)} ETH`);
        console.log(`Total Borrows: ${ethers.utils.formatEther(totalBorrows)} ETH`);
        console.log(`Total Fees: ${ethers.utils.formatEther(totalFees)} ETH`);
        console.log(`Interest Rate: ${ethers.utils.formatUnits(interestRate, 27)}%`); // Assuming interestRate is in 27 decimal format
        console.log(`Last Update Timestamp: ${new Date(lastUpdateTimestamp * 1000).toLocaleString()}`);
    } catch (error) {
        // Handle errors gracefully
        console.error("Error fetching DeFi data:", error);
    }
}

// Fetch data every 30 seconds
setInterval(fetchDeFiData, 30000);

// Initial fetch
fetchDeFiData();
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` and `"0xYourDeFiContractAddress"` with your actual Infura project ID and the DeFi contract address you want to interact with. Also, ensure that the ABI matches the contract you are querying.
