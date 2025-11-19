"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Write a JavaScript function that interacts with Ethereum smart contracts to retrieve and display hackathon project data, similar to the projects showcased during ETHBerlin04.
Generated: DETERMINISTIC_27f0611f324deca1
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Define constants for Ethereum provider and contract ABI
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS';
const CONTRACT_ABI = [
  {
    "inputs": [],
    "name": "getProjects",
    "outputs": [
      {
        "components": [
          {
            "name": "id",
            "type": "uint256"
          },
          {
            "name": "name",
            "type": "string"
          },
          {
            "name": "description",
            "type": "string"
          },
          {
            "name": "team",
            "type": "string"
          }
        ],
        "internalType": "struct Project[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Create a new Ethereum provider
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Create a new contract instance
const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, provider);

/**
 * Retrieves and displays hackathon project data from an Ethereum smart contract.
 * 
 * @async
 * @function getHackathonProjects
 * @returns {Promise<void>}
 */
async function getHackathonProjects() {
  try {
    // Call the contract's getProjects function
    const projects = await contract.getProjects();

    // Display project data
    projects.forEach((project) => {
      console.log(`Project ID: ${project.id}`);
      console.log(`Name: ${project.name}`);
      console.log(`Description: ${project.description}`);
      console.log(`Team: ${project.team}`);
      console.log('------------------------');
    });
  } catch (error) {
    // Handle errors
    console.error('Error retrieving project data:', error);
  }
}

// Example usage
async function main() {
  await getHackathonProjects();
}

main();
```
