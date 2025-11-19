"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Provide an example of how to check the balance of an account using MetaMask in a DApp, based on the information from Wormhole.
Generated: DETERMINISTIC_10a5198d9ebc1ad4
Batch ID: 20250612_162502
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

// Ensure the code runs only after the DOM has loaded
document.addEventListener('DOMContentLoaded', async () => {
  // Function to check account balance using MetaMask
  async function checkBalance() {
    try {
      // Check if MetaMask (or other Ethereum provider) is installed
      if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install MetaMask to proceed.');
        return;
      }

      // Request access to MetaMask
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Create a Web3 instance using MetaMask's provider
      const web3 = new Web3(window.ethereum);

      // Get the currently selected account in MetaMask
      const accounts = await web3.eth.getAccounts();
      if (accounts.length === 0) {
        console.error('No accounts found. Please ensure your MetaMask account is unlocked.');
        return;
      }

      const account = accounts[0]; // Take the first account as the active one

      // Fetch the balance of the account
      const balanceWei = await web3.eth.getBalance(account);

      // Format the balance from Wei to Ether
      const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

      // Log or display the result
      console.log(`Account: ${account}`);
      console.log(`Balance: ${balanceEther} ETH`);

      // Optionally display balance in the UI (example)
      document.getElementById('balance-display').textContent = `Balance: ${balanceEther} ETH`;
    } catch (error) {
      // Handle errors gracefully
      console.error('An error occurred while checking the account balance:', error.message);
    }
  }

  // Attach event listener to a button (example)
  document.getElementById('check-balance-button').addEventListener('click', checkBalance);
});

// Example HTML:
// <button id="check-balance-button">Check Balance</button>
// <div id="balance-display"></div>
```
