"""
Generated Code Metadata:
========================
Original URL: https://memegames-web.pages.dev
Prompt: "Generate a step-by-step guide on how to participate in The Meme Games, including buying $MGMES tokens and selecting a meme athlete, using JavaScript and MetaMask API."
Generated: DETERMINISTIC_6eba772fd1725393
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define constants for the contract and token details
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress'; // Replace with actual token contract address
const TOKEN_ABI = [ /* ABI array here */ ]; // Replace with actual ABI of the token contract
const MEME_GAMES_CONTRACT_ADDRESS = '0xYourMemeGamesContractAddress'; // Replace with actual Meme Games contract address
const MEME_GAMES_ABI = [ /* ABI array here */ ]; // Replace with actual ABI of the Meme Games contract

// Initialize Web3
let web3;
let accounts;

// Function to initialize Web3 and MetaMask
async function initWeb3() {
    if (window.ethereum) {
        web3 = new Web3(window.ethereum);
        try {
            // Request account access
            accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
        } catch (error) {
            console.error('User denied account access:', error);
            alert('Please allow access to your MetaMask account.');
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this application.');
        alert('MetaMask is required to use this application.');
    }
}

// Function to buy $MGMES tokens
async function buyTokens(amount) {
    const tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
    const value = web3.utils.toWei(amount.toString(), 'ether'); // Convert amount to Wei

    try {
        const transaction = await tokenContract.methods.buyTokens().send({
            from: accounts[0],
            value: value,
        });
        console.log('Transaction successful:', transaction);
        alert('Tokens purchased successfully!');
    } catch (error) {
        console.error('Error purchasing tokens:', error);
        alert('Failed to purchase tokens. Please try again.');
    }
}

// Function to select a meme athlete
async function selectMemeAthlete(athleteId) {
    const memeGamesContract = new web3.eth.Contract(MEME_GAMES_ABI, MEME_GAMES_CONTRACT_ADDRESS);

    try {
        const transaction = await memeGamesContract.methods.selectAthlete(athleteId).send({
            from: accounts[0],
        });
        console.log('Athlete selected successfully:', transaction);
        alert('Meme athlete selected successfully!');
    } catch (error) {
        console.error('Error selecting meme athlete:', error);
        alert('Failed to select meme athlete. Please try again.');
    }
}

// Event listener for DOMContentLoaded to initialize Web3
document.addEventListener('DOMContentLoaded', async () => {
    await initWeb3();
});

// Example usage: Call these functions with appropriate parameters
// buyTokens(1); // Call this function to buy tokens
// selectMemeAthlete(1); // Call this function to select a meme athlete
```

**Note:** Replace placeholder values for contract addresses and ABI arrays with actual values before running the code.
