"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesolana.com
Prompt: Generate code that demonstrates how to create and manage NFTs on the Solana blockchain, incorporating best practices mentioned in recent Web3 insights from Inside Solana.
Generated: DETERMINISTIC_6891248332354b02
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://node1.bundlr.network": {
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
// Import necessary packages and dependencies
const { Connection, clusterApiUrl, Keypair, LAMPORTS_PER_SOL } = require('@solana/web3.js');
const { Metaplex, keypairIdentity, bundlrStorage } = require('@metaplex-foundation/js');
const fs = require('fs');

// Constants
const SOLANA_NETWORK = 'mainnet-beta'; // Change to 'devnet' for testing
const NFT_METADATA = {
  name: 'My First NFT',
  symbol: 'MFT',
  description: 'A test NFT created on Solana.',
  image: './assets/nft-image.png', // Path to your image file
  attributes: [
    { trait_type: 'Background', value: 'Blue' },
    { trait_type: 'Rarity', value: 'Rare' },
  ],
};

// Function to create a connection to the Solana blockchain
async function createConnection() {
  try {
    const connection = new Connection(clusterApiUrl(SOLANA_NETWORK), 'confirmed');
    console.log('Successfully connected to Solana blockchain.');
    return connection;
  } catch (error) {
    console.error('Error creating Solana connection:', error.message);
    throw error;
  }
}

// Function to fund a wallet with SOL (only for devnet testing)
async function airdropSol(connection, publicKey) {
  try {
    const airdropSignature = await connection.requestAirdrop(publicKey, LAMPORTS_PER_SOL);
    await connection.confirmTransaction(airdropSignature);
    console.log('Airdrop successful.');
  } catch (error) {
    console.error('Error during airdrop:', error.message);
    throw error;
  }
}

// Function to initialize Metaplex instance
function initializeMetaplex(connection, keypair) {
  try {
    const metaplex = Metaplex.make(connection)
      .use(keypairIdentity(keypair))
      .use(bundlrStorage({ address: 'https://node1.bundlr.network', providerUrl: clusterApiUrl(SOLANA_NETWORK) }));
    console.log('Metaplex initialized successfully.');
    return metaplex;
  } catch (error) {
    console.error('Error initializing Metaplex:', error.message);
    throw error;
  }
}

// Function to create and upload NFT metadata
async function uploadNFTMetadata(metaplex, metadata) {
  try {
    // Upload metadata and asset to decentralized storage
    const { uri, metadata: uploadedMetadata } = await metaplex.nfts().uploadMetadata({
      name: metadata.name,
      symbol: metadata.symbol,
      description: metadata.description,
      image: fs.readFileSync(metadata.image), // Read image file
      attributes: metadata.attributes,
    });
    console.log('NFT metadata uploaded successfully:', uri);
    return { uri, uploadedMetadata };
  } catch (error) {
    console.error('Error uploading NFT metadata:', error.message);
    throw error;
  }
}

// Function to mint the NFT
async function mintNFT(metaplex, uri, ownerPublicKey) {
  try {
    const { nft } = await metaplex.nfts().create({
      uri,
      name: NFT_METADATA.name,
      sellerFeeBasisPoints: 500, // 5% royalty fee
      symbol: NFT_METADATA.symbol,
      creators: [
        { address: ownerPublicKey, share: 100 },
      ],
    });
    console.log('NFT minted successfully:', nft.address.toBase58());
    return nft;
  } catch (error) {
    console.error('Error minting NFT:', error.message);
    throw error;
  }
}

// Main function
async function main() {
  try {
    console.log('Starting NFT creation process...');

    // Step 1: Establish connection to Solana
    const connection = await createConnection();

    // Step 2: Generate a new wallet keypair
    const wallet = Keypair.generate();
    console.log('Generated new wallet:', wallet.publicKey.toBase58());

    // Step 3: (Optional) Airdrop SOL for testing (devnet only)
    if (SOLANA_NETWORK === 'devnet') {
      await airdropSol(connection, wallet.publicKey);
    }

    // Step 4: Initialize Metaplex instance
    const metaplex = initializeMetaplex(connection, wallet);

    // Step 5: Upload NFT metadata
    const { uri } = await uploadNFTMetadata(metaplex, NFT_METADATA);

    // Step 6: Mint the NFT
    const nft = await mintNFT(metaplex, uri, wallet.publicKey);

    console.log('NFT creation process completed successfully.');
    console.log('NFT Address:', nft.address.toBase58());
  } catch (error) {
    console.error('Error during NFT creation process:', error.message);
  }
}

// Execute main function
main();
```
