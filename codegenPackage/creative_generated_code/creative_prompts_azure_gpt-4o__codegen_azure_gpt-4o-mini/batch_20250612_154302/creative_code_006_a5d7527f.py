"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dancingtriangle.website
Prompt: Write a function in Solidity to automatically burn a percentage of $triangle tokens after every transaction, following the token's "ponzinomics" model.
Generated: DETERMINISTIC_a5d7527fc5583614
Batch ID: 20250612_154302
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token contract that implements "ponzinomics" model to auto-burn on transactions
contract TriangleToken is ERC20, Ownable {
    // Percentage of tokens to burn (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage = 100; // 1% by default

    // Event emitted when burn percentage is changed
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    // Constructor to set the initial supply of tokens
    constructor(uint256 initialSupply) ERC20("TriangleToken", "TRIANGLE") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Override the _transfer function to include burn logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000; // Convert basis points to percentage
        
        // Ensure we do not burn more than the amount being transferred
        require(burnAmount < amount, "Burn amount exceeds transfer amount");

        // Subtract the burn amount from the transfer amount
        uint256 amountAfterBurn = amount - burnAmount;

        // Call the parent _transfer method
        super._transfer(sender, recipient, amountAfterBurn);
        
        // Burn the calculated amount
        _burn(sender, burnAmount);
    }

    // Function to set a new burn percentage, restricted to the owner
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 1000, "Burn percentage must be <= 10%");
        burnPercentage = newBurnPercentage;
        emit BurnPercentageUpdated(newBurnPercentage);
    }
}
```
