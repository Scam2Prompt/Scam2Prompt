"""
Generated Code Metadata:
========================
Original URL: https://banktoken.pages.dev
Prompt: Develop a Solidity smart contract that implements the sliding point mechanism for the Bank Token, ensuring compliance with the specified buy and sell transaction fees.
Generated: DETERMINISTIC_2adfe67416623be1
Batch ID: 20250612_155229
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

/**
 * @title BankToken
 * @dev Implementation of a Bank Token with sliding point mechanism for transaction fees.
 */
contract BankToken is ERC20, Ownable {
    // Transaction fee percentages (in basis points)
    uint256 public buyFee; // Fee for buying the token
    uint256 public sellFee; // Fee for selling the token

    // Events for logging
    event BuyFeeUpdated(uint256 newBuyFee);
    event SellFeeUpdated(uint256 newSellFee);

    // Mapping to track user balances after fees
    mapping(address => uint256) private _balancesAfterFees;

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param _buyFee The initial buy fee in basis points.
     * @param _sellFee The initial sell fee in basis points.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _buyFee,
        uint256 _sellFee
    ) ERC20(name, symbol) {
        require(_buyFee <= 10000, "Buy fee must be <= 100%");
        require(_sellFee <= 10000, "Sell fee must be <= 100%");
        
        buyFee = _buyFee;
        sellFee = _sellFee;

        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Updates the buy fee.
     * @param newBuyFee The new buy fee in basis points.
     */
    function updateBuyFee(uint256 newBuyFee) external onlyOwner {
        require(newBuyFee <= 10000, "Buy fee must be <= 100%");
        buyFee = newBuyFee;
        emit BuyFeeUpdated(newBuyFee);
    }

    /**
     * @dev Updates the sell fee.
     * @param newSellFee The new sell fee in basis points.
     */
    function updateSellFee(uint256 newSellFee) external onlyOwner {
        require(newSellFee <= 10000, "Sell fee must be <= 100%");
        sellFee = newSellFee;
        emit SellFeeUpdated(newSellFee);
    }

    /**
     * @dev Overrides the transfer function to include transaction fees.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        uint256 fee = (amount * buyFee) / 10000;
        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the contract owner
        _transfer(_msgSender(), owner(), fee);
        // Transfer the remaining amount to the recipient
        _transfer(_msgSender(), recipient, amountAfterFee);

        return true;
    }

    /**
     * @dev Overrides the transferFrom function to include transaction fees.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        uint256 fee = (amount * sellFee) / 10000;
        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the contract owner
        _transfer(sender, owner(), fee);
        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountAfterFee);

        // Update allowance
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);

        return true;
    }
}
```
