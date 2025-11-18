"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kishu.finance
Prompt: Write a Solidity contract that implements a token burning mechanism similar to the one described for $KISHU, where tokens are permanently removed from circulation.
Generated: DETERMINISTIC_f65e4fc084da813f
Batch ID: 20250612_150602
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
 * @title KishuToken
 * @dev Implementation of the Kishu token with a burning mechanism.
 */
contract KishuToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all existing tokens.
     */
    constructor(uint256 initialSupply) ERC20("Kishu Token", "KISHU") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to burn a specific amount of tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        // Ensure the amount is greater than 0
        require(amount > 0, "Amount must be greater than 0");
        
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);
        
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override the _burn function to include custom logic if needed.
     * @param account The address of the token holder.
     * @param amount The amount to be burned.
     */
    function _burn(address account, uint256 amount) internal override {
        super._burn(account, amount);
    }
}
```
