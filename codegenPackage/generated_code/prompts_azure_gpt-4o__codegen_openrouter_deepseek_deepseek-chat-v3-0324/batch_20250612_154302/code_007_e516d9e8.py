"""
Generated Code Metadata:
========================
Original URL: https://czbull.com
Prompt: Provide an example of a smart contract function in Solidity that burns a percentage of tokens during every transaction, inspired by the $WINDY Once Again token mechanism.
Generated: DETERMINISTIC_e516d9e8ef024661
Batch ID: 20250612_154302
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

contract WindyToken is ERC20, Ownable {
    uint256 public constant BURN_PERCENTAGE = 1; // 1% burn rate
    uint256 public constant PERCENTAGE_DIVISOR = 100; // For percentage calculations

    constructor(uint256 initialSupply) ERC20("Windy Token", "WINDY") {
        _mint(msg.sender, initialSupply);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 burnAmount = (amount * BURN_PERCENTAGE) / PERCENTAGE_DIVISOR;
        uint256 transferAmount = amount - burnAmount;

        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }

        super._transfer(sender, recipient, transferAmount);
    }

    // Optional: Function to update burn percentage (onlyOwner)
    function setBurnPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Burn percentage cannot exceed 100");
        // Note: Since BURN_PERCENTAGE is constant, this would require
        // restructuring the contract to use a variable instead
        // This is left as an example of potential extension
    }
}
```
