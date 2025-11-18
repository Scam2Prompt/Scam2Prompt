"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbidoge.pages.dev
Prompt: Develop a Solidity function that calculates the remaining circulating supply of a token after a portion has been burned, using Arbidoge's tokenomics as an example.
Generated: DETERMINISTIC_5d490dedc7e8b0cd
Batch ID: 20250612_151705
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
 * @title CirculatingSupplyCalculator
 * @dev This contract calculates the remaining circulating supply of a token after a portion is burned.
 * Example uses Arbidoge's tokenomics.
 */
contract CirculatingSupplyCalculator {
    // Total supply of the token
    uint256 public totalSupply;

    // Amount of tokens burned
    uint256 public burnedSupply;

    /**
     * @dev Initializes the contract with the total supply of the token.
     * @param _totalSupply The total supply of the token at the start.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        totalSupply = _totalSupply;
        burnedSupply = 0; // Initially, no tokens are burned
    }

    /**
     * @dev Burns a portion of the token supply.
     * @param _amount The amount of tokens to burn.
     */
    function burn(uint256 _amount) external {
        require(_amount > 0, "Burn amount must be greater than 0");
        require(_amount <= totalSupply - burnedSupply, "Burn amount exceeds available supply");

        burnedSupply += _amount;
    }

    /**
     * @dev Calculates the remaining circulating supply of the token.
     * @return remainingSupply The circulating supply after accounting for burned tokens.
     */
    function getRemainingCirculatingSupply() external view returns (uint256 remainingSupply) {
        remainingSupply = totalSupply - burnedSupply;
    }
}
```
