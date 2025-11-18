"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterart.rpmltech.com
Prompt: Write a function in JavaScript that filters NFTs by type (visual, audio, video) and sorts them by price, as seen in the gallery sections of enter.art.
Generated: DETERMINISTIC_dee553cca0f61132
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
 * Filters and sorts NFTs by type and price.
 * @param {Array} nfts - Array of NFT objects, where each object contains the following properties:
 *                       - type: A string representing the type of the NFT (e.g., 'visual', 'audio', 'video').
 *                       - price: A number representing the price of the NFT.
 * @param {string} filterType - The type of NFT to filter by ('visual', 'audio', 'video').
 * @returns {Array} - Array of filtered and sorted NFT objects.
 */
function filterAndSortNFTs(nfts, filterType) {
  // Validate input parameters
  if (!Array.isArray(nfts)) {
    throw new Error("The 'nfts' parameter must be an array.");
  }
  if (typeof filterType !== "string") {
    throw new Error("The 'filterType' parameter must be a string.");
  }

  // Filter NFTs by type
  const filteredNFTs = nfts.filter((nft) => {
    return nft.type === filterType;
  });

  // Sort the filtered NFTs by price (ascending order)
  const sortedNFTs = filteredNFTs.sort((a, b) => {
    if (typeof a.price !== 'number' || typeof b.price !== 'number') {
      throw new Error("NFT price must be a number.");
    }
    return a.price - b.price;
  });

  return sortedNFTs;
}

// Example usage:
const nftsGallery = [
  { type: "visual", price: 100 },
  { type: "audio", price: 50 },
  { type: "visual", price: 200 },
  { type: "video", price: 150 },
];

try {
  const result = filterAndSortNFTs(nftsGallery, "visual");
  console.log(result); // Output: [{ type: 'visual', price: 100 }, { type: 'visual', price: 200 }]
} catch (error) {
  console.error(error.message);
}
```
