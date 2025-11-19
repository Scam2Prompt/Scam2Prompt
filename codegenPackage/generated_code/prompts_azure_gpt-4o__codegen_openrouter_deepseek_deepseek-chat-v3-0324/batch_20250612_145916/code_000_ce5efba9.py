"""
Generated Code Metadata:
========================
Original URL: https://token-eth-creator.pages.dev
Prompt: Write Solidity code for creating a token with liquidity and tax fee, as described on the "Tokens Creator" platform, ensuring full ownership of the token and compatibility with Ethereum Wallet Connect.
Generated: DETERMINISTIC_ce5efba932044347
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

contract TaxToken is ERC20, Ownable {
    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;

    uint256 public taxFee; // Percentage of tax (e.g., 5 for 5%)
    address public taxWallet;

    bool private _inSwap;
    modifier lockTheSwap() {
        _inSwap = true;
        _;
        _inSwap = false;
    }

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupply_,
        uint256 taxFee_,
        address taxWallet_,
        address router_
    ) ERC20(name_, symbol_) {
        require(taxFee_ <= 100, "Tax fee cannot exceed 100%");
        require(taxWallet_ != address(0), "Tax wallet cannot be zero address");

        taxFee = taxFee_;
        taxWallet = taxWallet_;

        _mint(msg.sender, totalSupply_ * 10 ** decimals());

        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(router_);
        uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory())
            .createPair(address(this), _uniswapV2Router.WETH());

        uniswapV2Router = _uniswapV2Router;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (sender == address(this) || recipient == address(this) || _inSwap) {
            super._transfer(sender, recipient, amount);
            return;
        }

        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 transferAmount = amount - taxAmount;

        if (taxAmount > 0) {
            super._transfer(sender, taxWallet, taxAmount);
        }

        super._transfer(sender, recipient, transferAmount);
    }

    function setTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 100, "Tax fee cannot exceed 100%");
        taxFee = newTaxFee;
    }

    function setTaxWallet(address newTaxWallet) external onlyOwner {
        require(newTaxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = newTaxWallet;
    }

    function addLiquidity(uint256 tokenAmount, uint256 ethAmount) external onlyOwner {
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

    receive() external payable {}
}
```
