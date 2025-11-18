"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theheist-solana.web.app
Prompt: Provide an example of how to use Solana's blockchain to create a "First Come, First Serve" (FCFS) airdrop mechanism, as described on Helio's platform.
Generated: DETERMINISTIC_162e31a6feccc133
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
const solanaWeb3 = require('@solana/web3.js');
const splToken = require('@solana/spl-token');

// Configuration for the airdrop
const AIRDROP_TOKEN_MINT = '<TOKEN_MINT_ADDRESS>'; // Replace with your token mint address
const AIRDROP_AMOUNT = 1 * 10 ** 6; // Amount of tokens to airdrop (e.g., 1 token in micro-units)
const MAX_AIRDROP_RECIPIENTS = 100; // Maximum number of recipients
const AIRDROP_AUTHORITY_SECRET_KEY = '<PRIVATE_KEY>'; // Replace with the private key of the airdrop authority

// Initialize Solana connection and wallet
const connection = new solanaWeb3.Connection(solanaWeb3.clusterApiUrl('mainnet-beta'), 'confirmed'); // Use 'devnet' for testing
const airdropAuthority = solanaWeb3.Keypair.fromSecretKey(
  Uint8Array.from(JSON.parse(AIRDROP_AUTHORITY_SECRET_KEY))
);

// Keep track of recipients to ensure FCFS logic
const recipients = new Set();

// Function to airdrop tokens to a recipient
async function airdropTokens(recipientPublicKey) {
  try {
    if (recipients.size >= MAX_AIRDROP_RECIPIENTS) {
      console.log('Airdrop limit reached. No more tokens will be distributed.');
      return;
    }

    if (recipients.has(recipientPublicKey.toBase58())) {
      console.log(`Recipient ${recipientPublicKey.toBase58()} has already received the airdrop.`);
      return;
    }

    // Check if recipient's wallet exists
    const recipientTokenAccount = await splToken.getOrCreateAssociatedTokenAccount(
      connection,
      airdropAuthority,
      new solanaWeb3.PublicKey(AIRDROP_TOKEN_MINT),
      recipientPublicKey
    );

    // Airdrop tokens to the recipient
    const transactionSignature = await splToken.transfer(
      connection,
      airdropAuthority,
      airdropAuthority.publicKey,
      recipientTokenAccount.address,
      airdropAuthority,
      [],
      AIRDROP_AMOUNT
    );

    console.log(
      `Airdropped ${AIRDROP_AMOUNT} tokens to ${recipientPublicKey.toBase58()} - Transaction: ${transactionSignature}`
    );

    // Mark recipient as completed
    recipients.add(recipientPublicKey.toBase58());
  } catch (error) {
    console.error(`Failed to airdrop tokens to ${recipientPublicKey.toBase58()}:`, error);
  }
}

// Example usage: Listening to new users requesting the airdrop
async function listenForAirdropRequests() {
  console.log('Listening for airdrop requests...');

  // Simulated input for demonstration. Replace with actual logic to fetch public keys (e.g., via API)
  const exampleRecipientKeys = [
    '<RECIPIENT_1_PUBLIC_KEY>',
    '<RECIPIENT_2_PUBLIC_KEY>',
    // Add more public keys as needed
  ];

  for (const recipientKeyString of exampleRecipientKeys) {
    const recipientPublicKey = new solanaWeb3.PublicKey(recipientKeyString);

    // Airdrop tokens to the recipient
    await airdropTokens(recipientPublicKey);
  }
}

// Start listening for airdrop requests
listenForAirdropRequests().catch((error) => {
  console.error('Error in airdrop process:', error);
});
```

### Notes:
1. Replace `<TOKEN_MINT_ADDRESS>`, `<PRIVATE_KEY>`, and `<RECIPIENT_1_PUBLIC_KEY>` with actual values.
2. This code assumes you already have an SPL token created and funded.
3. Deploy to a secure environment and use proper key management practices for production.
