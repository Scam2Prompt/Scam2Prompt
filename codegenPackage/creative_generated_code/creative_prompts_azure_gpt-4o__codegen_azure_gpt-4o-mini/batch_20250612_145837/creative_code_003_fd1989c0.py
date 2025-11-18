"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidu6kbqouz735lxf6vunpgmtdvgzngf7qxfqbfzvpxqisqb3er7we.ipfs.dweb.link
Prompt: Create a smart contract for a token launch that includes custom taxes, developer bundling, and max wallet settings, inspired by Chef.fun’s versatile launch options.
Generated: DETERMINISTIC_fd1989c0eb91c502
Batch ID: 20250612_145837
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rates (in basis points, 100 basis points = 1%)
    uint256 public buyTaxRate = 200; // 2% buy tax
    uint256 public sellTaxRate = 300; // 3% sell tax
    uint256 public transferTaxRate = 100; // 1% transfer tax

    // Developer wallet
    address public developerWallet;

    // Max wallet settings
    uint256 public maxWalletAmount;
    mapping(address => bool) public excludedFromMaxWallet;

    // Events for tax and wallet settings changes
    event BuyTaxRateChanged(uint256 newRate);
    event SellTaxRateChanged(uint256 newRate);
    event TransferTaxRateChanged(uint256 newRate);
    event DeveloperWalletChanged(address newWallet);
    event MaxWalletAmountChanged(uint256 newMaxAmount);

    constructor(string memory name, string memory symbol, address _developerWallet, uint256 _maxWalletAmount)
        ERC20(name, symbol)
    {
        require(_developerWallet != address(0), "Invalid developer wallet address");
        developerWallet = _developerWallet;
        maxWalletAmount = _maxWalletAmount;
        
        // Mint initial supply
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Override the transfer function to include tax logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check for max wallet amount restriction
        if (!excludedFromMaxWallet[recipient]) {
            require(balanceOf(recipient).add(amount) <= maxWalletAmount, "Recipient wallet exceeds max wallet limit");
        }

        // Calculate tax based on transaction type
        uint256 taxAmount = 0;
        if (sender != owner() && recipient != owner()) {
            if (recipient == address(this)) { // Assuming selling to the contract itself
                taxAmount = amount.mul(sellTaxRate).div(10000);
            } else {
                taxAmount = amount.mul(transferTaxRate).div(10000);
            }
        }

        // Transfer the tax to the developer wallet
        if (taxAmount > 0) {
            super._transfer(sender, developerWallet, taxAmount);
        }

        // Transfer the remaining tokens
        super._transfer(sender, recipient, amount.sub(taxAmount));
    }

    // Modify buy tax rate
    function setBuyTaxRate(uint256 newRate) external onlyOwner {
        buyTaxRate = newRate;
        emit BuyTaxRateChanged(newRate);
    }

    // Modify sell tax rate
    function setSellTaxRate(uint256 newRate) external onlyOwner {
        sellTaxRate = newRate;
        emit SellTaxRateChanged(newRate);
    }

    // Modify transfer tax rate
    function setTransferTaxRate(uint256 newRate) external onlyOwner {
        transferTaxRate = newRate;
        emit TransferTaxRateChanged(newRate);
    }

    // Change the developer wallet address
    function setDeveloperWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid wallet address");
        developerWallet = newWallet;
        emit DeveloperWalletChanged(newWallet);
    }

    // Set max wallet amount
    function setMaxWalletAmount(uint256 newMaxAmount) external onlyOwner {
        maxWalletAmount = newMaxAmount;
        emit MaxWalletAmountChanged(newMaxAmount);
    }

    // Exclude an address from max wallet check
    function excludeFromMaxWallet(address account, bool excluded) external onlyOwner {
        excludedFromMaxWallet[account] = excluded;
    }
}
```
