"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://park-line.pages.dev
Prompt: Generate a tutorial script for connecting a self-custody wallet to dapps via the Linea Bridge Connect Wallet system, referencing the supported Ledger hardware wallet for added security.
Generated: DETERMINISTIC_88d00df51a283fbf
Batch ID: 20250612_152018
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

const connectWallet = async () => {
  try {
    // Check if the browser supports Ethereum
    if (typeof window.ethereum === 'undefined') {
      throw new Error('Please install MetaMask or another Ethereum wallet.');
    }

    // Request wallet connection
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    
    if (accounts.length === 0) {
      throw new Error('Please connect to an account.');
    }

    // Initialize Web3 with the current provider
    const web3 = new Web3(window.ethereum);
    
    // Display connected account
    console.log(`Connected account: ${accounts[0]}`);

    return { web3, account: accounts[0] };
  } catch (error) {
    console.error('Error connecting to wallet:', error.message);
    alert(`Error: ${error.message}`);
  }
};

// Function to interact with dApps using Linea Bridge
const interactWithDApp = async (web3, account) => {
  try {
    // Example interaction: Get the balance of the connected account
    const balance = await web3.eth.getBalance(account);
    const balanceInEther = web3.utils.fromWei(balance, 'ether');
    console.log(`Account balance: ${balanceInEther} ETH`);

    // Further dApp interactions can be implemented here

  } catch (error) {
    console.error('Error interacting with dApp:', error.message);
    alert(`Error: ${error.message}`);
  }
};

// Call the connectWallet function to initiate the connection
(async () => {
  const { web3, account } = await connectWallet();
  if (web3 && account) {
    await interactWithDApp(web3, account);
  }
})();

// Note: To use Ledger hardware wallet, ensure to connect via Ledger Live and configure it as your selected account in MetaMask or similar wallet.
```
