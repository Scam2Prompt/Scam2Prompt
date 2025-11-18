"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Generate a step-by-step guide in JavaScript for integrating MetaMask with a webpage to enable users to connect their wallets and buy $SCOTTY tokens using ETH, BNB, MATIC, or USDT.
Generated: DETERMINISTIC_d252696a62f268cf
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Step-by-step guide for integrating MetaMask into a webpage
 * to enable wallet connection and token purchase functionality.
 */

// 1. Include Web3.js library in your project.
// Add this script tag in your HTML file to use Web3.js:
// <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>

// 2. Define global variables.
let web3; // Instance of Web3
let userAddress; // Connected wallet address

// 3. Function to check if MetaMask is installed.
function isMetaMaskInstalled() {
  return typeof window.ethereum !== 'undefined';
}

// 4. Function to request wallet connection.
async function connectWallet() {
  try {
    if (!isMetaMaskInstalled()) {
      alert('MetaMask is not installed. Please install MetaMask and try again.');
      return;
    }

    // Request accounts from MetaMask.
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    userAddress = accounts[0]; // Set the first connected account as the user's address.
    web3 = new Web3(window.ethereum); // Initialize Web3 instance.
    alert(`Wallet connected: ${userAddress}`);
  } catch (error) {
    console.error('Error connecting wallet:', error);
    alert('Failed to connect wallet. See console for details.');
  }
}

// 5. Function to listen for account changes.
function setupAccountChangeListener() {
  if (window.ethereum) {
    window.ethereum.on('accountsChanged', (accounts) => {
      if (accounts.length > 0) {
        userAddress = accounts[0];
        alert(`Account changed. New account: ${userAddress}`);
      } else {
        userAddress = null;
        alert('Wallet disconnected. Please reconnect.');
      }
    });
  }
}

// 6. Function to purchase $SCOTTY tokens.
async function purchaseSCOTTYToken(tokenAddress, paymentToken, paymentAmount) {
  try {
    if (!userAddress || !web3) {
      alert('Please connect your wallet first.');
      return;
    }

    // Define the ABI for the $SCOTTY token contract (replace with actual ABI).
    const scottyTokenABI = [
      // Example function: replace with your token contract's actual ABI.
      {
        "inputs": [
          { "name": "recipient", "type": "address" },
          { "name": "amount", "type": "uint256" }
        ],
        "name": "buyTokens",
        "stateMutability": "nonpayable",
        "type": "function"
      }
    ];

    // Initialize the token contract instance.
    const scottyTokenContract = new web3.eth.Contract(scottyTokenABI, tokenAddress);

    // Define payment token and amount details.
    const paymentDetails = {
      from: userAddress, // User's wallet address.
      value: web3.utils.toWei(paymentAmount.toString(), 'ether') // Convert payment amount to Wei.
    };

    // Call the buyTokens function on the contract.
    await scottyTokenContract.methods.buyTokens(paymentToken, paymentAmount).send(paymentDetails);

    alert('Purchase successful!');
  } catch (error) {
    console.error('Error purchasing tokens:', error);
    alert('Failed to purchase tokens. See console for details.');
  }
}

// 7. Add event listeners for user interactions.
document.getElementById('connectWalletButton').addEventListener('click', connectWallet);
document.getElementById('buyTokensButton').addEventListener('click', () => {
  const tokenAddress = document.getElementById('tokenAddressInput').value;
  const paymentToken = document.getElementById('paymentTokenInput').value;
  const paymentAmount = document.getElementById('paymentAmountInput').value;

  purchaseSCOTTYToken(tokenAddress, paymentToken, paymentAmount);
});

// 8. Setup MetaMask-related events.
setupAccountChangeListener();

// Example HTML structure:
// <button id="connectWalletButton">Connect Wallet</button>
// <input id="tokenAddressInput" placeholder="Token Contract Address" />
// <input id="paymentTokenInput" placeholder="Payment Token (ETH/BNB/MATIC/USDT)" />
// <input id="paymentAmountInput" placeholder="Payment Amount" />
// <button id="buyTokensButton">Buy $SCOTTY Tokens</button>
```

Note: Replace the sample ABI and contract method `buyTokens` with the actual ABI and method from the $SCOTTY token smart contract. Always test in a development environment before deploying to production.
