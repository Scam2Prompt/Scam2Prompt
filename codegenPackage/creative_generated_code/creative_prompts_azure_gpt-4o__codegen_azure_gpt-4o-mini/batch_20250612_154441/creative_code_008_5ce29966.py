"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract that integrates a reward system for NFT holders based on their category (e.g., Alien, Golden Alien), inspired by Clone Force™.
Generated: DETERMINISTIC_5ce29966d6d084e6
Batch ID: 20250612_154441
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

// Importing OpenZeppelin's ERC721 and Ownable contracts for NFT functionality and ownership management
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the NFT reward system
contract CloneForceNFT is ERC721Enumerable, Ownable {
    // Enum defining the NFT categories
    enum Category { Alien, GoldenAlien }

    // Mapping to store the category of each NFT
    mapping(uint256 => Category) private _categories;

    // Mapping to store rewards for each category
    mapping(Category => uint256) public rewards;

    // Event emitted when rewards are updated
    event RewardsUpdated(Category category, uint256 amount);

    // Constructor to initialize the NFT contract
    constructor() ERC721("CloneForceNFT", "CFNFT") {
        // Initializing reward amounts for categories
        rewards[Category.Alien] = 10 ether; // 10 ether for Alien holders
        rewards[Category.GoldenAlien] = 50 ether; // 50 ether for Golden Alien holders
    }

    // Function to mint new NFTs with a specified category
    function mintNFT(address to, uint256 tokenId, Category category) external onlyOwner {
        require(!_exists(tokenId), "Token ID already exists");
        _mint(to, tokenId);
        _categories[tokenId] = category; // Assign category to the minted NFT
    }

    // Function to get the category of a specific NFT
    function getCategory(uint256 tokenId) external view returns (Category) {
        require(_exists(tokenId), "Token does not exist");
        return _categories[tokenId];
    }

    // Function for the owner to update rewards for a specific category
    function updateRewards(Category category, uint256 amount) external onlyOwner {
        rewards[category] = amount;
        emit RewardsUpdated(category, amount);
    }

    // Function for NFT holders to claim their rewards
    function claimReward(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        Category category = _categories[tokenId];
        uint256 rewardAmount = rewards[category];

        // Transfer rewards to the NFT owner (this requires the contract to have sufficient balance)
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");
        
        // Optional: Implement logic to prevent re-entrancy
    }

    // Function to withdraw contract balance for the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept ether
    receive() external payable {}
}
```
