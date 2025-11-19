"""
Generated Code Metadata:
========================
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Write a smart contract function in Solidity that integrates with the Internet Money (IM) token to calculate and display the total burned supply percentage, similar to the "Total Burned (0.225% OF TOTAL SUPPLY)" feature described on the website.
Generated: DETERMINISTIC_8f4c0fb118b4067d
Batch ID: 20250612_153700
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

// Interface for the Internet Money (IM) token
interface IIMToken {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract BurnedSupplyCalculator {
    // Address of the Internet Money (IM) token contract
    IIMToken public imToken;

    // Event to log the burned supply percentage
    event BurnedSupplyPercentage(uint256 percentage);

    // Constructor to set the IM token address
    constructor(address _imTokenAddress) {
        require(_imTokenAddress != address(0), "Invalid token address");
        imToken = IIMToken(_imTokenAddress);
    }

    // Function to calculate and display the total burned supply percentage
    function calculateBurnedSupplyPercentage() external {
        // Get the total supply of the IM token
        uint256 totalSupply = imToken.totalSupply();
        require(totalSupply > 0, "Total supply must be greater than zero");

        // Calculate the burned supply (assuming burned tokens are tracked in a specific way)
        uint256 burnedSupply = totalBurnedSupply(); // Placeholder for actual burned supply logic

        // Calculate the burned supply percentage
        uint256 burnedSupplyPercentage = (burnedSupply * 100) / totalSupply;

        // Emit the burned supply percentage
        emit BurnedSupplyPercentage(burnedSupplyPercentage);
    }

    // Placeholder function to get the total burned supply
    // This should be replaced with actual logic to track burned tokens
    function totalBurnedSupply() internal view returns (uint256) {
        // For demonstration purposes, returning a fixed value
        // In a real implementation, this should return the actual burned supply
        return 225000000000000000; // Example: 0.225% of a total supply of 100 million tokens (in wei)
    }
}
```
