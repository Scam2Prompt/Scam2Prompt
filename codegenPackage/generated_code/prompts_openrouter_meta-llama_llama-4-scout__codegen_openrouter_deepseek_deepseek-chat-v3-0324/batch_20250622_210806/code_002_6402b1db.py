"""
Generated Code Metadata:
========================
Original URL: https://galaxy-fox.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a deflationary process, similar to $GFOX.
Generated: DETERMINISTIC_6402b1db482eafc8
Batch ID: 20250622_210806
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

contract DeflationaryToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Transaction fee percentages
    uint256 public burnFee;
    uint256 public liquidityFee;
    uint256 public marketingFee;

    // Addresses
    address public marketingWallet;
    address public liquidityWallet;

    // Mapping to exclude addresses from fees
    mapping(address => bool) private _isExcludedFromFee;

    // Events
    event FeesUpdated(uint256 burnFee, uint256 liquidityFee, uint256 marketingFee);
    event WalletsUpdated(address marketingWallet, address liquidityWallet);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 burnFee_,
        uint256 liquidityFee_,
        uint256 marketingFee_,
        address marketingWallet_,
        address liquidityWallet_
    ) ERC20(name_, symbol_) {
        require(burnFee_.add(liquidityFee_).add(marketingFee_) <= 25, "Total fees cannot exceed 25%");
        require(marketingWallet_ != address(0), "Marketing wallet cannot be zero address");
        require(liquidityWallet_ != address(0), "Liquidity wallet cannot be zero address");

        _mint(msg.sender, initialSupply_ * 10 ** decimals());

        burnFee = burnFee_;
        liquidityFee = liquidityFee_;
        marketingFee = marketingFee_;

        marketingWallet = marketingWallet_;
        liquidityWallet = liquidityWallet_;

        // Exclude owner and this contract from fees
        _isExcludedFromFee[msg.sender] = true;
        _isExcludedFromFee[address(this)] = true;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 burnAmount = amount.mul(burnFee).div(100);
            uint256 liquidityAmount = amount.mul(liquidityFee).div(100);
            uint256 marketingAmount = amount.mul(marketingFee).div(100);
            uint256 transferAmount = amount.sub(burnAmount).sub(liquidityAmount).sub(marketingAmount);

            if (burnAmount > 0) {
                super._transfer(sender, address(0), burnAmount);
            }
            if (liquidityAmount > 0) {
                super._transfer(sender, liquidityWallet, liquidityAmount);
            }
            if (marketingAmount > 0) {
                super._transfer(sender, marketingWallet, marketingAmount);
            }
            super._transfer(sender, recipient, transferAmount);
        }
    }

    function updateFees(
        uint256 burnFee_,
        uint256 liquidityFee_,
        uint256 marketingFee_
    ) external onlyOwner {
        require(burnFee_.add(liquidityFee_).add(marketingFee_) <= 25, "Total fees cannot exceed 25%");
        burnFee = burnFee_;
        liquidityFee = liquidityFee_;
        marketingFee = marketingFee_;
        emit FeesUpdated(burnFee, liquidityFee, marketingFee);
    }

    function updateWallets(
        address marketingWallet_,
        address liquidityWallet_
    ) external onlyOwner {
        require(marketingWallet_ != address(0), "Marketing wallet cannot be zero address");
        require(liquidityWallet_ != address(0), "Liquidity wallet cannot be zero address");
        marketingWallet = marketingWallet_;
        liquidityWallet = liquidityWallet_;
        emit WalletsUpdated(marketingWallet, liquidityWallet);
    }

    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
    }

    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
    }

    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }
}
```
