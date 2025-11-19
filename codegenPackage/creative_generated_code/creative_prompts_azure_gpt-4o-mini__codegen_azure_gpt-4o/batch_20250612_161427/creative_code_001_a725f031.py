"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyber-networkrw.web.app
Prompt: Write a code snippet to implement a claiming function for an ERC-20 token that allows users to claim rewards until a countdown ends.
Generated: DETERMINISTIC_a725f031b566ae87
Batch ID: 20250612_161427
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

/// @title ERC-20 Reward Claiming Contract
/// @author Expert Programmer
/// @notice This contract allows users to claim ERC-20 token rewards within a specified countdown period.
/// @dev Ensure to deploy the contract with an ERC-20 token address and initial countdown duration.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RewardClaimer {
    // The ERC-20 token being rewarded
    IERC20 public rewardToken;

    // Countdown duration (in seconds) for claiming rewards
    uint256 public countdownDuration;

    // Start timestamp for the countdown
    uint256 public countdownStart;

    // Mapping to track claimed rewards
    mapping(address => bool) public hasClaimed;

    // Owner of the contract (used for administrative purposes)
    address public owner;

    /// @notice Emitted when a user successfully claims their rewards
    /// @param claimer Address of the user who claimed rewards
    /// @param amount Amount of tokens claimed
    event RewardClaimed(address indexed claimer, uint256 amount);

    /// @notice Constructor to initialize the contract
    /// @param _rewardToken Address of the ERC-20 token used for rewards
    /// @param _countdownDuration Countdown duration in seconds
    constructor(IERC20 _rewardToken, uint256 _countdownDuration) {
        require(address(_rewardToken) != address(0), "Invalid token address");
        require(_countdownDuration > 0, "Countdown duration must be positive");

        rewardToken = _rewardToken;
        countdownDuration = _countdownDuration;
        owner = msg.sender;

        // Start the countdown at deployment
        countdownStart = block.timestamp;
    }

    /// @notice Allows users to claim their rewards before the countdown ends
    /// @dev Users can only claim once and only if the countdown is active
    function claimReward() external {
        // Check if the countdown has ended
        require(block.timestamp <= countdownStart + countdownDuration, "Countdown has ended");

        // Ensure the user has not claimed rewards yet
        require(!hasClaimed[msg.sender], "Rewards already claimed");

        // Mark the user as having claimed rewards
        hasClaimed[msg.sender] = true;

        // Define the reward amount (hardcoded but can be parameterized)
        uint256 rewardAmount = 100 * (10 ** 18); // Example: 100 tokens (assuming 18 decimals)

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(msg.sender, rewardAmount), "Token transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /// @notice Allows the owner to withdraw unused tokens after the countdown ends
    /// @dev Only callable by the contract owner
    function withdrawUnusedTokens() external {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(block.timestamp > countdownStart + countdownDuration, "Countdown is still active");

        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        require(rewardToken.transfer(owner, contractBalance), "Token transfer failed");
    }
}
```
