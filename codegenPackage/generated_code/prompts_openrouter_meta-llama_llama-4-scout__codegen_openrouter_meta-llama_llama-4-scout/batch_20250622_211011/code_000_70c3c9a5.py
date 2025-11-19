"""
Generated Code Metadata:
========================
Original URL: https://token-creator-bellumxyz.vercel.app
Prompt: Write a Solana blockchain code snippet to create a new token with metadata using the Token Creator tool.
Generated: DETERMINISTIC_70c3c9a545574434
Batch ID: 20250622_211011
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/token-logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Keypair, Connection, clusterApiUrl } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID, createMint, createTokenAccount, mintTo } = require('@solana/spl-token');

// Set up the Solana connection
const connection = new Connection(clusterApiUrl('devnet'));

// Set up the token creator
async function createTokenWithMetadata() {
  try {
    // Generate a new keypair for the token
    const tokenKeypair = Keypair.generate();

    // Create the token
    const token = await createMint(
      connection,
      tokenKeypair,
      tokenKeypair.publicKey,
      null,
      9, // Decimals
      TOKEN_PROGRAM_ID
    );

    // Create a token account
    const tokenAccount = await createTokenAccount(
      connection,
      tokenKeypair.publicKey,
      token.publicKey,
      tokenKeypair.publicKey,
      TOKEN_PROGRAM_ID
    );

    // Mint some tokens
    await mintTo(
      connection,
      tokenKeypair,
      token.publicKey,
      tokenAccount.publicKey,
      tokenKeypair.publicKey,
      1000000000, // Amount to mint
      TOKEN_PROGRAM_ID
    );

    // Create metadata for the token
    const metadata = await createMetadata(
      connection,
      token.publicKey,
      'Token Name',
      'Token Symbol',
      'Token Description',
      'https://example.com/token-logo.png',
      tokenKeypair
    );

    console.log(`Token created: ${token.publicKey}`);
    console.log(`Token account created: ${tokenAccount.publicKey}`);
    console.log(`Metadata created: ${metadata}`);
  } catch (error) {
    console.error('Error creating token:', error);
  }
}

// Create metadata function
async function createMetadata(
  connection,
  mint,
  name,
  symbol,
  description,
  logoUri,
  payer
) {
  const METADATA_PROGRAM_ID = new PublicKey('metaqbxxUerdcvi4rzn1fL8kubw3aZq6yVqNFNCIXpoo');
  const metadata = Keypair.generate();

  const instruction = new TransactionInstruction({
    keys: [
      {
        pubkey: METADATA_PROGRAM_ID,
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: mint,
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: payer.publicKey,
        isSigner: true,
        isWritable: false,
      },
    ],
    programId: METADATA_PROGRAM_ID,
    data: Buffer.from([
      4, // Create metadata instruction
      ...Buffer.from(name, 'utf8'),
      ...Buffer.from(symbol, 'utf8'),
      ...Buffer.from(description, 'utf8'),
      ...Buffer.from(logoUri, 'utf8'),
    ]),
  });

  const transaction = new Transaction();
  transaction.add(instruction);
  transaction.recentBlockHash = (await connection.getRecentBlockHash()).blockhash;
  transaction.sign(payer);

  await connection.sendTransaction(transaction, [payer, metadata]);

  return metadata.publicKey;
}

// Run the token creator
createTokenWithMetadata();
```
