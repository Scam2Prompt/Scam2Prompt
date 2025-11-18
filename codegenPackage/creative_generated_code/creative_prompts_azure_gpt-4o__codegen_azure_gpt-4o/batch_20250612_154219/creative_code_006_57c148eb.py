"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applecoin-49f.pages.dev
Prompt: Create a code snippet for a Solana-based NFT gallery that showcases artwork inspired by the Silly Dragon meme coin.
Generated: DETERMINISTIC_57c148eb53b42ba3
Batch ID: 20250612_154219
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}/gallery`": {
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
/**
 * Solana NFT Gallery
 * This script creates a simple NFT gallery for displaying Silly Dragon-themed artwork.
 * It connects to the Solana blockchain, fetches NFT metadata, and renders the gallery.
 */

// Import necessary modules
const { Connection, PublicKey } = require('@solana/web3.js');
const { Metadata } = require('@metaplex-foundation/mpl-token-metadata');
const express = require('express');
const path = require('path');

// Constants
const SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com'; // Solana RPC endpoint
const COLLECTION_CREATOR_ADDRESS = 'YOUR_COLLECTION_CREATOR_ADDRESS'; // Replace with your creator's public key
const PORT = 3000; // Port for the local server

// Initialize Solana connection
const connection = new Connection(SOLANA_RPC_URL);

// Initialize Express app
const app = express();

// Serve static assets (CSS, images, etc.)
app.use(express.static(path.join(__dirname, 'public')));

/**
 * Fetch NFT metadata for a given creator address
 * @param {string} creatorAddress - Public key of the collection creator
 * @returns {Promise<Array>} - List of NFTs with metadata
 */
async function fetchNFTsFromCreator(creatorAddress) {
  try {
    const creatorPublicKey = new PublicKey(creatorAddress);

    // Fetch all accounts owned by the creator
    const accounts = await connection.getProgramAccounts(Metadata.programId, {
      filters: [
        {
          // Filter: Metadata accounts where the creator matches
          memcmp: {
            offset: 326, // Creator's public key is located at offset 326 in metadata
            bytes: creatorPublicKey.toString(),
          },
        },
      ],
    });

    // Parse NFT metadata
    const nfts = accounts.map((account) => {
      const metadata = Metadata.deserialize(account.account.data);
      return {
        name: metadata.data.name,
        uri: metadata.data.uri,
        symbol: metadata.data.symbol,
      };
    });

    return nfts;
  } catch (error) {
    console.error('Error fetching NFTs:', error);
    throw new Error('Failed to fetch NFTs');
  }
}

// Endpoint: Display NFT gallery
app.get('/gallery', async (req, res) => {
  try {
    // Fetch NFTs associated with the Silly Dragon collection
    const nfts = await fetchNFTsFromCreator(COLLECTION_CREATOR_ADDRESS);

    // Render gallery as HTML
    let html = '<!DOCTYPE html><html><head><title>Silly Dragon NFT Gallery</title></head><body>';
    html += '<h1>Silly Dragon NFT Gallery</h1><div style="display: flex; flex-wrap: wrap;">';
    nfts.forEach((nft) => {
      html += `<div style="margin: 10px; border: 1px solid #ddd; padding: 10px;">
                <h2>${nft.name}</h2>
                <p>Symbol: ${nft.symbol}</p>
                <img src="${nft.uri}" alt="${nft.name}" style="max-width: 200px; max-height: 200px;">
               </div>`;
    });
    html += '</div></body></html>';

    res.send(html);
  } catch (error) {
    console.error('Error rendering gallery:', error);
    res.status(500).send('Failed to load gallery');
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Silly Dragon NFT Gallery is running on http://localhost:${PORT}/gallery`);
});

// Note:
// - Replace COLLECTION_CREATOR_ADDRESS with your actual creator's public key.
// - Ensure that NFTs in your collection have valid metadata URIs pointing to image assets.
// - You may need to install the dependencies `@solana/web3.js`, `@metaplex-foundation/mpl-token-metadata`, and `express`.
```
