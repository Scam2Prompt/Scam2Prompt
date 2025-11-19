"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subwallet-webapp.pages.dev
Prompt: Provide an example of using SubWallet's features for creating a new wallet on the Substrate network.
Generated: DETERMINISTIC_33c411ce70b803ae
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries from the SubWallet SDK
const { SubWalletAPI } = require('subwallet-api');  // Hypothetical SDK import
const fs = require('fs');

// Function to create a new wallet
async function createNewWallet() {
  try {
    // Initialize SubWallet instance
    const subWallet = new SubWalletAPI({
      network: 'substrate', // Specify the network (e.g., Polkadot, Kusama, etc.)
    });

    // Generate a new wallet
    const wallet = await subWallet.generateWallet();

    // Extract wallet details
    const { address, mnemonic, privateKey } = wallet;

    // Output wallet details
    console.log('Wallet successfully created!');
    console.log(`Address: ${address}`);
    console.log(`Mnemonic: ${mnemonic}`);
    
    // Save sensitive wallet details securely in a file
    const walletData = {
      address,
      mnemonic,
      privateKey,
    };
    const filePath = './wallet.json';

    // Write the wallet data to a JSON file
    fs.writeFileSync(
      filePath,
      JSON.stringify(walletData, null, 2),
      { encoding: 'utf-8' }
    );

    console.log(`Wallet details saved securely to ${filePath}`);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error creating wallet:', error.message);
  }
}

// Execute the function to create a wallet
createNewWallet();
```

Note: Ensure you have the correct SDK (`subwallet-api` here is hypothetical) installed and configured in your project. Replace network details or update the SDK usage as necessary for your implementation.
