"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testuser.usdtddex.com
Prompt: Using the contract address `0xAad3172844A4e106D32E2F0c206E5Be7D143325A`, write a Solidity function to calculate the daily staking rewards for a given amount of USDTD tokens based on the staking plans described (0.90% for 10-1,000 USDTD and 1.80% for 1,001+ USDTD).
Generated: DETERMINISTIC_4539c610ef69e010
Batch ID: 20250612_150345
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

contract StakingRewards {
    // Address of the USDTD token contract
    address public usdtdTokenAddress;

    // Event to log the calculated rewards
    event RewardsCalculated(address indexed user, uint256 amountStaked, uint256 rewards);

    // Constructor to set the USDTD token address
    constructor(address _usdtdTokenAddress) {
        require(_usdtdTokenAddress != address(0), "Invalid token address");
        usdtdTokenAddress = _usdtdTokenAddress;
    }

    /**
     * @dev Function to calculate daily staking rewards based on the amount staked.
     * @param amountStaked The amount of USDTD tokens staked.
     * @return dailyRewards The calculated daily rewards in USDTD tokens.
     */
    function calculateDailyRewards(uint256 amountStaked) external view returns (uint256 dailyRewards) {
        // Validate the amount staked is not zero
        require(amountStaked > 0, "Staked amount must be greater than zero");

        // Calculate rewards based on the staking plan
        if (amountStaked >= 10 && amountStaked <= 1000) {
            // Reward rate for 10-1,000 USDTD
            dailyRewards = (amountStaked * 90) / 10000; // 0.90% rewards
        } else if (amountStaked > 1000) {
            // Reward rate for 1,001+ USDTD
            dailyRewards = (amountStaked * 180) / 10000; // 1.80% rewards
        } else {
            // If the amount staked is less than the minimum required
            revert("Amount staked must be at least 10 USDTD");
        }

        // Emit the event with calculated rewards
        emit RewardsCalculated(msg.sender, amountStaked, dailyRewards);
    }
}
```
