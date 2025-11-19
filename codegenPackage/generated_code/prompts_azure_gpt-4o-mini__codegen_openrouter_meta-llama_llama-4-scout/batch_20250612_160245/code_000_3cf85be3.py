"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: How can I connect a MetaMask wallet to a DApp using the Chain Id and Balance features mentioned on the Dapp Starter website?
Generated: DETERMINISTIC_3cf85be3c0fd2ee8
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';

// Define constants for supported chain IDs
const SUPPORTED_CHAIN_IDS = [1, 3, 4, 5, 42]; // Mainnet, Ropsten, Rinkeby, Goerli, Kovan

// Define a class for handling MetaMask connections
class MetaMaskConnector {
  /**
   * Initialize the MetaMask connector
   * @param {function} onConnect - Callback function for when the user connects their wallet
   * @param {function} onDisconnect - Callback function for when the user disconnects their wallet
   */
  constructor(onConnect, onDisconnect) {
    this.onConnect = onConnect;
    this.onDisconnect = onDisconnect;
    this.web3 = new Web3(window.ethereum);
  }

  /**
   * Check if MetaMask is installed and connected
   * @returns {boolean} True if MetaMask is installed and connected, false otherwise
   */
  async isMetaMaskConnected() {
    try {
      const accounts = await this.web3.eth.getAccounts();
      return accounts.length > 0;
    } catch (error) {
      console.error('Error checking MetaMask connection:', error);
      return false;
    }
  }

  /**
   * Connect to MetaMask and handle chain ID and balance
   */
  async connect() {
    try {
      // Check if MetaMask is installed
      if (!window.ethereum) {
        throw new Error('MetaMask is not installed');
      }

      // Request access to the user's Ethereum account
      const accounts = await window.ethereum.request({
        method: 'eth_requestAccounts',
      });

      // Get the current chain ID
      const chainId = await this.web3.eth.getChainId();

      // Check if the chain ID is supported
      if (!SUPPORTED_CHAIN_IDS.includes(chainId)) {
        throw new Error(`Unsupported chain ID: ${chainId}`);
      }

      // Get the user's balance
      const balance = await this.web3.eth.getBalance(accounts[0]);

      // Call the onConnect callback function
      this.onConnect(accounts[0], chainId, balance);

      // Handle chain ID changes
      window.ethereum.on('chainChanged', (newChainId) => {
        if (!SUPPORTED_CHAIN_IDS.includes(newChainId)) {
          console.error(`Unsupported chain ID: ${newChainId}`);
          this.disconnect();
        } else {
          this.web3.eth.getBalance(accounts[0]).then((balance) => {
            this.onConnect(accounts[0], newChainId, balance);
          });
        }
      });

      // Handle account changes
      window.ethereum.on('accountsChanged', (newAccounts) => {
        if (newAccounts.length === 0) {
          this.disconnect();
        } else {
          this.web3.eth.getBalance(newAccounts[0]).then((balance) => {
            this.onConnect(newAccounts[0], chainId, balance);
          });
        }
      });
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
      this.disconnect();
    }
  }

  /**
   * Disconnect from MetaMask
   */
  disconnect() {
    this.onDisconnect();
  }
}

// Example usage:
const onConnect = (account, chainId, balance) => {
  console.log(`Connected to MetaMask: ${account} (Chain ID: ${chainId}, Balance: ${balance})`);
};

const onDisconnect = () => {
  console.log('Disconnected from MetaMask');
};

const metaMaskConnector = new MetaMaskConnector(onConnect, onDisconnect);

document.addEventListener('DOMContentLoaded', async () => {
  if (await metaMaskConnector.isMetaMaskConnected()) {
    metaMaskConnector.connect();
  } else {
    console.log('MetaMask is not connected');
  }
});
```
