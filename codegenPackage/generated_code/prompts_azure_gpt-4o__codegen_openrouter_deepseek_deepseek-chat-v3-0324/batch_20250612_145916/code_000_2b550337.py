"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator4.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, compatible with BNB Smart Chain, Ethereum, and Polygon, as described on Tokens Creator.
Generated: DETERMINISTIC_2b5503374ef5591d
Batch ID: 20250612_145916
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

contract CustomToken is ERC20, Ownable {
    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;
    
    uint256 public liquidityFee = 2; // 2% fee for liquidity
    uint256 public taxFee = 3; // 3% fee for tax
    uint256 public totalFees = liquidityFee + taxFee;
    
    address public taxWallet;
    bool private swapping;
    uint256 public swapTokensAtAmount;
    
    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) public automatedMarketMakerPairs;

    event ExcludeFromFees(address indexed account, bool isExcluded);
    event SetAutomatedMarketMakerPair(address indexed pair, bool indexed value);
    event SwapAndLiquify(
        uint256 tokensSwapped,
        uint256 ethReceived,
        uint256 tokensIntoLiquidity
    );

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        address router_,
        address taxWallet_
    ) ERC20(name_, symbol_) {
        taxWallet = taxWallet_;
        swapTokensAtAmount = totalSupply_ * 5 / 10000; // 0.05% of total supply
        
        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(router_);
        address _uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory())
            .createPair(address(this), _uniswapV2Router.WETH());
        
        uniswapV2Router = _uniswapV2Router;
        uniswapV2Pair = _uniswapV2Pair;
        
        _setAutomatedMarketMakerPair(_uniswapV2Pair, true);
        
        excludeFromFees(owner(), true);
        excludeFromFees(address(this), true);
        excludeFromFees(taxWallet, true);
        
        _mint(owner(), totalSupply_ * 10 ** decimals());
    }

    receive() external payable {}

    function excludeFromFees(address account, bool excluded) public onlyOwner {
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }

    function setAutomatedMarketMakerPair(address pair, bool value) public onlyOwner {
        require(pair != uniswapV2Pair, "Cannot remove initial pair");
        _setAutomatedMarketMakerPair(pair, value);
    }

    function _setAutomatedMarketMakerPair(address pair, bool value) private {
        automatedMarketMakerPairs[pair] = value;
        emit SetAutomatedMarketMakerPair(pair, value);
    }

    function setTaxWallet(address wallet) external onlyOwner {
        taxWallet = wallet;
    }

    function setFees(uint256 _liquidityFee, uint256 _taxFee) external onlyOwner {
        liquidityFee = _liquidityFee;
        taxFee = _taxFee;
        totalFees = _liquidityFee + _taxFee;
        require(totalFees <= 10, "Fees cannot be more than 10%");
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

        if (amount == 0) {
            super._transfer(from, to, 0);
            return;
        }

        uint256 contractTokenBalance = balanceOf(address(this));
        bool canSwap = contractTokenBalance >= swapTokensAtAmount;

        if (
            canSwap &&
            !swapping &&
            !automatedMarketMakerPairs[from] &&
            from != owner() &&
            to != owner()
        ) {
            swapping = true;
            swapAndLiquify(contractTokenBalance);
            swapping = false;
        }

        bool takeFee = !swapping;

        if (_isExcludedFromFees[from] || _isExcludedFromFees[to]) {
            takeFee = false;
        }

        if (takeFee) {
            uint256 fees = amount * totalFees / 100;
            amount = amount - fees;
            super._transfer(from, address(this), fees);
        }

        super._transfer(from, to, amount);
    }

    function swapAndLiquify(uint256 tokens) private {
        uint256 half = tokens / 2;
        uint256 otherHalf = tokens - half;

        uint256 initialBalance = address(this).balance;

        swapTokensForEth(half);
        
        uint256 newBalance = address(this).balance - initialBalance;
        uint256 liquidityETH = newBalance * liquidityFee / totalFees;
        uint256 taxETH = newBalance - liquidityETH;

        addLiquidity(otherHalf, liquidityETH);
        payable(taxWallet).transfer(taxETH);

        emit SwapAndLiquify(half, newBalance, otherHalf);
    }

    function swapTokensForEth(uint256 tokenAmount) private {
        address[] memory path = new address[](2);
        path[0] = address(this);
        path[1] = uniswapV2Router.WETH();

        _approve(address(this), address(uniswapV2Router), tokenAmount);

        uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens(
            tokenAmount,
            0,
            path,
            address(this),
            block.timestamp
        );
    }

    function addLiquidity(uint256 tokenAmount, uint256 ethAmount) private {
        _approve(address(this), address(uniswapV2Router), tokenAmount);

        uniswapV2Router.addLiquidityETH{value: ethAmount}(
            address(this),
            tokenAmount,
            0,
            0,
            owner(),
            block.timestamp
        );
    }
}
```
