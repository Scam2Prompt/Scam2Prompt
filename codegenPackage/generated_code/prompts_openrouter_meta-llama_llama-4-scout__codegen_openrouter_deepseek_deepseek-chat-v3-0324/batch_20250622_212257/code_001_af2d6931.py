"""
Generated Code Metadata:
========================
Original URL: https://teddybearprc20.org
Prompt: What are the tokenomics of Teddy Bear ($BEAR) cryptocurrency, and how does its contract renouncement affect its functionality?
Generated: DETERMINISTIC_af2d69311da6df55
Batch ID: 20250622_212257
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

/**
 * @title Teddy Bear Token ($BEAR)
 * @dev Implementation of the Teddy Bear ERC20 token with tokenomics features
 */
contract TeddyBearToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TAX_PERCENTAGE = 5; // 5% tax on transfers
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    
    // Tokenomics addresses
    address public marketingWallet;
    address public developmentWallet;
    address public liquidityWallet;
    
    // Contract state
    bool public isTaxActive = true;
    bool public isTradingEnabled = true;
    
    // Mapping of excluded addresses from tax
    mapping(address => bool) private _isExcludedFromTax;
    
    /**
     * @dev Constructor that initializes the token and mints initial supply
     * @param _marketingWallet Address for marketing funds
     * @param _developmentWallet Address for development funds
     * @param _liquidityWallet Address for liquidity funds
     */
    constructor(
        address _marketingWallet,
        address _developmentWallet,
        address _liquidityWallet
    ) ERC20("Teddy Bear", "BEAR") {
        require(
            _marketingWallet != address(0) &&
            _developmentWallet != address(0) &&
            _liquidityWallet != address(0),
            "Zero address not allowed"
        );
        
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;
        liquidityWallet = _liquidityWallet;
        
        // Exclude tax for special addresses
        _isExcludedFromTax[owner()] = true;
        _isExcludedFromTax[marketingWallet] = true;
        _isExcludedFromTax[developmentWallet] = true;
        _isExcludedFromTax[liquidityWallet] = true;
        _isExcludedFromTax[BURN_ADDRESS] = true;
        _isExcludedFromTax[address(this)] = true;
        
        // Mint initial supply to owner
        _mint(msg.sender, MAX_SUPPLY);
    }
    
    /**
     * @dev Override transfer function to implement tax mechanism
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(isTradingEnabled, "Trading is currently disabled");
        
        if (isTaxActive && !_isExcludedFromTax[sender] && !_isExcludedFromTax[recipient]) {
            uint256 taxAmount = (amount * TAX_PERCENTAGE) / 100;
            uint256 transferAmount = amount - taxAmount;
            
            // Distribute tax
            uint256 burnAmount = taxAmount / 5; // 20% of tax to burn
            uint256 marketingAmount = taxAmount / 5; // 20% to marketing
            uint256 developmentAmount = taxAmount / 5; // 20% to development
            uint256 liquidityAmount = taxAmount - burnAmount - marketingAmount - developmentAmount; // 40% to liquidity
            
            super._transfer(sender, BURN_ADDRESS, burnAmount);
            super._transfer(sender, marketingWallet, marketingAmount);
            super._transfer(sender, developmentWallet, developmentAmount);
            super._transfer(sender, liquidityWallet, liquidityAmount);
            super._transfer(sender, recipient, transferAmount);
        } else {
            super._transfer(sender, recipient, amount);
        }
    }
    
    /**
     * @dev Function to renounce ownership and disable future changes
     */
    function renounceOwnership() public override onlyOwner {
        // Disable tax and trading control before renouncing
        isTaxActive = false;
        isTradingEnabled = true;
        
        // Renounce ownership permanently
        super.renounceOwnership();
    }
    
    /**
     * @dev Function to exclude/included address from tax
     */
    function setExcludedFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
    }
    
    /**
     * @dev Function to toggle tax status
     */
    function toggleTax() external onlyOwner {
        isTaxActive = !isTaxActive;
    }
    
    /**
     * @dev Function to toggle trading status
     */
    function toggleTrading() external onlyOwner {
        isTradingEnabled = !isTradingEnabled;
    }
    
    /**
     * @dev Function to update marketing wallet
     */
    function updateMarketingWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        marketingWallet = newWallet;
    }
    
    /**
     * @dev Function to update development wallet
     */
    function updateDevelopmentWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        developmentWallet = newWallet;
    }
    
    /**
     * @dev Function to update liquidity wallet
     */
    function updateLiquidityWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        liquidityWallet = newWallet;
    }
}
```
