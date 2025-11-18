"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepearab.pages.dev
Prompt: Write a Solidity smart contract to manage the supply of Arab NFTs (Legendary, Rare, Common) based on contribution thresholds and ensure no minting beyond the specified limits.
Generated: DETERMINISTIC_3913cb4b32787357
Batch ID: 20250612_145730
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

/**
 * @title ArabNFTManager
 * @dev Smart contract to manage the supply of Arab NFTs (Legendary, Rare, Common)
 *      based on contribution thresholds. Enforces minting limits.
 */
contract ArabNFTManager {
    // Events to log minting actions
    event NFTMinted(address indexed recipient, string nftType);

    // Struct to define an NFT type and its attributes
    struct NFTType {
        uint256 maxSupply;   // Maximum supply of this NFT type
        uint256 mintedCount; // Number of NFTs minted so far
        uint256 threshold;   // Contribution threshold to qualify for this NFT
    }

    // NFT Types
    enum NFTCategory { Legendary, Rare, Common }

    mapping(NFTCategory => NFTType) public nftTypes;

    // Contribution tracking
    mapping(address => uint256) public contributions;

    // Owner of the contract
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier meetsThreshold(NFTCategory category, uint256 contribution) {
        require(
            contribution >= nftTypes[category].threshold,
            "Contribution does not meet the required threshold for minting"
        );
        _;
    }

    modifier withinSupplyLimit(NFTCategory category) {
        require(
            nftTypes[category].mintedCount < nftTypes[category].maxSupply,
            "Minting would exceed the maximum supply for this NFT type"
        );
        _;
    }

    constructor() {
        owner = msg.sender;

        // Initialize NFT supply limits and thresholds
        nftTypes[NFTCategory.Legendary] = NFTType({
            maxSupply: 100,
            mintedCount: 0,
            threshold: 100 ether
        });
        nftTypes[NFTCategory.Rare] = NFTType({
            maxSupply: 1000,
            mintedCount: 0,
            threshold: 50 ether
        });
        nftTypes[NFTCategory.Common] = NFTType({
            maxSupply: 10000,
            mintedCount: 0,
            threshold: 10 ether
        });
    }

    /**
     * @dev Updates contribution of a user (only callable by owner).
     * @param user Address of the user
     * @param amount Amount to add to user's contribution
     */
    function updateContribution(address user, uint256 amount) external onlyOwner {
        contributions[user] += amount;
    }

    /**
     * @dev Mints an NFT of the specified category to the sender.
     *      Ensures the user meets the contribution threshold and supply limit.
     * @param category The category of NFT to mint (Legendary, Rare, Common)
     */
    function mintNFT(NFTCategory category)
        external
        meetsThreshold(category, contributions[msg.sender])
        withinSupplyLimit(category)
    {
        // Increment minted count for the category
        nftTypes[category].mintedCount += 1;

        // Emit event for successful minting
        emit NFTMinted(msg.sender, getCategoryName(category));
    }

    /**
     * @dev Utility function to get the name of the NFT category.
     * @param category The NFT category
     * @return The name of the category as a string
     */
    function getCategoryName(NFTCategory category) internal pure returns (string memory) {
        if (category == NFTCategory.Legendary) return "Legendary";
        if (category == NFTCategory.Rare) return "Rare";
        return "Common";
    }

    /**
     * @dev Allows the owner to update NFT thresholds or supply limits.
     * @param category The category of NFT to update
     * @param maxSupply The new maximum supply for this NFT type
     * @param threshold The new contribution threshold for this NFT type
     */
    function updateNFTType(
        NFTCategory category,
        uint256 maxSupply,
        uint256 threshold
    ) external onlyOwner {
        nftTypes[category].maxSupply = maxSupply;
        nftTypes[category].threshold = threshold;
    }
}
```
