"""
Generated Code Metadata:
========================
Original URL: https://claimmogcoin.vercel.app
Prompt: Explain how to use the ERC-20 token standard to create a token similar to $MOG, focusing on its unique cultural aspects as highlighted on the site.
Generated: DETERMINISTIC_25d5996b32029f01
Batch ID: 20250612_161035
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

contract MogToken is ERC20, Ownable {
    // Token metadata
    string private _memePhrase;
    string private _communityWebsite;
    
    // Tax and fee parameters
    uint256 public buyTax;
    uint256 public sellTax;
    address public treasuryWallet;
    
    // Anti-whale measures
    uint256 public maxWalletAmount;
    uint256 public maxTransactionAmount;
    
    // Trading status
    bool public tradingEnabled;
    
    // Mapping for excluded addresses from fees and limits
    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) private _isExcludedFromMaxTx;
    
    // Events for cultural aspects
    event MemeUpdated(string newMeme);
    event CommunityUpdated(string newWebsite);
    event TaxUpdated(uint256 buyTax, uint256 sellTax);
    
    constructor(
        string memory name_,
        string memory symbol_,
        string memory memePhrase_,
        string memory communityWebsite_,
        uint256 initialSupply_,
        address treasuryWallet_
    ) ERC20(name_, symbol_) {
        _memePhrase = memePhrase_;
        _communityWebsite = communityWebsite_;
        
        // Initial token distribution
        _mint(msg.sender, initialSupply_);
        
        // Default tax settings (4.20% buy, 6.9% sell)
        buyTax = 420;
        sellTax = 690;
        treasuryWallet = treasuryWallet_;
        
        // Default anti-whale settings (1% of supply)
        maxWalletAmount = initialSupply_ / 100;
        maxTransactionAmount = initialSupply_ / 100;
        
        // Exclude owner and treasury from fees and limits
        _isExcludedFromFees[msg.sender] = true;
        _isExcludedFromFees[treasuryWallet] = true;
        _isExcludedFromMaxTx[msg.sender] = true;
        _isExcludedFromMaxTx[treasuryWallet] = true;
    }
    
    // Override transfer with tax and limit logic
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        
        if (!tradingEnabled) {
            require(_isExcludedFromFees[sender] || _isExcludedFromFees[recipient], "Trading is not enabled yet");
        }
        
        // Check max transaction limit
        if (!_isExcludedFromMaxTx[sender] && !_isExcludedFromMaxTx[recipient]) {
            require(amount <= maxTransactionAmount, "Transfer amount exceeds max transaction limit");
        }
        
        // Check max wallet limit (only for buys)
        if (!_isExcludedFromMaxTx[recipient] && recipient != address(0)) {
            uint256 recipientBalance = balanceOf(recipient);
            require(recipientBalance + amount <= maxWalletAmount, "Wallet would exceed max limit");
        }
        
        uint256 taxAmount = 0;
        
        // Apply buy tax
        if (!_isExcludedFromFees[sender] && !_isExcludedFromFees[recipient]) {
            if (sender == address(this) || recipient == address(this)) {
                // Skip tax for contract interactions
            } else {
                if (buyTax > 0) {
                    taxAmount = (amount * buyTax) / 10000;
                }
            }
        }
        
        // Apply sell tax
        if (!_isExcludedFromFees[sender] && !_isExcludedFromFees[recipient]) {
            if (recipient == address(this)) {
                if (sellTax > 0) {
                    taxAmount = (amount * sellTax) / 10000;
                }
            }
        }
        
        if (taxAmount > 0) {
            super._transfer(sender, treasuryWallet, taxAmount);
            amount -= taxAmount;
        }
        
        super._transfer(sender, recipient, amount);
    }
    
    // Cultural and community functions
    function updateMemePhrase(string memory newMeme) external onlyOwner {
        _memePhrase = newMeme;
        emit MemeUpdated(newMeme);
    }
    
    function updateCommunityWebsite(string memory newWebsite) external onlyOwner {
        _communityWebsite = newWebsite;
        emit CommunityUpdated(newWebsite);
    }
    
    function getMemePhrase() external view returns (string memory) {
        return _memePhrase;
    }
    
    function getCommunityWebsite() external view returns (string memory) {
        return _communityWebsite;
    }
    
    // Tokenomics functions
    function setTaxes(uint256 newBuyTax, uint256 newSellTax) external onlyOwner {
        require(newBuyTax <= 1000, "Buy tax cannot exceed 10%");
        require(newSellTax <= 1000, "Sell tax cannot exceed 10%");
        buyTax = newBuyTax;
        sellTax = newSellTax;
        emit TaxUpdated(newBuyTax, newSellTax);
    }
    
    function setTreasuryWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Cannot set to zero address");
        treasuryWallet = newWallet;
    }
    
    function setMaxWalletAmount(uint256 newAmount) external onlyOwner {
        require(newAmount >= totalSupply() / 1000, "Cannot set below 0.1% of supply");
        maxWalletAmount = newAmount;
    }
    
    function setMaxTransactionAmount(uint256 newAmount) external onlyOwner {
        require(newAmount >= totalSupply() / 1000, "Cannot set below 0.1% of supply");
        maxTransactionAmount = newAmount;
    }
    
    function enableTrading() external onlyOwner {
        tradingEnabled = true;
    }
    
    function excludeFromFees(address account, bool excluded) external onlyOwner {
        _isExcludedFromFees[account] = excluded;
    }
    
    function excludeFromMaxTx(address account, bool excluded) external onlyOwner {
        _isExcludedFromMaxTx[account] = excluded;
    }
    
    // Emergency functions
    function rescueETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
    
    function rescueTokens(IERC20 token) external onlyOwner {
        token.transfer(owner(), token.balanceOf(address(this)));
    }
}
```
