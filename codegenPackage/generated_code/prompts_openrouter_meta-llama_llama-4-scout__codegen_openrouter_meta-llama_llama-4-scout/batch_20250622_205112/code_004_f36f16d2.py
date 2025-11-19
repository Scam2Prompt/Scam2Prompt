"""
Generated Code Metadata:
========================
Original URL: https://launchmynft.pages.dev
Prompt: "Create a code example for burning NFTs on Solana using LaunchMyNFT's NFT Burn tool."
Generated: DETERMINISTIC_f36f16d25c590165
Batch ID: 20250622_205112
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://devnet.bundlr.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://devnet.solana.com": {
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
const { Connection, clusterApiUrl, Keypair, Transaction } = require('@solana/web3.js');
const { bundlrStorage, keypairIdentity, Metaplex } = require('@metaplex-foundation/js');
const { MetaplexPlugin } = require('@metaplex-foundation/js-plugin-toolbox');

// Set up the Solana connection and Metaplex instance
async function setupSolanaConnection() {
    try {
        // Create a new Solana connection
        const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

        // Create a new Metaplex instance
        const metaplex = Metaplex.make(connection)
            .use(keypairIdentity(Keypair.generate()))
            .use(bundlrStorage({
                endpoint: 'https://devnet.bundlr.network',
                providerUrl: 'https://devnet.solana.com',
                timeout: 60000
            }));

        return { connection, metaplex };
    } catch (error) {
        console.error('Error setting up Solana connection:', error);
        throw error;
    }
}

// Burn an NFT using LaunchMyNFT's NFT Burn tool
async function burnNft(nftAddress, creatorKeypair) {
    try {
        // Set up the Solana connection and Metaplex instance
        const { connection, metaplex } = await setupSolanaConnection();

        // Create a new keypair for the creator
        const creatorKp = Keypair.fromSecretKey(creatorKeypair);

        // Get the NFT
        const nft = await metaplex
            .nfts()
            .findByMintAddress({
                mintAddress: nftAddress
            });

        if (!nft) {
            throw new Error(`NFT not found at address ${nftAddress}`);
        }

        // Create a burn transaction
        const tx = await metaplex
            .nfts()
            .burn({
                mintAddress: nftAddress,
                maxBurns: 1
            })
            .transaction();

        // Sign the transaction
        tx.sign([creatorKp]);

        // Send the transaction
        const txid = await connection.sendTransaction(tx);

        console.log(`NFT burned successfully: ${txid}`);
    } catch (error) {
        console.error('Error burning NFT:', error);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        // Replace with your own NFT address and creator keypair
        const nftAddress = 'your-nft-address';
        const creatorKeypair = new Uint8Array([/* your creator keypair */]);

        await burnNft(nftAddress, creatorKeypair);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
```
