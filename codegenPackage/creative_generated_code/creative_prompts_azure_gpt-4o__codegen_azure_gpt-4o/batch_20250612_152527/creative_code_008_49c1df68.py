"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yooshi-io.pages.dev
Prompt: Write a Solidity contract for an NFT farming system inspired by YooShi's model, where transaction fees are injected into the farming pool and profits are distributed based on NFT rarity.
Generated: DETERMINISTIC_49c1df6820bafe52
Batch ID: 20250612_152527
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTFarming is Ownable {
    // Struct to represent NFT rarity and allocation points
    struct NFTRarity {
        uint256 allocationPoints; // Allocation points for the rarity
        bool exists;              // Whether this rarity exists
    }

    // Token used for rewards distribution (e.g., ERC20 reward token)
    IERC20 public rewardToken;

    // NFT contract address (e.g., ERC721 token)
    IERC721 public nftContract;

    // Mapping to store rarity information for each NFT ID
    mapping(uint256 => uint256) public nftRarity;

    // Mapping to store allocation points per rarity
    mapping(uint256 => NFTRarity) public rarityInfo;

    // Total allocation points across all staked NFTs
    uint256 public totalAllocationPoints;

    // Mapping to store staked balances for each user
    mapping(address => uint256) public userAllocationPoints;

    // Mapping to store pending rewards for users
    mapping(address => uint256) public pendingRewards;

    // Event declarations
    event RarityUpdated(uint256 indexed rarity, uint256 allocationPoints);
    event NFTStaked(address indexed user, uint256 indexed tokenId, uint256 rarity);
    event NFTWithdrawn(address indexed user, uint256 indexed tokenId, uint256 rarity);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC721 _nftContract, IERC20 _rewardToken) {
        nftContract = _nftContract;
        rewardToken = _rewardToken;
    }

    // Owner function to set rarity and allocation points
    function setRarity(uint256 rarity, uint256 allocationPoints) external onlyOwner {
        rarityInfo[rarity].allocationPoints = allocationPoints;
        rarityInfo[rarity].exists = true;
        emit RarityUpdated(rarity, allocationPoints);
    }

    // Function to stake NFTs into the farming pool
    function stakeNFT(uint256 tokenId, uint256 rarity) external {
        require(rarityInfo[rarity].exists, "Invalid rarity");
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Transfer NFT to contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Update mappings
        nftRarity[tokenId] = rarity;
        totalAllocationPoints += rarityInfo[rarity].allocationPoints;
        userAllocationPoints[msg.sender] += rarityInfo[rarity].allocationPoints;

        emit NFTStaked(msg.sender, tokenId, rarity);
    }

    // Function to withdraw NFTs from the farming pool
    function withdrawNFT(uint256 tokenId) external {
        uint256 rarity = nftRarity[tokenId];
        require(nftContract.ownerOf(tokenId) == address(this), "NFT not staked");
        require(rarityInfo[rarity].exists, "Invalid rarity");

        // Transfer NFT back to user
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Update mappings
        totalAllocationPoints -= rarityInfo[rarity].allocationPoints;
        userAllocationPoints[msg.sender] -= rarityInfo[rarity].allocationPoints;
        delete nftRarity[tokenId];

        emit NFTWithdrawn(msg.sender, tokenId, rarity);
    }

    // Function to distribute rewards based on user allocation points
    function distributeRewards() external onlyOwner {
        uint256 totalRewardAmount = rewardToken.balanceOf(address(this));
        require(totalRewardAmount > 0, "No rewards to distribute");

        for (uint256 i = 0; i < totalRewardAmount; i++) {
            address user = msg.sender;

            uint allocation
