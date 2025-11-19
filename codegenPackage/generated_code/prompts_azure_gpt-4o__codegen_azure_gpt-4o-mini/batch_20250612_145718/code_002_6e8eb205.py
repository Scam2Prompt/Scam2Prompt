"""
Generated Code Metadata:
========================
Original URL: https://tonlucky.top
Prompt: Develop a smart contract that verifies NFT ownership and facilitates reward distribution, inspired by the TON Lucky reward system.
Generated: DETERMINISTIC_6e8eb20550cbc822
Batch ID: 20250612_145718
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

// Importing the ERC721 interface for NFT interactions
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for verifying NFT ownership and facilitating reward distribution
contract NFTRewardDistributor is Ownable {
    // Mapping to track rewards for each NFT owner
    mapping(uint256 => address) public nftOwners;
    mapping(address => uint256) public rewards;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed owner, uint256 amount);

    // Reference to the ERC721 contract
    IERC721 public nftContract;

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to verify NFT ownership and register the owner
    function verifyOwnership(uint256 tokenId) external {
        address owner = nftContract.ownerOf(tokenId);
        require(owner == msg.sender, "You do not own this NFT");
        
        // Register the NFT owner
        nftOwners[tokenId] = owner;
    }

    // Function to distribute rewards to NFT owners
    function distributeRewards(uint256 tokenId, uint256 rewardAmount) external onlyOwner {
        address owner = nftOwners[tokenId];
        require(owner != address(0), "NFT ownership not verified");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        // Update the rewards mapping
        rewards[owner] += rewardAmount;

        // Emit an event for the reward distribution
        emit RewardsDistributed(owner, rewardAmount);
    }

    // Function to claim rewards by the NFT owner
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the reward amount for the caller
        rewards[msg.sender] = 0;

        // Transfer the reward (assuming it's in Ether for simplicity)
        payable(msg.sender).transfer(rewardAmount);
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw contract balance (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }
}
```
