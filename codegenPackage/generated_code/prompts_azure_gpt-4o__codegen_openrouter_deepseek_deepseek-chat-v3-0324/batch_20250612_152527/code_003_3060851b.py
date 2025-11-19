"""
Generated Code Metadata:
========================
Original URL: https://yooshi-io.pages.dev
Prompt: Generate a smart contract on Binance Smart Chain that implements a burning mechanism similar to YooShi's Black Hole algorithm, where a percentage of transaction fees is sent to a burn address.
Generated: DETERMINISTIC_3060851b89782dde
Batch ID: 20250612_152527
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

contract BurnToken is ERC20, Ownable {
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    uint256 public burnFeePercent = 5; // 5% of each transaction will be burned
    uint256 public constant PERCENT_DIVISOR = 100;
    
    mapping(address => bool) private _isExcludedFromFees;

    event Burn(address indexed sender, uint256 amount);
    event FeeUpdated(uint256 newFee);
    event ExcludedFromFees(address indexed account, bool excluded);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply_ * 10 ** decimals());
        _isExcludedFromFees[msg.sender] = true;
        _isExcludedFromFees[BURN_ADDRESS] = true;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transferWithBurn(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _spendAllowance(sender, _msgSender(), amount);
        _transferWithBurn(sender, recipient, amount);
        return true;
    }

    function _transferWithBurn(address sender, address recipient, uint256 amount) private {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        uint256 burnAmount = 0;
        if (!_isExcludedFromFees[sender] && !_isExcludedFromFees[recipient]) {
            burnAmount = (amount * burnFeePercent) / PERCENT_DIVISOR;
        }

        if (burnAmount > 0) {
            super._transfer(sender, BURN_ADDRESS, burnAmount);
            emit Burn(sender, burnAmount);
        }

        super._transfer(sender, recipient, amount - burnAmount);
    }

    function setBurnFeePercent(uint256 newFee) external onlyOwner {
        require(newFee <= 20, "Fee cannot be more than 20%");
        burnFeePercent = newFee;
        emit FeeUpdated(newFee);
    }

    function excludeFromFees(address account, bool excluded) external onlyOwner {
        require(account != address(0), "Cannot exclude zero address");
        _isExcludedFromFees[account] = excluded;
        emit ExcludedFromFees(account, excluded);
    }

    function isExcludedFromFees(address account) public view returns (bool) {
        return _isExcludedFromFees[account];
    }
}
```
