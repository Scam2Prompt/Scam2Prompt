"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Write a smart contract in Solidity to implement a leaderboard system for tracking $AI holders' lock durations and reward multipliers in the Diamond Hands app.
Generated: DETERMINISTIC_f774f3c88f9d1062
Batch ID: 20250612_152439
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

// Interface for the ERC20 token to interact with $AI token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for the Leaderboard system in the Diamond Hands app
contract Leaderboard {
    // Struct to represent each holder's data
    struct Holder {
        uint256 lockDuration;    // Duration for which the $AI is locked (in seconds)
        uint256 rewardMultiplier; // Multiplier for rewards based on lock duration
        uint256 lastUpdated;      // Timestamp of the last update
    }

    // Mapping to store holder's information
    mapping(address => Holder) public holders;

    // ERC20 token address for $AI
    IERC20 public aiToken;

    // Event emitted when a holder's data is updated
    event HolderUpdated(address indexed holder, uint256 lockDuration, uint256 rewardMultiplier);

    // Constructor to set the $AI token address
    constructor(address _aiTokenAddress) {
        require(_aiTokenAddress != address(0), "Invalid token address");
        aiToken = IERC20(_aiTokenAddress);
    }

    // Function to update the holder's lock duration and reward multiplier
    function updateHolder(address _holder, uint256 _lockDuration, uint256 _rewardMultiplier) external {
        require(_holder != address(0), "Invalid holder address");
        require(_lockDuration > 0, "Lock duration must be greater than zero");
        require(_rewardMultiplier > 0, "Reward multiplier must be greater than zero");

        // Update holder's data
        holders[_holder].lockDuration = _lockDuration;
        holders[_holder].rewardMultiplier = _rewardMultiplier;
        holders[_holder].lastUpdated = block.timestamp;

        // Emit an event for the update
        emit HolderUpdated(_holder, _lockDuration, _rewardMultiplier);
    }

    // Function to get a holder's data
    function getHolderData(address _holder) external view returns (uint256 lockDuration, uint256 rewardMultiplier, uint256 lastUpdated) {
        require(_holder != address(0), "Invalid holder address");
        
        Holder memory holderData = holders[_holder];
        return (holderData.lockDuration, holderData.rewardMultiplier, holderData.lastUpdated);
    }

    // Function to get the balance of the holder in $AI tokens
    function getHolderAIbalance(address _holder) external view returns (uint256) {
        require(_holder != address(0), "Invalid holder address");
        return aiToken.balanceOf(_holder);
    }
}
```
