"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbox.top
Prompt: Develop a smart contract function that restricts reward claims to verified NFT owners, inspired by the TON Lucky NFT ownership requirement.
Generated: DETERMINISTIC_3e2f0cf0a762d271
Batch ID: 20250612_163926
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

// Interface for the NFT contract to check ownership
interface INFT {
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Smart contract for managing reward claims for verified NFT owners
contract RewardManager {
    // Address of the NFT contract
    INFT public nftContract;
    
    // Mapping to keep track of claimed rewards
    mapping(address => mapping(uint256 => bool)) public claimedRewards;

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = INFT(_nftContract);
    }

    // Function to claim reward for NFT owner, restricted to verified owners
    function claimReward(uint256 tokenId) external {
        // Verify that the msg.sender is the owner of the specified NFT
        address owner = nftContract.ownerOf(tokenId);
        require(msg.sender == owner, "Caller is not the NFT owner");

        // Check if the reward has already been claimed
        require(!claimedRewards[owner][tokenId], "Reward already claimed");

        // Mark the reward as claimed
        claimedRewards[owner][tokenId] = true;

        // Logic to transfer reward to the owner can be added here
        // For example: transferReward(owner);

        // Emit the RewardClaimed event
        emit RewardClaimed(owner, tokenId);
    }

    // Optional: Function to check if a reward has been claimed
    function isRewardClaimed(address owner, uint256 tokenId) external view returns (bool) {
        return claimedRewards[owner][tokenId];
    }
}
```
