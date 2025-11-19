"""
Generated Code Metadata:
========================
Original URL: https://kishu.finance
Prompt: Write a Solidity contract that implements a token burning mechanism similar to the one described for $KISHU, where tokens are permanently removed from circulation.
Generated: DETERMINISTIC_f65e4fc084da813f
Batch ID: 20250612_150602
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
 * @title KishuToken
 * @dev Implementation of a token with a burning mechanism.
 */
contract KishuToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * @param initialSupply The initial supply of tokens to be minted.
     */
    constructor(uint256 initialSupply) ERC20("KishuToken", "KISHU") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to burn a specific amount of tokens.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);
        
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens on behalf of another address.
     * @param account The address of the account whose tokens will be burned.
     * @param amount The amount of tokens to be burned.
     */
    function burnFrom(address account, uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(account) >= amount, "Insufficient balance to burn");
        require allowance(account, msg.sender) >= amount, "Allowance exceeded");

        // Burn the tokens
        _burn(account, amount);
        
        // Decrease the allowance
        _approve(account, msg.sender, allowance(account, msg.sender) - amount);
        
        // Emit the burn event
        emit TokensBurned(account, amount);
    }
}
```
