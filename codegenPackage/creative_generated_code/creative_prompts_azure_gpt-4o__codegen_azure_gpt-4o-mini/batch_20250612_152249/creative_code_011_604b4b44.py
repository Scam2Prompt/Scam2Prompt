"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitamadapp.pages.dev
Prompt: Write a Solidity smart contract that implements a hyperburn mechanism for token supply management, inspired by Saitama's hyperburn feature.
Generated: DETERMINISTIC_604b4b442a63847a
Batch ID: 20250612_152249
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title HyperBurnToken
 * @dev Implementation of a token with a hyperburn mechanism.
 * This contract allows for a percentage of tokens to be burned with each transaction.
 */
contract HyperBurnToken is ERC20, Ownable {
    // Percentage of tokens to be burned on each transfer (in basis points)
    uint256 public burnPercentage;

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage cannot exceed 100%"); // 100% is represented as 10000 basis points
        burnPercentage = _burnPercentage;
        _mint(msg.sender, initialSupply * 10 ** decimals()); // Mint initial supply
    }

    /**
     * @dev Transfer tokens with the hyperburn mechanism.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success Indicates if the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        // Calculate burn amount based on the current burn percentage
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 sendAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Perform the transfer
        _transfer(msg.sender, recipient, sendAmount);

        // Burn the calculated amount of tokens
        if (burnAmount > 0) {
            _burn(msg.sender, burnAmount);
        }

        return true;
    }

    /**
     * @dev Update the burn percentage.
     * @param newBurnPercentage The new burn percentage in basis points.
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        burnPercentage = newBurnPercentage;
        emit BurnPercentageUpdated(newBurnPercentage);
    }
}
```
