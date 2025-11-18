"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stealt-mint.web.app
Prompt: Write a Solana blockchain-based script to track the burn period of NFTs (Dec 5 - Dec 10) and ensure burned boxes are excluded from utility, as specified in the Magic Box event.
Generated: DETERMINISTIC_c338d70f8bf587ea
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and modules
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const { Metadata } = require('@metaplex-foundation/mpl-token-metadata');
const moment = require('moment');

// Constants
const NETWORK = "mainnet-beta"; // Solana network to connect to
const MAGIC_BOX_PROGRAM_ID = new PublicKey("Your_Magic_Box_Program_ID"); // Replace this with the actual Magic Box event program ID
const START_DATE = moment("2023-12-05T00:00:00Z"); // Start of the burn period
const END_DATE = moment("2023-12-10T23:59:59Z"); // End of the burn period

// Initialize connection to the Solana blockchain
const connection = new Connection(clusterApiUrl(NETWORK), "confirmed");

/**
 * Fetch NFTs for a specific wallet
 * @param {PublicKey} walletAddress - Wallet public key to fetch NFTs for
 * @returns {Array} - List of NFTs metadata
 */
async function fetchNFTs(walletAddress) {
  try {
    const accounts = await connection.getParsedTokenAccountsByOwner(walletAddress, {
      programId: new PublicKey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"), // Solana SPL Token Program
    });

    const nfts = [];
    for (let account of accounts.value) {
      const tokenAmount = account.account.data.parsed.info.tokenAmount;
      if (tokenAmount.decimals === 0 && tokenAmount.uiAmount === 1) { // SPL token with 1 unit and 0 decimals indicates an NFT
        const metadataAddress = await Metadata.getPDA(new PublicKey(account.account.data.parsed.info.mint));
        const metadata = await Metadata.load(connection, metadataAddress);
        nfts.push(metadata.data);
      }
    }
    return nfts;
  } catch (error) {
    console.error("Error fetching NFTs:", error.message);
    return [];
  }
}

/**
 * Check if the NFT was burned during the Magic Box burn period
 * @param {Object} nft - NFT metadata
 * @returns {boolean} - True if NFT was burned during the burn period, false otherwise
 */
function isBurnedDuringEvent(nft) {
  if (!nft.data.uri) return false; // If no metadata URI exists, treat as not burned

  const burnDate = moment(nft.data.updatedOn); // Assuming 'updatedOn' contains the last burn/update timestamp
  return burnDate.isBetween(START_DATE, END_DATE, null, "[]");
}

/**
 * Main function to track burned NFTs and exclude them from utility
 */
async function trackBurnedNFTs() {
  try {
    // Replace "Your_Wallet_Public_Key" with the wallet address of the Magic Box event organizer or participant
    const walletAddress = new PublicKey("Your_Wallet_Public_Key");

    console.log("Fetching NFTs for wallet:", walletAddress.toBase58());
    const nfts = await fetchNFTs(walletAddress);

    if (nfts.length === 0) {
      console.log("No NFTs found for the wallet.");
      return;
    }

    console.log(`Found ${nfts.length} NFTs. Checking burn status...`);

    const validNFTs = [];
    const burnedNFTs = [];

    for (let nft of nfts) {
      if (isBurnedDuringEvent(nft)) {
        console.log(`NFT ${nft.data.name} burned during the event. Excluding from utility.`);
        burnedNFTs.push(nft);
      } else {
        validNFTs.push(nft);
      }
    }

    console.log(`Burned NFTs: ${burnedNFTs.length}`);
    console.log(`Valid NFTs (eligible for utility): ${validNFTs.length}`);
  } catch (error) {
    console.error("Error tracking burned NFTs:", error.message);
  }
}

// Run the main function
trackBurnedNFTs();
```
