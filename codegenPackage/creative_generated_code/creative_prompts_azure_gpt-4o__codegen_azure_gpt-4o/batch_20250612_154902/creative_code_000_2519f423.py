"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-whiterock.web.app
Prompt: Write a smart contract in Solidity that implements a tokenized stock trading system similar to WhiteRock, ensuring transparency and security through OpenZeppelin audits.
Generated: DETERMINISTIC_2519f423e0e05497
Batch ID: 20250612_154902
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

// Importing OpenZeppelin libraries for security and standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title Tokenized Stock Trading System
/// @dev Implements a system for trading tokenized stocks, ensuring transparency and security.
contract TokenizedStock is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping to store stock price in USD (represented in cents for precision)
    mapping(string => uint256) public stockPrices;

    // Event emitted when a stock price is updated
    event StockPriceUpdated(string indexed stockSymbol, uint256 newPrice);

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, string stockSymbol, uint256 amount, uint256 cost);

    // Constructor to initialize the token
    /// @param name Name of the token
    /// @param symbol Symbol of the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /// @notice Update the price of a specific stock
    /// @dev Only the owner can call this function
    /// @param stockSymbol The symbol of the stock (e.g., "AAPL", "MSFT")
    /// @param newPrice The new price of the stock in cents
    function updateStockPrice(string memory stockSymbol, uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be positive");
        stockPrices[stockSymbol] = newPrice;
        emit StockPriceUpdated(stockSymbol, newPrice);
    }

    /// @notice Buy tokenized shares of a stock
    /// @param stockSymbol The symbol of the stock to buy (e.g., "AAPL", "MSFT")
    /// @param amount The amount of shares to purchase
    function buyTokens(string memory stockSymbol, uint256 amount) external payable whenNotPaused {
        uint256 stockPrice = stockPrices[stockSymbol];
        require(stockPrice > 0, "Stock not available");
        require(amount > 0, "Amount must be greater than zero");

        uint256 cost = stockPrice.mul(amount);
        require(msg.value >= cost, "Insufficient ETH sent");

        // Mint tokens to the buyer, representing the shares purchased
        _mint(msg.sender, amount);
        emit TokensPurchased(msg.sender, stockSymbol, amount, cost);

        // Refund excess ETH if any
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value.sub(cost));
        }
    }

    /// @dev Allows the owner to withdraw the contract's balance
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /// @notice Pause the contract to disable token purchases
    /// @dev Only the owner can call this function
    function pause() external onlyOwner {
        _pause();
    }

    /// @notice Unpause the contract to enable token purchases
    /// @dev Only the owner can call this function
    function unpause() external onlyOwner {
        _unpause();
    }

    /// @dev Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("ETH transfers not allowed");
    }
}
```
