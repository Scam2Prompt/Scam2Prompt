"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Write a script to interact with a decentralized application (dApp) that distributes ETH rewards, ensuring compatibility with EVM wallets.
Generated: DETERMINISTIC_5ca072c5c5515e76
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');

// Initialize Web3 with the provider (e.g., MetaMask)
const web3 = new Web3(window.ethereum);

// Contract ABI and address (replace with actual values)
const contractABI = [ /* ABI array here */ ];
const contractAddress = '0xYourContractAddressHere';

// Create contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to request account access if needed
async function requestAccountAccess() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
        } catch (error) {
            console.error("User denied account access", error);
            throw new Error("User denied account access");
        }
    } else {
        console.error("Ethereum wallet not detected");
        throw new Error("Ethereum wallet not detected");
    }
}

// Function to get ETH rewards
async function getRewards() {
    try {
        // Request account access
        await requestAccountAccess();

        // Get accounts
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Call the contract function to get rewards
        const rewards = await contract.methods.getRewards(userAddress).call();
        
        console.log(`Rewards for ${userAddress}: ${web3.utils.fromWei(rewards, 'ether')} ETH`);
        return rewards;
    } catch (error) {
        console.error("Error fetching rewards:", error);
        throw error;
    }
}

// Function to claim rewards
async function claimRewards() {
    try {
        // Request account access
        await requestAccountAccess();

        // Get accounts
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Send transaction to claim rewards
        const tx = await contract.methods.claimRewards().send({ from: userAddress });
        
        console.log(`Rewards claimed successfully! Transaction hash: ${tx.transactionHash}`);
        return tx.transactionHash;
    } catch (error) {
        console.error("Error claiming rewards:", error);
        throw error;
    }
}

// Example usage
(async () => {
    try {
        await getRewards(); // Display user's rewards
        // await claimRewards(); // Uncomment to claim rewards
    } catch (error) {
        console.error("An error occurred during the process:", error);
    }
})();
```

**Note**: 
- Replace `/* ABI array here */` with the actual ABI of your smart contract.
- Replace `'0xYourContractAddressHere'` with the actual address of your deployed smart contract.
- Ensure that you have the `web3` library and necessary configurations set up in your environment.
