"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Write a function to optimize the cost of minting 10,000 NFTs using Truffle's cost optimization tools.
Generated: DETERMINISTIC_6cfec46ab64868ac
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFTMintOptimizer
 * @dev Optimizes the cost of minting 10,000 NFTs using batch minting
 */
contract NFTMintOptimizer {
    uint256 public constant TOTAL_NFTS = 10000; // Total number of NFTs to mint
    uint256 public constant BATCH_SIZE = 100;  // Batch size for minting
    uint256 public mintedCount;               // Track total NFTs minted

    mapping(uint256 => address) public owners; // Mapping of token IDs to their owners

    /**
     * @dev Mints NFTs in batches to optimize cost.
     * @param _owner Address of the NFT owner.
     */
    function mintBatch(address _owner) external {
        require(_owner != address(0), "Invalid owner address");
        require(mintedCount < TOTAL_NFTS, "All NFTs already minted");
        
        // Determine the number of NFTs to mint in this batch
        uint256 remainingNFTs = TOTAL_NFTS - mintedCount;
        uint256 batchMintCount = remainingNFTs > BATCH_SIZE ? BATCH_SIZE : remainingNFTs;

        // Mint batch
        for (uint256 i = 0; i < batchMintCount; i++) {
            uint256 tokenId = mintedCount + i; // Calculate token ID
            owners[tokenId] = _owner;         // Assign ownership
        }

        mintedCount += batchMintCount; // Update minted count
    }

    /**
     * @dev Gets the owner of a specific NFT.
     * @param _tokenId The ID of the NFT.
     * @return The address of the owner.
     */
    function getOwner(uint256 _tokenId) external view returns (address) {
        require(_tokenId < TOTAL_NFTS, "Invalid token ID");
        return owners[_tokenId];
    }
}
```
