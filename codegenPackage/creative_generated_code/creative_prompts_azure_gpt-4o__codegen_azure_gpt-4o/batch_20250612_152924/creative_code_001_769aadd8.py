"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Create a function in Solidity that calculates the number of SHROOM tokens a buyer receives based on their ETH contribution, using the rate of 0.1 ETH = 99,500 SHROOM.
Generated: DETERMINISTIC_769aadd808108026
Batch ID: 20250612_152924
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
 * @title TokenPurchase
 * @dev Contract to calculate SHROOM token allocation based on ETH contribution.
 */
contract TokenPurchase {
    // Conversion rate: 0.1 ETH = 99,500 SHROOM
    uint256 public constant RATE = 99500; // Number of SHROOM tokens per 0.1 ETH
    uint256 public constant ETH_UNIT = 0.1 ether; // Equivalent of 0.1 ETH in wei

    /**
     * @dev Calculates the number of SHROOM tokens a buyer receives based on their ETH contribution.
     * @param ethAmount The amount of ETH contributed (in wei).
     * @return The number of SHROOM tokens allocated to the buyer.
     */
    function calculateShroomTokens(uint256 ethAmount) external pure returns (uint256) {
        require(ethAmount > 0, "ETH amount must be greater than zero");

        // Calculate the number of SHROOM tokens based on the ETH contribution
        uint256 shroomTokens = (ethAmount * RATE) / ETH_UNIT;

        return shroomTokens;
    }
}
```
