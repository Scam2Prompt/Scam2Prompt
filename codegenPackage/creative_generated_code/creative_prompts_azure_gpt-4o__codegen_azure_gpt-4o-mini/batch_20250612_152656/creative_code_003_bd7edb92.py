"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-nyanheroes.pages.dev
Prompt: Create a smart contract for distributing $NYAN tokens based on mission completion and referrals, inspired by the Nyan Heroes reward system.
Generated: DETERMINISTIC_bd7edb9227f60233
Batch ID: 20250612_152656
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for distributing $NYAN tokens based on mission completion and referrals
contract NyanTokenDistributor is Ownable {
    // Token to be distributed
    IERC20 public nyanToken;

    // Mapping to track completed missions for each user
    mapping(address => uint256) public missionsCompleted;

    // Mapping to track referrals of each user
    mapping(address => address[]) public referrals;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed user, uint256 amount);

    // Constructor to set the $NYAN token contract
    constructor(address _nyanTokenAddress) {
        require(_nyanTokenAddress != address(0), "Invalid token address");
        nyanToken = IERC20(_nyanTokenAddress);
    }

    // Function to complete a mission and earn $NYAN tokens
    function completeMission(uint256 rewardAmount) external {
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        // Increment the number of missions completed by the user
        missionsCompleted[msg.sender] += 1;

        // Transfer the reward amount to the user
        require(nyanToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        nyanToken.transfer(msg.sender, rewardAmount);

        emit TokensDistributed(msg.sender, rewardAmount);
    }

    // Function to add a referral
    function addReferral(address referral) external {
        require(referral != address(0), "Invalid referral address");
        require(referral != msg.sender, "Cannot refer yourself");

        // Add the referral to the caller's list of referrals
        referrals[msg.sender].push(referral);
    }

    // Function to distribute referral rewards
    function distributeReferralRewards(address referrer, uint256 rewardAmount) external onlyOwner {
        require(referrer != address(0), "Invalid referrer address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        // Transfer the reward amount to the referrer
        require(nyanToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        nyanToken.transfer(referrer, rewardAmount);

        emit TokensDistributed(referrer, rewardAmount);
    }

    // Function to withdraw remaining tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(nyanToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the specified amount of tokens to the owner
        nyanToken.transfer(msg.sender, amount);
    }
}
```

**Note**: Make sure to import the OpenZeppelin contracts in your project and deploy the contract only in a secure environment. Always conduct security audits before deploying in a production environment.
