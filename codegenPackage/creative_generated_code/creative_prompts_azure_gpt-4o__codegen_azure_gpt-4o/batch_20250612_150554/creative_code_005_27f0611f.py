"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Write a JavaScript function that interacts with Ethereum smart contracts to retrieve and display hackathon project data, similar to the projects showcased during ETHBerlin04.
Generated: DETERMINISTIC_27f0611f324deca1
Batch ID: 20250612_150554
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import required libraries
// Ensure Web3.js is installed via npm (`npm install web3`) before running this code
const Web3 = require('web3');

// Define the Ethereum provider (use Infura or another provider URL)
const providerUrl = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';

// Connect to the Ethereum provider
const web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));

// Smart contract details (replace these with the actual contract address and ABI)
const contractAddress = '0xYourContractAddressHere';
const contractABI = [
  // Replace this with the actual ABI for your smart contract
];

// Create a contract instance
const hackathonContract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * Function to retrieve hackathon project data from the smart contract
 * @param {number} projectId - The ID of the project to retrieve
 * @returns {Promise<void>} - Displays project data in the console
 */
async function getHackathonProjectData(projectId) {
  try {
    // Validate the project ID
    if (typeof projectId !== 'number' || projectId < 0) {
      throw new Error('Invalid project ID. Please provide a positive integer.');
    }

    // Call the smart contract method to fetch project data
    const projectData = await hackathonContract.methods.getProjectData(projectId).call();

    // Display project data
    console.log('Hackathon Project Data:', projectData);
  } catch (error) {
    // Handle errors appropriately
    console.error('Error retrieving project data:', error.message || error);
  }
}

// Example usage
// Replace the project ID with a valid one as per your smart contract logic
const exampleProjectId = 1;
getHackathonProjectData(exampleProjectId);

module.exports = { getHackathonProjectData };
```
