"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesolana.com
Prompt: Generate code that demonstrates how to create and manage NFTs on the Solana blockchain, incorporating best practices mentioned in recent Web3 insights from Inside Solana.
Generated: DETERMINISTIC_6891248332354b02
Batch ID: 20250612_152235
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://my-nft-metadata-uri.com/nft.json": {
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
// Import necessary libraries for Solana and NFT management
const {
    Connection,
    PublicKey,
    Keypair,
    Transaction,
    SystemProgram,
    sendAndConfirmTransaction,
} = require('@solana/web3.js');
const {
    createMint,
    createMetadata,
    createMasterEdition,
    TOKEN_PROGRAM_ID,
    Metadata,
    MetadataDataData,
} = require('@metaplex/mpl-token-metadata');
const BN = require('bn.js');

// Constants for Solana RPC and wallet
const SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com';
const connection = new Connection(SOLANA_RPC_URL, 'confirmed');

// Function to create a new NFT
async function createNFT(wallet, name, symbol, uri) {
    // Generate a new mint keypair for the NFT
    const mint = Keypair.generate();

    // Create the mint account for the NFT
    const transaction = new Transaction().add(
        SystemProgram.createAccount({
            fromPubkey: wallet.publicKey,
            newAccountPubkey: mint.publicKey,
            lamports: await connection.getMinimumBalanceForRentExemption(82),
            space: 82,
            programId: TOKEN_PROGRAM_ID,
        }),
        createMint(wallet.publicKey, mint.publicKey, wallet.publicKey, null, 0)
    );

    // Send and confirm the transaction
    await sendAndConfirmTransaction(connection, transaction, [wallet, mint]);

    // Create NFT metadata
    const metadata = Keypair.generate();
    const metadataTx = await createMetadata(
        {
            metadata: metadata.publicKey,
            mint: mint.publicKey,
            updateAuthority: wallet.publicKey,
            payer: wallet.publicKey,
        },
        {
            data: new MetadataDataData({
                name: name,
                symbol: symbol,
                uri: uri,
                sellerFeeBasisPoints: 500, // 5%
                creators: null,
            }),
        },
        wallet
    );

    // Create master edition
    const editionTx = await createMasterEdition(
        {
            edition: metadata.publicKey,
            mint: mint.publicKey,
            updateAuthority: wallet.publicKey,
            payer: wallet.publicKey,
            metadata: metadata.publicKey,
        },
        {
            maxSupply: new BN(0), // For 1 of 1 NFT
        },
        wallet
    );

    console.log("NFT created successfully:", {
        mint: mint.publicKey.toBase58(),
        metadata: metadata.publicKey.toBase58(),
        edition: metadata.publicKey.toBase58(),
    });
}

// Error handling wrapper function
async function main() {
    try {
        // Load your wallet keypair (replace with your keypair loading logic)
        const wallet = Keypair.fromSecretKey(new Uint8Array(JSON.parse(process.env.WALLET_SECRET_KEY)));

        // Define NFT details
        const nftName = "My First NFT";
        const nftSymbol = "NFT1";
        const nftURI = "https://my-nft-metadata-uri.com/nft.json";

        // Create the NFT
        await createNFT(wallet, nftName, nftSymbol, nftURI);
    } catch (error) {
        console.error("Error creating NFT:", error);
    }
}

// Execute main function
main();
```

Make sure to replace `process.env.WALLET_SECRET_KEY` with the appropriate method for loading your wallet's secret key. Ensure you have the necessary dependencies installed in your project, such as `@solana/web3.js` and `@metaplex/mpl-token-metadata`.
