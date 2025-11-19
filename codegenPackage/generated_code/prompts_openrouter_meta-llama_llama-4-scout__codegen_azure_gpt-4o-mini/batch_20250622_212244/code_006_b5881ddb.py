"""
Generated Code Metadata:
========================
Original URL: https://nft-rewards.online
Prompt: "Create a simple NFT rewards contract using OpenZeppelin."
Generated: DETERMINISTIC_b5881ddb01e756d9
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTRewards contract that inherits from ERC721Enumerable and Ownable
contract NFTRewards is ERC721Enumerable, Ownable {
    // Mapping from token ID to reward points
    mapping(uint256 => uint256) private _rewardPoints;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, uint256 rewardPoints);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT with reward points
    function mintNFT(address to, uint256 tokenId, uint256 rewardPoints) external onlyOwner {
        require(!_exists(tokenId), "Token ID already exists");
        require(to != address(0), "Cannot mint to the zero address");

        // Mint the NFT
        _mint(to, tokenId);
        
        // Assign reward points to the minted NFT
        _rewardPoints[tokenId] = rewardPoints;

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId, rewardPoints);
    }

    // Function to get reward points for a specific token ID
    function getRewardPoints(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token ID does not exist");
        return _rewardPoints[tokenId];
    }

    // Function to update reward points for a specific token ID
    function updateRewardPoints(uint256 tokenId, uint256 newRewardPoints) external onlyOwner {
        require(_exists(tokenId), "Token ID does not exist");
        _rewardPoints[tokenId] = newRewardPoints;
    }

    // Function to burn an NFT and its associated reward points
    function burnNFT(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Token ID does not exist");

        // Clear reward points before burning
        delete _rewardPoints[tokenId];

        // Burn the NFT
        _burn(tokenId);
    }
}
```
