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

// Interface for the ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

// Contract to calculate reward multipliers based on $STARS token holdings
contract StarRewardCalculator {
    // Token contract instance
    IERC20 public starsToken;

    // Mapping to store reward multipliers based on token holdings
    mapping(uint256 => uint256) public rewardMultipliers;

    // Constructor to initialize the $STARS token address
    constructor(address _starsToken) {
        require(_starsToken != address(0), "Invalid token address");
        starsToken = IERC20(_starsToken);
        initializeRewardMultipliers();
    }

    // Function to initialize reward multipliers
    function initializeRewardMultipliers() internal {
        // Define multipliers based on the number of tokens held
        rewardMultipliers[0] = 1;      // 0 - 999 tokens: 1x multiplier
        rewardMultipliers[1000] = 2;   // 1000 - 4999 tokens: 2x multiplier
        rewardMultipliers[5000] = 3;   // 5000 - 9999 tokens: 3x multiplier
        rewardMultipliers[10000] = 5;  // 10000+ tokens: 5x multiplier
    }

    // Function to calculate the reward multiplier based on the holder's token balance
    function calculateRewardMultiplier(address holder) external view returns (uint256) {
        // Get the balance of $STARS tokens for the holder
        uint256 balance = starsToken.balanceOf(holder);

        // Determine the appropriate multiplier based on the balance
        if (balance >= 10000) {
            return rewardMultipliers[10000];
        } else if (balance >= 5000) {
            return rewardMultipliers[5000];
        } else if (balance >= 1000) {
            return rewardMultipliers[1000];
        } else {
            return rewardMultipliers[0];
        }
    }
}
```
