"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Write a smart contract function to distribute transaction taxes (1% LP, 2% marketing, 2% dev) for Baby Grok tokens.
Generated: DETERMINISTIC_9e217efa43e20b1c
Batch ID: 20250612_150028
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

contract BabyGrok is ERC20, Ownable {
    address public lpWallet;
    address public marketingWallet;
    address public devWallet;
    
    uint256 public constant LP_TAX = 1;
    uint256 public constant MARKETING_TAX = 2;
    uint256 public constant DEV_TAX = 2;
    uint256 public constant TAX_DENOMINATOR = 100;
    
    bool public taxEnabled = true;
    
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _lpWallet,
        address _marketingWallet,
        address _devWallet
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        lpWallet = _lpWallet;
        marketingWallet = _marketingWallet;
        devWallet = _devWallet;
    }
    
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (taxEnabled && sender != owner() && recipient != owner()) {
            uint256 lpTax = (amount * LP_TAX) / TAX_DENOMINATOR;
            uint256 marketingTax = (amount * MARKETING_TAX) / TAX_DENOMINATOR;
            uint256 devTax = (amount * DEV_TAX) / TAX_DENOMINATOR;
            uint256 totalTax = lpTax + marketingTax + devTax;
            
            if (totalTax > 0) {
                super._transfer(sender, address(this), totalTax);
                _distributeTaxes(lpTax, marketingTax, devTax);
            }
            
            uint256 transferAmount = amount - totalTax;
            super._transfer(sender, recipient, transferAmount);
        } else {
            super._transfer(sender, recipient, amount);
        }
    }
    
    function _distributeTaxes(
        uint256 lpAmount,
        uint256 marketingAmount,
        uint256 devAmount
    ) private {
        if (lpAmount > 0 && lpWallet != address(0)) {
            super._transfer(address(this), lpWallet, lpAmount);
        }
        if (marketingAmount > 0 && marketingWallet != address(0)) {
            super._transfer(address(this), marketingWallet, marketingAmount);
        }
        if (devAmount > 0 && devWallet != address(0)) {
            super._transfer(address(this), devWallet, devAmount);
        }
    }
    
    function setTaxWallets(
        address _lpWallet,
        address _marketingWallet,
        address _devWallet
    ) external onlyOwner {
        require(
            _lpWallet != address(0) &&
            _marketingWallet != address(0) &&
            _devWallet != address(0),
            "Invalid wallet address"
        );
        lpWallet = _lpWallet;
        marketingWallet = _marketingWallet;
        devWallet = _devWallet;
    }
    
    function setTaxEnabled(bool _enabled) external onlyOwner {
        taxEnabled = _enabled;
    }
    
    function withdrawStuckTokens(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }
}
```
