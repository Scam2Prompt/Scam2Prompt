"""
Generated Code Metadata:
========================
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: Write a Solidity smart contract for a token relaunch, similar to HMNG v2, ensuring liquidity locking, fair launch, and re-auditing features.
Generated: DETERMINISTIC_c0b82c56f94a9ca8
Batch ID: 20250612_151343
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

contract TokenRelaunch is ERC20, Ownable {
    using SafeMath for uint256;

    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;

    bool private swapping;
    bool public tradingEnabled = false;
    bool public liquidityLocked = false;

    uint256 public maxTransactionAmount;
    uint256 public maxWalletAmount;
    uint256 public swapTokensAtAmount;

    address public liquidityWallet;
    address public marketingWallet;
    address public developmentWallet;

    uint256 public liquidityFee;
    uint256 public marketingFee;
    uint256 public developmentFee;
    uint256 public totalFees;

    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) public _isExcludedFromMaxTx;
    mapping(address => bool) public _isExcludedFromMaxWallet;

    // Lock liquidity for 1 year by default
    uint256 public liquidityLockTime = 365 days;
    uint256 public liquidityUnlockTime;

    event UpdateUniswapV2Router(address indexed newAddress, address indexed oldAddress);
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event ExcludeFromMaxTx(address indexed account, bool isExcluded);
    event ExcludeFromMaxWallet(address indexed account, bool isExcluded);
    event LiquidityLocked(uint256 unlockTime);
    event TradingEnabled();
    event SwapAndLiquify(uint256 tokensSwapped, uint256 ethReceived, uint256 tokensIntoLiquidity);

    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 _maxTransactionAmount,
        uint256 _maxWalletAmount,
        uint256 _liquidityFee,
        uint256 _marketingFee,
        uint256 _developmentFee,
        address _liquidityWallet,
        address _marketingWallet,
        address _developmentWallet,
        address routerAddress
    ) ERC20(name, symbol) {
        require(_liquidityFee.add(_marketingFee).add(_developmentFee) <= 25, "Total fees cannot exceed 25%");

        maxTransactionAmount = _maxTransactionAmount * (10**decimals());
        maxWalletAmount = _maxWalletAmount * (10**decimals());
        swapTokensAtAmount = totalSupply.mul(5).div(10000); // 0.05% of total supply

        liquidityFee = _liquidityFee;
        marketingFee = _marketingFee;
        developmentFee = _developmentFee;
        totalFees = _liquidityFee.add(_marketingFee).add(_developmentFee);

        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;

        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(routerAddress);
        address _uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory())
            .createPair(address(this), _uniswapV2Router.WETH());

        uniswapV2Router = _uniswapV2Router;
        uniswapV2Pair = _uniswapV2Pair;

        _isExcludedFromFees[owner()] = true;
        _isExcludedFromFees[address(this)] = true;
        _isExcludedFromFees[marketingWallet] = true;
        _isExcludedFromFees[developmentWallet] = true;

        _isExcludedFromMaxTx[owner()] = true;
        _isExcludedFromMaxTx[address(this)] = true;
        _isExcludedFromMaxTx[marketingWallet] = true;
        _isExcludedFromMaxTx[developmentWallet] = true;

        _isExcludedFromMaxWallet[owner()] = true;
        _isExcludedFromMaxWallet[address(this)] = true;
        _isExcludedFromMaxWallet[marketingWallet] = true;
        _isExcludedFromMaxWallet[developmentWallet] = true;

        _mint(owner(), totalSupply * (10**decimals()));
    }

    receive() external payable {}

    function lockLiquidity() external onlyOwner {
        require(!liquidityLocked, "Liquidity is already locked");
        liquidityUnlockTime = block.timestamp.add(liquidityLockTime);
        liquidityLocked = true;
        emit LiquidityLocked(liquidityUnlockTime);
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading is already enabled");
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function updateUniswapV2Router(address newAddress) external onlyOwner {
        require(newAddress != address(uniswapV2Router), "The router already has that address");
        emit UpdateUniswapV2Router(newAddress, address(uniswapV2Router));
        uniswapV2Router = IUniswapV2Router02(newAddress);
        uniswapV2Pair = IUniswapV2Factory(uniswapV2Router.factory())
            .createPair(address(this), uniswapV2Router.WETH());
    }

    function excludeFromFees(address account, bool excluded) external onlyOwner {
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }

    function excludeFromMaxTx(address account, bool excluded) external onlyOwner {
        _isExcludedFromMaxTx[account] = excluded;
        emit ExcludeFromMaxTx(account, excluded);
    }

    function excludeFromMaxWallet(address account, bool excluded) external onlyOwner {
        _isExcludedFromMaxWallet[account] = excluded;
        emit ExcludeFromMaxWallet(account, excluded);
    }

    function setFees(uint256 _liquidityFee, uint256 _marketingFee, uint256 _developmentFee) external onlyOwner {
        require(_liquidityFee.add(_marketingFee).add(_developmentFee) <= 25, "Total fees cannot exceed 25%");
        liquidityFee = _liquidityFee;
        marketingFee = _marketingFee;
        developmentFee = _developmentFee;
        totalFees = _liquidityFee.add(_marketingFee).add(_developmentFee);
    }

    function setWallets(address _liquidityWallet, address _marketingWallet, address _developmentWallet) external onlyOwner {
        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;
    }

    function setSwapTokensAtAmount(uint256 amount) external onlyOwner {
        swapTokensAtAmount = amount;
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
            require(amount <= maxTransactionAmount, "Transfer amount exceeds the maxTxAmount");
        }

        if (!_isExcludedFromMaxWallet[to]) {
            require(balanceOf(to).add(amount) <= maxWalletAmount, "Transfer would exceed max wallet limit");
        }

        uint256 contractTokenBalance = balanceOf(address(this));
        bool canSwap = contractTokenBalance >= swapTokensAtAmount;

        if (
            canSwap &&
            !swapping &&
            from != uniswapV2Pair &&
            !_isExcludedFromFees[from] &&
            !_isExcludedFromFees[to]
        ) {
            swapping = true;
            swapAndLiquify();
            swapping = false;
        }

        bool takeFee = !swapping;

        if (_isExcludedFromFees[from] || _isExcludedFromFees[to]) {
            takeFee = false;
        }

        if (takeFee) {
            uint256 fees = amount.mul(totalFees).div(100);
            amount = amount.sub(fees);
            super._transfer(from, address(this), fees);
        }

        super._transfer(from, to, amount);
    }

    function swapAndLiquify() private {
        uint256 contractTokenBalance = balanceOf(address(this));
        uint256 totalFee = liquidityFee.add(marketingFee).add(development
