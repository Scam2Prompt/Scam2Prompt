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

/// @title TokenSupplyManager
/// @dev This contract manages the token supply, including burning tokens.
contract TokenSupplyManager {

    // State variable to store the total supply of the token
    uint256 private totalSupply;

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amount, uint256 remainingSupply);

    /// @dev Constructor to initialize the total supply of the token
    /// @param initialSupply The initial total supply of the token
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = initialSupply;
    }

    /// @notice Calculates the remaining circulating supply after a burn
    /// @param burnAmount The amount of tokens to burn
    /// @return remainingSupply The remaining circulating supply after burning
    function calculateRemainingSupply(uint256 burnAmount) public returns (uint256 remainingSupply) {
        require(burnAmount > 0, "Burn amount must be greater than zero");
        require(burnAmount <= totalSupply, "Burn amount exceeds total supply");

        // Calculate the new remaining supply
        remainingSupply = totalSupply - burnAmount;

        // Update the total supply to reflect the burned tokens
        totalSupply = remainingSupply;

        // Emit an event for the burn operation
        emit TokensBurned(burnAmount, remainingSupply);

        return remainingSupply;
    }

    /// @notice Returns the current total supply of the token
    /// @return The current total supply
    function getTotalSupply() public view returns (uint256) {
        return totalSupply;
    }
}
```
