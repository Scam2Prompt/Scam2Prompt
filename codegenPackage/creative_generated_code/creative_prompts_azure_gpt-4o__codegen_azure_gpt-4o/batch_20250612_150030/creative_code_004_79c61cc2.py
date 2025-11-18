"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.xyz
Prompt: Implement a function in Solidity that calculates the amount of USDC a user will receive for a given amount of ETH, considering a fixed exchange rate.
Generated: DETERMINISTIC_79c61cc2ba4fd338
Batch ID: 20250612_150030
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

/**
 * @title ETHToUSDCConverter
 * @dev This contract allows users to calculate the amount of USDC
 * they will receive for a given amount of ETH based on a fixed exchange rate.
 */
contract ETHToUSDCConverter {
    // Fixed exchange rate: 1 ETH = 2000 USDC (example rate)
    uint256 private constant EXCHANGE_RATE = 2000;

    /**
     * @dev Calculates the amount of USDC a user will receive for a given amount of ETH.
     * @param ethAmount The amount of ETH (in wei) provided by the user.
     * @return The equivalent amount of USDC (in smallest denomination, e.g., 6 decimals for USDC).
     */
    function calculateUSDC(uint256 ethAmount) public pure returns (uint256) {
        // Validate the input to ensure a non-zero amount is provided
        require(ethAmount > 0, "ETH amount must be greater than 0");

        // Calculate the equivalent USDC amount (1 ETH = 2000 USDC)
        uint256 usdcAmount = (ethAmount * EXCHANGE_RATE) / 1 ether;

        return usdcAmount;
    }
}
```
