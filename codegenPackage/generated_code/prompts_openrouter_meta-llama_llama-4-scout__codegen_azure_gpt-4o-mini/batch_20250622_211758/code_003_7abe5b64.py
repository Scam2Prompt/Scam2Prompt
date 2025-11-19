"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Design a locator tool using JavaScript and web3.js library to track and display information about Clone Force guardians and their pledges.
Generated: DETERMINISTIC_7abe5b647f8924a8
Batch ID: 20250622_211758
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

# Generated Code:
# ===============

```javascript
// Import the required libraries
const Web3 = require('web3');

// Initialize Web3 with an Ethereum provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'));

// Clone Force Guardians contract address and ABI (Application Binary Interface)
const contractAddress = '0xYourContractAddressHere';
const contractABI = [
    // Add the relevant ABI details here
];

// Create a contract instance
const cloneForceContract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * Fetches the guardian information and their pledges.
 * @param {string} guardianAddress - The Ethereum address of the guardian.
 * @returns {Promise<Object>} - A promise that resolves to an object containing guardian info and pledges.
 */
async function getGuardianInfo(guardianAddress) {
    try {
        // Validate the Ethereum address
        if (!web3.utils.isAddress(guardianAddress)) {
            throw new Error('Invalid Ethereum address');
        }

        // Fetch guardian details from the contract
        const guardianDetails = await cloneForceContract.methods.getGuardianDetails(guardianAddress).call();
        const pledges = await cloneForceContract.methods.getPledges(guardianAddress).call();

        // Return the combined information
        return {
            guardianDetails,
            pledges
        };
    } catch (error) {
        console.error('Error fetching guardian information:', error);
        throw new Error('Failed to fetch guardian information');
    }
}

/**
 * Displays the guardian information and their pledges in the console.
 * @param {string} guardianAddress - The Ethereum address of the guardian.
 */
async function displayGuardianInfo(guardianAddress) {
    try {
        const info = await getGuardianInfo(guardianAddress);
        console.log('Guardian Information:', info.guardianDetails);
        console.log('Pledges:', info.pledges);
    } catch (error) {
        console.error('Error displaying guardian information:', error.message);
    }
}

// Example usage: Replace with a valid guardian address
const guardianAddress = '0xYourGuardianAddressHere';
displayGuardianInfo(guardianAddress);
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID`, `0xYourContractAddressHere`, and `0xYourGuardianAddressHere` with actual values. Also, ensure to fill in the contract ABI with the correct details for the Clone Force Guardians contract.
