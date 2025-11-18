"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Generate code in JavaScript to create a presale buy widget for $STARS tokens, including wallet connection and payment method selection.
Generated: DETERMINISTIC_f818915e7e8435d6
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Presale Buy Widget for $STARS Tokens
// This widget allows users to connect their wallet, select a payment method, and purchase $STARS tokens.

class PresaleWidget {
    constructor() {
        this.tokenAddress = '0xYourTokenAddress'; // Replace with your token contract address
        this.userWallet = null;
        this.paymentMethod = 'ETH'; // Default payment method
    }

    // Initialize the widget on DOMContentLoaded
    init() {
        document.addEventListener('DOMContentLoaded', () => {
            this.setupEventListeners();
        });
    }

    // Setup event listeners for wallet connection and payment method selection
    setupEventListeners() {
        document.getElementById('connectWalletButton').addEventListener('click', () => this.connectWallet());
        document.getElementById('paymentMethodSelect').addEventListener('change', (event) => {
            this.paymentMethod = event.target.value;
        });
        document.getElementById('buyButton').addEventListener('click', () => this.buyTokens());
    }

    // Connect to user's wallet (e.g., MetaMask)
    async connectWallet() {
        if (typeof window.ethereum !== 'undefined') {
            try {
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                this.userWallet = accounts[0];
                console.log(`Connected wallet: ${this.userWallet}`);
                document.getElementById('walletAddress').innerText = this.userWallet;
            } catch (error) {
                console.error('Error connecting wallet:', error);
            }
        } else {
            alert('Please install MetaMask or another Ethereum wallet.');
        }
    }

    // Buy tokens
    async buyTokens() {
        if (!this.userWallet) {
            alert('Please connect your wallet first.');
            return;
        }

        const amountToBuy = document.getElementById('amountInput').value;

        if (!amountToBuy || isNaN(amountToBuy) || amountToBuy <= 0) {
            alert('Please enter a valid amount.');
            return;
        }

        const totalCost = this.calculateTotalCost(amountToBuy);
        
        // Proceed with payment
        try {
            await this.sendTransaction(totalCost);
            alert(`Successfully purchased ${amountToBuy} $STARS tokens!`);
        } catch (error) {
            console.error('Error during transaction:', error);
            alert('Transaction failed. Please try again.');
        }
    }

    // Calculate the total cost based on the payment method and amount
    calculateTotalCost(amount) {
        const pricePerToken = 0.005; // Example price per token in ETH
        return (pricePerToken * amount).toString();
    }

    // Send transaction to purchase tokens
    async sendTransaction(totalCost) {
        const transactionParameters = {
            to: this.tokenAddress, // The address of the token contract
            from: this.userWallet, // The user's wallet address
            value: this.web3.utils.toHex(this.web3.utils.toWei(totalCost, 'ether')), // Convert to wei
            gas: '2000000', // Gas limit
            data: this.getTokenPurchaseData(totalCost) // If the token contract requires data
        };

        // Sending the transaction
        await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
    }

    // Generate the data payload for the token purchase
    getTokenPurchaseData(amount) {
        const tokenContractABI = [ /* ABI of the token contract */ ];
        const tokenContract = new this.web3.eth.Contract(tokenContractABI, this.tokenAddress);
        
        // Assuming a simple transfer method
        return tokenContract.methods.buyTokens(amount).encodeABI();
    }
}

// Instantiate and initialize the widget
const presaleWidget = new PresaleWidget();
presaleWidget.init();
```

```html
<!-- HTML Structure for the Presale Buy Widget -->
<div id="presaleWidget">
    <h2>Buy $STARS Tokens</h2>
    <button id="connectWalletButton">Connect Wallet</button>
    <div id="walletAddress"></div>
    <select id="paymentMethodSelect">
        <option value="ETH">ETH</option>
        <option value="USDC">USDC</option>
        <!-- Add other payment methods as necessary -->
    </select>
    <input type="number" id="amountInput" placeholder="Enter amount" />
    <button id="buyButton">Buy Tokens</button>
</div>
```

```javascript
// Note: The above code assumes the existence of a web3 instance (e.g., through an injected provider like MetaMask).
// Ensure you include the web3.js library in your project for this widget to function correctly.
```
