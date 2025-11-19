"""
Generated Code Metadata:
========================
Original URL: https://www.chibiheadnft.com
Prompt: Write code to create a "sold-out" indicator for NFTs in a collection, referencing the functionality described for "Chibi Head NFT."
Generated: DETERMINISTIC_43367c4386e7c558
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// soldOutIndicator.js

/**
 * Represents a collection of NFTs with a "sold-out" indicator.
 */
class NFTCollection {
  /**
   * Initializes an NFT collection.
   * @param {Object[]} nfts - Array of NFT objects.
   * @param {string} nfts[].id - Unique identifier for the NFT.
   * @param {string} nfts[].name - Name of the NFT.
   * @param {boolean} nfts[].isSoldOut - Sold-out status of the NFT.
   */
  constructor(nfts) {
    this.nfts = nfts;
  }

  /**
   * Checks if an NFT is sold out.
   * @param {string} id - ID of the NFT to check.
   * @returns {boolean} True if the NFT is sold out, false otherwise.
   */
  isNFTSoldOut(id) {
    const nft = this.nfts.find((n) => n.id === id);
    if (!nft) {
      throw new Error(`NFT with ID ${id} not found in collection.`);
    }
    return nft.isSoldOut;
  }

  /**
   * Updates the sold-out status of an NFT.
   * @param {string} id - ID of the NFT to update.
   * @param {boolean} isSoldOut - New sold-out status.
   */
  updateNFTStatus(id, isSoldOut) {
    const nftIndex = this.nfts.findIndex((n) => n.id === id);
    if (nftIndex === -1) {
      throw new Error(`NFT with ID ${id} not found in collection.`);
    }
    this.nfts[nftIndex].isSoldOut = isSoldOut;
  }

  /**
   * Gets the sold-out status of all NFTs in the collection.
   * @returns {Object[]} Array of objects with NFT ID and sold-out status.
   */
  getSoldOutStatus() {
    return this.nfts.map((nft) => ({ id: nft.id, isSoldOut: nft.isSoldOut }));
  }
}

// Example usage:
function main() {
  try {
    const nfts = [
      { id: 'nft-1', name: 'Chibi Head 1', isSoldOut: false },
      { id: 'nft-2', name: 'Chibi Head 2', isSoldOut: true },
      { id: 'nft-3', name: 'Chibi Head 3', isSoldOut: false },
    ];

    const collection = new NFTCollection(nfts);

    console.log('Initial Sold-out Status:');
    console.log(collection.getSoldOutStatus());

    console.log(`Is NFT with ID 'nft-2' sold out? ${collection.isNFTSoldOut('nft-2')}`);

    collection.updateNFTStatus('nft-1', true);

    console.log('Updated Sold-out Status:');
    console.log(collection.getSoldOutStatus());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
