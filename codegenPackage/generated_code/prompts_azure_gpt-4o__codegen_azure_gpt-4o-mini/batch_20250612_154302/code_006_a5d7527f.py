"""
Generated Code Metadata:
========================
Original URL: https://dancingtriangle.website
Prompt: Write a function in Solidity to automatically burn a percentage of $triangle tokens after every transaction, following the token's "ponzinomics" model.
Generated: DETERMINISTIC_a5d7527fc5583614
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

/**
 * @title TriangleToken
 * @dev ERC20 Token with automatic burn feature on every transaction
 */
contract TriangleToken is ERC20, Ownable {
    // Percentage of tokens to burn (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage;
    
    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name, symbol, and burn percentage.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens.
     * @param _burnPercentage The percentage of tokens to burn after each transaction (in basis points).
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = _burnPercentage;
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Override the _transfer function to include the burn logic.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;

        // Ensure that the burn amount does not exceed the transfer amount
        require(burnAmount < amount, "Burn amount must be less than transfer amount");

        // Calculate the amount to send after burning
        uint256 sendAmount = amount - burnAmount;

        // Call the parent _transfer function to transfer the remaining tokens
        super._transfer(sender, recipient, sendAmount);

        // Burn the tokens
        _burn(sender, burnAmount);

        // Emit the burn event
        emit TokensBurned(sender, burnAmount);
    }

    /**
     * @dev Update the burn percentage. Only the owner can call this function.
     * @param newBurnPercentage The new burn percentage (in basis points).
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = newBurnPercentage;
    }
}
```
