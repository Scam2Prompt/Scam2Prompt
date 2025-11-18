"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pikmisobakilive.com
Prompt: Create a smart contract in Solidity that handles reward distribution for a TON-based platform, including NFT qualification notifications.
Generated: DETERMINISTIC_4360383907d8a5f3
Batch ID: 20250612_153915
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
import "@openzeppelin/contracts/access/Ownable.sol";

// A contract that manages reward distribution for NFT holders on a TON-based platform
contract RewardDistributor is Ownable {
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);
    
    // Event emitted for NFT qualification notifications
    event NFTQualified(address indexed holder, uint256 tokenId);

    // Mapping to track rewards for each address
    mapping(address => uint256) private rewards;
    
    // The ERC721 NFT contract address
    IERC721 public nftContract;

    // Constructor to set the NFT contract address
    constructor(IERC721 _nftContract) {
        nftContract = _nftContract;
    }

    // Function to distribute rewards to NFT holders
    function distributeRewards(address[] memory recipients, uint256[] memory amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            rewards[recipients[i]] += amounts[i];
            emit RewardsDistributed(recipients[i], amounts[i]);
        }
    }

    // Function to claim rewards by the NFT holders
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset user's reward balance to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user (this example assumes rewards are in Ether)
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Function to notify NFT qualification based on token ownership
    function notifyNFTQualification(uint256 tokenId) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        emit NFTQualified(msg.sender, tokenId);
    }

    // Function to withdraw contract balance (onlyOwner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
