"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://docs.matrixinfos.com
Prompt: Create a sample code snippet that demonstrates how to integrate $MATRIX Token into a decentralized application (dApp) for financial autonomy.
Generated: DETERMINISTIC_d96ff4773110dcbe
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';
import { Contract } from 'web3-eth-contract';

// Initialize Web3 provider (using MetaMask's provider for this example)
const web3 = new Web3(window.ethereum);

// Define the contract ABI and Address (replace with actual values)
const MATRIX_ABI = [
    // ABI details here
];
const MATRIX_ADDRESS = '0xYourMATRIXTokenAddressHere';

// Create a contract instance
const matrixContract = new Contract(MATRIX_ABI, MATRIX_ADDRESS);

// Function to fetch the user's account
async function getAccount() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0];
    } catch (error) {
        console.error('Error fetching account:', error);
        throw new Error('Could not fetch account; user may not be connected to MetaMask');
    }
}

// Function to get the MATRIX token balance of an account
async function getTokenBalance(account) {
    try {
        const balance = await matrixContract.methods.balanceOf(account).call();
        return web3.utils.fromWei(balance, 'ether'); // Convert from wei to ether
    } catch (error) {
        console.error('Error fetching token balance:', error);
        throw new Error('Could not fetch token balance');
    }
}

// Function to transfer MATRIX tokens
async function transferTokens(to, amount) {
    try {
        const account = await getAccount();
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        const transaction = await matrixContract.methods.transfer(to, amountInWei).send({ from: account });
        console.log('Transaction successful:', transaction);
    } catch (error) {
        console.error('Error during token transfer:', error);
        throw new Error('Token transfer failed');
    }
}

// Event listener for the transfer button
document.getElementById('transferButton').addEventListener('click', async () => {
    const toAddress = document.getElementById('toAddress').value;
    const amount = document.getElementById('amount').value;

    try {
        await transferTokens(toAddress, amount);
        alert('Transfer successful!');
    } catch (error) {
        alert(error.message);
    }
});

// Example function to run when the page is loaded
(async () => {
    try {
        const account = await getAccount();
        const balance = await getTokenBalance(account);
        console.log(`Account: ${account}, MATRIX Balance: ${balance}`);
    } catch (error) {
        console.error('Initialization error:', error);
    }
})();
```

Make sure to replace the placeholders in the ABI and MATRIX_ADDRESS with the actual values for the $MATRIX token contract. This code should be run in an environment where MetaMask is installed and your dApp is able to interact with the Ethereum blockchain.
