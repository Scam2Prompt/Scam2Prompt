"""
Generated Code Metadata:
========================
Original URL: https://supertruimpcoin.xyz
Prompt: Write a smart contract in Solidity for a tokenomics system with a 0.3% tax, 0.8% allocation to a specific wallet, and a total supply of 2.6 billion tokens.
Generated: DETERMINISTIC_460fdb2247212b48
Batch ID: 20250622_205836
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

contract TaxToken is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY = 2_600_000_000 * 10**18;
    uint256 public constant TAX_PERCENT = 3; // 0.3%
    uint256 public constant ALLOCATION_PERCENT = 8; // 0.8%
    address public immutable allocationWallet;

    mapping(address => bool) private _isExcludedFromTax;

    event TaxCollected(address indexed from, address indexed to, uint256 amount);
    event AllocationSent(address indexed wallet, uint256 amount);

    constructor(address _allocationWallet) ERC20("TaxToken", "TAX") {
        require(_allocationWallet != address(0), "Allocation wallet cannot be zero address");
        allocationWallet = _allocationWallet;
        _mint(msg.sender, TOTAL_SUPPLY);
        _isExcludedFromTax[msg.sender] = true;
        _isExcludedFromTax[_allocationWallet] = true;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (_isExcludedFromTax[_msgSender()] || _isExcludedFromTax[recipient]) {
            _transfer(_msgSender(), recipient, amount);
        } else {
            uint256 taxAmount = (amount * TAX_PERCENT) / 1000;
            uint256 allocationAmount = (amount * ALLOCATION_PERCENT) / 1000;
            uint256 transferAmount = amount - taxAmount - allocationAmount;

            _transfer(_msgSender(), recipient, transferAmount);
            _transfer(_msgSender(), allocationWallet, allocationAmount);
            _burn(_msgSender(), taxAmount);

            emit TaxCollected(_msgSender(), recipient, taxAmount);
            emit AllocationSent(allocationWallet, allocationAmount);
        }
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            _transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * TAX_PERCENT) / 1000;
            uint256 allocationAmount = (amount * ALLOCATION_PERCENT) / 1000;
            uint256 transferAmount = amount - taxAmount - allocationAmount;

            _transfer(sender, recipient, transferAmount);
            _transfer(sender, allocationWallet, allocationAmount);
            _burn(sender, taxAmount);

            emit TaxCollected(sender, recipient, taxAmount);
            emit AllocationSent(allocationWallet, allocationAmount);
        }
        return true;
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
    }

    function isExcludedFromTax(address account) public view returns (bool) {
        return _isExcludedFromTax[account];
    }
}
```
