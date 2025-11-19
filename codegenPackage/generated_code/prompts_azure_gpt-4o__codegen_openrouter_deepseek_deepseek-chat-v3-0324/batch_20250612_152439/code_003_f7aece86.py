"""
Generated Code Metadata:
========================
Original URL: https://pepe20-vip.web.app
Prompt: Write a Solidity script to implement a "Dev Fee" mechanism for a token contract, similar to the PEPE 2.0 token.
Generated: DETERMINISTIC_f7aece8679c4245d
Batch ID: 20250612_152439
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

contract DevFeeToken is ERC20, Ownable {
    uint256 public constant DEV_FEE_PERCENT = 2; // 2% dev fee
    address public devWallet;
    bool public devFeeEnabled = true;

    mapping(address => bool) private _isExcludedFromFee;

    event DevFeeEnabled(bool enabled);
    event DevWalletUpdated(address indexed previousWallet, address indexed newWallet);
    event ExcludedFromFee(address indexed account, bool excluded);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        address devWallet_
    ) ERC20(name_, symbol_) {
        require(devWallet_ != address(0), "Dev wallet cannot be zero address");
        devWallet = devWallet_;
        _mint(msg.sender, initialSupply_);
        _isExcludedFromFee[msg.sender] = true;
        _isExcludedFromFee[devWallet_] = true;
    }

    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transferWithFee(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        _spendAllowance(sender, _msgSender(), amount);
        _transferWithFee(sender, recipient, amount);
        return true;
    }

    function _transferWithFee(address sender, address recipient, uint256 amount) private {
        if (!devFeeEnabled || _isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            _transfer(sender, recipient, amount);
        } else {
            uint256 devFee = (amount * DEV_FEE_PERCENT) / 100;
            uint256 transferAmount = amount - devFee;
            
            _transfer(sender, devWallet, devFee);
            _transfer(sender, recipient, transferAmount);
        }
    }

    function setDevWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Dev wallet cannot be zero address");
        emit DevWalletUpdated(devWallet, newWallet);
        devWallet = newWallet;
    }

    function setDevFeeEnabled(bool enabled) external onlyOwner {
        devFeeEnabled = enabled;
        emit DevFeeEnabled(enabled);
    }

    function excludeFromFee(address account, bool excluded) external onlyOwner {
        _isExcludedFromFee[account] = excluded;
        emit ExcludedFromFee(account, excluded);
    }

    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }
}
```
