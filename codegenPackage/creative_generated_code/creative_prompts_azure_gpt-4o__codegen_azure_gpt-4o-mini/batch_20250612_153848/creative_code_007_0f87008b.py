"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: Develop a grant proposal for building a new dApp on Flare that utilizes its Web2 connectivity feature to trigger smart contracts based on external API data.
Generated: DETERMINISTIC_0f87008b137f5365
Batch ID: 20250612_153848
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://flare.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/data": {
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
const Web3 = require('web3');
const axios = require('axios');

// Initialize Web3 with Flare network provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://flare.network'));

// Smart contract ABI and address
const contractABI = [
    // Add your contract's ABI here
];
const contractAddress = '0xYourContractAddress';

// Create a contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to fetch data from an external API
async function fetchExternalData(apiUrl) {
    try {
        const response = await axios.get(apiUrl);
        return response.data;
    } catch (error) {
        console.error('Error fetching data from API:', error);
        throw new Error('API fetch failed');
    }
}

// Function to trigger smart contract function
async function triggerSmartContract(data) {
    const accounts = await web3.eth.getAccounts();
    const callerAccount = accounts[0]; // Select the first account to call the contract

    try {
        const tx = await contract.methods.yourSmartContractMethod(data).send({ from: callerAccount });
        console.log('Transaction successful:', tx.transactionHash);
    } catch (error) {
        console.error('Error sending transaction:', error);
        throw new Error('Transaction failed');
    }
}

// Main function to execute the dApp logic
async function main() {
    const apiUrl = 'https://api.example.com/data'; // Replace with your API URL

    try {
        // Fetch data from external API
        const externalData = await fetchExternalData(apiUrl);
        
        // Trigger the smart contract with the fetched data
        await triggerSmartContract(externalData);
    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Execute the main function
main();
```
