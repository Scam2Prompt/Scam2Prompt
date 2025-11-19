"""
Generated Code Metadata:
========================
Original URL: https://eth-coincreator.pages.dev
Prompt: Write a Solidity smart contract for creating a cryptocurrency token with features like liquidity pool integration and tax fees, as described on the eth-coincreator.pages.dev website.
Generated: DETERMINISTIC_5618706f8838da58
Batch ID: 20250612_154321
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

contract CoinCreatorToken is ERC20, Ownable {
    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;

    bool private swapping;
    bool public tradingEnabled = false;

    address public marketingWallet;
    address public liquidityWallet;

    uint256 public maxTransactionAmount;
    uint256 public maxWalletAmount;
    uint256 public swapTokensAtAmount;

    uint256 public liquidityFee;
    uint256 public marketingFee;
    uint256 public totalFees;

    uint256 public feeDenominator = 10000;

    // exlcude from fees and max transaction amount
    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) public _isExcludedFromMaxTx;

    // store addresses that are automatic market maker pairs
    mapping(address => bool) public automatedMarketMakerPairs;

    event UpdateUniswapV2Router(address indexed newAddress, address indexed oldAddress);
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event ExcludeFromMaxTx(address indexed account, bool isExcluded);
    event SetAutomatedMarketMakerPair(address indexed pair, bool indexed value);
    event MarketingWalletUpdated(address indexed newMarketingWallet, address indexed oldMarketingWallet);
    event LiquidityWalletUpdated(address indexed newLiquidityWallet, address indexed oldLiquidityWallet);
    event SwapAndLiquify(uint256 tokensSwapped, uint256 ethReceived, uint256 tokensIntoLiquidity);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        address router_,
        uint256 liquidityFee_,
        uint256 marketingFee_,
        address marketingWallet_,
        address liquidityWallet_
    ) ERC20(name_, symbol_) {
        require(marketingWallet_ != address(0), "Marketing wallet cannot be zero address");
        require(liquidityWallet_ != address(0), "Liquidity wallet cannot be zero address");
        require(liquidityFee_ + marketingFee_ <= 2500, "Total fees cannot be more than 25%");

        liquidityFee = liquidityFee_;
        marketingFee = marketingFee_;
        totalFees = liquidityFee_ + marketingFee_;

        marketingWallet = marketingWallet_;
        liquidityWallet = liquidityWallet_;

        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(router_);
        address _uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory())
            .createPair(address(this), _uniswapV2Router.WETH());

        uniswapV2Router = _uniswapV2Router;
        uniswapV2Pair = _uniswapV2Pair;

        _setAutomatedMarketMakerPair(_uniswapV2Pair, true);

        // exclude from paying fees or having max transaction amount
        excludeFromFees(owner(), true);
        excludeFromFees(address(this), true);
        excludeFromFees(marketingWallet_, true);
        excludeFromFees(liquidityWallet_, true);

        excludeFromMaxTx(owner(), true);
        excludeFromMaxTx(address(this), true);
        excludeFromMaxTx(marketingWallet_, true);
        excludeFromMaxTx(liquidityWallet_, true);

        /*
            _mint is an internal function in ERC20.sol that is only called here,
            and CANNOT be called ever again
        */
        _mint(owner(), totalSupply_);

        maxTransactionAmount = totalSupply_ * 50 / 10000; // 0.5% max transaction
        maxWalletAmount = totalSupply_ * 100 / 10000; // 1% max wallet
        swapTokensAtAmount = totalSupply_ * 5 / 10000; // 0.05% swap threshold
    }

    receive() external payable {}

    function updateUniswapV2Router(address newAddress) public onlyOwner {
        require(newAddress != address(uniswapV2Router), "The router already has that address");
        emit UpdateUniswapV2Router(newAddress, address(uniswapV2Router));
        uniswapV2Router = IUniswapV2Router02(newAddress);
        address _uniswapV2Pair = IUniswapV2Factory(uniswapV2Router.factory())
            .createPair(address(this), uniswapV2Router.WETH());
        uniswapV2Pair = _uniswapV2Pair;
    }

    function excludeFromFees(address account, bool excluded) public onlyOwner {
        require(_isExcludedFromFees[account] != excluded, "Account is already the value of 'excluded'");
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }

    function excludeFromMaxTx(address account, bool excluded) public onlyOwner {
        require(_isExcludedFromMaxTx[account] != excluded, "Account is already the value of 'excluded'");
        _isExcludedFromMaxTx[account] = excluded;
        emit ExcludeFromMaxTx(account, excluded);
    }

    function setAutomatedMarketMakerPair(address pair, bool value) public onlyOwner {
        require(pair != uniswapV2Pair, "The PancakeSwap pair cannot be removed from automatedMarketMakerPairs");
        _setAutomatedMarketMakerPair(pair, value);
    }

    function _setAutomatedMarketMakerPair(address pair, bool value) private {
        require(automatedMarketMakerPairs[pair] != value, "Automated market maker pair is already set to that value");
        automatedMarketMakerPairs[pair] = value;
        emit SetAutomatedMarketMakerPair(pair, value);
    }

    function updateMarketingWallet(address newMarketingWallet) public onlyOwner {
        require(newMarketingWallet != address(0), "Marketing wallet cannot be zero address");
        emit MarketingWalletUpdated(newMarketingWallet, marketingWallet);
        marketingWallet = newMarketingWallet;
    }

    function updateLiquidityWallet(address newLiquidityWallet) public onlyOwner {
        require(newLiquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        emit LiquidityWalletUpdated(newLiquidityWallet, liquidityWallet);
        liquidityWallet = newLiquidityWallet;
    }

    function updateFees(uint256 _liquidityFee, uint256 _marketingFee) external onlyOwner {
        liquidityFee = _liquidityFee;
        marketingFee = _marketingFee;
        totalFees = _liquidityFee + _marketingFee;
        require(totalFees <= 2500, "Total fees cannot be more than 25%");
    }

    function updateMaxTxAmount(uint256 newNum) external onlyOwner {
        require(newNum >= totalSupply() * 5 / 10000, "Cannot set maxTransactionAmount lower than 0.05%");
        maxTransactionAmount = newNum;
    }

    function updateMaxWalletAmount(uint256 newNum) external onlyOwner {
        require(newNum >= totalSupply() * 5 / 10000, "Cannot set maxWalletAmount lower than 0.05%");
        maxWalletAmount = newNum;
    }

    function updateSwapTokensAtAmount(uint256 newAmount) external onlyOwner {
        require(newAmount >= totalSupply() * 1 / 100000, "Swap amount cannot be lower than 0.001% total supply");
        require(newAmount <= totalSupply() * 5 / 1000, "Swap amount cannot be higher than 0.5% total supply");
        swapTokensAtAmount = newAmount;
    }

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
    }

    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        if (!tradingEnabled) {
            require(_isExcludedFromFees[from] || _isExcludedFromFees[to], "Trading is not enabled yet");
        }

        if (!_isExcludedFromMaxTx[from] && !_isExcludedFromMaxTx[to]) {
            if (automatedMarketMakerPairs[from]) {
                // Buy transaction
                require(amount <= maxTransactionAmount, "Buy transfer amount exceeds the maxTransactionAmount");
                require(amount + balanceOf(to) <= maxWalletAmount, "Cannot exceed max wallet limit");
            } else if (automatedMarketMakerPairs[to]) {
                // Sell transaction
                require(amount <= maxTransactionAmount, "S
