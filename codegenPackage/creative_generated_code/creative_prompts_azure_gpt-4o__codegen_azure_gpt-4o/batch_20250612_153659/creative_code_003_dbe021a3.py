"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-creator-seven.vercel.app
Prompt: Provide an example of updating token metadata on the Solana blockchain, referencing the Solana Scaffold Token Creator's metadata update feature.
Generated: DETERMINISTIC_dbe021a3e21e0f20
Batch ID: 20250612_153659
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/new-metadata.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
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
// Import required modules from the solana web3.js and @metaplex libraries
const { Connection, PublicKey, Keypair, Transaction, sendAndConfirmTransaction } = require('@solana/web3.js');
const { Metadata, DataV2, UpdateMetadataAccount } = require('@metaplex-foundation/mpl-token-metadata');

// Load environment variables for configuration
require('dotenv').config();

// Define constants
const SOLANA_RPC_URL = process.env.SOLANA_RPC_URL; // Solana RPC endpoint (e.g., "https://api.mainnet-beta.solana.com")
const TOKEN_METADATA_PROGRAM_ID = new PublicKey(process.env.TOKEN_METADATA_PROGRAM_ID); // Token Metadata Program ID
const OWNER_PRIVATE_KEY = process.env.OWNER_PRIVATE_KEY; // Private key of the token's owner (base58 encoded)
const MINT_ADDRESS = process.env.MINT_ADDRESS; // Address of the mint/token
const NEW_METADATA = {
  name: "Updated Token Name",
  symbol: "NEW",
  uri: "https://example.com/new-metadata.json",
  sellerFeeBasisPoints: 500, // 5% seller fee
  creators: [
    {
      address: "CreatorPublicKey",
      verified: true,
      share: 100,
    },
  ],
};

// Initialize Solana connection and wallet
const connection = new Connection(SOLANA_RPC_URL, "confirmed");
const payer = Keypair.fromSecretKey(Uint8Array.from(JSON.parse(OWNER_PRIVATE_KEY))); // Load keypair from private key
const mintAddress = new PublicKey(MINT_ADDRESS);

// Function to update metadata
async function updateTokenMetadata() {
  try {
    // Find the metadata account for the given mint address
    const metadataAddress = await Metadata.getPDA(mintAddress);

    // Prepare the data for the update
    const newData = new DataV2({
      name: NEW_METADATA.name,
      symbol: NEW_METADATA.symbol,
      uri: NEW_METADATA.uri,
      sellerFeeBasisPoints: NEW_METADATA.sellerFeeBasisPoints,
      creators: NEW_METADATA.creators.map((creator) => ({
        address: new PublicKey(creator.address),
        verified: creator.verified,
        share: creator.share,
      })),
    });

    // Create the instruction
    const updateMetadataInstruction = new UpdateMetadataAccount(
      { feePayer: payer.publicKey },
      {
        metadata: metadataAddress,
        updateAuthority: payer.publicKey,
        data: newData,
      }
    );

    // Create a transaction
    const transaction = new Transaction().add(updateMetadataInstruction);

    // Sign and send the transaction
    const signature = await sendAndConfirmTransaction(connection, transaction, [payer]);

    console.log(`Transaction successful with signature: ${signature}`);
  } catch (error) {
    console.error("Error updating token metadata:", error);
  }
}

// Execute the function
updateTokenMetadata();
```

**Note:** Replace environment variables (`SOLANA_RPC_URL`, `TOKEN_METADATA_PROGRAM_ID`, `OWNER_PRIVATE_KEY`, `MINT_ADDRESS`) and other placeholder values (e.g., "CreatorPublicKey") with actual values before running the script. Ensure that the wallet has sufficient SOL for transaction fees.
