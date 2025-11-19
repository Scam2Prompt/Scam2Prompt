"""
Generated Code Metadata:
========================
Original URL: https://spyro-vip.pages.dev
Prompt: Create a guide for deploying a similar ERC-20 token with features like audited contracts, renounced ownership, and locked liquidity, as described on the SPYRO webpage.
Generated: DETERMINISTIC_a5e264986755fad7
Batch ID: 20250612_152422
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract SpyroToken is ERC20, Ownable {
    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;
    
    uint256 public maxTransactionAmount;
    uint256 public maxWalletAmount;
    
    bool private _swapping;
    uint256 public swapTokensAtAmount;
    
    address public marketingWallet;
    address public liquidityWallet;
    
    uint256 public buyTotalFees;
    uint256 public sellTotalFees;
    
    bool public tradingActive = false;
    bool public limitsInEffect = true;
    
    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) private _isExcludedMaxTransactionAmount;
    
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event SetAutomatedMarketMakerPair(address indexed pair, bool indexed value);
    event MarketingWalletUpdated(address indexed newWallet, address indexed oldWallet);
    event LiquidityWalletUpdated(address indexed newWallet, address indexed oldWallet);
    event SwapAndLiquify(uint256 tokensSwapped, uint256 ethReceived, uint256 tokensIntoLiquidity);
    
    constructor() ERC20("SpyroToken", "SPYRO") {
        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D);
        
        excludeFromMaxTransaction(address(_uniswapV2Router), true);
        uniswapV2Router = _uniswapV2Router;
        
        uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory()).createPair(address(this), _uniswapV2Router.WETH());
        excludeFromMaxTransaction(address(uniswapV2Pair), true);
        
        uint256 totalSupply = 1_000_000_000 * 1e18; // 1 billion tokens
        
        maxTransactionAmount = (totalSupply * 1) / 100; // 1% max transaction
        maxWalletAmount = (totalSupply * 2) / 100; // 2% max wallet
        swapTokensAtAmount = (totalSupply * 5) / 10000; // 0.05% swap threshold
        
        buyTotalFees = 5; // 5% buy fee
        sellTotalFees = 5; // 5% sell fee
        
        marketingWallet = owner();
        liquidityWallet = owner();
        
        excludeFromFees(owner(), true);
        excludeFromFees(address(this), true);
        excludeFromFees(address(0xdead), true);
        
        excludeFromMaxTransaction(owner(), true);
        excludeFromMaxTransaction(address(this), true);
        excludeFromMaxTransaction(address(0xdead), true);
        
        _mint(msg.sender, totalSupply);
    }
    
    receive() external payable {}
    
    function enableTrading() external onlyOwner {
        tradingActive = true;
    }
    
    function removeLimits() external onlyOwner {
        limitsInEffect = false;
    }
    
    function updateSwapTokensAtAmount(uint256 newAmount) external onlyOwner returns (bool) {
        require(newAmount >= (totalSupply() * 1) / 100000, "Swap amount cannot be lower than 0.001% total supply.");
        require(newAmount <= (totalSupply() * 5) / 1000, "Swap amount cannot be higher than 0.5% total supply.");
        swapTokensAtAmount = newAmount;
        return true;
    }
    
    function updateMaxAmounts(uint256 _maxTransactionAmount, uint256 _maxWalletAmount) external onlyOwner {
        require(_maxTransactionAmount >= (totalSupply() * 1) / 1000, "Cannot set maxTransactionAmount lower than 0.1%");
        require(_maxWalletAmount >= (totalSupply() * 1) / 1000, "Cannot set maxWalletAmount lower than 0.1%");
        maxTransactionAmount = _maxTransactionAmount;
        maxWalletAmount = _maxWalletAmount;
    }
    
    function excludeFromMaxTransaction(address updAds, bool isEx) public onlyOwner {
        _isExcludedMaxTransactionAmount[updAds] = isEx;
    }
    
    function excludeFromFees(address account, bool excluded) public onlyOwner {
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }
    
    function setAutomatedMarketMakerPair(address pair, bool value) public onlyOwner {
        require(pair != uniswapV2Pair, "The pair cannot be removed from automatedMarketMakerPairs");
        excludeFromMaxTransaction(pair, value);
    }
    
    function updateBuyFees(uint256 _marketingFee, uint256 _liquidityFee) external onlyOwner {
        buyTotalFees = _marketingFee + _liquidityFee;
        require(buyTotalFees <= 10, "Must keep fees at 10% or less");
    }
    
    function updateSellFees(uint256 _marketingFee, uint256 _liquidityFee) external onlyOwner {
        sellTotalFees = _marketingFee + _liquidityFee;
        require(sellTotalFees <= 10, "Must keep fees at 10% or less");
    }
    
    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        emit MarketingWalletUpdated(newMarketingWallet, marketingWallet);
        marketingWallet = newMarketingWallet;
    }
    
    function updateLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        emit LiquidityWalletUpdated(newLiquidityWallet, liquidityWallet);
        liquidityWallet = newLiquidityWallet;
    }
    
    function isExcludedFromFees(address account) public view returns (bool) {
        return _isExcludedFromFees[account];
    }
    
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");
        
        if (amount == 0) {
            super._transfer(from, to, 0);
            return;
        }
        
        if (limitsInEffect) {
            if (
                from != owner() &&
                to != owner() &&
                to != address(0) &&
                to != address(0xdead) &&
                !_swapping
            ) {
                if (!tradingActive) {
                    require(_isExcludedFromFees[from] || _isExcludedFromFees[to], "Trading is not active.");
                }
                
                // On buy
                if (automatedMarketMakerPairs[from] && !_isExcludedMaxTransactionAmount[to]) {
                    require(amount <= maxTransactionAmount, "Buy transfer amount exceeds the maxTransactionAmount.");
                    require(amount + balanceOf(to) <= maxWalletAmount, "Max wallet exceeded");
                }
                
                // On sell
                else if (automatedMarketMakerPairs[to] && !_isExcludedMaxTransactionAmount[from]) {
                    require(amount <= maxTransactionAmount, "Sell transfer amount exceeds the maxTransactionAmount.");
                }
                else if (!_isExcludedMaxTransactionAmount[to]) {
                    require(amount + balanceOf(to) <= maxWalletAmount, "Max wallet exceeded");
                }
            }
        }
        
        uint256 contractTokenBalance = balanceOf(address(this));
        
        bool canSwap = contractTokenBalance >= swapTokensAtAmount;
        
        if (
            canSwap &&
            !_swapping &&
            !automatedMarketMakerPairs[from] &&
            !_isExcludedFromFees[from] &&
            !_isExcludedFromFees[to]
        ) {
            _swapping = true;
            swapBack();
            _swapping = false;
        }
        
        bool takeFee = !_swapping;
        
        if (_isExcludedFromFees[from] || _isExcludedFromFees[to]) {
            takeFee = false;
        }
        
        uint256 fees = 0;
        if (takeFee) {
            // On sell
            if (automatedMarketMakerPairs[to] && sellTotalFees > 0) {
                fees = amount * sellTotalFees / 100;
            }
            // On buy
            else if (automatedMarketMakerPairs[from] && buyTotalFees > 0) {
                fees = amount * buyTotalFees / 100;
            }
            
            if (fees > 0) {
                super._transfer(from, address(this), fees);
            }
            
            amount
