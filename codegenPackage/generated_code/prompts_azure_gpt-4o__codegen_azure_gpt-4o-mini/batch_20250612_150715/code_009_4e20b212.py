"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Write a smart contract that enables Farcaster members to earn rewards based on their downstream influence on other members, as specified by the Moxie Protocol.
Generated: DETERMINISTIC_4e20b21213c6ce00
Batch ID: 20250612_150715
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title FarcasterRewards
 * @dev A smart contract that allows Farcaster members to earn rewards based on their downstream influence.
 */
contract FarcasterRewards is Ownable {
    // Token used for rewards
    IERC20 public rewardToken;

    // Mapping to track member influence and rewards
    mapping(address => uint256) public influencePoints;
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed member, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to update influence points for a member.
     * @param member Address of the member whose influence points are being updated.
     * @param points Amount of influence points to add.
     */
    function updateInfluencePoints(address member, uint256 points) external onlyOwner {
        require(member != address(0), "Invalid member address");
        require(points > 0, "Points must be greater than zero");

        influencePoints[member] += points;
    }

    /**
     * @dev Function to calculate rewards based on influence points.
     * @param member Address of the member for whom rewards are calculated.
     * @return uint256 Amount of rewards earned.
     */
    function calculateRewards(address member) public view returns (uint256) {
        // Simple reward calculation: 1 token per influence point
        return influencePoints[member];
    }

    /**
     * @dev Function for members to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the member's influence points after claiming
        influencePoints[msg.sender] = 0;

        // Transfer rewards to the member
        rewards[msg.sender] += rewardAmount;
        require(rewardToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract by the owner.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
