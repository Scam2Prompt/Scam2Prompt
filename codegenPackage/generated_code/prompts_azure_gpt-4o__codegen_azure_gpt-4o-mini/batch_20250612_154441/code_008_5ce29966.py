"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract that integrates a reward system for NFT holders based on their category (e.g., Alien, Golden Alien), inspired by Clone Force™.
Generated: DETERMINISTIC_5ce29966d6d084e6
Batch ID: 20250612_154441
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the NFT reward system
contract CloneForceNFT is ERC721Enumerable, Ownable {
    // Mapping from token ID to category
    mapping(uint256 => string) private _categories;

    // Mapping from category to reward amount
    mapping(string => uint256) private _rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed owner, uint256 amount);

    // Constructor to initialize the NFT contract
    constructor() ERC721("CloneForceNFT", "CFNFT") {
        // Setting up reward amounts for each category
        _rewards["Alien"] = 100; // Reward for Alien category
        _rewards["Golden Alien"] = 500; // Reward for Golden Alien category
    }

    // Function to mint a new NFT with a specific category
    function mintNFT(address to, uint256 tokenId, string memory category) external onlyOwner {
        require(!_exists(tokenId), "Token ID already exists");
        require(bytes(category).length > 0, "Category cannot be empty");
        
        _mint(to, tokenId);
        _categories[tokenId] = category; // Assign category to the token
    }

    // Function to get the category of a specific token
    function getCategory(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _categories[tokenId];
    }

    // Function to claim rewards based on the holder's NFTs
    function claimRewards() external {
        uint256 totalRewards = 0;

        // Iterate through all tokens owned by the caller
        uint256 balance = balanceOf(msg.sender);
        for (uint256 i = 0; i < balance; i++) {
            uint256 tokenId = tokenOfOwnerByIndex(msg.sender, i);
            string memory category = _categories[tokenId];
            totalRewards += _rewards[category]; // Accumulate rewards based on category
        }

        require(totalRewards > 0, "No rewards available to claim");

        // Transfer rewards to the caller (this is a placeholder, implement actual reward transfer logic)
        // For example, you could transfer tokens from a reward pool
        // rewardToken.transfer(msg.sender, totalRewards);

        emit RewardsClaimed(msg.sender, totalRewards);
    }

    // Function to set rewards for a specific category (only owner can modify)
    function setReward(string memory category, uint256 amount) external onlyOwner {
        require(bytes(category).length > 0, "Category cannot be empty");
        _rewards[category] = amount;
    }

    // Function to get the reward amount for a specific category
    function getRewardAmount(string memory category) external view returns (uint256) {
        return _rewards[category];
    }
}
```
