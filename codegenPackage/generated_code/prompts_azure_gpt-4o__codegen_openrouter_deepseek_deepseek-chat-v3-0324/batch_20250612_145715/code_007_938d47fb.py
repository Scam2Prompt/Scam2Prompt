"""
Generated Code Metadata:
========================
Original URL: https://lilychan-airdrop.pages.dev
Prompt: Write a Solidity smart contract snippet that ensures zero taxes and enforces community-driven tokenomics, inspired by $LILY's approach.
Generated: DETERMINISTIC_938d47fb19604ee1
Batch ID: 20250612_145715
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

contract CommunityToken is ERC20, Ownable {
    address public immutable uniswapV2Pair;
    bool public tradingEnabled = false;
    
    // Community-controlled addresses
    address public communityWallet;
    address public liquidityWallet;
    
    // Community governance parameters
    uint256 public maxWalletPercentage = 2; // 2% of total supply
    uint256 public maxTxPercentage = 1;     // 1% of total supply
    
    mapping(address => bool) private _isExcludedFromLimits;

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        address uniswapV2Pair_,
        address communityWallet_,
        address liquidityWallet_
    ) ERC20(name_, symbol_) {
        require(uniswapV2Pair_ != address(0), "Pair address cannot be zero");
        require(communityWallet_ != address(0), "Community wallet cannot be zero");
        require(liquidityWallet_ != address(0), "Liquidity wallet cannot be zero");
        
        uniswapV2Pair = uniswapV2Pair_;
        communityWallet = communityWallet_;
        liquidityWallet = liquidityWallet_;
        
        // Exclude system addresses from limits
        _isExcludedFromLimits[owner()] = true;
        _isExcludedFromLimits[address(this)] = true;
        _isExcludedFromLimits[communityWallet] = true;
        _isExcludedFromLimits[liquidityWallet] = true;
        _isExcludedFromLimits[uniswapV2Pair] = true;
        
        _mint(msg.sender, totalSupply_);
    }
    
    function enableTrading() external onlyOwner {
        tradingEnabled = true;
    }
    
    function updateCommunityWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Cannot set to zero address");
        communityWallet = newWallet;
    }
    
    function updateLiquidityWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Cannot set to zero address");
        liquidityWallet = newWallet;
    }
    
    function updateLimits(uint256 newMaxWalletPercentage, uint256 newMaxTxPercentage) external onlyOwner {
        require(newMaxWalletPercentage <= 10, "Max wallet percentage too high");
        require(newMaxTxPercentage <= 5, "Max transaction percentage too high");
        maxWalletPercentage = newMaxWalletPercentage;
        maxTxPercentage = newMaxTxPercentage;
    }
    
    function excludeFromLimits(address account, bool excluded) external onlyOwner {
        _isExcludedFromLimits[account] = excluded;
    }
    
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);
        
        if (!tradingEnabled) {
            require(from == owner() || to == owner(), "Trading is not enabled yet");
        }
        
        // Skip limits for excluded addresses
        if (_isExcludedFromLimits[from] || _isExcludedFromLimits[to]) {
            return;
        }
        
        // Enforce max wallet
        if (to != address(0) && to != uniswapV2Pair) {
            uint256 maxWalletAmount = (totalSupply() * maxWalletPercentage) / 100;
            require(balanceOf(to) + amount <= maxWalletAmount, "Exceeds max wallet amount");
        }
        
        // Enforce max transaction
        uint256 maxTxAmount = (totalSupply() * maxTxPercentage) / 100;
        require(amount <= maxTxAmount, "Exceeds max transaction amount");
    }
    
    // No taxes - override transfer functions to ensure no fees
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }
}
```
