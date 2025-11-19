"""
Generated Code Metadata:
========================
Original URL: https://peppermeme.org
Prompt: Write a Solidity contract that implements the $PEPPER tokenomics, including liquidity management, token allocation across wallets, and gradual liquidation.
Generated: DETERMINISTIC_ccee4b0a1e09a7ea
Batch ID: 20250612_154010
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract PEPPER is ERC20, Ownable {
    using SafeMath for uint256;

    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;

    bool private swapping;
    bool public tradingEnabled = false;

    address public marketingWallet;
    address public developmentWallet;
    address public liquidityWallet;

    uint256 public maxTransactionAmount;
    uint256 public swapTokensAtAmount;
    uint256 public maxWallet;

    uint256 public liquidityFee;
    uint256 public marketingFee;
    uint256 public developmentFee;
    uint256 public totalFees;

    uint256 public sellLiquidityFee;
    uint256 public sellMarketingFee;
    uint256 public sellDevelopmentFee;
    uint256 public sellTotalFees;

    uint256 public tokensForLiquidity;
    uint256 public tokensForMarketing;
    uint256 public tokensForDevelopment;

    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) public _isExcludedMaxTransactionAmount;
    mapping(address => bool) public automatedMarketMakerPairs;

    event UpdateUniswapV2Router(address indexed newAddress, address indexed oldAddress);
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event SetAutomatedMarketMakerPair(address indexed pair, bool indexed value);
    event SwapAndLiquify(uint256 tokensSwapped, uint256 ethReceived, uint256 tokensIntoLiquidity);

    constructor() ERC20("PEPPER", "PEPPER") {
        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D);
        
        excludeFromMaxTransaction(address(_uniswapV2Router), true);
        uniswapV2Router = _uniswapV2Router;
        
        uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory()).createPair(address(this), _uniswapV2Router.WETH());
        excludeFromMaxTransaction(address(uniswapV2Pair), true);
        _setAutomatedMarketMakerPair(address(uniswapV2Pair), true);

        uint256 totalSupply = 1_000_000_000 * 10**decimals();
        
        maxTransactionAmount = totalSupply * 20 / 1000; // 2% max transaction
        maxWallet = totalSupply * 20 / 1000; // 2% max wallet
        swapTokensAtAmount = totalSupply * 5 / 10000; // 0.05% swap threshold

        marketingWallet = address(0x123...); // Replace with actual marketing wallet
        developmentWallet = address(0x456...); // Replace with actual development wallet
        liquidityWallet = address(0x789...); // Replace with actual liquidity wallet

        excludeFromFees(owner(), true);
        excludeFromFees(address(this), true);
        excludeFromFees(address(0xdead), true);
        
        excludeFromMaxTransaction(owner(), true);
        excludeFromMaxTransaction(address(this), true);
        excludeFromMaxTransaction(address(0xdead), true);

        liquidityFee = 2;
        marketingFee = 3;
        developmentFee = 2;
        totalFees = liquidityFee + marketingFee + developmentFee;

        sellLiquidityFee = 2;
        sellMarketingFee = 3;
        sellDevelopmentFee = 2;
        sellTotalFees = sellLiquidityFee + sellMarketingFee + sellDevelopmentFee;

        _mint(msg.sender, totalSupply);
    }

    receive() external payable {}

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
    }

    function updateSwapTokensAtAmount(uint256 newAmount) external onlyOwner returns (bool) {
        require(newAmount >= totalSupply() * 1 / 100000, "Swap amount cannot be lower than 0.001% total supply.");
        require(newAmount <= totalSupply() * 5 / 1000, "Swap amount cannot be higher than 0.5% total supply.");
        swapTokensAtAmount = newAmount;
        return true;
    }

    function updateMaxAmount(uint256 newNum) external onlyOwner {
        require(newNum >= (totalSupply() * 5 / 1000)/1e18, "Cannot set maxTransactionAmount lower than 0.5%");
        maxTransactionAmount = newNum * (10**18);
    }

    function updateMaxWalletAmount(uint256 newNum) external onlyOwner {
        require(newNum >= (totalSupply() * 1 / 100)/1e18, "Cannot set maxWallet lower than 1%");
        maxWallet = newNum * (10**18);
    }

    function excludeFromMaxTransaction(address updAds, bool isEx) public onlyOwner {
        _isExcludedMaxTransactionAmount[updAds] = isEx;
    }

    function updateFees(uint256 _liquidityFee, uint256 _marketingFee, uint256 _developmentFee) external onlyOwner {
        liquidityFee = _liquidityFee;
        marketingFee = _marketingFee;
        developmentFee = _developmentFee;
        totalFees = liquidityFee + marketingFee + developmentFee;
        require(totalFees <= 15, "Must keep fees at 15% or less");
    }

    function updateSellFees(uint256 _liquidityFee, uint256 _marketingFee, uint256 _developmentFee) external onlyOwner {
        sellLiquidityFee = _liquidityFee;
        sellMarketingFee = _marketingFee;
        sellDevelopmentFee = _developmentFee;
        sellTotalFees = sellLiquidityFee + sellMarketingFee + sellDevelopmentFee;
        require(sellTotalFees <= 15, "Must keep fees at 15% or less");
    }

    function excludeFromFees(address account, bool excluded) public onlyOwner {
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }

    function setAutomatedMarketMakerPair(address pair, bool value) public onlyOwner {
        require(pair != uniswapV2Pair, "The pair cannot be removed from automatedMarketMakerPairs");
        _setAutomatedMarketMakerPair(pair, value);
    }

    function _setAutomatedMarketMakerPair(address pair, bool value) private {
        automatedMarketMakerPairs[pair] = value;
        emit SetAutomatedMarketMakerPair(pair, value);
    }

    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        marketingWallet = newMarketingWallet;
    }

    function updateDevelopmentWallet(address newDevelopmentWallet) external onlyOwner {
        developmentWallet = newDevelopmentWallet;
    }

    function updateLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        liquidityWallet = newLiquidityWallet;
    }

    function isExcludedFromFees(address account) public view returns(bool) {
        return _isExcludedFromFees[account];
    }

    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        if(amount == 0) {
            super._transfer(from, to, 0);
            return;
        }

        if(!tradingEnabled) {
            require(_isExcludedFromFees[from] || _isExcludedFromFees[to], "Trading is not active.");
        }

        if(!_isExcludedMaxTransactionAmount[from] && !_isExcludedMaxTransactionAmount[to]) {
            if(automatedMarketMakerPairs[from] && !_isExcludedMaxTransactionAmount[to]) {
                require(amount <= maxTransactionAmount, "Buy transfer amount exceeds the maxTransactionAmount.");
                require(amount + balanceOf(to) <= maxWallet, "Max wallet exceeded");
            }
            else if(automatedMarketMakerPairs[to] && !_isExcludedMaxTransactionAmount[from]) {
                require(amount <= maxTransactionAmount, "Sell transfer amount exceeds the maxTransactionAmount.");
            }
            else if(!_isExcludedMaxTransactionAmount[to]) {
                require(amount + balanceOf(to) <= maxWallet, "Max wallet exceeded");
            }
        }

        uint256 contractTokenBalance = balanceOf(address(this));
        bool canSwap = contractTokenBalance >= swapTokensAtAmount;
        
        if(canSwap && !swapping && !automatedMarketMakerPairs[from] && !_isEx
