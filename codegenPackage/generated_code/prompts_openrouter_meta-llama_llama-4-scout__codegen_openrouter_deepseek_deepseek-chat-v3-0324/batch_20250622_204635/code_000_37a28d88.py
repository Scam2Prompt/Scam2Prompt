"""
Generated Code Metadata:
========================
Original URL: https://uspepe-vip.pages.dev
Prompt: Write a Solidity code snippet for a cryptocurrency token with a contract address similar to 0x07040971246a73ebda9cf29ea1306bb47c7c4e76, incorporating features like 0% taxes and burned liquidity pool.
Generated: DETERMINISTIC_37a28d88a0488c76
Batch ID: 20250622_204635
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

contract ZeroTaxToken is ERC20, Ownable {
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    address public immutable liquidityPool;

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _liquidityPool
    ) ERC20(name, symbol) {
        require(_liquidityPool != address(0), "Liquidity pool cannot be zero address");
        liquidityPool = _liquidityPool;
        _mint(msg.sender, initialSupply);
    }

    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    function burnLiquidityTokens(uint256 amount) external onlyOwner {
        _transfer(liquidityPool, BURN_ADDRESS, amount);
    }

    function renounceOwnership() public override onlyOwner {
        super.renounceOwnership();
    }
}
```
