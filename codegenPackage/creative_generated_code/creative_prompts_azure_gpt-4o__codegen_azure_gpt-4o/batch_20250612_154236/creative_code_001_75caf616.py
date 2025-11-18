"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfdbull.pages.dev
Prompt: Generate code in JavaScript to automate the process of connecting a wallet (e.g., MetaMask) and purchasing $BTFD tokens using ETH or BNB during the presale.
Generated: DETERMINISTIC_75caf6165fba78e2
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js library
const Web3 = require('web3');

// Contract Details
const PRESALE_CONTRACT_ADDRESS = '0xYourPresaleContractAddress';  // Replace with the presale contract address
const PRESALE_ABI = [/* ABI array here */];                       // Replace with the presale contract's ABI
const TOKEN_SYMBOL = '$BTFD';                                    // Replace with the token symbol
const SUPPORTED_CHAIN_IDS = [1, 56];                             // Ethereum Mainnet (1), Binance Smart Chain Mainnet (56)

// Connect Wallet and Purchase Tokens
async function connectWalletAndBuyTokens(amountToBuy, paymentCurrency) {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
        }

        // Request wallet connection
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];

        console.log(`Wallet connected: ${userAddress}`);

        // Get Chain ID
        const chainId = await window.ethereum.request({ method: 'eth_chainId' });
        const numericChainId = parseInt(chainId, 16);
        if (!SUPPORTED_CHAIN_IDS.includes(numericChainId)) {
            throw new Error(`Unsupported network. Please connect to Ethereum Mainnet or Binance Smart Chain.`);
        }

        console.log(`Connected to chain ID: ${numericChainId}`);

        // Initialize Web3 instance
        const web3 = new Web3(window.ethereum);

        // Reference the presale contract
        const presaleContract = new web3.eth.Contract(PRESALE_ABI, PRESALE_CONTRACT_ADDRESS);

        // Validate payment currency
        if (!['ETH', 'BNB'].includes(paymentCurrency)) {
            throw new Error(`Invalid payment currency. Supported currencies are ETH and BNB.`);
        }

        // Determine payment method
        const paymentMethod = paymentCurrency === 'ETH' ? 'buyWithETH' : 'buyWithBNB';

        // Calculate value in Wei
        const valueToSend = web3.utils.toWei(amountToBuy.toString(), 'ether');

        // Execute transaction
        const tx = await presaleContract.methods[paymentMethod]().send({
            from: userAddress,
            value: valueToSend // Sending ETH or BNB value
        });

        console.log(`Transaction successful! ${amountToBuy} ${TOKEN_SYMBOL} purchased.`);
        console.log(`Transaction hash: ${tx.transactionHash}`);
    } catch (error) {
        // Log errors
        console.error(`Error: ${error.message}`);
    }
}

// Example usage: Connect wallet and buy 1 $BTFD with ETH
connectWalletAndBuyTokens(1, 'ETH');
```

---

**Note:** Replace placeholders (`PRESALE_CONTRACT_ADDRESS`, `PRESALE_ABI`, etc.) with actual values from your presale contract setup, and ensure you have the ABI and network details ready.
