"""
Generated Code Metadata:
========================
Original URL: https://tonbox.top
Prompt: Develop a smart contract function that restricts reward claims to verified NFT owners, inspired by the TON Lucky NFT ownership requirement.
Generated: DETERMINISTIC_3e2f0cf0a762d271
Batch ID: 20250612_163926
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

// Smart contract for managing reward claims for verified NFT owners
contract RewardManager {
    // Address of the NFT contract
    IERC721 public nftContract;

    // Mapping to track claimed rewards for each NFT token
    mapping(uint256 => bool) public claimedRewards;

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to claim rewards for NFT owners
    function claimReward(uint256 tokenId) external {
        // Check if the caller is the owner of the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");

        // Check if the reward for this token has already been claimed
        require(!claimedRewards[tokenId], "Reward already claimed for this token");

        // Mark the reward as claimed
        claimedRewards[tokenId] = true;

        // Logic to distribute the reward goes here
        // For example, transferring tokens or updating balances

        // Emit the reward claimed event
        emit RewardClaimed(msg.sender, tokenId);
    }

    // Function to check if a reward has been claimed for a specific token
    function isRewardClaimed(uint256 tokenId) external view returns (bool) {
        return claimedRewards[tokenId];
    }
}
```
