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

/**
 * @title WindyToken
 * @dev ERC20 Token that burns a percentage of tokens during every transaction.
 */
contract WindyToken is ERC20, Ownable {
    // Percentage of tokens to burn (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage;

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    /**
     * @dev Constructor that initializes the token with a name, symbol, and initial supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens to be minted.
     * @param _burnPercentage The initial burn percentage in basis points.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = _burnPercentage;
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract deployer
    }

    /**
     * @dev Updates the burn percentage. Only the owner can call this function.
     * @param newBurnPercentage The new burn percentage in basis points.
     */
    function updateBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = newBurnPercentage;
        emit BurnPercentageUpdated(newBurnPercentage);
    }

    /**
     * @dev Overrides the _transfer function to include the burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the burn amount
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Burn the tokens
        _burn(sender, burnAmount);

        // Transfer the remaining tokens to the recipient
        super._transfer(sender, recipient, transferAmount);
    }
}
```
