"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-starknet-project.vercel.app
Prompt: Create a JavaScript demo application that connects to StarkNet and fetches metadata for NFTs stored on the network.
Generated: DETERMINISTIC_4ce15668b26d6418
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { Provider } = require('starknet');
const axios = require('axios');

// Function to connect to StarkNet and fetch NFT metadata
async function fetchNFTMetadata(contractAddress, tokenId) {
  try {
    // Initialize the StarkNet provider
    const provider = new Provider({ network: 'mainnet-alpha' });

    // Fetch the token URI by calling the StarkNet contract
    const { result: tokenUriResult } = await provider.callContract({
      contractAddress: contractAddress, // The address of the NFT contract
      entrypoint: 'tokenURI',          // The method to fetch token URI
      calldata: [tokenId],             // The token ID to fetch metadata for
    });

    // Decode the token URI from the result (assuming UTF-8 encoding)
    const tokenUri = parseHexStringToUtf8(tokenUriResult[0]);

    if (!tokenUri) {
      throw new Error('Unable to decode token URI from contract response.');
    }

    console.log(`Token URI: ${tokenUri}`);

    // Fetch metadata from the token URI using HTTP GET request
    const metadataResponse = await axios.get(tokenUri);

    if (metadataResponse.status === 200) {
      console.log('NFT Metadata:', metadataResponse.data);
      return metadataResponse.data; // Return the metadata object
    } else {
      throw new Error(
        `Failed to fetch metadata. HTTP Status: ${metadataResponse.status}`
      );
    }
  } catch (error) {
    console.error('Error fetching NFT metadata:', error.message);
    throw error; // Re-throw the error for handling at a higher level
  }
}

// Helper function to parse hex strings to UTF-8 text
function parseHexStringToUtf8(hexString) {
  try {
    // Remove "0x" prefix if present
    const cleanHex = hexString.startsWith('0x')
      ? hexString.slice(2)
      : hexString;

    // Convert hex to buffer and decode UTF-8
    const buffer = Buffer.from(cleanHex, 'hex');
    return buffer.toString('utf8');
  } catch (error) {
    console.error('Error decoding hex string to UTF-8:', error.message);
    return null;
  }
}

// Sample invocation
(async function demo() {
  try {
    const contractAddress = '0x1234...abcd'; // Replace with actual contract address
    const tokenId = '1'; // Replace with actual token ID

    console.log('Fetching metadata for NFT...');
    const metadata = await fetchNFTMetadata(contractAddress, tokenId);

    console.log('Metadata successfully fetched:', metadata);
  } catch (error) {
    console.error('Demo failed:', error.message);
  }
})();
```

---

**Notes:**
- Replace `0x1234...abcd` with the actual StarkNet NFT contract address.
- Ensure `entrypoint: 'tokenURI'` matches the contract's method name for fetching token URI.
- Install dependencies via `npm install starknet axios` prior to running the code.
- Make sure the StarkNet contract supports the `tokenURI` method and adheres to expected standards.
