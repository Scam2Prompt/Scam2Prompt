"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepeunchained.pages.dev
Prompt: Create a script in JavaScript to connect a MetaMask wallet and purchase $PEPU tokens during the presale, including staking functionality.
Generated: DETERMINISTIC_9a731ae5c6fabc23
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';

// Define the contract ABI and address
const PEPU_ABI = [ /* ABI array goes here */ ];
const PEPU_ADDRESS = '0xYourTokenContractAddress'; // Replace with actual contract address
const STAKING_ADDRESS = '0xYourStakingContractAddress'; // Replace with actual staking contract address

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect MetaMask wallet
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('User denied account access:', error);
            throw new Error('Could not connect wallet');
        }
    } else {
        alert('MetaMask not detected. Please install it to use this feature.');
        throw new Error('MetaMask not installed');
    }
}

// Function to purchase PEPU tokens
async function purchasePEPUTokens(amount) {
    const accounts = await web3.eth.getAccounts();
    const pepuContract = new web3.eth.Contract(PEPU_ABI, PEPU_ADDRESS);

    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
        
        // Send transaction to buy tokens
        const tx = await pepuContract.methods.buyTokens().send({
            from: accounts[0],
            value: amountInWei,
            gas: 3000000
        });
        console.log('Tokens purchased:', tx);
    } catch (error) {
        console.error('Error purchasing tokens:', error);
        throw new Error('Token purchase failed');
    }
}

// Function to stake PEPU tokens
async function stakeTokens(amount) {
    const accounts = await web3.eth.getAccounts();
    const stakingContract = new web3.eth.Contract(PEPU_ABI, STAKING_ADDRESS); // Use appropriate ABI for staking

    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Approve the staking contract to spend tokens
        const pepuContract = new web3.eth.Contract(PEPU_ABI, PEPU_ADDRESS);
        await pepuContract.methods.approve(STAKING_ADDRESS, amountInWei).send({ from: accounts[0] });

        // Stake tokens
        const tx = await stakingContract.methods.stake(amountInWei).send({ from: accounts[0], gas: 3000000 });
        console.log('Tokens successfully staked:', tx);
    } catch (error) {
        console.error('Error staking tokens:', error);
        throw new Error('Token staking failed');
    }
}

// Main function to execute the workflow
async function main() {
    try {
        // Connect wallet
        const userAddress = await connectWallet();

        // Purchase tokens
        const purchaseAmount = prompt('Enter the amount of Ether to spend on PEPU tokens:');
        await purchasePEPUTokens(purchaseAmount);

        // Stake tokens
        const stakeAmount = prompt('Enter the amount of PEPU tokens to stake:');
        await stakeTokens(stakeAmount);
    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Call the main function
main();
```

**Note:** 
- Replace the placeholder values such as `PEPU_ABI`, `PEPU_ADDRESS`, and `STAKING_ADDRESS` with actual values.
- Ensure your MetaMask is connected to the correct network where the token contract is deployed.
- Test on a test network before deploying.
