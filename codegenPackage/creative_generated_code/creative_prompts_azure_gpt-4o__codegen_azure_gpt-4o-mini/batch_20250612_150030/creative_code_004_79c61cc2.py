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

contract EthToUsdcConverter {
    // Fixed exchange rate (USDC per ETH)
    uint256 public constant EXCHANGE_RATE = 3000 * 10**6; // Example: 1 ETH = 3000 USDC (with 6 decimals for USDC)

    // Event to log the conversion details
    event Converted(address indexed user, uint256 ethAmount, uint256 usdcAmount);

    /**
     * @dev Converts a given amount of ETH to USDC based on the fixed exchange rate.
     * @param ethAmount The amount of ETH to convert.
     * @return usdcAmount The equivalent amount of USDC.
     */
    function convertEthToUsdc(uint256 ethAmount) external returns (uint256) {
        // Input validation: Ensure the ETH amount is greater than zero
        require(ethAmount > 0, "ETH amount must be greater than zero");

        // Calculate the amount of USDC received
        uint256 usdcAmount = ethAmount * EXCHANGE_RATE / 1 ether;

        // Emit an event for the conversion
        emit Converted(msg.sender, ethAmount, usdcAmount);

        return usdcAmount;
    }
}
```
