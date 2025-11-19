"""
Generated Code Metadata:
========================
Original URL: https://simpsontrump.pages.dev
Prompt: Generate a smart contract for the Simpson Trump ($TRUMP) token that includes a total supply of 420 trillion and a tax rate of 0.
Generated: DETERMINISTIC_ab2c669d2aec9f46
Batch ID: 20250612_164304
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
 * @title Simpson Trump ($TRUMP) Token
 * @dev ERC20 token with a fixed supply of 420 trillion tokens and 0% tax.
 */
contract SimpsonTrumpToken is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 420_000_000_000_000 * 10**18; // 420 trillion tokens

    /**
     * @dev Constructor that mints the total supply to the deployer.
     */
    constructor() ERC20("Simpson Trump", "TRUMP") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Overrides the ERC20 transfer function to enforce 0% tax.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides the ERC20 transferFrom function to enforce 0% tax.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }
}
```
