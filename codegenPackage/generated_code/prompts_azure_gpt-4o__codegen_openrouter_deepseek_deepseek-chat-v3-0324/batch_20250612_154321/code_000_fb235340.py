"""
Generated Code Metadata:
========================
Original URL: https://ethereum-creator.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee, similar to the functionality described on the Ethereum Creator website. Ensure the contract is fully audited and supports multiple networks.
Generated: DETERMINISTIC_fb23534040fec5f8
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

contract TaxToken is ERC20, Ownable {
    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;

    uint256 public taxFee; // Percentage of tax (e.g., 5 for 5%)
    address public taxWallet; // Wallet to receive tax fees

    bool private _inSwap;
    modifier lockTheSwap {
        _inSwap = true;
        _;
        _inSwap = false;
    }

    event TaxFeeUpdated(uint256 newTaxFee);
    event TaxWalletUpdated(address newTaxWallet);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 taxFee_,
        address taxWallet_,
        address routerAddress_
    ) ERC20(name_, symbol_) {
        require(taxFee_ <= 100, "Tax fee cannot exceed 100%");
        require(taxWallet_ != address(0), "Tax wallet cannot be zero address");
        require(routerAddress_ != address(0), "Router address cannot be zero");

        _mint(msg.sender, initialSupply_ * 10 ** decimals());

        taxFee = taxFee_;
        taxWallet = taxWallet_;

        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(routerAddress_);
        uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory())
            .createPair(address(this), _uniswapV2Router.WETH());

        uniswapV2Router = _uniswapV2Router;
    }

    function setTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 100, "Tax fee cannot exceed 100%");
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    function setTaxWallet(address newTaxWallet) external onlyOwner {
        require(newTaxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = newTaxWallet;
        emit TaxWalletUpdated(newTaxWallet);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (
            _inSwap ||
            sender == owner() ||
            recipient == owner() ||
            sender == address(this) ||
            recipient == address(this)
        ) {
            super._transfer(sender, recipient, amount);
            return;
        }

        bool isSell = recipient == uniswapV2Pair;
        bool isBuy = sender == uniswapV2Pair;

        uint256 taxAmount = 0;
        if (isBuy || isSell) {
            taxAmount = (amount * taxFee) / 100;
        }

        if (taxAmount > 0) {
            super._transfer(sender, taxWallet, taxAmount);
            amount -= taxAmount;
        }

        super._transfer(sender, recipient, amount);
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
