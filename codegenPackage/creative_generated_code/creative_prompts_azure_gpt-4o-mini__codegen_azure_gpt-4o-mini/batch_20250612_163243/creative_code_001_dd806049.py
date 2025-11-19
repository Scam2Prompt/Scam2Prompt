"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Write a code snippet to create a decaying NFT that burns itself over time using Meta Blocks.
Generated: DETERMINISTIC_dd806049bf647ae3
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for a decaying NFT
contract DecayingNFT is ERC721, Ownable {
    using SafeMath for uint256;

    // Structure to hold metadata for each NFT
    struct NFT {
        uint256 creationTime;
        uint256 decayDuration;
        bool isBurned;
    }

    // Mapping from token ID to NFT data
    mapping(uint256 => NFT) private _nfts;

    // Event emitted when an NFT is burned
    event NFTBurned(uint256 indexed tokenId);

    // Constructor to initialize the NFT contract with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT
    function mintNFT(address to, uint256 tokenId, uint256 decayDuration) external onlyOwner {
        require(!_exists(tokenId), "Token ID already exists");

        _mint(to, tokenId);
        _nfts[tokenId] = NFT(block.timestamp, decayDuration, false);
    }

    // Function to check if an NFT has decayed and should be burned
    function checkAndBurnNFT(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(!_nfts[tokenId].isBurned, "Token is already burned");

        // Calculate the time since creation
        uint256 timeElapsed = block.timestamp.sub(_nfts[tokenId].creationTime);

        // Check if the NFT has decayed and burn it if so
        if (timeElapsed >= _nfts[tokenId].decayDuration) {
            _burn(tokenId);
            _nfts[tokenId].isBurned = true;
            emit NFTBurned(tokenId);
        }
    }

    // Function to safely transfer an NFT with decay check
    function safeTransferNFT(address from, address to, uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        checkAndBurnNFT(tokenId); // Check for decay before transferring
        safeTransferFrom(from, to, tokenId);
    }

    // Function to retrieve NFT details
    function getNFTDetails(uint256 tokenId) external view returns (NFT memory) {
        require(_exists(tokenId), "Token does not exist");
        return _nfts[tokenId];
    }
}
```
