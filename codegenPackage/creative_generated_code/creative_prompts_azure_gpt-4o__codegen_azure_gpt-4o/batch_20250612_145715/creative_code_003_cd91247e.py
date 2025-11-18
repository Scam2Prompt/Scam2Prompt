"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Create a web application using JavaScript and Web3.js that allows users to connect their wallets and purchase $DPOOL tokens directly from Uniswap.
Generated: DETERMINISTIC_cd91247ec3777f78
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and dependencies
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';
import ABI from './abis/UniswapRouter.json'; // ABI of the Uniswap Router

// Constants
const UNISWAP_ROUTER_ADDRESS = '0xYourUniswapRouterAddress'; // Replace with Uniswap router address
const DPOOL_TOKEN_ADDRESS = '0xYourDpoolTokenAddress';      // Replace with $DPOOL token address
const ETH_ADDRESS = '0x0000000000000000000000000000000000000000'; // Address representation for Ether (used in Uniswap)

// Initialize variables
let web3, accounts, uniswapRouter;

async function initializeApp() {
  try {
    // Detect Ethereum provider (e.g., MetaMask)
    const provider = await detectEthereumProvider();
    if (!provider) {
      alert('Please install MetaMask or another Ethereum wallet.');
      return;
    }

    // Initialize Web3 instance
    web3 = new Web3(provider);

    // Request user's accounts (wallet connection)
    accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Initialize Uniswap router contract
    uniswapRouter = new web3.eth.Contract(ABI, UNISWAP_ROUTER_ADDRESS);

    // Update UI with connected wallet address
    document.getElementById('walletAddress').innerText = `Connected Wallet: ${accounts[0]}`;
  } catch (error) {
    console.error('Failed to initialize app:', error);
    alert('Failed to initialize application. Check console for details.');
  }
}

async function purchaseDPoolTokens() {
  try {
    // Get input values from the user
    const ethAmount = document.getElementById('ethAmount').value; // Amount of ETH user wants to spend
    const slippage = parseFloat(document.getElementById('slippage').value) / 100; // User-defined slippage tolerance

    if (!ethAmount || ethAmount <= 0 || isNaN(ethAmount)) {
      alert('Please enter a valid ETH amount.');
      return;
    }

    // Calculate minimum output amount based on slippage
    const ethAmountInWei = web3.utils.toWei(ethAmount, 'ether');
    const amountsOut = await uniswapRouter.methods
      .getAmountsOut(ethAmountInWei, [ETH_ADDRESS, DPOOL_TOKEN_ADDRESS])
      .call();
    const dpoolMinAmountOut = amountsOut[1] - amountsOut[1] * slippage; // Min output after slippage

    // Execute the swap on Uniswap
    const deadline = Math.floor(Date.now() / 1000) + 60 * 10; // Transaction deadline (10 minutes from now)
    await uniswapRouter.methods
      .swapExactETHForTokens(
        web3.utils.toHex(dpoolMinAmountOut), // Minimum amount of $DPOOL tokens
        [ETH_ADDRESS, DPOOL_TOKEN_ADDRESS], // Token swap path
        accounts[0],                        // Recipient address
        deadline                            // Deadline timestamp
      )
      .send({
        from: accounts[0],
        value: ethAmountInWei, // ETH amount to send
      });

    alert('Purchase successful!');
  } catch (error) {
    console.error('Failed to purchase $DPOOL tokens:', error);
    alert('Transaction failed. Check console for details.');
  }
}

// Add event listeners to buttons
document.getElementById('connectWalletBtn').addEventListener('click', initializeApp);
document.getElementById('purchaseBtn').addEventListener('click', purchaseDPoolTokens);
```

### HTML (for the Frontend)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Buy $DPOOL Tokens</title>
  <script type="module" src="app.js"></script>
</head>
<body>
  <h1>Buy $DPOOL Tokens</h1>
  <div>
    <button id="connectWalletBtn">Connect Wallet</button>
    <p id="walletAddress">Wallet Address: Not Connected</p>
  </div>

  <div>
    <h2>Purchase $DPOOL</h2>
    <label for="ethAmount">Amount of ETH to Spend:</label>
    <input type="number" id="ethAmount" placeholder="e.g., 0.1" step="0.01" min="0">
    <br>
    <label for="slippage">Slippage Tolerance (%):</label>
    <input type="number" id="slippage" placeholder="e.g., 2" step="1" min="0">
    <br>
    <button id="purchaseBtn">Purchase</button>
  </div>
</body>
</html>
```
