"""
Generated Code Metadata:
========================
Original URL: https://dancingtriangle.website
Prompt: Write a Solidity smart contract code to burn a specific percentage of $triangle cryptocurrency supply, similar to the 6.9% market-bought and burned tokens mentioned on the webpage.
Generated: DETERMINISTIC_ee981952d0fc22f3
Batch ID: 20250622_211546
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TriangleToken
 * @dev ERC20 token with burn functionality and percentage-based burning mechanism
 */
contract TriangleToken is ERC20, Ownable {
    /**
     * @dev Constructor that mints initial supply to the contract deployer
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) ERC20("Triangle", "TRIANGLE") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Burns a percentage of the total supply from the caller's balance
     * @param percentage The percentage of total supply to burn (e.g., 690 for 6.9%)
     * @notice Only the owner can call this function
     * @notice Percentage should be between 1 and 10000 (0.01% to 100%)
     */
    function burnPercentageOfSupply(uint256 percentage) external onlyOwner {
        require(percentage > 0 && percentage <= 10000, "Invalid percentage (0.01-100%)");
        
        uint256 totalSupply = totalSupply();
        uint256 amountToBurn = (totalSupply * percentage) / 10000;
        
        require(balanceOf(msg.sender) >= amountToBurn, "Insufficient balance for burn");
        
        _burn(msg.sender, amountToBurn);
    }

    /**
     * @dev Burns tokens from the caller's balance
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        _burn(msg.sender, amount);
    }
}
```
