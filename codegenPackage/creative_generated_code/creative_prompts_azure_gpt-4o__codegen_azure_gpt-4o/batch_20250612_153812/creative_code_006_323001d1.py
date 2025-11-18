"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support-metamask-helps.bravesites.com
Prompt: Write a script that integrates MetaMask with a decentralized application (dApp) to enable seamless login and authentication using Web3.js.
Generated: DETERMINISTIC_323001d1be28d8bd
Batch ID: 20250612_153812
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

// Check if MetaMask is installed
if (window.ethereum) {
  // Create a new Web3 instance using MetaMask's provider
  const web3 = new Web3(window.ethereum);

  // Function to request account access and authenticate user
  async function authenticateWithMetaMask() {
    try {
      // Request account access from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      if (accounts.length === 0) {
        console.error('No accounts found. Please ensure MetaMask is connected.');
        return;
      }

      // Get the first connected account
      const userAccount = accounts[0];

      // Display user's account address in the console or use it for dApp logic
      console.log('User authenticated with MetaMask. Account:', userAccount);

      // Fetch the user's balance (optional, could be used for additional logic)
      const balance = await web3.eth.getBalance(userAccount);
      console.log('Account Balance:', web3.utils.fromWei(balance, 'ether'), 'ETH');

      // You can now proceed with your application logic using the authenticated account
      // Example: Call smart contract functions or store authenticated user info
    } catch (error) {
      console.error('Error during MetaMask authentication:', error);
    }
  }

  // Event listener to detect account changes in MetaMask
  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length > 0) {
      console.log('MetaMask account changed. New account:', accounts[0]);
    } else {
      console.warn('MetaMask account disconnected.');
    }
  });

  // Event listener to detect network changes in MetaMask
  window.ethereum.on('chainChanged', (chainId) => {
    console.log('MetaMask network changed. New chain ID:', chainId);
  });

  // Call the authentication function (e.g., when a user clicks a login button)
  document.getElementById('loginButton').addEventListener('click', authenticateWithMetaMask);
} else {
  console.error('MetaMask is not installed or not detected.');
  // You can prompt the user to install MetaMask or display an appropriate message
}
```

**HTML Example for Login Button**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>dApp Login</title>
</head>
<body>
  <button id="loginButton">Login with MetaMask</button>
  <script src="app.js"></script>
</body>
</html>
``` 

Make sure to save the JavaScript code as `app.js` and include Web3.js in your project using npm (`npm install web3`) or by adding a CDN link for Web3.js in your HTML file.
