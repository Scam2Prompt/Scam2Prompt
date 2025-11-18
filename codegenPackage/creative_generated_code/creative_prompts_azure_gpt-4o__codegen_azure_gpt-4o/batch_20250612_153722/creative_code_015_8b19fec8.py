"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Write a Solidity function to calculate reward multipliers based on the number of $STARS tokens held, as incentivized in the Crypto All-Stars MemeVault.
Generated: DETERMINISTIC_8b19fec8ec803a5d
Batch ID: 20250612_153722
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

/// @title Crypto All-Stars MemeVault Reward Multiplier Calculator
/// @author Developer XYZ
/// @notice This contract calculates reward multipliers based on the number of $STARS tokens held.
/// @dev Ensure proper integration with the $STARS token contract for accurate balances.

contract RewardMultiplier {
    // Address of the $STARS token contract
    address public starsTokenAddress;

    /// @notice Constructor to set the $STARS token address
    /// @param _starsTokenAddress Address of the deployed $STARS token contract
    constructor(address _starsTokenAddress) {
        require(_starsTokenAddress != address(0), "Invalid token address");
        starsTokenAddress = _starsTokenAddress;
    }

    /// @notice Function to calculate reward multiplier based on $STARS token balance
    /// @param user Address of the user whose $STARS balance will be checked
    /// @return multiplier Reward multiplier
    function calculateRewardMultiplier(address user) external view returns (uint256 multiplier) {
        require(user != address(0), "Invalid user address");

        // Interface to interact with the $STARS token contract
        IERC20 starsToken = IERC20(starsTokenAddress);

        // Fetching the $STARS balance of the user
        uint256 balance = starsToken.balanceOf(user);

        // Reward multiplier logic
        if (balance >= 10000 ether) {
            // High-tier multiplier for balances >= 10,000 $STARS
            multiplier = 5; // 5x multiplier
        } else if (balance >= 5000 ether) {
            // Mid-tier multiplier for balances >= 5,000 $STARS
            multiplier = 3; // 3x multiplier
        } else if (balance >= 1000 ether) {
            // Low-tier multiplier for balances >= 1,000 $STARS
            multiplier = 2; // 2x multiplier
        } else {
            // Default multiplier for balances < 1,000 $STARS
            multiplier = 1; // 1x multiplier
        }

        return multiplier;
    }
}

/// @dev Interface for ERC20 token to interact with the $STARS contract
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
