"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metumasikliogginn.godaddysites.com
Prompt: Provide an example of using the ethers.js library to authenticate a user via Metamask login and fetch their transaction history.
Generated: DETERMINISTIC_438de98c899bd45d
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library
import { ethers } from "ethers";

// Function to authenticate user with MetaMask
async function authenticateUser() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error("MetaMask is not installed. Please install it to use this feature.");
        return;
    }

    // Request account access
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];
        console.log("User authenticated:", userAddress);
        return userAddress;
    } catch (error) {
        console.error("User denied account access or there was an error:", error);
    }
}

// Function to fetch transaction history for a given address
async function fetchTransactionHistory(userAddress) {
    // Define the provider (using Etherscan API or Infura as an example)
    const provider = new ethers.providers.InfuraProvider("homestead", YOUR_INFURA_PROJECT_ID);

    try {
        // Fetch transaction history (using Etherscan)
        const transactionHistory = await provider.getHistory(userAddress);
        console.log("Transaction History:", transactionHistory);
        return transactionHistory;
    } catch (error) {
        console.error("Error fetching transaction history:", error);
    }
}

// Main function to execute the authentication and fetching process
async function main() {
    const userAddress = await authenticateUser();
    if (userAddress) {
        await fetchTransactionHistory(userAddress);
    }
}

// Execute the main function
main().catch(error => {
    console.error("Error in main execution:", error);
});

// Note: Replace YOUR_INFURA_PROJECT_ID with your actual Infura project ID for the provider.
```
