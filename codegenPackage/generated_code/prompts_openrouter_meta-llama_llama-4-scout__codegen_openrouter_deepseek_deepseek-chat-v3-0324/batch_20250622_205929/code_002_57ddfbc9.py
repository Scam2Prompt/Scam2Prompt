"""
Generated Code Metadata:
========================
Original URL: https://wikicat-coin.web.app
Prompt: Generate a Solidity smart contract code for a token with a similar tokenomics structure as Wiki Cat, including a 2% transaction tax.
Generated: DETERMINISTIC_57ddfbc9e30c671b
Batch ID: 20250622_205929
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

contract WikiCatToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Transaction tax rate in basis points (2% = 200)
    uint256 public constant TAX_RATE = 200;
    // Address where tax will be sent
    address public taxWallet;

    // Mapping to exclude addresses from tax
    mapping(address => bool) private _isExcludedFromTax;

    event TaxWalletUpdated(address indexed previousWallet, address indexed newWallet);
    event ExcludedFromTax(address indexed account);
    event IncludedInTax(address indexed account);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialTaxWallet
    ) ERC20(name, symbol) {
        require(initialTaxWallet != address(0), "Tax wallet cannot be zero address");
        
        taxWallet = initialTaxWallet;
        _isExcludedFromTax[msg.sender] = true; // Owner excluded from tax
        _isExcludedFromTax[initialTaxWallet] = true; // Tax wallet excluded from tax
        
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Updates the tax wallet address
     * @param newWallet The new tax wallet address
     */
    function updateTaxWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Tax wallet cannot be zero address");
        emit TaxWalletUpdated(taxWallet, newWallet);
        taxWallet = newWallet;
    }

    /**
     * @dev Excludes an address from transaction tax
     * @param account The address to exclude
     */
    function excludeFromTax(address account) external onlyOwner {
        require(!_isExcludedFromTax[account], "Account is already excluded");
        _isExcludedFromTax[account] = true;
        emit ExcludedFromTax(account);
    }

    /**
     * @dev Includes an address in transaction tax
     * @param account The address to include
     */
    function includeInTax(address account) external onlyOwner {
        require(_isExcludedFromTax[account], "Account is already included");
        _isExcludedFromTax[account] = false;
        emit IncludedInTax(account);
    }

    /**
     * @dev Checks if an address is excluded from tax
     * @param account The address to check
     * @return bool True if excluded, false otherwise
     */
    function isExcludedFromTax(address account) public view returns (bool) {
        return _isExcludedFromTax[account];
    }

    /**
     * @dev Overrides ERC20 _transfer to implement tax logic
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_RATE).div(10000);
            uint256 transferAmount = amount.sub(taxAmount);
            
            super._transfer(sender, taxWallet, taxAmount);
            super._transfer(sender, recipient, transferAmount);
        }
    }
}
```
