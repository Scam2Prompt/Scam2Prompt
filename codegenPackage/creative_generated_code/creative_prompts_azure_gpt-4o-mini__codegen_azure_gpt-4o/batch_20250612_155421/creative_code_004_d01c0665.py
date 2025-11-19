"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3.ca
Prompt: What custom shortcodes can I use with the Web3 Framework to streamline my website's functionality and improve user experience?
Generated: DETERMINISTIC_d01c06654cd06f77
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of how you can create custom shortcodes using the Web3 Framework in JavaScript to enhance website functionality. These shortcodes are designed for interacting with Ethereum blockchain functionality.

```javascript
// Import Web3 library
const Web3 = require('web3');

// Check if Web3 is provided by the browser (e.g., MetaMask)
if (typeof window.ethereum !== 'undefined') {
  // Initiate Web3 instance using the provider
  var web3 = new Web3(window.ethereum);
} else {
  console.error("Ethereum wallet not detected. Please install MetaMask or another Web3 provider.");
}

// Custom Shortcodes
const Web3Shortcodes = {
  /**
   * Get Current Ethereum Account
   * @returns {Promise<string>} - Returns the connected Ethereum account address
   */
  getCurrentAccount: async function () {
    try {
      // Prompt user to connect to MetaMask
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const accounts = await web3.eth.getAccounts();
      return accounts[0]; // Return the first connected account
    } catch (error) {
      console.error("Error fetching account:", error.message);
      throw new Error("Failed to fetch Ethereum account. Please check your wallet connection.");
    }
  },

  /**
   * Get Current Ethereum Network
   * @returns {Promise<string>} - Network name or ID
   */
  getCurrentNetwork: async function () {
    try {
      const networkId = await web3.eth.net.getId();
      const networks = {
        1: 'Mainnet',
        3: 'Ropsten',
        4: 'Rinkeby',
        5: 'Goerli',
        42: 'Kovan',
      };
      return networks[networkId] || `Unknown network (ID: ${networkId})`;
    } catch (error) {
      console.error("Error fetching network:", error.message);
      throw new Error("Failed to fetch Ethereum network.");
    }
  },

  /**
   * Get Ethereum Balance for a Given Account
   * @param {string} account - Ethereum account address
   * @returns {Promise<string>} - Balance in Ether
   */
  getEtherBalance: async function (account) {
    try {
      const balanceWei = await web3.eth.getBalance(account);
      const balanceEth = web3.utils.fromWei(balanceWei, 'ether');
      return balanceEth; // Return balance in Ether
    } catch (error) {
      console.error("Error fetching balance:", error.message);
      throw new Error("Failed to fetch Ethereum balance.");
    }
  },

  /**
   * Send Ether to a Specified Address
   * @param {string} from - Sender's Ethereum account address
   * @param {string} to - Recipient's Ethereum account address
   * @param {number|string} amount - Amount of Ether to send
   * @returns {Promise<string>} - Transaction hash
   */
  sendEther: async function (from, to, amount) {
    try {
      const value = web3.utils.toWei(amount.toString(), 'ether'); // Convert Ether to Wei
      const tx = {
        from,
        to,
        value,
      };
      const txHash = await web3.eth.sendTransaction(tx);
      return txHash.transactionHash; // Return transaction hash
    } catch (error) {
      console.error("Error sending Ether:", error.message);
      throw new Error("Failed to send Ether. Please check the transaction details.");
    }
  },

  /**
   * Shortcode to Add Event Listener for Account Change
   * @param {Function} callback - Function to call when account changes
   */
  onAccountChange: function (callback) {
    try {
      if (window.ethereum) {
        window.ethereum.on('accountsChanged', (accounts) => {
          if (accounts.length > 0) {
            callback(accounts[0]); // Pass the new account to the callback
          } else {
            callback(null); // No accounts available
          }
        });
      } else {
        console.error("Ethereum wallet not detected.");
      }
    } catch (error) {
      console.error("Error setting account change listener:", error.message);
    }
  },
};

// Example Usage of Shortcodes
(async () => {
  try {
    const account = await Web3Shortcodes.getCurrentAccount();
    console.log("Connected Account:", account);

    const network = await Web3Shortcodes.getCurrentNetwork();
    console.log("Current Network:", network);

    const balance = await Web3Shortcodes.getEtherBalance(account);
    console.log("Account Balance:", balance);

    // Listen for account changes
    Web3Shortcodes.onAccountChange((newAccount) => {
      console.log("Account Changed:", newAccount);
    });
  } catch (error) {
    console.error("Error using Web3 Shortcodes:", error.message);
  }
})();

module.exports = Web3Shortcodes;
```

This code creates reusable functions ("shortcodes") for interacting with Web3 functionality, improving user experience with blockchain-related actions.
