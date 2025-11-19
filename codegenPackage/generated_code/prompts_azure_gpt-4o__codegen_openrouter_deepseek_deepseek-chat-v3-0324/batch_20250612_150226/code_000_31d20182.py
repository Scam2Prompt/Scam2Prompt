"""
Generated Code Metadata:
========================
Original URL: https://basednormus.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency token similar to `$NORMUS` on the BASE blockchain, ensuring features like renounced ownership, 0% tax, and 100% locked liquidity.
Generated: DETERMINISTIC_31d2018222317f50
Batch ID: 20250612_150226
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

contract NormusToken is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    address public immutable liquidityPool;

    constructor(address _liquidityPool) ERC20("Normus", "NORMUS") {
        require(_liquidityPool != address(0), "Liquidity pool cannot be zero address");
        liquidityPool = _liquidityPool;
        _mint(msg.sender, TOTAL_SUPPLY);
        renounceOwnership(); // Immediately renounce ownership after deployment
    }

    // Override transfer functions to ensure 0% tax
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    // Lock liquidity by preventing transfers to the liquidity pool except during initial mint
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        
        if (from != address(0) && to == liquidityPool) {
            revert("Liquidity is locked and cannot be modified");
        }
    }
}
```
