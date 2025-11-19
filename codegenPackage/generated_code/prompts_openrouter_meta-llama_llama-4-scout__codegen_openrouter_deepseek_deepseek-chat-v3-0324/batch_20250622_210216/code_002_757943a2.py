"""
Generated Code Metadata:
========================
Original URL: https://memekombatio.pages.dev
Prompt: Generate a smart contract code in Solidity for a token launch on Uniswap, similar to the $MK token launch on Meme Kombat.
Generated: DETERMINISTIC_757943a26da1a272
Batch ID: 20250622_210216
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

contract MemeToken is ERC20, Ownable {
    IUniswapV2Router02 public immutable uniswapV2Router;
    address public uniswapV2Pair;
    
    uint256 public maxTransactionAmount;
    uint256 public maxWalletAmount;
    
    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) private _isExcludedFromMaxTx;
    mapping(address => bool) private _isExcludedFromMaxWallet;
    
    bool public tradingEnabled = false;
    bool public limitsInEffect = true;
    
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event ExcludeFromMaxTx(address indexed account, bool isExcluded);
    event ExcludeFromMaxWallet(address indexed account, bool isExcluded);
    event TradingEnabled();
    event LimitsRemoved();

    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        address routerAddress
    ) ERC20(name, symbol) {
        // Initialize Uniswap V2 Router
        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(routerAddress);
        uniswapV2Router = _uniswapV2Router;
        
        // Create initial supply
        _mint(msg.sender, totalSupply);
        
        // Set initial limits (2% of total supply)
        maxTransactionAmount = totalSupply * 2 / 100;
        maxWalletAmount = totalSupply * 2 / 100;
        
        // Exclude owner and this contract from fees
        _isExcludedFromFees[msg.sender] = true;
        _isExcludedFromFees[address(this)] = true;
        
        // Exclude owner from max TX and wallet limits
        _isExcludedFromMaxTx[msg.sender] = true;
        _isExcludedFromMaxWallet[msg.sender] = true;
    }

    function createPair() external onlyOwner {
        require(uniswapV2Pair == address(0), "Pair already created");
        uniswapV2Pair = IUniswapV2Factory(uniswapV2Router.factory()).createPair(
            address(this),
            uniswapV2Router.WETH()
        );
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading already enabled");
        require(uniswapV2Pair != address(0), "Pair not created");
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function removeLimits() external onlyOwner {
        require(limitsInEffect, "Limits already removed");
        limitsInEffect = false;
        emit LimitsRemoved();
    }

    function excludeFromFees(address account, bool excluded) external onlyOwner {
        require(_isExcludedFromFees[account] != excluded, "Account already set");
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }

    function excludeFromMaxTx(address account, bool excluded) external onlyOwner {
        require(_isExcludedFromMaxTx[account] != excluded, "Account already set");
        _isExcludedFromMaxTx[account] = excluded;
        emit ExcludeFromMaxTx(account, excluded);
    }

    function excludeFromMaxWallet(address account, bool excluded) external onlyOwner {
        require(_isExcludedFromMaxWallet[account] != excluded, "Account already set");
        _isExcludedFromMaxWallet[account] = excluded;
        emit ExcludeFromMaxWallet(account, excluded);
    }

    function setMaxTransactionAmount(uint256 amount) external onlyOwner {
        require(amount >= totalSupply() / 1000, "Amount too low");
        maxTransactionAmount = amount;
    }

    function setMaxWalletAmount(uint256 amount) external onlyOwner {
        require(amount >= totalSupply() / 1000, "Amount too low");
        maxWalletAmount = amount;
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
            require(
                _isExcludedFromFees[from] || _isExcludedFromFees[to],
                "Trading is not enabled yet"
            );
        }

        if (limitsInEffect) {
            if (
                from != owner() &&
                to != owner() &&
                to != address(0) &&
                to != address(0xdead) &&
                !_isExcludedFromFees[from] &&
                !_isExcludedFromFees[to]
            ) {
                // Enforce max transaction amount
                if (!_isExcludedFromMaxTx[from] && !_isExcludedFromMaxTx[to]) {
                    require(
                        amount <= maxTransactionAmount,
                        "Transfer amount exceeds max transaction amount"
                    );
                }

                // Enforce max wallet amount
                if (!_isExcludedFromMaxWallet[to]) {
                    uint256 balance = balanceOf(to);
                    require(
                        balance + amount <= maxWalletAmount,
                        "Wallet balance exceeds max wallet amount"
                    );
                }
            }
        }

        super._transfer(from, to, amount);
    }
}
```
