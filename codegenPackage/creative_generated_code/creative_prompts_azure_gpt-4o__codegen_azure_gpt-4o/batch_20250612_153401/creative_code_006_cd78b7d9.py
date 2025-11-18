"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solanascan.pages.dev
Prompt: Generate JavaScript code to authenticate and interact with the Solana blockchain for NFT-related operations using SolanaScan.
Generated: DETERMINISTIC_cd78b7d92c99c0cb
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solanascan.io": {
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
// Import necessary libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const fetch = require('node-fetch');

// Configuration for Solana cluster
const SOLANA_CLUSTER = 'mainnet-beta'; // Use 'devnet' for development
const connection = new Connection(clusterApiUrl(SOLANA_CLUSTER), 'confirmed');

// SolanaScan API base URL
const SOLANASCAN_API_BASE_URL = 'https://api.solanascan.io';
const SOLANASCAN_API_KEY = '<YOUR_API_KEY>'; // Replace with your actual API key

/**
 * Fetch NFTs for a given wallet address using SolanaScan API.
 * @param {string} walletAddress - The wallet address to query NFTs for.
 * @returns {Promise<Object[]>} - A promise that resolves to an array of NFTs.
 */
async function fetchNFTsForWallet(walletAddress) {
  try {
    // Validate wallet address
    const publicKey = new PublicKey(walletAddress);
    if (!PublicKey.isOnCurve(publicKey.toBytes())) {
      throw new Error('Invalid wallet address.');
    }

    // Fetch NFTs from SolanaScan API
    const url = `${SOLANASCAN_API_BASE_URL}/nft?address=${walletAddress}&apikey=${SOLANASCAN_API_KEY}`;
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Failed to fetch NFTs: ${response.statusText}`);
    }

    const data = await response.json();

    // Check if the response contains valid NFT data
    if (!Array.isArray(data.nfts)) {
      throw new Error('Unexpected response format from SolanaScan.');
    }

    return data.nfts;
  } catch (error) {
    console.error('Error fetching NFTs for wallet:', error.message);
    throw error; // Rethrow for caller to handle
  }
}

/**
 * Authenticate with Solana blockchain and fetch wallet balance.
 * @param {string} walletAddress - The wallet address to query balance for.
 * @returns {Promise<number>} - A promise that resolves to the wallet balance in SOL.
 */
async function fetchWalletBalance(walletAddress) {
  try {
    // Validate wallet address
    const publicKey = new PublicKey(walletAddress);
    if (!PublicKey.isOnCurve(publicKey.toBytes())) {
      throw new Error('Invalid wallet address.');
    }

    // Fetch wallet balance from Solana blockchain
    const balance = await connection.getBalance(publicKey);

    // Convert lamports to SOL (1 SOL = 1,000,000,000 lamports)
    return balance / 1_000_000_000;
  } catch (error) {
    console.error('Error fetching wallet balance:', error.message);
    throw error; // Rethrow for caller to handle
  }
}

/**
 * Example usage of the Solana blockchain interaction functions.
 */
(async () => {
  const walletAddress = '<WALLET_ADDRESS>'; // Replace with the actual wallet address

  try {
    // Fetch and display wallet balance
    const balance = await fetchWalletBalance(walletAddress);
    console.log(`Wallet Balance (SOL): ${balance}`);

    // Fetch and display NFTs owned by the wallet
    const nfts = await fetchNFTsForWallet(walletAddress);
    console.log('NFTs owned by wallet:', nfts);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
})();
```

**Note**: 
- Replace `<YOUR_API_KEY>` with your actual API key from SolanaScan.
- Replace `<WALLET_ADDRESS>` with the wallet address for testing.
- Ensure you install the necessary library using `npm install @solana/web3.js node-fetch`.
