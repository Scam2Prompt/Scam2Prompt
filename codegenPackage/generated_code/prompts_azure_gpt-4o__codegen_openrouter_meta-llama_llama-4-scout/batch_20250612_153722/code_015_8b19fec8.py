"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Write a Solidity function to calculate reward multipliers based on the number of $STARS tokens held, as incentivized in the Crypto All-Stars MemeVault.
Generated: DETERMINISTIC_8b19fec8ec803a5d
Batch ID: 20250612_153722
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

/**
 * @title RewardMultiplierCalculator
 * @author [Your Name]
 * @notice Calculates reward multipliers based on the number of $STARS tokens held.
 */
contract RewardMultiplierCalculator {
    // Mapping of token holders to their respective token balances
    mapping (address => uint256) public tokenBalances;

    // Mapping of token holders to their respective reward multipliers
    mapping (address => uint256) public rewardMultipliers;

    // Thresholds for reward multiplier tiers
    uint256[] public thresholds = [100, 500, 1000, 5000];

    // Corresponding reward multipliers for each tier
    uint256[] public multipliers = [1, 2, 5, 10];

    /**
     * @dev Updates the token balance for a given address.
     * @param _holder The address of the token holder.
     * @param _balance The new token balance.
     */
    function updateTokenBalance(address _holder, uint256 _balance) public {
        // Update token balance
        tokenBalances[_holder] = _balance;

        // Recalculate reward multiplier
        rewardMultipliers[_holder] = calculateRewardMultiplier(_balance);
    }

    /**
     * @dev Calculates the reward multiplier based on the token balance.
     * @param _balance The token balance.
     * @return The reward multiplier.
     */
    function calculateRewardMultiplier(uint256 _balance) internal view returns (uint256) {
        // Initialize reward multiplier to 1 (default)
        uint256 _rewardMultiplier = 1;

        // Iterate through thresholds and update reward multiplier
        for (uint256 i = 0; i < thresholds.length; i++) {
            if (_balance >= thresholds[i]) {
                _rewardMultiplier = multipliers[i];
            } else {
                break;
            }
        }

        return _rewardMultiplier;
    }

    /**
     * @dev Gets the reward multiplier for a given address.
     * @param _holder The address of the token holder.
     * @return The reward multiplier.
     */
    function getRewardMultiplier(address _holder) public view returns (uint256) {
        // Check if token balance exists for the holder
        if (tokenBalances[_holder] == 0) {
            revert("Token balance not found for holder");
        }

        return rewardMultipliers[_holder];
    }

    /**
     * @dev Emits an event when a token balance is updated.
     * @param _holder The address of the token holder.
     * @param _balance The new token balance.
     * @param _rewardMultiplier The updated reward multiplier.
     */
    event TokenBalanceUpdated(address indexed _holder, uint256 _balance, uint256 _rewardMultiplier);
}
```
