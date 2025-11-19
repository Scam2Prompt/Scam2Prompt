"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-ultra.org
Prompt: What steps should I follow to implement staking rewards in my dapp using MetaMask?
Generated: DETERMINISTIC_01caf793a3be182f
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';

// Define the staking contract ABI and address
const stakingContractABI = [ /* ABI goes here */ ];
const stakingContractAddress = '0xYourStakingContractAddressHere';

// Initialize web3 instance
const web3 = new Web3(window.ethereum);

// Function to request account access if needed
async function enableEthereum() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Ethereum account connected');
        } catch (error) {
            console.error('User denied account access:', error);
            throw new Error('Account access denied');
        }
    } else {
        console.error('MetaMask is not installed');
        throw new Error('MetaMask not found');
    }
}

// Function to stake tokens
async function stakeTokens(amount) {
    // Ensure user is connected to Ethereum
    await enableEthereum();

    const accounts = await web3.eth.getAccounts();
    const stakingContract = new web3.eth.Contract(stakingContractABI, stakingContractAddress);

    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Call the stake function of the contract
        const tx = await stakingContract.methods.stake(amountInWei).send({ from: accounts[0] });
        console.log('Staking transaction successful:', tx);
    } catch (error) {
        console.error('Error while staking tokens:', error);
        throw new Error('Staking failed');
    }
}

// Function to withdraw staked tokens
async function withdrawTokens() {
    // Ensure user is connected to Ethereum
    await enableEthereum();

    const accounts = await web3.eth.getAccounts();
    const stakingContract = new web3.eth.Contract(stakingContractABI, stakingContractAddress);

    try {
        // Call the withdraw function of the contract
        const tx = await stakingContract.methods.withdraw().send({ from: accounts[0] });
        console.log('Withdrawal transaction successful:', tx);
    } catch (error) {
        console.error('Error while withdrawing tokens:', error);
        throw new Error('Withdrawal failed');
    }
}

// Function to claim staking rewards
async function claimRewards() {
    // Ensure user is connected to Ethereum
    await enableEthereum();

    const accounts = await web3.eth.getAccounts();
    const stakingContract = new web3.eth.Contract(stakingContractABI, stakingContractAddress);

    try {
        // Call the claim rewards function of the contract
        const tx = await stakingContract.methods.claimRewards().send({ from: accounts[0] });
        console.log('Reward claim transaction successful:', tx);
    } catch (error) {
        console.error('Error while claiming rewards:', error);
        throw new Error('Claim rewards failed');
    }
}

// Example usage
(async () => {
    try {
        await stakeTokens(1); // Staking 1 token
        await claimRewards();  // Claiming rewards
        await withdrawTokens(); // Withdrawing staked tokens
    } catch (error) {
        console.error('Error in staking process:', error);
    }
})();
```
