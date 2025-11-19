"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Develop a function in Solidity that burns 10% of token payouts as part of Everyworld’s ecosystem economic equilibrium mechanism.
Generated: DETERMINISTIC_e18e35959f070d17
Batch ID: 20250612_152739
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

contract EveryworldToken is ERC20, Ownable {
    uint256 public constant BURN_PERCENTAGE = 10; // 10% burn rate
    
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Transfers tokens to recipient and burns 10% of the amount
     * @param recipient Address receiving the tokens
     * @param amount Total amount to be transferred (before burn)
     */
    function transferWithBurn(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "EveryworldToken: transfer to zero address");
        require(amount > 0, "EveryworldToken: amount must be greater than 0");
        
        uint256 burnAmount = (amount * BURN_PERCENTAGE) / 100;
        uint256 transferAmount = amount - burnAmount;
        
        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, transferAmount);
        
        return true;
    }

    /**
     * @dev Overrides ERC20 transfer to include burn mechanism
     * @param recipient Address receiving the tokens
     * @param amount Amount to be transferred (before burn)
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        require(recipient != address(0), "EveryworldToken: transfer to zero address");
        require(amount > 0, "EveryworldToken: amount must be greater than 0");
        
        uint256 burnAmount = (amount * BURN_PERCENTAGE) / 100;
        uint256 transferAmount = amount - burnAmount;
        
        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, transferAmount);
        
        return true;
    }
}
```
