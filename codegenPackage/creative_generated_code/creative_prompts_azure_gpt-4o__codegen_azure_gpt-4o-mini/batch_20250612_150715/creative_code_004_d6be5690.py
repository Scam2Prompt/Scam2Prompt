"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Generate a smart contract that enables Farcaster channels to issue programmatic rewards for followers who engage with specific content, using Moxie Reward functionality.
Generated: DETERMINISTIC_d6be56909411643a
Batch ID: 20250612_150715
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FarcasterRewards
 * @dev A smart contract that rewards users for engaging with specific content in Farcaster channels.
 */
contract FarcasterRewards is Ownable {
    using SafeMath for uint256;

    // Event to log rewards issued
    event RewardIssued(address indexed follower, uint256 amount, string contentId);

    // Mapping to track rewards issued to each follower for each content
    mapping(address => mapping(string => uint256)) public rewards;

    // The ERC20 token used for rewards
    IERC20 public rewardToken;

    /**
     * @dev Constructor to set the reward token contract address.
     * @param _rewardToken The address of the ERC20 token to be used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Function to issue rewards to followers for engaging with specific content.
     * @param follower The address of the follower receiving the reward.
     * @param amount The amount of tokens to reward.
     * @param contentId The ID of the content the follower engaged with.
     */
    function issueReward(address follower, uint256 amount, string calldata contentId) external onlyOwner {
        require(follower != address(0), "Invalid follower address");
        require(amount > 0, "Reward amount must be greater than zero");
        require(bytes(contentId).length > 0, "Invalid content ID");

        // Transfer the reward tokens from the contract to the follower
        require(rewardToken.transfer(follower, amount), "Token transfer failed");

        // Update the rewards mapping
        rewards[follower][contentId] = rewards[follower][contentId].add(amount);

        // Emit an event to log the reward issuance
        emit RewardIssued(follower, amount, contentId);
    }

    /**
     * @dev Function to check the rewards issued to a follower for a specific content.
     * @param follower The address of the follower.
     * @param contentId The ID of the content.
     * @return The amount of rewards issued to the follower for the specified content.
     */
    function checkRewards(address follower, string calldata contentId) external view returns (uint256) {
        return rewards[follower][contentId];
    }

    /**
     * @dev Function to withdraw tokens from the contract by the owner.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner's address
        require(rewardToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
