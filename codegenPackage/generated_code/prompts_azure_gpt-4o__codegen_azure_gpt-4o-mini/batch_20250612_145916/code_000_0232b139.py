"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, similar to the functionality described on Tokens Creator, ensuring 100% token ownership.
Generated: DETERMINISTIC_0232b139356601b6
Batch ID: 20250612_145916
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

contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax fee in basis points (1 basis point = 0.01%)
    uint256 public taxFee;
    // Address where tax fees will be sent
    address public taxWallet;

    // Events
    event TaxFeeUpdated(uint256 newTaxFee);
    event TaxWalletUpdated(address newTaxWallet);

    // Constructor to initialize the token
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _taxFee,
        address _taxWallet
    ) ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(_taxFee <= 1000, "Tax fee must be less than or equal to 10%");
        require(_taxWallet != address(0), "Tax wallet cannot be the zero address");

        taxFee = _taxFee;
        taxWallet = _taxWallet;

        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Override the transfer function to include tax fee
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        // Calculate tax amount
        uint256 taxAmount = amount.mul(taxFee).div(10000);
        uint256 amountAfterTax = amount.sub(taxAmount);

        // Transfer tax to tax wallet
        super._transfer(sender, taxWallet, taxAmount);
        // Transfer remaining amount to recipient
        super._transfer(sender, recipient, amountAfterTax);
    }

    // Function to update the tax fee
    function updateTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 1000, "Tax fee must be less than or equal to 10%");
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    // Function to update the tax wallet address
    function updateTaxWallet(address newTaxWallet) external onlyOwner {
        require(newTaxWallet != address(0), "Tax wallet cannot be the zero address");
        taxWallet = newTaxWallet;
        emit TaxWalletUpdated(newTaxWallet);
    }
}
```
