"""
Generated Code Metadata:
========================
Original URL: https://ratotheratcoin.com
Prompt: Generate code to deploy a cryptocurrency token named "Rato the Rat" ($RATO) on the Ethereum blockchain, ensuring it matches the specifications provided (e.g., supply, tax settings, and contract address).
Generated: DETERMINISTIC_58e7b0b048770c70
Batch ID: 20250612_154131
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

contract RatoTheRat is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TAX_PERCENT = 5; // 5% tax
    address public constant TAX_WALLET = 0x742d35Cc6634C0532925a3b844Bc454e4438f44e; // Example tax wallet
    
    mapping(address => bool) private _isExcludedFromTax;
    mapping(address => bool) private _isBlacklisted;

    event ExcludedFromTax(address indexed account, bool excluded);
    event Blacklisted(address indexed account, bool blacklisted);
    event TaxCollected(address indexed from, uint256 amount);

    constructor() ERC20("Rato the Rat", "RATO") {
        _mint(msg.sender, MAX_SUPPLY);
        _isExcludedFromTax[msg.sender] = true;
        _isExcludedFromTax[TAX_WALLET] = true;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(!_isBlacklisted[msg.sender], "RATO: Sender is blacklisted");
        require(!_isBlacklisted[recipient], "RATO: Recipient is blacklisted");

        if (_isExcludedFromTax[msg.sender] || _isExcludedFromTax[recipient]) {
            _transfer(msg.sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_PERCENT).div(100);
            uint256 transferAmount = amount.sub(taxAmount);
            
            _transfer(msg.sender, TAX_WALLET, taxAmount);
            _transfer(msg.sender, recipient, transferAmount);
            
            emit TaxCollected(msg.sender, taxAmount);
        }
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(!_isBlacklisted[sender], "RATO: Sender is blacklisted");
        require(!_isBlacklisted[recipient], "RATO: Recipient is blacklisted");

        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            super.transferFrom(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_PERCENT).div(100);
            uint256 transferAmount = amount.sub(taxAmount);
            
            super.transferFrom(sender, TAX_WALLET, taxAmount);
            super.transferFrom(sender, recipient, transferAmount);
            
            emit TaxCollected(sender, taxAmount);
        }
        return true;
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
        emit ExcludedFromTax(account, excluded);
    }

    function blacklist(address account, bool blacklisted) external onlyOwner {
        _isBlacklisted[account] = blacklisted;
        emit Blacklisted(account, blacklisted);
    }

    function isExcludedFromTax(address account) external view returns (bool) {
        return _isExcludedFromTax[account];
    }

    function isBlacklisted(address account) external view returns (bool) {
        return _isBlacklisted[account];
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
