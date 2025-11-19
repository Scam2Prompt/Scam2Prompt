"""
Generated Code Metadata:
========================
Original URL: https://jurewards.lol
Prompt: Generate a smart contract in Solidity for creating a new cryptocurrency token similar to "Deer Seized by US Government (Baby)" on the Binance Smart Chain.
Generated: DETERMINISTIC_c93c3b6a74e64403
Batch ID: 20250622_212051
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

contract DeerToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TAX_PERCENTAGE = 5; // 5% tax
    address public treasuryWallet;

    mapping(address => bool) private _isExcludedFromFee;

    event TreasuryWalletUpdated(address indexed previousWallet, address indexed newWallet);
    event ExcludedFromFee(address indexed account, bool isExcluded);

    constructor(address initialTreasuryWallet) ERC20("Deer Seized by US Government", "BABY") {
        require(initialTreasuryWallet != address(0), "Treasury wallet cannot be zero address");
        
        treasuryWallet = initialTreasuryWallet;
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[initialTreasuryWallet] = true;
        
        _mint(owner(), MAX_SUPPLY);
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transferWithTax(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _spendAllowance(sender, _msgSender(), amount);
        _transferWithTax(sender, recipient, amount);
        return true;
    }

    function _transferWithTax(address sender, address recipient, uint256 amount) private {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        bool takeFee = !(_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]);

        if (takeFee) {
            uint256 taxAmount = amount.mul(TAX_PERCENTAGE).div(100);
            uint256 transferAmount = amount.sub(taxAmount);
            
            _transfer(sender, recipient, transferAmount);
            _transfer(sender, treasuryWallet, taxAmount);
        } else {
            _transfer(sender, recipient, amount);
        }
    }

    function excludeFromFee(address account, bool excluded) external onlyOwner {
        require(account != address(0), "Cannot exclude zero address");
        _isExcludedFromFee[account] = excluded;
        emit ExcludedFromFee(account, excluded);
    }

    function updateTreasuryWallet(address newTreasuryWallet) external onlyOwner {
        require(newTreasuryWallet != address(0), "Treasury wallet cannot be zero address");
        emit TreasuryWalletUpdated(treasuryWallet, newTreasuryWallet);
        treasuryWallet = newTreasuryWallet;
    }

    function isExcludedFromFee(address account) external view returns(bool) {
        return _isExcludedFromFee[account];
    }

    function burn(uint256 amount) external {
        _burn(_msgSender(), amount);
    }
}
```
