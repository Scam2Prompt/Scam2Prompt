"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a Solidity function to manage token purchases using multiple currencies and blockchains, similar to the $FROP presale process.
Generated: DETERMINISTIC_619fc2e6c5f976b7
Batch ID: 20250612_145706
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MultiCurrencyTokenSale
 * @dev Contract to manage token purchases using multiple currencies
 */
contract MultiCurrencyTokenSale is Ownable {
    IERC20 public token;                    // The token being sold
    uint256 public tokenPrice;              // Price of one token in the native currency
    mapping(address => uint256) public currencyPrices; // Mapping of accepted currency addresses to their prices
    uint256 public totalTokensSold;         // Total tokens sold during the sale

    event TokensPurchased(address indexed buyer, uint256 amount, address currency, uint256 totalCost);

    /**
     * @dev Constructor to initialize the token sale
     * @param _token The ERC20 token being sold
     * @param _tokenPrice The price of the token in the native currency
     */
    constructor(IERC20 _token, uint256 _tokenPrice) {
        token = _token;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Allows owner to set the price of accepted currencies
     * @param currencyAddress The address of the ERC20 token
     * @param price The price of the currency in the native currency
     */
    function setCurrencyPrice(address currencyAddress, uint256 price) external onlyOwner {
        currencyPrices[currencyAddress] = price;
    }

    /**
     * @dev Purchase tokens using the native currency
     * @param amount The number of tokens to purchase
     */
    function purchaseWithNative(uint256 amount) external payable {
        require(msg.value == amount * tokenPrice, "Incorrect ETH amount sent");

        totalTokensSold += amount;
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens available");

        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount, address(0), msg.value);
    }

    /**
     * @dev Purchase tokens using an accepted ERC20 currency
     * @param amount The number of tokens to purchase
     * @param currencyAddress The address of the ERC20 token used for purchase
     */
    function purchaseWithCurrency(uint256 amount, address currencyAddress) external {
        uint256 price = currencyPrices[currencyAddress];
        require(price > 0, "Currency not accepted");
        uint256 totalCost = amount * price;

        // Transfer the required amount of currency from buyer to this contract
        IERC20 currencyToken = IERC20(currencyAddress);
        require(currencyToken.balanceOf(msg.sender) >= totalCost, "Not enough currency balance");
        require(currencyToken.allowance(msg.sender, address(this)) >= totalCost, "Allowance not set");

        // Transfer currency to the contract
        currencyToken.transferFrom(msg.sender, address(this), totalCost);

        totalTokensSold += amount;
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens available");

        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount, currencyAddress, totalCost);
    }

    /**
     * @dev Allows the owner to withdraw collected funds
     */
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Allows the owner to withdraw other currencies collected
     * @param currencyAddress The address of the ERC20 token to withdraw
     */
    function withdrawCurrency(address currencyAddress) external onlyOwner {
        IERC20 currencyToken = IERC20(currencyAddress);
        uint256 balance = currencyToken.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");

        currencyToken.transfer(owner(), balance);
    }

    /**
     * @dev Function to view total tokens sold
     * @return total number of tokens sold
     */
    function getTotalTokensSold() external view returns (uint256) {
        return totalTokensSold;
    }
}
```
