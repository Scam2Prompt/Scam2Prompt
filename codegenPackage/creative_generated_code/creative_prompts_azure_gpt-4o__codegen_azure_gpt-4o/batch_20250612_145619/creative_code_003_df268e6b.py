"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbod.com
Prompt: Provide an example of integrating Ethereum wallet functionality into a website using JavaScript, ensuring mobile browser support.
Generated: DETERMINISTIC_df268e6b45883733
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example of integrating Ethereum wallet functionality into a website using JavaScript.
 * This code uses the Web3.js library and Metamask for Ethereum wallet interaction.
 * Make sure to include Web3.js in your project via: npm install web3
 */

// Import Web3
const Web3 = require('web3');

// Initialize Web3 instance
let web3;

// Check if the browser supports Ethereum (e.g., Metamask)
if (window.ethereum) {
  web3 = new Web3(window.ethereum);
} else if (window.web3) {
  // Legacy dapp browsers
  web3 = new Web3(window.web3.currentProvider);
} else {
  // No Ethereum wallet detected
  alert("No Ethereum wallet detected. Please install Metamask or use a compatible browser.");
  throw new Error("Ethereum wallet not detected");
}

/**
 * Function to request wallet connection and fetch accounts.
 */
async function connectWallet() {
  try {
    // Request account access (triggers Metamask connection popup)
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (!accounts || accounts.length === 0) {
      alert("No accounts found. Please ensure your wallet is unlocked.");
      return;
    }

    // Successfully connected
    const walletAddress = accounts[0];
    console.log("Connected wallet address:", walletAddress);
    alert(`Connected wallet: ${walletAddress}`);
    return walletAddress;
  } catch (error) {
    console.error("Error connecting wallet:", error);
    alert("Failed to connect wallet. See console for details.");
  }
}

/**
 * Function to fetch the wallet's Ethereum balance in Ether.
 * @param {string} address - Wallet address to fetch balance for.
 */
async function getWalletBalance(address) {
  try {
    if (!web3.utils.isAddress(address)) {
      throw new Error("Invalid Ethereum address");
    }

    // Fetch balance in Wei
    const balanceWei = await web3.eth.getBalance(address);

    // Convert Wei to Ether
    const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
    console.log(`Balance: ${balanceEther} ETH`);
    alert(`Wallet Balance: ${balanceEther} ETH`);
    return balanceEther;
  } catch (error) {
    console.error("Error fetching wallet balance:", error);
    alert("Failed to fetch wallet balance. See console for details.");
  }
}

/**
 * Attach event listeners for Metamask account changes and chain changes.
 */
function setupWalletListeners() {
  if (window.ethereum) {
    // Listen for account changes
    window.ethereum.on('accountsChanged', (accounts) => {
      console.log("Accounts changed:", accounts);
      alert(`Account changed. Connected account: ${accounts[0]}`);
    });

    // Listen for chain (network) changes
    window.ethereum.on('chainChanged', (chainId) => {
      console.log("Chain changed:", chainId);
      alert(`Chain changed to ID: ${chainId}`);
      // Reload the page to reflect the new chain
      window.location.reload();
    });
  }
}

/**
 * Example usage: Call these functions from your UI event handlers.
 */
document.getElementById('connectWalletButton').addEventListener('click', async () => {
  const walletAddress = await connectWallet();
  if (walletAddress) {
    await getWalletBalance(walletAddress);
  }
});

setupWalletListeners();
```

### Add this HTML snippet to your website to test the integration:
```html
<button id="connectWalletButton">Connect Wallet</button>
<script src="web3.min.js"></script>
<script src="your-script.js"></script>
```

### Dependencies:
- Ensure the `Web3.js` library is installed via `npm install web3` or include it via CDN.
- Metamask extension should be installed in the browser for functionality.
