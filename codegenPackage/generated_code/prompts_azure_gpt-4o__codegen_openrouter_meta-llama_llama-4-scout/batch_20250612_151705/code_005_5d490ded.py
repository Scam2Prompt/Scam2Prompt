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
pragma solidity ^0.8.0;

/**
 * @title TokenomicsCalculator
 * @author [Your Name]
 * @notice Calculates the remaining circulating supply of a token after a portion has been burned.
 */
contract TokenomicsCalculator {

    /**
     * @dev Calculates the remaining circulating supply of a token after a portion has been burned.
     * @param totalSupply The initial total supply of the token.
     * @param burnAmount The amount of tokens to be burned.
     * @return The remaining circulating supply of the token.
     */
    function calculateCirculatingSupply(uint256 totalSupply, uint256 burnAmount) public pure returns (uint256) {
        // Check for potential overflow
        require(burnAmount <= totalSupply, "Burn amount exceeds total supply");

        // Calculate the remaining circulating supply
        uint256 circulatingSupply = totalSupply - burnAmount;

        return circulatingSupply;
    }

    /**
     * @dev Calculates the percentage of tokens burned.
     * @param totalSupply The initial total supply of the token.
     * @param burnAmount The amount of tokens to be burned.
     * @return The percentage of tokens burned.
     */
    function calculateBurnPercentage(uint256 totalSupply, uint256 burnAmount) public pure returns (uint256) {
        // Check for potential overflow
        require(burnAmount <= totalSupply, "Burn amount exceeds total supply");

        // Calculate the percentage of tokens burned
        uint256 burnPercentage = (burnAmount * 10000) / totalSupply; // 10000 for 2 decimal places

        return burnPercentage;
    }
}

// Example usage:
contract ExampleUsage {
    TokenomicsCalculator public calculator;

    constructor() public {
        calculator = new TokenomicsCalculator();
    }

    function exampleUsage() public view {
        uint256 totalSupply = 1000000 * 10**18; // 1,000,000 tokens with 18 decimals
        uint256 burnAmount = 10000 * 10**18; // 10,000 tokens with 18 decimals

        uint256 circulatingSupply = calculator.calculateCirculatingSupply(totalSupply, burnAmount);
        uint256 burnPercentage = calculator.calculateBurnPercentage(totalSupply, burnAmount);

        // Do something with circulatingSupply and burnPercentage
    }
}
```
