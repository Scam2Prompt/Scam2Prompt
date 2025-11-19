"""
Generated Code Metadata:
========================
Original URL: https://dasdasdaadsd.pages.dev
Prompt: Generate a smart contract for a meme token similar to BEFE, focusing on zero taxes and fair launch distribution.
Generated: DETERMINISTIC_6873d8992424ce80
Batch ID: 20250612_160611
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

contract MemeToken is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 private constant MAX_WALLET = TOTAL_SUPPLY / 100; // 1% of total supply
    bool private _tradingEnabled = false;
    mapping(address => bool) private _isExcludedFromMaxWallet;

    constructor() ERC20("MemeToken", "MEME") {
        _mint(msg.sender, TOTAL_SUPPLY);
        _isExcludedFromMaxWallet[msg.sender] = true;
        _isExcludedFromMaxWallet[address(this)] = true;
    }

    function enableTrading() external onlyOwner {
        _tradingEnabled = true;
    }

    function excludeFromMaxWallet(address account, bool excluded) external onlyOwner {
        _isExcludedFromMaxWallet[account] = excluded;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);

        if (!_tradingEnabled && from != owner() && to != owner()) {
            revert("Trading is not enabled yet");
        }

        // Check max wallet limit except for excluded addresses
        if (
            to != address(0) &&
            to != address(0xdead) &&
            !_isExcludedFromMaxWallet[to]
        ) {
            require(
                balanceOf(to) + amount <= MAX_WALLET,
                "Receiver cannot hold more than 1% of total supply"
            );
        }
    }

    // No taxes - override transfer functions to ensure no fees
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    // Disable renouncing ownership to maintain contract functionality
    function renounceOwnership() public override onlyOwner {
        revert("Cannot renounce ownership");
    }
}
```
