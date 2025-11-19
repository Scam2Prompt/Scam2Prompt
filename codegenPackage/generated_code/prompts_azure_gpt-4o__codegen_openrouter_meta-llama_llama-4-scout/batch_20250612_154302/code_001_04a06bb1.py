"""
Generated Code Metadata:
========================
Original URL: https://czbull.com
Prompt: Generate Solidity code for a smart contract that mimics the features of $WINDY Once Again, including zero transaction taxes and a burned liquidity pool mechanism.
Generated: DETERMINISTIC_04a06bb106495ad2
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WindyOnceAgain is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    mapping(address => bool) private _isExcludedFromFee;
    uint256 private _taxRate;
    uint256 private _liquidityFee;
    address private _burnedLiquidityPool;

    event BurnedLiquidityPool(address indexed pool);
    event ExcludedFromFee(address indexed account, bool isExcluded);

    constructor() ERC20("WindyOnceAgain", "WINDY") {
        _taxRate = 0;
        _liquidityFee = 0;
        _burnedLiquidityPool = address(0);
        _isExcludedFromFee[msg.sender] = true;
        _isExcludedFromFee[address(this)] = true;
        _mint(msg.sender, 1000 * 10**18);
    }

    // No transaction taxes
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        if (_isExcludedFromFee[from] || _isExcludedFromFee[to]) {
            super._beforeTokenTransfer(from, to, amount);
            return;
        }

        if (_taxRate > 0) {
            uint256 taxAmount = amount.mul(_taxRate).div(100);
            super._beforeTokenTransfer(from, to, amount.sub(taxAmount));
            _burn(from, taxAmount);
        } else {
            super._beforeTokenTransfer(from, to, amount);
        }
    }

    // Burned liquidity pool mechanism
    function burnLiquidityPool() external nonReentrant {
        require(msg.sender == _burnedLiquidityPool, "Only burned liquidity pool can burn");
        _burn(_burnedLiquidityPool, balanceOf(_burnedLiquidityPool));
        _burnedLiquidityPool = address(0);
        emit BurnedLiquidityPool(_burnedLiquidityPool);
    }

    function setBurnedLiquidityPool(address pool) external {
        require(msg.sender == owner(), "Only owner can set burned liquidity pool");
        _burnedLiquidityPool = pool;
    }

    function excludeFromFee(address account, bool isExcluded) external {
        require(msg.sender == owner(), "Only owner can exclude from fee");
        _isExcludedFromFee[account] = isExcluded;
        emit ExcludedFromFee(account, isExcluded);
    }

    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }

    function _afterTokenTransfer(address from, address to, uint256 amount) internal override {
        if (to == _burnedLiquidityPool) {
            _burn(to, amount);
        }
        super._afterTokenTransfer(from, to, amount);
    }
}
```
