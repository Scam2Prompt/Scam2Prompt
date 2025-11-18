"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riarus.ru
Prompt: Write a tutorial-style prompt for connecting a Web3 wallet (e.g., MetaMask) to Perpetual Protocol and executing a short position trade with 5x leverage. Include code snippets in JavaScript.
Generated: DETERMINISTIC_3c680ac0a2ac14c3
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import PerpetualProtocol from './PerpetualProtocol.json'; // Import the contract ABI

// Define constants
const CONTRACT_ADDRESS = '0xYourContractAddress'; // Replace with the actual contract address
const LEVERAGE = 5; // Desired leverage
const TOKEN_ADDRESS = '0xYourTokenAddress'; // Replace with the token address for trading
const SLIPPAGE = 0.01; // 1% slippage
const DECIMALS = 18; // Token decimals

// Initialize Web3
let web3 = new Web3(window.ethereum);
let provider;

// Connect to Web3 Wallet (MetaMask)
async function connectWallet() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        provider = new ethers.providers.Web3Provider(window.ethereum);
        console.log("Wallet connected!");
    } catch (error) {
        console.error("Failed to connect wallet: ", error);
    }
}

// Execute Short Position Trade
async function executeShortPosition(amount) {
    const signer = provider.getSigner();
    const contract = new ethers.Contract(CONTRACT_ADDRESS, PerpetualProtocol.abi, signer);
    
    // Calculate the amount with leverage
    const leveragedAmount = ethers.utils.parseUnits((amount * LEVERAGE).toString(), DECIMALS);

    try {
        // Start the short position trade
        const tx = await contract.openShortPosition(TOKEN_ADDRESS, leveragedAmount, {
            gasLimit: 500000,
            value: ethers.utils.parseEther((amount).toString()), // Value to send
        });

        // Wait for transaction to be mined
        await tx.wait();
        console.log("Short position executed: ", tx);
    } catch (error) {
        console.error("Transaction failed: ", error);
    }
}

// Example usage
(async () => {
    await connectWallet(); // Connect to the wallet
    const tradeAmount = 0.1; // Amount in ETH to trade
    await executeShortPosition(tradeAmount); // Execute the short position
})();
```
