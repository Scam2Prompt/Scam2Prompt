"""
Generated Code Metadata:
========================
Original URL: https://bengonbase-xyz.pages.dev
Prompt: Write a Solidity smart contract for a meme token called $BENG on the Base blockchain with a total supply of 10 billion tokens and 0% tax.
Generated: DETERMINISTIC_e04e66965c645238
Batch ID: 20250622_210802
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
 * @title $BENG Token Contract
 * @dev ERC20 token with 10 billion total supply and 0% tax
 */
contract BENGToken is ERC20, Ownable {
    /**
     * @dev Total supply is set to 10 billion tokens with 18 decimals
     */
    uint256 public constant TOTAL_SUPPLY = 10_000_000_000 * 10**18;

    /**
     * @dev Constructor mints the total supply to the deployer's address
     */
    constructor() ERC20("BENG", "BENG") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Overrides the transfer function to ensure no tax/fee logic
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides the transferFrom function to ensure no tax/fee logic
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }
}
```
