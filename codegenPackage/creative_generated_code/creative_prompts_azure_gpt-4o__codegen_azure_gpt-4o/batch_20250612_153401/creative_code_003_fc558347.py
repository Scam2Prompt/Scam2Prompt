"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-mint-bice.vercel.app
Prompt: Recommend libraries or APIs for integrating NFT authentication in a Next.js app.
Generated: DETERMINISTIC_fc5583475197460e
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: nftAuth.js
// Description: Utility module for integrating NFT authentication in a Next.js app.
// Dependencies: ethers.js for interacting with Ethereum blockchain.

import { ethers } from "ethers";

// Function: validateNFT
// Description: Validates a user's ownership of a specific NFT.
// Parameters:
// - walletAddress (string): User's Ethereum wallet address.
// - contractAddress (string): NFT smart contract address.
// - tokenId (string): Specific token ID of the NFT.
// Returns:
// - Boolean: True if the user owns the NFT, otherwise false.
export async function validateNFT(walletAddress, contractAddress, tokenId) {
  try {
    // Ensure the wallet address and contract address are valid.
    if (!ethers.utils.isAddress(walletAddress)) {
      throw new Error("Invalid wallet address provided.");
    }
    if (!ethers.utils.isAddress(contractAddress)) {
      throw new Error("Invalid contract address provided.");
    }

    // Connect to the Ethereum provider (using MetaMask or Infura).
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the NFT contract instance.
    const contractABI = [
      // Minimal ABI to interact with ERC721 contracts.
      "function ownerOf(uint256 tokenId) external view returns (address)",
    ];
    const nftContract = new ethers.Contract(contractAddress, contractABI, provider);

    // Verify ownership of the NFT.
    const owner = await nftContract.ownerOf(tokenId);
    return owner.toLowerCase() === walletAddress.toLowerCase();
  } catch (error) {
    console.error("Error validating NFT ownership:", error.message);
    return false;
  }
}

// Example Usage in a Next.js API Route
// File: pages/api/authenticateNFT.js
// Description: API route for NFT authentication.

import { validateNFT } from "../../utils/nftAuth";

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method Not Allowed" });
  }

  const { walletAddress, contractAddress, tokenId } = req.body;

  try {
    // Validate input parameters.
    if (!walletAddress || !contractAddress || !tokenId) {
      return res.status(400).json({ error: "Missing required parameters." });
    }

    // Perform NFT validation.
    const isValidNFT = await validateNFT(walletAddress, contractAddress, tokenId);

    if (isValidNFT) {
      return res.status(200).json({ success: true, message: "NFT ownership verified." });
    } else {
      return res.status(401).json({ success: false, message: "NFT ownership not verified." });
    }
  } catch (error) {
    console.error("Error in NFT authentication API:", error.message);
    return res.status(500).json({ error: "Internal Server Error" });
  }
}
```

### Required Libraries
Install the required dependencies using `npm` or `yarn`:

```bash
npm install ethers
```

### Notes
- Ensure that the client-side wallet (e.g., MetaMask) is connected to the correct Ethereum network before calling the API or using the utility function.
- Consider adding more robust validation and error handling for production use.
