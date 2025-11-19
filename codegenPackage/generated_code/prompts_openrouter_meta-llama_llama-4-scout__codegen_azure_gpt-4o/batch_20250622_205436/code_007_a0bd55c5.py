"""
Generated Code Metadata:
========================
Original URL: https://injective.news
Prompt: "Create a basic example of a decentralized application (dApp) that utilizes Injective's oracle for price feeds."
Generated: DETERMINISTIC_a0bd55c510202bb0
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { Wallet, Provider, MsgCreateOracleRequest, MsgQueryOraclePrice } = require('@injectivelabs/sdk-ts');
const { BigNumberInBase } = require('@injectivelabs/utils');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Configuration
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Your wallet's private key
const RPC_URL = process.env.RPC_URL; // Injective RPC URL
const ORACLE_NAME = 'price_feed_oracle'; // Name of the oracle
const SYMBOL = 'BTC/USD'; // Symbol for the price feed

// Initialize wallet and provider
const wallet = new Wallet(PRIVATE_KEY);
const provider = new Provider(RPC_URL);

// Function to create an oracle
async function createOracle() {
  try {
    const msg = MsgCreateOracleRequest.fromJSON({
      name: ORACLE_NAME,
      description: 'An oracle for BTC/USD price feed',
      owner: wallet.address,
    });

    const txResponse = await provider.broadcastTx(wallet.signTransaction(msg));
    console.log('Oracle created successfully:', txResponse.txHash);
  } catch (error) {
    console.error('Error creating oracle:', error.message);
  }
}

// Function to query price from the oracle
async function queryPrice() {
  try {
    const msg = MsgQueryOraclePrice.fromJSON({
      oracleName: ORACLE_NAME,
      symbol: SYMBOL,
    });

    const priceResponse = await provider.query(msg);
    const price = new BigNumberInBase(priceResponse.price).toFixed(2);
    console.log(`Price for ${SYMBOL}: $${price}`);
  } catch (error) {
    console.error('Error querying price:', error.message);
  }
}

// Main function to demonstrate the dApp functionality
async function main() {
  console.log('Starting dApp...');
  
  // Create the oracle
  await createOracle();

  // Query the price feed
  await queryPrice();
}

// Execute the main function
main().catch((error) => {
  console.error('Unexpected error:', error.message);
});
```

### Notes:
- Ensure you have the `@injectivelabs/sdk-ts` and `dotenv` packages installed (`npm install @injectivelabs/sdk-ts dotenv`).
- Set up a `.env` file with your `PRIVATE_KEY` and `RPC_URL` values.
- Replace `RPC_URL` and `PRIVATE_KEY` with valid Injective RPC endpoint and wallet private key, respectively.
- This code assumes the Injective SDK supports the methods used. Adjustments may be needed based on the SDK's actual API.
