"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: How can I connect a MetaMask wallet to a DApp using the Chain Id and Balance features mentioned on the Dapp Starter website?
Generated: DETERMINISTIC_3cf85be3c0fd2ee8
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3 library for blockchain interactions
import Web3 from 'web3';

// Ensure the script is executed after the DOM is fully loaded
window.addEventListener('load', async () => {
  // Check if MetaMask or other Ethereum-compatible browser extension is installed
  if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask detected.');

    try {
      // Initialize a Web3 instance using MetaMask provider
      const web3 = new Web3(window.ethereum);

      // Prompt user to connect their MetaMask wallet
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Get the connected user's wallet address (first account in the list)
      const accounts = await web3.eth.getAccounts();
      const walletAddress = accounts[0];
      console.log('Wallet Address:', walletAddress);

      // Get the chain ID of the connected blockchain
      const chainId = await web3.eth.getChainId();
      console.log('Connected Chain ID:', chainId);

      // Get the balance of the connected wallet in Wei
      const balanceWei = await web3.eth.getBalance(walletAddress);

      // Convert the balance from Wei to Ether for better readability
      const balanceEther = web3.utils.fromWei(balanceWei, 'ether');
      console.log('Wallet Balance in Ether:', balanceEther);

      // Display wallet details (chain ID and balance) on the DApp
      document.getElementById('walletAddress').innerText = `Wallet Address: ${walletAddress}`;
      document.getElementById('chainId').innerText = `Chain ID: ${chainId}`;
      document.getElementById('balance').innerText = `Balance: ${balanceEther} ETH`;
    } catch (error) {
      // Handle any errors that occur during the connection process
      console.error('Error connecting to MetaMask:', error.message);
      alert('An error occurred while connecting to MetaMask. Please check the console for details.');
    }
  } else {
    // Notify the user if MetaMask is not installed
    alert('MetaMask is not installed. Please install MetaMask to use this DApp.');
  }
});

/* HTML Elements required for displaying wallet details */
/* Ensure the following elements exist in your HTML file:
<div id="walletAddress"></div>
<div id="chainId"></div>
<div id="balance"></div>
*/
```
