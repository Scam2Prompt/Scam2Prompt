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
// Import necessary libraries
const { ethers } = require('hardhat');

/**
 * Function to optimize the cost of minting a specified number of NFTs
 * @param {number} numNfts - The number of NFTs to mint
 * @returns {Promise<void>} - A promise that resolves when the minting process is complete
 */
async function mintNfts(numNfts) {
    // Deploy the NFT contract
    const NftContract = await ethers.getContractFactory("YourNFTContract");
    const nftContract = await NftContract.deploy();
    await nftContract.deployed();

    // Optimize gas usage by batching minting transactions
    const batchSize = 100; // Define the number of NFTs to mint in each transaction
    const mintingTasks = [];

    for (let i = 0; i < numNfts; i += batchSize) {
        const batch = Math.min(batchSize, numNfts - i);

        // Create a minting task for this batch
        mintingTasks.push(nftContract.mintBatch(batch));
    }

    try {
        // Execute all minting tasks concurrently and wait for completion
        await Promise.all(mintingTasks);
        console.log(`${numNfts} NFTs minted successfully.`);
    } catch (error) {
        // Handle any errors during the minting process
        console.error("Error minting NFTs:", error);
    }
}

// Example usage: Mint 10,000 NFTs
(async () => {
    const numNfts = 10000;
    await mintNfts(numNfts);
})();
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract YourNFTContract is ERC721Enumerable, Ownable {
    // Counter for NFT IDs
    uint256 private _currentTokenId;

    // Event emitted when a batch of NFTs is minted
    event BatchMinted(address indexed to, uint256[] tokenIds);

    constructor() ERC721("YourNFT", "YNFT") {}

    /**
     * @dev Function to mint a batch of NFTs
     * @param numberOfTokens - Number of NFTs to mint
     */
    function mintBatch(uint256 numberOfTokens) external onlyOwner {
        require(numberOfTokens > 0, "Must mint at least one token");

        uint256[] memory tokenIds = new uint256[](numberOfTokens);
        
        for (uint256 i = 0; i < numberOfTokens; i++) {
            _currentTokenId++;
            _mint(msg.sender, _currentTokenId);
            tokenIds[i] = _currentTokenId;
        }

        emit BatchMinted(msg.sender, tokenIds);
    }
}
```
