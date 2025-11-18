"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda-io.web.app
Prompt: Write a smart contract in Solidity for a Play-to-Earn game that integrates $MEDA-like tokens as rewards, aligning with Milei Moneda's roadmap goals.
Generated: DETERMINISTIC_1ad13010e8258dc9
Batch ID: 20250612_153401
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

/// @title Play-to-Earn Game Smart Contract
/// @author Your Name
/// @notice This contract allows players to earn $MEDA-like tokens through gameplay activities.
/// @dev The contract manages player rewards, tracks gameplay, and ensures secure token transfers.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PlayToEarnGame is Ownable {
    // Token used for rewards
    IERC20 public rewardToken;

    // Mapping to track player rewards
    mapping(address => uint256) public playerRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed player, uint256 amount);

    // Event emitted when a player claims their rewards
    event RewardsClaimed(address indexed player, uint256 amount);

    /// @notice Constructor to set the reward token address
    /// @param _rewardToken Address of the ERC20 token to be used as rewards
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /// @notice Function to distribute rewards to a player
    /// @param player Address of the player to distribute rewards to
    /// @param amount Amount of rewards to distribute
    function distributeRewards(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update the player rewards
        playerRewards[player] += amount;

        // Emit the rewards distribution event
        emit RewardsDistributed(player, amount);
    }

    /// @notice Function for players to claim their rewards
    /// @dev Ensures that the contract has enough tokens to cover the claim
    function claimRewards() external {
        uint256 amount = playerRewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset player's rewards to prevent re-entrancy attacks
        playerRewards[msg.sender] = 0;

        // Transfer the reward tokens to the player
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the rewards claim event
        emit RewardsClaimed(msg.sender, amount);
    }

    /// @notice Function to withdraw tokens from the contract by the owner
    /// @param amount Amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transfer the specified amount of tokens to the owner
        bool success = rewardToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    /// @notice Function to check the reward balance of a player
    /// @param player Address of the player
    /// @return The amount of rewards available for the player
    function getPlayerRewards(address player) external view returns (uint256) {
        return playerRewards[player];
    }
}
```
