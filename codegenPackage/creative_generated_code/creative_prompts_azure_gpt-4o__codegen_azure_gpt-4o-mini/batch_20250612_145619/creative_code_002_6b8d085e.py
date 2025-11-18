"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltovken.com
Prompt: Generate code to enable JavaScript-based interaction with an Ethereum smart contract for managing pledges.
Generated: DETERMINISTIC_6b8d085e2a6cd6e2
Batch ID: 20250612_145619
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8545": {
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
// Import necessary libraries
import Web3 from 'web3';

// ABI and contract address for the smart contract
const contractABI = [ /* ABI array goes here */ ];
const contractAddress = '0xYourContractAddressHere';

// Initialize Web3
const web3 = new Web3(Web3.givenProvider || 'http://localhost:8545');

// Create a contract instance
const pledgeContract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * Function to make a pledge
 * @param {string} userAddress - The address of the user making the pledge
 * @param {number} amount - The amount to pledge
 * @returns {Promise<string>} - The transaction hash
 */
async function makePledge(userAddress, amount) {
    try {
        // Validate input parameters
        if (!web3.utils.isAddress(userAddress)) {
            throw new Error("Invalid user address");
        }
        if (amount <= 0) {
            throw new Error("Pledge amount must be greater than zero");
        }
        
        // Make the pledge transaction
        const transaction = await pledgeContract.methods.makePledge().send({
            from: userAddress,
            value: web3.utils.toWei(amount.toString(), 'ether'),
        });
        
        return transaction.transactionHash;
    } catch (error) {
        console.error("Error making pledge:", error);
        throw error; // Propagate the error after logging
    }
}

/**
 * Function to withdraw a pledge
 * @param {string} userAddress - The address of the user withdrawing their pledge
 * @returns {Promise<string>} - The transaction hash
 */
async function withdrawPledge(userAddress) {
    try {
        // Validate input parameter
        if (!web3.utils.isAddress(userAddress)) {
            throw new Error("Invalid user address");
        }

        // Withdraw the pledge
        const transaction = await pledgeContract.methods.withdrawPledge().send({
            from: userAddress,
        });
        
        return transaction.transactionHash;
    } catch (error) {
        console.error("Error withdrawing pledge:", error);
        throw error; // Propagate the error after logging
    }
}

/**
 * Function to get the total pledged amount
 * @returns {Promise<number>} - The total amount pledged
 */
async function getTotalPledged() {
    try {
        const totalPledged = await pledgeContract.methods.getTotalPledged().call();
        return web3.utils.fromWei(totalPledged, 'ether');
    } catch (error) {
        console.error("Error fetching total pledged:", error);
        throw error; // Propagate the error after logging
    }
}

// Example usage
(async () => {
    const userAddress = '0xYourUserAddressHere';
    try {
        const pledgeAmount = 1; // Amount in Ether
        const pledgeHash = await makePledge(userAddress, pledgeAmount);
        console.log("Pledge successful, transaction hash:", pledgeHash);

        const totalPledged = await getTotalPledged();
        console.log("Total pledged amount:", totalPledged);

        const withdrawHash = await withdrawPledge(userAddress);
        console.log("Withdraw successful, transaction hash:", withdrawHash);
    } catch (error) {
        console.error("An error occurred during the operation:", error);
    }
})();
```
