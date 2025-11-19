"""
Generated Code Metadata:
========================
Original URL: https://snapshot-ethosmobileorg.pages.dev
Prompt: Generate a script using Web3.js or ethers.js to burn an NFT and trigger a redemption process for a product, similar to the ethOS phone redemption described on the site.
Generated: DETERMINISTIC_6f646f3c61e808f2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const { ethers } = require("ethers");
require("dotenv").config();

// Contract ABI for the NFT and Redemption contracts
const NFT_ABI = [
  "function burn(uint256 tokenId) public",
  "function ownerOf(uint256 tokenId) public view returns (address)",
];
const REDEMPTION_ABI = [
  "function redeem(uint256 tokenId, string memory productCode) public",
];

async function burnAndRedeem() {
  try {
    // Initialize provider and signer
    const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
    const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

    // Initialize contracts
    const nftContract = new ethers.Contract(
      process.env.NFT_CONTRACT_ADDRESS,
      NFT_ABI,
      wallet
    );
    const redemptionContract = new ethers.Contract(
      process.env.REDEMPTION_CONTRACT_ADDRESS,
      REDEMPTION_ABI,
      wallet
    );

    // Token ID and product code to redeem
    const tokenId = 123; // Replace with actual token ID
    const productCode = "PHONE-001"; // Replace with actual product code

    // Verify ownership before burning
    const owner = await nftContract.ownerOf(tokenId);
    if (owner.toLowerCase() !== wallet.address.toLowerCase()) {
      throw new Error("Caller is not the owner of this NFT");
    }

    // Burn the NFT
    console.log(`Burning NFT with token ID: ${tokenId}`);
    const burnTx = await nftContract.burn(tokenId);
    await burnTx.wait();
    console.log(`NFT burned successfully. Tx hash: ${burnTx.hash}`);

    // Trigger redemption
    console.log(`Initiating redemption for product: ${productCode}`);
    const redeemTx = await redemptionContract.redeem(tokenId, productCode);
    await redeemTx.wait();
    console.log(`Redemption successful. Tx hash: ${redeemTx.hash}`);

    return {
      burnTxHash: burnTx.hash,
      redeemTxHash: redeemTx.hash,
    };
  } catch (error) {
    console.error("Error in burnAndRedeem:", error.message);
    throw error;
  }
}

// Execute the function
burnAndRedeem()
  .then((result) => console.log("Process completed:", result))
  .catch((error) => console.error("Process failed:", error));
```
