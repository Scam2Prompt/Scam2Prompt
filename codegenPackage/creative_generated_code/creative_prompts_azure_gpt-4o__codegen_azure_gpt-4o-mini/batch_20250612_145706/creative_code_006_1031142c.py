"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: Provide an example of how to fetch voter data from Agora's on-chain governance system using JavaScript or Solidity.
Generated: DETERMINISTIC_1031142c0431141b
Batch ID: 20250612_145706
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

// Define the contract address and ABI for Agora's on-chain governance system
const contractAddress = "0xYourContractAddressHere"; // Replace with the actual contract address
const contractABI = [
    // Replace with the actual ABI of the Agora governance contract
    "function getVoterData(address voterAddress) view returns (string memory voterName, bool hasVoted, uint256 voteChoice)"
];

// Define a function to fetch voter data
async function fetchVoterData(voterAddress) {
    // Validate the input address
    if (!ethers.utils.isAddress(voterAddress)) {
        throw new Error("Invalid voter address provided.");
    }

    // Connect to the Ethereum network (using a provider of your choice)
    const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID"); // Replace with your Infura Project ID
    const contract = new ethers.Contract(contractAddress, contractABI, provider);

    try {
        // Call the contract function to fetch voter data
        const voterData = await contract.getVoterData(voterAddress);
        // Log the voter data
        console.log(`Voter Name: ${voterData.voterName}`);
        console.log(`Has Voted: ${voterData.hasVoted}`);
        console.log(`Vote Choice: ${voterData.voteChoice}`);
    } catch (error) {
        // Handle any errors that occur during the call
        console.error("Error fetching voter data:", error.message);
    }
}

// Example usage:
// Replace with the actual voter's address you want to check
const voterAddress = "0xSomeVoterAddressHere"; // Replace with a valid voter address
fetchVoterData(voterAddress);
```
