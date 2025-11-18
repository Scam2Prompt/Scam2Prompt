"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-flockerz-com.pages.dev
Prompt: Write JavaScript code using Web3.js to connect a MetaMask wallet and execute a staking transaction for $FLOCK tokens.
Generated: DETERMINISTIC_4ca7f2ef08221c02
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
import Web3 from 'web3';

// Define the contract ABI and address (replace with actual values)
const contractABI = [/* ABI Array */];
const contractAddress = '0xYourContractAddress';

// Initialize Web3 and create a new instance
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask wallet
async function connectWallet() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected:', await web3.eth.getAccounts());
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
    }
}

// Function to execute staking transaction
async function stakeTokens(amount) {
    try {
        // Check if MetaMask is connected
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            throw new Error('No account found. Please connect your wallet.');
        }

        // Create a contract instance
        const contract = new web3.eth.Contract(contractABI, contractAddress);

        // Convert amount to Wei (assuming you are working with Ether)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Call the staking function on the contract
        const response = await contract.methods.stake(amountInWei).send({ from: accounts[0] });

        console.log('Staking transaction successful:', response);
    } catch (error) {
        console.error('Error during staking transaction:', error);
    }
}

// Event listener for the connect button
document.getElementById('connectButton').addEventListener('click', connectWallet);

// Event listener for the stake button
document.getElementById('stakeButton').addEventListener('click', () => {
    const amount = document.getElementById('stakeAmount').value;
    stakeTokens(amount);
});
```

**Note:** Replace `/* ABI Array */` with the actual ABI for your staking contract and `'0xYourContractAddress'` with the actual contract address. Ensure that your HTML has elements with IDs `connectButton`, `stakeButton`, and `stakeAmount` for this code to function correctly.
