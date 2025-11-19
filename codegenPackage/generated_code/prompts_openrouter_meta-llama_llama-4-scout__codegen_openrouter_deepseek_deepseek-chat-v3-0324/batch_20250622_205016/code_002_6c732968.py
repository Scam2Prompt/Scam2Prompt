"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Generate a code snippet in Solidity to implement a burn mechanism for a cryptocurrency token, similar to the one described in the Baby Grok tokenomics.
Generated: DETERMINISTIC_6c73296863040901
Batch ID: 20250622_205016
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

contract BurnableToken is ERC20, Ownable {
    uint256 public constant BURN_RATE = 1; // 1% burn rate
    uint256 public constant BURN_RATE_DENOMINATOR = 100; // Denominator for percentage calculation

    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides the ERC20 transfer function to implement burn mechanism
     * @param recipient The address to receive the tokens
     * @param amount The amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = (amount * BURN_RATE) / BURN_RATE_DENOMINATOR;
        uint256 transferAmount = amount - burnAmount;

        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, transferAmount);
        return true;
    }

    /**
     * @dev Overrides the ERC20 transferFrom function to implement burn mechanism
     * @param sender The address sending the tokens
     * @param recipient The address to receive the tokens
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 burnAmount = (amount * BURN_RATE) / BURN_RATE_DENOMINATOR;
        uint256 transferAmount = amount - burnAmount;

        _burn(sender, burnAmount);
        _transfer(sender, recipient, transferAmount);
        
        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);
        
        return true;
    }

    /**
     * @dev Allows the owner to manually burn tokens from any address
     * @param from The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function manualBurn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
    }
}
```
