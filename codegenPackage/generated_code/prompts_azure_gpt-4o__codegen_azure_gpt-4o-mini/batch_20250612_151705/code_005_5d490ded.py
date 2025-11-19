"""
Generated Code Metadata:
========================
Original URL: https://arbidoge.pages.dev
Prompt: Develop a Solidity function that calculates the remaining circulating supply of a token after a portion has been burned, using Arbidoge's tokenomics as an example.
Generated: DETERMINISTIC_5d490dedc7e8b0cd
Batch ID: 20250612_151705
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

contract ArbidogeToken {
    // Total supply of the token
    uint256 private totalSupply;

    // Circulating supply of the token
    uint256 private circulatingSupply;

    // Event to log the burning of tokens
    event TokensBurned(uint256 amount, uint256 newCirculatingSupply);

    // Constructor to initialize the total supply and circulating supply
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply;
        circulatingSupply = _initialSupply; // Initially, all tokens are in circulation
    }

    /**
     * @dev Function to burn a specified amount of tokens.
     * @param amount The amount of tokens to burn.
     * @return The new circulating supply after burning.
     */
    function burnTokens(uint256 amount) external returns (uint256) {
        require(amount > 0, "Burn amount must be greater than zero");
        require(amount <= circulatingSupply, "Cannot burn more than circulating supply");

        // Reduce the circulating supply by the amount burned
        circulatingSupply -= amount;

        // Emit an event for the burned tokens
        emit TokensBurned(amount, circulatingSupply);

        return circulatingSupply; // Return the new circulating supply
    }

    /**
     * @dev Function to get the current circulating supply.
     * @return The current circulating supply of the token.
     */
    function getCirculatingSupply() external view returns (uint256) {
        return circulatingSupply;
    }

    /**
     * @dev Function to get the total supply of the token.
     * @return The total supply of the token.
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }
}
```
