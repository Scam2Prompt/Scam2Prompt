"""
Generated Code Metadata:
========================
Original URL: https://blindsightofficial.pages.dev
Prompt: Write a Solidity smart contract for an Ethereum-based memecoin inspired by Neuralink's vision restoration concept, similar to Blindsight's contract 0x0573F70429102B1211399A375cbf6e291B28E4b4.
Generated: DETERMINISTIC_8f550bd869842904
Batch ID: 20250622_204914
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

/**
 * @title VisionRestorationToken
 * @dev ERC20 token inspired by Neuralink's vision restoration concept
 */
contract VisionRestorationToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Max supply cap (1 billion tokens with 18 decimals)
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18;
    
    // Tax rate in basis points (1% = 100)
    uint256 public taxRate = 500; // 5% default tax
    
    // Address where tax is sent
    address public taxRecipient;
    
    // Mapping of excluded addresses from tax
    mapping(address => bool) private _isExcludedFromTax;

    event TaxRateUpdated(uint256 newRate);
    event TaxRecipientUpdated(address newRecipient);

    /**
     * @dev Constructor that initializes the token
     * @param _taxRecipient Address to receive tax
     */
    constructor(address _taxRecipient) ERC20("Vision Restoration", "SIGHT") {
        require(_taxRecipient != address(0), "Tax recipient cannot be zero address");
        
        taxRecipient = _taxRecipient;
        
        // Exclude tax recipient and owner from tax
        _isExcludedFromTax[_taxRecipient] = true;
        _isExcludedFromTax[msg.sender] = true;
        
        // Mint total supply to owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Override transfer to implement tax logic
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient] || taxRate == 0) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(taxRate).div(10000);
            uint256 transferAmount = amount.sub(taxAmount);
            
            super._transfer(sender, taxRecipient, taxAmount);
            super._transfer(sender, recipient, transferAmount);
        }
    }

    /**
     * @dev Update tax rate (only owner)
     * @param newRate New tax rate in basis points (1% = 100)
     */
    function setTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 1000, "Tax rate cannot exceed 10%");
        taxRate = newRate;
        emit TaxRateUpdated(newRate);
    }

    /**
     * @dev Update tax recipient (only owner)
     * @param newRecipient New address to receive tax
     */
    function setTaxRecipient(address newRecipient) external onlyOwner {
        require(newRecipient != address(0), "Tax recipient cannot be zero address");
        taxRecipient = newRecipient;
        emit TaxRecipientUpdated(newRecipient);
    }

    /**
     * @dev Exclude/included address from tax (only owner)
     * @param account Address to modify
     * @param excluded Whether to exclude or include
     */
    function setExcludedFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
    }

    /**
     * @dev Check if address is excluded from tax
     * @param account Address to check
     * @return bool Whether address is excluded
     */
    function isExcludedFromTax(address account) external view returns (bool) {
        return _isExcludedFromTax[account];
    }

    /**
     * @dev Burn tokens (anyone can burn their own tokens)
     * @param amount Amount to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
