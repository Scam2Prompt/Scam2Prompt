"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-usdh-mint.web.app
Prompt: Provide code to implement a "Mint Now" button in a Solana dApp that triggers the minting process for eligible wallets, as demonstrated on the USDH Hubble Mint platform.
Generated: DETERMINISTIC_a42334106c64183d
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and libraries
const { Connection, PublicKey, clusterApiUrl, Transaction, SystemProgram } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');

// Constants and configuration
const NETWORK = clusterApiUrl('mainnet-beta'); // Solana mainnet URL
const MINT_ADDRESS = new PublicKey('YOUR_MINT_ADDRESS_HERE'); // Replace with your mint address
const DECIMALS = 6; // Token decimal places
const ELIGIBLE_WALLETS = ['WALLET_ADDRESS_1', 'WALLET_ADDRESS_2']; // Replace with eligible wallet addresses

// Initialize the connection to the Solana blockchain
const connection = new Connection(NETWORK, 'confirmed');

// Function to check wallet eligibility
const isEligibleWallet = (walletAddress) => {
  return ELIGIBLE_WALLETS.includes(walletAddress);
};

// Function to handle minting
async function mintTokens(walletAddress, payerPrivateKey) {
  try {
    // Ensure the wallet is eligible
    if (!isEligibleWallet(walletAddress)) {
      throw new Error('Wallet is not eligible for minting.');
    }

    // Create payer's keypair from private key
    const payerKeypair = Keypair.fromSecretKey(Uint8Array.from(payerPrivateKey));
    const payerPublicKey = payerKeypair.publicKey;

    // Create associated token account for the wallet if it doesn't exist
    const associatedTokenAddress = await Token.getAssociatedTokenAddress(
      TOKEN_PROGRAM_ID,
      MINT_ADDRESS,
      new PublicKey(walletAddress)
    );

    const tokenAccountInfo = await connection.getAccountInfo(associatedTokenAddress);
    const instructions = [];

    if (!tokenAccountInfo) {
      instructions.push(
        Token.createAssociatedTokenAccountInstruction(
          payerPublicKey,
          associatedTokenAddress,
          new PublicKey(walletAddress),
          MINT_ADDRESS
        )
      );
    }

    // Mint tokens to the associated token account
    instructions.push(
      Token.createMintToInstruction(
        TOKEN_PROGRAM_ID,
        MINT_ADDRESS,
        associatedTokenAddress,
        payerPublicKey,
        [],
        1 * Math.pow(10, DECIMALS) // Mint 1 token
      )
    );

    // Create transaction and send
    const transaction = new Transaction().add(...instructions);
    transaction.feePayer = payerPublicKey;
    const { blockhash } = await connection.getRecentBlockhash();
    transaction.recentBlockhash = blockhash;

    // Sign and send the transaction
    transaction.sign(payerKeypair);
    const txId = await connection.sendTransaction(transaction, [payerKeypair]);
    await connection.confirmTransaction(txId, 'confirmed');

    console.log(`Mint transaction successful. TxId: ${txId}`);
  } catch (error) {
    console.error('Minting failed:', error.message);
  }
}

// Example usage: Mint Now button handler
async function onMintNowButtonClick(walletAddress, payerPrivateKey) {
  console.log('Mint Now button clicked.');
  await mintTokens(walletAddress, payerPrivateKey);
}

// Example call (replace with actual wallet address and private key)
// onMintNowButtonClick('WALLET_ADDRESS_HERE', [PRIVATE_KEY_ARRAY_HERE]);
```

**Note:** Replace `YOUR_MINT_ADDRESS_HERE` with the mint address, `WALLET_ADDRESS_1`, `WALLET_ADDRESS_2` with eligible wallet addresses, and `'WALLET_ADDRESS_HERE'`, `[PRIVATE_KEY_ARRAY_HERE]` with actual wallet address and private key details. Ensure private keys are stored securely.
