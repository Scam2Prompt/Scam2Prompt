"""
Generated Code Metadata:
========================
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a total supply of 692 billion, inspired by the Crypto Burger project.
Generated: DETERMINISTIC_eae9c693691f67f2
Batch ID: 20250612_155910
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CryptoBurgerToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 private constant TOTAL_SUPPLY = 692_000_000_000 * 10**18;
    uint256 private constant MAX_TX_LIMIT = TOTAL_SUPPLY / 100; // 1% of total supply
    uint256 private constant MAX_WALLET_LIMIT = TOTAL_SUPPLY / 50; // 2% of total supply

    mapping(address => bool) private _isExcludedFromLimits;

    event ExcludedFromLimits(address indexed account, bool excluded);

    constructor() ERC20("CryptoBurger", "BURGER") {
        _mint(msg.sender, TOTAL_SUPPLY);
        _isExcludedFromLimits[msg.sender] = true;
        _isExcludedFromLimits[address(this)] = true;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _validateTransfer(_msgSender(), recipient, amount);
        return super.transfer(recipient, amount);
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _validateTransfer(sender, recipient, amount);
        return super.transferFrom(sender, recipient, amount);
    }

    function _validateTransfer(address sender, address recipient, uint256 amount) private view {
        if (!_isExcludedFromLimits[sender] && !_isExcludedFromLimits[recipient]) {
            require(amount <= MAX_TX_LIMIT, "Transfer amount exceeds max transaction limit");
            require(balanceOf(recipient).add(amount) <= MAX_WALLET_LIMIT, "Transfer would exceed max wallet limit");
        }
    }

    function excludeFromLimits(address account, bool excluded) external onlyOwner {
        require(_isExcludedFromLimits[account] != excluded, "Account is already set to that state");
        _isExcludedFromLimits[account] = excluded;
        emit ExcludedFromLimits(account, excluded);
    }

    function isExcludedFromLimits(address account) external view returns (bool) {
        return _isExcludedFromLimits[account];
    }

    function burn(uint256 amount) external {
        _burn(_msgSender(), amount);
    }
}
```
