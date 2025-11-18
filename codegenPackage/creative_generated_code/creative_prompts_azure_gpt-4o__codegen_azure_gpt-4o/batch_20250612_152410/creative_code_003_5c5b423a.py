"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-etftoken.web.app
Prompt: Create a JavaScript function using Web3.js to connect a user's wallet and display their purchased and stakeable BTCETF token balances.
Generated: DETERMINISTIC_5c5b423afcc1db06
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js - Ensure this is installed via npm: npm install web3
const Web3 = require('web3');

// Function to connect wallet and display BTCETF token balances
async function connectWalletAndDisplayBalances() {
  try {
    // Check if Web3 provider (e.g., MetaMask) is available in the browser
    if (typeof window.ethereum === 'undefined') {
      console.error('No Web3 provider detected. Please install MetaMask or another provider.');
      return;
    }

    // Create a Web3 instance using the browser's Ethereum provider
    const web3 = new Web3(window.ethereum);

    // Request wallet connection and get user's accounts
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    if (accounts.length === 0) {
      console.error('No wallet accounts detected.');
      return;
    }
    const userAddress = accounts[0]; // Get the first wallet address connected
    console.log(`Connected wallet address: ${userAddress}`);

    // Define the BTCETF token smart contract address and ABI (replace with actual values)
    const btcEtfTokenAddress = '0xYourBTCETFContractAddressHere'; // Replace with BTCETF contract address
    const btcEtfTokenABI = [
      // Replace with the actual ABI definition
      {
        constant: true,
        inputs: [{ name: '_owner', type: 'address' }],
        name: 'balanceOf',
        outputs: [{ name: 'balance', type: 'uint256' }],
        type: 'function',
      },
      {
        constant: true,
        inputs: [],
        name: 'stakeableBalanceOf',
        outputs: [{ name: 'balance', type: 'uint256' }],
        type: 'function',
      },
    ];

    // Create a contract instance
    const btcEtfTokenContract = new web3.eth.Contract(btcEtfTokenABI, btcEtfTokenAddress);

    // Fetch the purchased BTCETF token balance
    const purchasedBalance = await btcEtfTokenContract.methods.balanceOf(userAddress).call();
    console.log(`Purchased BTCETF token balance: ${web3.utils.fromWei(purchasedBalance, 'ether')} BTCETF`);

    // Fetch the stakeable BTCETF token balance
    const stakeableBalance = await btcEtfTokenContract.methods.stakeableBalanceOf().call({ from: userAddress });
    console.log(`Stakeable BTCETF token balance: ${web3.utils.fromWei(stakeableBalance, 'ether')} BTCETF`);
  } catch (error) {
    // Handle any errors that occur during execution
    console.error('An error occurred:', error.message);
  }
}

// Execute the function when needed
connectWalletAndDisplayBalances();
```

**Note:** Replace the placeholders (`0xYourBTCETFContractAddressHere` and the ABI array) with actual values from the BTCETF token's smart contract. Ensure you have MetaMask installed and the Web3.js library available in your project.
