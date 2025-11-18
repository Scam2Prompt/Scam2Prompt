"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btxumh.com
Prompt: Create a Node.js script using ethers.js to monitor and retrieve data from an Ethereum smart contract related to ETH pledges.
Generated: DETERMINISTIC_0658c80066f34f03
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { ethers } = require("ethers");

// Define the Ethereum provider and contract details
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura project ID
const INFURA_PROJECT_SECRET = "YOUR_INFURA_PROJECT_SECRET"; // Replace with your Infura project secret
const CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS"; // Replace with your smart contract address
const ABI = [ // Replace with your contract's ABI
    // Include relevant ABI functions here
];

// Create an Ethereum provider using Infura
const provider = new ethers.InfuraProvider("mainnet", {
    projectId: INFURA_PROJECT_ID,
    projectSecret: INFURA_PROJECT_SECRET
});

// Create a contract instance
const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, provider);

// Function to monitor events related to ETH pledges
async function monitorPledges() {
    try {
        // Set up an event listener for the PledgeMade event
        contract.on("PledgeMade", async (from, amount, event) => {
            // Log the pledge details
            console.log(`New pledge made by ${from}: ${ethers.utils.formatEther(amount)} ETH`);
            
            // Optionally, you could retrieve more data from the event object if necessary
            console.log("Event details:", event);
        });

        console.log("Monitoring for new pledges...");

    } catch (error) {
        console.error("Error while monitoring pledges:", error);
    }
}

// Function to fetch current pledge data
async function fetchCurrentPledges() {
    try {
        // Call a function from the contract that returns current pledges
        const currentPledges = await contract.getCurrentPledges(); // Replace with the actual function name
        
        // Log the current pledges
        console.log("Current pledges:", currentPledges);
    } catch (error) {
        console.error("Error while fetching current pledges:", error);
    }
}

// Start monitoring and fetching pledges
monitorPledges();
fetchCurrentPledges();
```

Make sure to replace `YOUR_INFURA_PROJECT_ID`, `YOUR_INFURA_PROJECT_SECRET`, `YOUR_CONTRACT_ADDRESS`, and the ABI array with your actual values. Additionally, ensure that the contract's function names in the code match those defined in your smart contract.
