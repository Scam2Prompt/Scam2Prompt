"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Write code to mint an NFT on the Solana blockchain using the `$BLD` token as part of the Buildoors ecosystem described on the Solana NFT Minter Delta platform.
Generated: DETERMINISTIC_5638ae917b5ce67b
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, clusterApiUrl, Keypair, Transaction } = require('@solana/web3.js');
const { NFTStorage, File } = require('nft.storage');
const fs = require('fs');

// Set up constants
const SOLANA_RPC_URL = clusterApiUrl('devnet');
const BUILD_OORS_CONTRACT_ADDRESS = 'your_build_oors_contract_address';
const BLD_TOKEN_ADDRESS = 'your_bld_token_address';
const NFT_STORAGE_API_KEY = 'your_nft_storage_api_key';

// Set up the Solana connection
const connection = new Connection(SOLANA_RPC_URL);

/**
 * Mint an NFT on the Solana blockchain using the $BLD token.
 * 
 * @param {string} name - The name of the NFT.
 * @param {string} description - The description of the NFT.
 * @param {string} imagePath - The path to the NFT image.
 * @param {string} ownerPublicKey - The public key of the NFT owner.
 * @returns {Promise<string>} The address of the minted NFT.
 */
async function mintNft(name, description, imagePath, ownerPublicKey) {
  try {
    // Create a new NFT storage client
    const nftStorageClient = new NFTStorage({ token: NFT_STORAGE_API_KEY });

    // Read the image file
    const imageFile = new File([fs.readFileSync(imagePath)], imagePath.split('/').pop(), { type: 'image/png' });

    // Upload the NFT metadata to IPFS
    const metadata = await nftStorageClient.store({
      name,
      description,
      image: imageFile,
    });

    // Create a new transaction
    const transaction = new Transaction();

    // Create a new Buildoors contract instance
    const buildoorsContract = await BuildoorsContract(connection, BUILD_OORS_CONTRACT_ADDRESS);

    // Mint the NFT
    const mintInstruction = await buildoorsContract.mintNft({
      metadataUri: metadata.uri,
      owner: ownerPublicKey,
      token: BLD_TOKEN_ADDRESS,
    });

    // Add the mint instruction to the transaction
    transaction.add(mintInstruction);

    // Sign the transaction
    const payer = Keypair.generate();
    transaction.sign(payer);

    // Send the transaction
    const txid = await connection.sendTransaction(transaction, [payer]);

    // Return the address of the minted NFT
    return txid;
  } catch (error) {
    console.error(error);
    throw error;
  }
}

// Helper function to create a new Buildoors contract instance
async function BuildoorsContract(connection, contractAddress) {
  // Assuming a BuildoorsContract class exists
  // Replace with actual implementation
  // For demonstration purposes, return a mock contract instance
  return {
    mintNft: async ({ metadataUri, owner, token }) => {
      // Replace with actual implementation
      return {};
    },
  };
}

// Example usage
async function main() {
  const ownerPublicKey = 'your_owner_public_key';
  const nftName = 'Example NFT';
  const nftDescription = 'This is an example NFT';
  const imagePath = './path/to/image.png';

  try {
    const nftAddress = await mintNft(nftName, nftDescription, imagePath, ownerPublicKey);
    console.log(`NFT minted at address: ${nftAddress}`);
  } catch (error) {
    console.error(error);
  }
}

main();
```
