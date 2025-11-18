"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Write a function in JavaScript to calculate and display financial literacy metrics based on NFT ownership and streaming revenue.
Generated: DETERMINISTIC_bceef7f1b708966e
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate and display financial literacy metrics based on NFT ownership and streaming revenue.
 * @param {Array<Object>} nftData - Array of NFT ownership data. Each object should include 'value' (number) and 'royalties' (number).
 * @param {Array<Object>} streamingData - Array of streaming revenue data. Each object should include 'platform' (string) and 'revenue' (number).
 * @returns {void}
 */
function calculateFinancialMetrics(nftData, streamingData) {
  try {
    // Validate input types
    if (!Array.isArray(nftData) || !Array.isArray(streamingData)) {
      throw new Error("Invalid input: Both nftData and streamingData should be arrays.");
    }
    
    // Calculate total NFT value and royalties
    const totalNFTValue = nftData.reduce((total, nft) => {
      if (typeof nft.value !== 'number' || typeof nft.royalties !== 'number') {
        throw new Error("Invalid NFT data: Each NFT object must include numeric 'value' and 'royalties' properties.");
      }
      return total + nft.value;
    }, 0);

    const totalNFTRoyalties = nftData.reduce((total, nft) => total + nft.royalties, 0);
    
    // Calculate total streaming revenue
    const totalStreamingRevenue = streamingData.reduce((total, stream) => {
      if (typeof stream.revenue !== 'number' || typeof stream.platform !== 'string') {
        throw new Error("Invalid streaming data: Each streaming object must include a numeric 'revenue' and a string 'platform' property.");
      }
      return total + stream.revenue;
    }, 0);

    // Display financial literacy metrics
    console.log("Financial Literacy Metrics:");
    console.log(`Total NFT Value: $${totalNFTValue.toFixed(2)}`);
    console.log(`Total NFT Royalties: $${totalNFTRoyalties.toFixed(2)}`);
    console.log(`Total Streaming Revenue: $${totalStreamingRevenue.toFixed(2)}`);

    // Optional: Calculate percentages (e.g., NFT vs streaming revenue)
    const totalRevenue = totalNFTValue + totalStreamingRevenue;
    const nftPercentage = ((totalNFTValue / totalRevenue) * 100).toFixed(2);
    const streamingPercentage = ((totalStreamingRevenue / totalRevenue) * 100).toFixed(2);

    console.log(`Percentage of Revenue from NFTs: ${nftPercentage}%`);
    console.log(`Percentage of Revenue from Streaming: ${streamingPercentage}%`);
  } catch (error) {
    // Handle errors gracefully
    console.error("Error calculating financial metrics:", error.message);
  }
}

// Example usage:
const nftData = [
  { value: 2500, royalties: 150 },
  { value: 4200, royalties: 300 },
];

const streamingData = [
  { platform: "Spotify", revenue: 500 },
  { platform: "Apple Music", revenue: 800 },
];

calculateFinancialMetrics(nftData, streamingData);
```
