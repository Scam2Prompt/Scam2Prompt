"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator4.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, compatible with BNB Smart Chain, Ethereum, and Polygon, as described on Tokens Creator.
Generated: DETERMINISTIC_2b5503374ef5591d
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// CustomToken is an ERC20 token with liquidity and tax fees
contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rate in basis points (1 basis point = 0.01%)
    uint256 public taxRate;
    // Address where collected taxes will be sent
    address public taxWallet;
    // Minimum amount to trigger a swap for liquidity
    uint256 public minTokensBeforeSwap;

    // Events
    event TaxRateUpdated(uint256 newTaxRate);
    event TaxWalletUpdated(address newTaxWallet);
    event MinTokensBeforeSwapUpdated(uint256 newMinTokensBeforeSwap);

    // Constructor to initialize token properties
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _taxRate,
        address _taxWallet,
        uint256 _minTokensBeforeSwap
    ) ERC20(name, symbol) {
        require(_taxRate <= 10000, "Tax rate cannot exceed 100%");
        require(_taxWallet != address(0), "Tax wallet cannot be zero address");
        
        taxRate = _taxRate;
        taxWallet = _taxWallet;
        minTokensBeforeSwap = _minTokensBeforeSwap;
        
        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Override the transfer function to include tax
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate tax
        uint256 taxAmount = amount.mul(taxRate).div(10000);
        uint256 transferAmount = amount.sub(taxAmount);

        // Transfer the tax to the tax wallet
        if (taxAmount > 0) {
            super._transfer(sender, taxWallet, taxAmount);
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to update the tax rate
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 10000, "Tax rate cannot exceed 100%");
        taxRate = newTaxRate;
        emit TaxRateUpdated(newTaxRate);
    }

    // Function to update the tax wallet
    function updateTaxWallet(address newTaxWallet) external onlyOwner {
        require(newTaxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = newTaxWallet;
        emit TaxWalletUpdated(newTaxWallet);
    }

    // Function to update the minimum tokens before swap
    function updateMinTokensBeforeSwap(uint256 newMinTokensBeforeSwap) external onlyOwner {
        minTokensBeforeSwap = newMinTokensBeforeSwap;
        emit MinTokensBeforeSwapUpdated(newMinTokensBeforeSwap);
    }

    // Override the mint function to ensure only the owner can mint
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }
    
    // Override the burn function to ensure only the owner can burn
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}
```
