"""
Generated Code Metadata:
========================
Original URL: https://poly-market.vercel.app
Prompt: Write code to interact with the PolyMarket 1.0 DApp using the Polygon-Mainnet or Mumbai-Testnet network via a Metamask wallet.
Generated: DETERMINISTIC_7b842da5f330ffd5
Batch ID: 20250612_145821
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
import { ethers } from 'ethers';

// Define the PolyMarket contract ABI and address (replace with actual values)
const POLYMARKET_ABI = [
    // Add the actual ABI of the PolyMarket contract here
];
const POLYMARKET_ADDRESS = '0xYourPolyMarketContractAddress'; // Replace with actual contract address

// Initialize Web3 and provider
let web3;
let provider;

// Function to initialize Web3 and connect to MetaMask
async function initWeb3() {
    if (window.ethereum) {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        provider = new ethers.providers.Web3Provider(window.ethereum);
        web3 = new Web3(window.ethereum);
    } else {
        console.error('MetaMask is not installed. Please install it to use this DApp.');
        alert('Please install MetaMask to use this DApp.');
        return;
    }
}

// Function to get the user's account
async function getAccount() {
    const accounts = await provider.listAccounts();
    if (accounts.length === 0) {
        console.error('No accounts found. Please connect your wallet.');
        alert('No accounts found. Please connect your wallet.');
        return null;
    }
    return accounts[0];
}

// Function to interact with the PolyMarket contract
async function interactWithPolyMarket() {
    try {
        const account = await getAccount();
        if (!account) return;

        // Create a contract instance
        const polyMarketContract = new web3.eth.Contract(POLYMARKET_ABI, POLYMARKET_ADDRESS);

        // Example: Fetch market data (replace with actual function call)
        const marketData = await polyMarketContract.methods.getMarketData().call();
        console.log('Market Data:', marketData);

        // Example: Place a bet (replace with actual function call)
        const betAmount = web3.utils.toWei('0.1', 'ether'); // Example bet amount
        const tx = await polyMarketContract.methods.placeBet(marketId, betAmount).send({ from: account });
        console.log('Transaction successful:', tx);
    } catch (error) {
        console.error('Error interacting with PolyMarket:', error);
        alert('An error occurred while interacting with PolyMarket. Check the console for details.');
    }
}

// Event listener for the "Connect Wallet" button
document.getElementById('connectWalletButton').addEventListener('click', async () => {
    await initWeb3();
});

// Event listener for the "Interact" button
document.getElementById('interactButton').addEventListener('click', async () => {
    await interactWithPolyMarket();
});

// HTML structure (for reference)
// <button id="connectWalletButton">Connect Wallet</button>
// <button id="interactButton">Interact with PolyMarket</button>
```

Make sure to replace the placeholder values in the code with the actual ABI and contract address of the PolyMarket contract. Additionally, ensure that the HTML structure is present in your application for the buttons to work.
