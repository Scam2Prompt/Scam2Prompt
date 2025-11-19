"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarwallet.co
Prompt: Provide an example of how to use the Stellar web wallet for micropayments and fundraising.
Generated: DETERMINISTIC_9b925f2f8b2610e4
Batch ID: 20250612_162511
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://horizon.stellar.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://horizon-testnet.stellar.org`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://laboratory.stellar.org/#account-creator": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://horizon-testnet.stellar.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example usage of the Stellar web wallet for micropayments and fundraising.
 * This code demonstrates how to use Stellar's SDK to create a micropayment
 * and fundraising system. It leverages the Stellar network for secure and efficient
 * payments.
 *
 * Prerequisites: Install the Stellar SDK using npm (`npm install stellar-sdk`).
 */

const StellarSdk = require('stellar-sdk');
const axios = require('axios');

// Constants
const STELLAR_HORIZON_URL = 'https://horizon.stellar.org'; // Use testnet for testing ('https://horizon-testnet.stellar.org')
const FUNDRAISING_ACCOUNT = 'YOUR_FUNDRAISING_PUBLIC_KEY'; // Replace with your fundraising account public key
const FUNDRAISING_SECRET = 'YOUR_FUNDRAISING_SECRET_KEY'; // Replace with your fundraising account secret key

// Initialize Stellar server
const server = new StellarSdk.Server(STELLAR_HORIZON_URL);

// Configure Stellar SDK to use the public network
StellarSdk.Networks.PUBLIC;

// Function to perform a micropayment
async function performMicropayment(senderSecret, recipientPublicKey, amount) {
  try {
    // Load sender account
    const senderKeypair = StellarSdk.Keypair.fromSecret(senderSecret);
    const senderAccount = await server.loadAccount(senderKeypair.publicKey());

    // Create transaction
    const transaction = new StellarSdk.TransactionBuilder(senderAccount, {
      fee: StellarSdk.BASE_FEE,
      networkPassphrase: StellarSdk.Networks.PUBLIC,
    })
      .addOperation(
        StellarSdk.Operation.payment({
          destination: recipientPublicKey,
          asset: StellarSdk.Asset.native(),
          amount: amount.toString(),
        })
      )
      .setTimeout(30)
      .build();

    // Sign transaction
    transaction.sign(senderKeypair);

    // Submit transaction
    const result = await server.submitTransaction(transaction);
    console.log('Transaction successful:', result);
  } catch (error) {
    console.error('Error performing micropayment:', error.response?.data || error.message);
  }
}

// Function to check and display account balance
async function checkAccountBalance(publicKey) {
  try {
    const account = await server.loadAccount(publicKey);
    console.log(`Balances for account ${publicKey}:`);
    account.balances.forEach((balance) => {
      console.log(`Type: ${balance.asset_type}, Balance: ${balance.balance}`);
    });
  } catch (error) {
    console.error('Error checking account balance:', error.response?.data || error.message);
  }
}

// Fundraising example
async function fundraisingExample() {
  try {
    const donorSecret = 'DONOR_SECRET_KEY'; // Replace with donor's secret key
    const donationAmount = '10'; // Amount to be donated (in XLM)

    console.log('Checking fundraiser account balance...');
    await checkAccountBalance(FUNDRAISING_ACCOUNT);

    console.log(`Performing donation of ${donationAmount} XLM to the fundraiser...`);
    await performMicropayment(donorSecret, FUNDRAISING_ACCOUNT, donationAmount);

    console.log('Updated fundraiser account balance:');
    await checkAccountBalance(FUNDRAISING_ACCOUNT);
  } catch (error) {
    console.error('Error during fundraising example:', error.message);
  }
}

// Main function to execute fundraising example
(async () => {
  console.log('Starting fundraising example...');
  await fundraisingExample();
})();
```

### Notes:
- Replace `YOUR_FUNDRAISING_PUBLIC_KEY`, `YOUR_FUNDRAISING_SECRET_KEY`, and `DONOR_SECRET_KEY` with actual keys.
- For testing, use the Stellar testnet (`https://horizon-testnet.stellar.org`) and generate test accounts using the Stellar Laboratory (https://laboratory.stellar.org/#account-creator).
- Ensure secrets are securely stored and accessed in production environments (e.g., using environment variables).
