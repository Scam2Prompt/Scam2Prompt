"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator.pages.dev
Prompt: Write a Solidity smart contract for creating a custom token with liquidity and tax fee, similar to the functionality described on Tokens Creator, ensuring 100% token ownership.
Generated: DETERMINISTIC_0232b139356601b6
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// CustomToken is an ERC20 token with a liquidity and tax fee
contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax and liquidity fee percentage (e.g., 5% will be represented as 5)
    uint256 public taxFee;
    uint256 public liquidityFee;

    // Total supply of the token
    uint256 private _totalSupply;

    // Mapping to keep track of balances
    mapping(address => uint256) private _balances;

    // Events for logging transfers
    event FeesDistributed(uint256 taxAmount, uint256 liquidityAmount);

    // Constructor to initialize the token with a name, symbol, and fees
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply_,
        uint256 taxFee_,
        uint256 liquidityFee_
    ) ERC20(name, symbol) {
        require(totalSupply_ > 0, "Total supply must be greater than zero");
        require(taxFee_.add(liquidityFee_) <= 100, "Total fees cannot exceed 100%");

        _totalSupply = totalSupply_ * (10**decimals());
        taxFee = taxFee_;
        liquidityFee = liquidityFee_;

        // Allocate the total supply to the creator of the contract
        _mint(msg.sender, _totalSupply);
    }

    // Override the transfer function to include fees
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate fees
        uint256 taxAmount = amount.mul(taxFee).div(100);
        uint256 liquidityAmount = amount.mul(liquidityFee).div(100);
        uint256 transferAmount = amount.sub(taxAmount).sub(liquidityAmount);

        // Transfer tax and liquidity amounts to the contract
        super._transfer(sender, address(this), taxAmount.add(liquidityAmount));

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);

        emit FeesDistributed(taxAmount, liquidityAmount);
    }

    // Function to withdraw collected fees (for liquidity or other purposes)
    function withdrawFees() external onlyOwner {
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No fees available to withdraw");

        // Transfer all fees to the owner
        super._transfer(address(this), owner(), balance);
    }

    // Function to update tax and liquidity fees
    function updateFees(uint256 newTaxFee, uint256 newLiquidityFee) external onlyOwner {
        require(newTaxFee.add(newLiquidityFee) <= 100, "Total fees cannot exceed 100%");
        taxFee = newTaxFee;
        liquidityFee = newLiquidityFee;
    }

    // Function to get the total supply of the token
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```
