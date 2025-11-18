"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiernerdogai-presale.pages.dev
Prompt: Write a Solidity contract for distributing community rewards, ensuring it aligns with the tokenomics breakdown provided by WienerAI.
Generated: DETERMINISTIC_a42b6f220e9e0111
Batch ID: 20250612_152235
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

/**
 * @title CommunityRewardDistributor
 * @dev This contract distributes community rewards based on specified tokenomics.
 */
contract CommunityRewardDistributor is Ownable {
    IERC20 public rewardToken; // Token used for rewards
    uint256 public totalRewards; // Total rewards available for distribution
    uint256 public lastDistribution; // Timestamp of the last distribution

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the reward token address and total rewards.
     * @param _rewardToken The address of the reward token contract.
     * @param _totalRewards The total amount of rewards available for distribution.
     */
    constructor(IERC20 _rewardToken, uint256 _totalRewards) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        rewardToken = _rewardToken;
        totalRewards = _totalRewards;
        lastDistribution = block.timestamp;
    }

    /**
     * @dev Distributes rewards to a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to distribute.
     */
    function distributeRewards(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= totalRewards, "Insufficient rewards available");

        // Transfer the reward tokens to the recipient
        bool success = rewardToken.transfer(recipient, amount);
        require(success, "Token transfer failed");

        // Update the remaining rewards and emit an event
        totalRewards -= amount;
        emit RewardsDistributed(recipient, amount);
    }

    /**
     * @dev Allows the owner to withdraw any leftover tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(amount <= rewardToken.balanceOf(address(this)), "Insufficient contract balance");

        // Transfer the specified amount of tokens to the owner
        bool success = rewardToken.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Allows the owner to update the total rewards pool.
     * @param newTotalRewards The new total rewards amount.
     */
    function updateTotalRewards(uint256 newTotalRewards) external onlyOwner {
        require(newTotalRewards > 0, "New total rewards must be greater than zero");
        totalRewards = newTotalRewards;
    }
}
```
