"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-minting-app-main.pages.dev
Prompt: Write JavaScript code to create a simple NFT minting application similar to the functionality described on the ALPACADABRAZ NFT website. Ensure the app requires JavaScript to run properly.
Generated: DETERMINISTIC_075480c01535654a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simple NFT Minting Application
 * This application simulates minting NFTs using JavaScript.
 * 
 * Features:
 * - Mint a new NFT with a unique ID and metadata.
 * - Display the minted NFTs.
 * - Basic error handling.
 */

// NFT Collection - This will store all the minted NFTs
const nftCollection = [];

/**
 * Function to mint a new NFT
 * @param {string} name - The name of the NFT
 * @param {string} description - A brief description of the NFT
 * @returns {object} - The minted NFT object
 */
function mintNFT(name, description) {
  try {
    // Validate inputs
    if (!name || !description) {
      throw new Error('Name and description are required to mint an NFT.');
    }

    // Create a unique ID for the NFT
    const id = nftCollection.length + 1;

    // Create the NFT object
    const nft = {
      id: id, // Unique identifier
      name: name, // Name of the NFT
      description: description, // Description of the NFT
      mintedAt: new Date(), // Timestamp of when the NFT was minted
    };

    // Add the NFT to the collection
    nftCollection.push(nft);

    console.log(`Successfully minted NFT: ${name}`);
    return nft;
  } catch (error) {
    console.error(`Error minting NFT: ${error.message}`);
    return null; // Return null if an error occurs
  }
}

/**
 * Function to display all minted NFTs
 */
function displayNFTs() {
  if (nftCollection.length === 0) {
    console.log('No NFTs have been minted yet.');
    return;
  }

  console.log('Minted NFTs:');
  nftCollection.forEach((nft) => {
    console.log(`ID: ${nft.id}, Name: ${nft.name}, Description: ${nft.description}, Minted At: ${nft.mintedAt}`);
  });
}

// Example Usage
const nft1 = mintNFT('CryptoDog', 'A rare NFT featuring a pixelated dog.');
const nft2 = mintNFT('MoonCat', 'An NFT of a cat on the moon.');
displayNFTs();
```
