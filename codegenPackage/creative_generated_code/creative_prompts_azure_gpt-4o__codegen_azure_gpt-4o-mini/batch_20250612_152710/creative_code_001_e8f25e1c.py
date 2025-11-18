"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-s.pages.dev
Prompt: Generate code to connect a decentralized wallet (e.g., MetaMask) to the DOGE20 presale widget for purchasing tokens using ETH, BNB, or USDT.
Generated: DETERMINISTIC_e8f25e1c7008e256
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';  // Web3 library for Ethereum interaction
import { ethers } from 'ethers';  // Ethers.js for handling Ethereum transactions

// Constants
const DOGE20_CONTRACT_ADDRESS = '0xYourDoge20ContractAddress'; // Replace with actual DOGE20 contract address
const ABI = [ /* ABI of the DOGE20 contract */ ]; // Replace with actual ABI

// Initialize Web3 and ethers
let web3;
let provider;

// Connect to MetaMask and get the selected account
async function connectWallet() {
    if (typeof window.ethereum === 'undefined') {
        alert('Please install MetaMask to use this feature.');
        return;
    }

    try {
        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Set up provider and web3 instance
        provider = new ethers.providers.Web3Provider(window.ethereum);
        web3 = new Web3(window.ethereum);
        console.log('Wallet connected:', await getCurrentAccount());
    } catch (error) {
        console.error('Error connecting to wallet:', error);
    }
}

// Get the current Ethereum account
async function getCurrentAccount() {
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    return accounts[0];
}

// Purchase DOGE20 tokens
async function purchaseTokens(amount, currency) {
    const account = await getCurrentAccount();
    
    // Validate that account is connected
    if (!account) {
        alert('Please connect your wallet first.');
        return;
    }

    // Convert the amount to wei (for ETH) and prepare transaction
    let transaction;
    try {
        switch (currency) {
            case 'ETH':
                transaction = {
                    to: DOGE20_CONTRACT_ADDRESS,
                    value: web3.utils.toWei(amount, 'ether'), // Convert ETH to wei
                    gas: 2000000,
                };
                break;
                
            case 'BNB':
                // Logic for BNB purchase (if using Binance Smart Chain)
                transaction = {
                    to: DOGE20_CONTRACT_ADDRESS,
                    value: web3.utils.toWei(amount, 'ether'), // Assuming similar conversion
                    gas: 2000000,
                };
                break;

            case 'USDT':
                // Add logic for USDT purchase (ERC20 token transfer)
                const usdtContract = new ethers.Contract('0xYourUSDTContractAddress', USDT_ABI, provider.getSigner());
                const usdtAmount = ethers.utils.parseUnits(amount, 6); // USDT typically has 6 decimals

                // Approve the DOGE20 contract to spend USDT
                await usdtContract.approve(DOGE20_CONTRACT_ADDRESS, usdtAmount);

                // Call the DOGE20 contract for the purchase
                const doge20Contract = new ethers.Contract(DOGE20_CONTRACT_ADDRESS, ABI, provider.getSigner());
                await doge20Contract.purchaseWithUSDT(usdtAmount);
                console.log('Tokens purchased with USDT');
                return;

            default:
                alert('Unsupported currency type.');
                return;
        }

        // Send the transaction to purchase tokens
        await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transaction],
        });

        console.log('Tokens purchased successfully');
    } catch (error) {
        console.error('Error purchasing tokens:', error);
        alert('Transaction failed: ' + error.message);
    }
}

// Event listeners for UI buttons (assumes buttons with IDs 'connectButton' and 'purchaseButton')
document.getElementById('connectButton').addEventListener('click', connectWallet);
document.getElementById('purchaseButton').addEventListener('click', () => {
    const amount = document.getElementById('amountInput').value; // Get user input for amount
    const currency = document.querySelector('input[name="currency"]:checked').value; // Get selected currency
    purchaseTokens(amount, currency);
});
```

Make sure to replace placeholders like `0xYourDoge20ContractAddress`, `USDT_ABI`, and `0xYourUSDTContractAddress` with actual contract addresses and ABI definitions as necessary.
