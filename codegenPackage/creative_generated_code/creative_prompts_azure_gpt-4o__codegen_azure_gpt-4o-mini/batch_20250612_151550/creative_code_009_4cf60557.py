"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Explain how to use Solana's blockchain tools to create a minting platform similar to Buildoors, with `$BLD` token rewards and character progression features.
Generated: DETERMINISTIC_4cf6055749ce3cf4
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and packages for Solana development
const {
  Connection,
  PublicKey,
  clusterApiUrl,
  Keypair,
  SystemProgram,
  Transaction,
  sendAndConfirmTransaction,
} = require('@solana/web3.js');
const {
  Token,
  TOKEN_PROGRAM_ID,
} = require('@solana/spl-token');
const bs58 = require('bs58');

// Define constants
const NETWORK = 'devnet'; // Change to 'mainnet-beta' for production
const CONNECTION_URL = clusterApiUrl(NETWORK);
const REWARD_TOKEN_DECIMALS = 9; // Set decimals for $BLD token

// Create a connection to the Solana cluster
const connection = new Connection(CONNECTION_URL, 'confirmed');

// Generate a new keypair for the minting platform
const platformKeypair = Keypair.generate();

// Function to create a new SPL token for $BLD rewards
async function createRewardToken() {
  try {
    // Create the token
    const mint = await Token.createMint(
      connection,
      platformKeypair,
      platformKeypair.publicKey,
      null,
      REWARD_TOKEN_DECIMALS,
      TOKEN_PROGRAM_ID
    );

    console.log('Reward token mint address:', mint.publicKey.toString());
    return mint;
  } catch (error) {
    console.error('Failed to create reward token:', error);
  }
}

// Function to create a token account for a user
async function createTokenAccount(mintAddress, owner) {
  try {
    const mintPublicKey = new PublicKey(mintAddress);
    const tokenAccount = await Token.getAssociatedTokenAddress(
      TOKEN_PROGRAM_ID,
      mintPublicKey,
      owner,
      true // create if not found
    );

    const transaction = new Transaction().add(
      Token.createAssociatedTokenAccountInstruction(
        TOKEN_PROGRAM_ID,
        mintPublicKey,
        tokenAccount,
        owner,
        platformKeypair.publicKey,
        platformKeypair
      )
    );

    await sendAndConfirmTransaction(connection, transaction, {
      signers: [platformKeypair],
    });

    console.log('Token account created:', tokenAccount.toString());
    return tokenAccount;
  } catch (error) {
    console.error('Failed to create token account:', error);
  }
}

// Function to mint tokens to a user's account
async function mintTokens(mintAddress, recipientAddress, amount) {
  try {
    const mintPublicKey = new PublicKey(mintAddress);
    const recipientPublicKey = new PublicKey(recipientAddress);
    
    const transaction = new Transaction().add(
      Token.createMintToInstruction(
        TOKEN_PROGRAM_ID,
        mintPublicKey,
        recipientPublicKey,
        platformKeypair.publicKey,
        [],
        amount * Math.pow(10, REWARD_TOKEN_DECIMALS) // Adjust for decimals
      )
    );

    await sendAndConfirmTransaction(connection, transaction, {
      signers: [platformKeypair],
    });

    console.log(`Minted ${amount} $BLD tokens to ${recipientAddress}`);
  } catch (error) {
    console.error('Failed to mint tokens:', error);
  }
}

// Entry point
(async () => {
  const rewardToken = await createRewardToken();
  
  // Example: Create a token account for a specific user
  // Replace with actual user public key
  const userPublicKey = 'Enter_User_Public_Key_Here'; 
  const userTokenAccount = await createTokenAccount(rewardToken.publicKey, userPublicKey);
  
  // Example: Mint tokens to the user
  await mintTokens(rewardToken.publicKey, userTokenAccount.toString(), 100); // Mint 100 $BLD
})();
```

Make sure to install the necessary dependencies by running:
```bash
npm install @solana/web3.js @solana/spl-token bs58
```

Replace `Enter_User_Public_Key_Here` with the actual public key of the user to simulate minting tokens.
