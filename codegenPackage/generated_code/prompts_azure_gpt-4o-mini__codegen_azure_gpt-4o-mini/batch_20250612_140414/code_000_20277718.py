"""
Generated Code Metadata:
========================
Original URL: https://arbitrum.nfts2.me
Prompt: How can I implement a referral system for an NFT minting platform using Arbitrum that allows users to earn ETH for each mint through their referral link?
Generated: DETERMINISTIC_20277718ad1836d7
Batch ID: 20250612_140414
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTMintingReferral is Ownable {
    using SafeMath for uint256;

    // ERC20 token for rewards
    IERC20 public rewardToken;

    // Mapping to track referrals
    mapping(address => address) public referrals;
    mapping(address => uint256) public referralRewards;

    // Event emitted when a mint occurs
    event Minted(address indexed user, address indexed referrer, uint256 amount);

    // Constructor to set the reward token
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    // Function to mint an NFT and handle referral rewards
    function mintNFT(address referrer) external payable {
        require(msg.value > 0, "Minting requires ETH payment");

        // Handle referral logic
        if (referrer != address(0) && referrer != msg.sender) {
            // Set the referrer if not already set
            if (referrals[msg.sender] == address(0)) {
                referrals[msg.sender] = referrer;
            }
        }

        // Mint the NFT (placeholder for actual minting logic)
        _mintNFT(msg.sender);

        // Reward the referrer
        if (referrals[msg.sender] != address(0)) {
            uint256 rewardAmount = calculateReward();
            referralRewards[referrals[msg.sender]] = referralRewards[referrals[msg.sender]].add(rewardAmount);
            emit Minted(msg.sender, referrals[msg.sender], rewardAmount);
        }
    }

    // Placeholder function for NFT minting logic
    function _mintNFT(address to) internal {
        // Implement actual NFT minting logic here
    }

    // Function to calculate the reward amount
    function calculateReward() internal pure returns (uint256) {
        // Define the reward logic (e.g., fixed amount or percentage of mint price)
        return 0.01 ether; // Example: fixed reward of 0.01 ETH
    }

    // Function for users to withdraw their earned rewards
    function withdrawRewards() external {
        uint256 amount = referralRewards[msg.sender];
        require(amount > 0, "No rewards to withdraw");

        // Reset the user's rewards before transferring to prevent re-entrancy
        referralRewards[msg.sender] = 0;

        // Transfer the reward to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to withdraw contract balance (only owner)
    function withdrawContractBalance() external onlyOwner {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
