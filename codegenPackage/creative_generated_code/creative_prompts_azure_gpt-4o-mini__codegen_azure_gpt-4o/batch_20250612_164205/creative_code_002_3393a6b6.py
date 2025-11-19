"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: What are the unique features of Fortmatic that allow for building dApps without downloads?
Generated: DETERMINISTIC_3393a6b652bbc8af
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to demonstrate the unique features of Fortmatic 
 * that allow for building dApps without downloads.
 * This script uses the Fortmatic SDK to connect to Ethereum blockchain
 * and demonstrates how it simplifies dApp development.
 */

// Import the Fortmatic SDK
const Fortmatic = require('fortmatic');

// Your Fortmatic API key (replace with your own API key for production)
const FORTMATIC_API_KEY = 'YOUR_API_KEY_HERE';

// Initialize Fortmatic with Mainnet (you can switch to test networks if needed)
const fm = new Fortmatic(FORTMATIC_API_KEY);

// Import Web3.js and initialize it with Fortmatic provider
const Web3 = require('web3');
const web3 = new Web3(fm.getProvider());

/**
 * Function to demonstrate Fortmatic's unique features
 */
async function demonstrateFortmaticFeatures() {
  try {
    console.log('Attempting to connect to Ethereum blockchain via Fortmatic...');

    // Request user authentication (login through Fortmatic's web-based modal)
    const accounts = await web3.eth.getAccounts();

    if (accounts.length === 0) {
      console.log('No accounts found. User is not authenticated.');
      return;
    }

    console.log(`User authenticated. Connected account: ${accounts[0]}`);

    // Demonstrate signing a transaction
    const transactionDetails = {
      to: '0x0000000000000000000000000000000000000000', // Dummy address (replace with valid address)
      value: web3.utils.toWei('0.01', 'ether'), // 0.01 ETH
      gas: 21000, // Gas limit
    };

    console.log('Signing a sample transaction...');
    const signedTransaction = await web3.eth.signTransaction(transactionDetails, accounts[0]);

    console.log('Transaction signed successfully:', signedTransaction);

    // Fortmatic's web-based authentication eliminates the need for downloads
    console.log('Fortmatic allows dApp users to interact without needing extensions or app downloads!');
  } catch (error) {
    console.error('An error occurred while demonstrating Fortmatic features:', error.message);
  }
}

// Execute the function
demonstrateFortmaticFeatures();
```

**Note:** To run this code, ensure you have installed the `fortmatic` and `web3` packages via npm (`npm install fortmatic web3`). Replace `YOUR_API_KEY_HERE` with your actual Fortmatic API key.
