"""
Generated Code Metadata:
========================
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Develop a Solidity smart contract for distributing rewards in a multichain Web3 gaming ecosystem, similar to Kewl's features mentioned on the GAINS Associates platform.
Generated: DETERMINISTIC_e382f432e3249370
Batch ID: 20250612_152109
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

/**
 * @title RewardDistributor
 * @dev A smart contract for distributing rewards in a multichain Web3 gaming ecosystem.
 */
contract RewardDistributor is Ownable {
    // Mapping to track user rewards
    mapping(address => uint256) private rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Distribute rewards to a user.
     * @param user Address of the user to receive rewards.
     * @param amount Amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");

        rewards[user] += amount;

        // Emit event for rewards distribution
        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Claim rewards for the caller.
     */
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's rewards before transferring to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");

        // Emit event for rewards claim
        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Get the rewards balance of a user.
     * @param user Address of the user.
     * @return The amount of rewards the user has.
     */
    function getRewardsBalance(address user) external view returns (uint256) {
        return rewards[user];
    }

    /**
     * @dev Withdraw tokens from the contract (only owner).
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");

        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Transfer failed");
    }
}
```
