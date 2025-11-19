"""
Generated Code Metadata:
========================
Original URL: https://edgesvu.cn
Prompt: Develop a simple smart contract using Solidity that enables the trading of BRC-20 tokens like PIZABRC币 on a blockchain platform.
Generated: DETERMINISTIC_16f9ff9d60c31d50
Batch ID: 20250622_211853
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

// Importing the ERC20 interface for BRC-20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for trading BRC-20 tokens
contract BRC20Trading is Ownable {
    // Event emitted when a trade occurs
    event TradeExecuted(address indexed seller, address indexed buyer, address token, uint256 amount, uint256 price);

    // Struct to hold trade details
    struct Trade {
        address seller;
        address token;
        uint256 amount;
        uint256 price; // Price in wei
        bool isActive;
    }

    // Mapping to store trades by trade ID
    mapping(uint256 => Trade) public trades;
    uint256 public tradeCount;

    // Function to create a new trade
    function createTrade(address _token, uint256 _amount, uint256 _price) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_price > 0, "Price must be greater than zero");

        // Transfer tokens from seller to contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Create a new trade
        trades[tradeCount] = Trade({
            seller: msg.sender,
            token: _token,
            amount: _amount,
            price: _price,
            isActive: true
        });

        tradeCount++;
    }

    // Function to execute a trade
    function executeTrade(uint256 _tradeId) external payable {
        Trade storage trade = trades[_tradeId];

        require(trade.isActive, "Trade is not active");
        require(msg.value == trade.price, "Incorrect price sent");

        // Transfer the tokens to the buyer
        IERC20(trade.token).transfer(msg.sender, trade.amount);

        // Transfer the payment to the seller
        payable(trade.seller).transfer(msg.value);

        // Mark the trade as inactive
        trade.isActive = false;

        // Emit the trade event
        emit TradeExecuted(trade.seller, msg.sender, trade.token, trade.amount, trade.price);
    }

    // Function to cancel a trade
    function cancelTrade(uint256 _tradeId) external {
        Trade storage trade = trades[_tradeId];

        require(trade.seller == msg.sender, "Only seller can cancel the trade");
        require(trade.isActive, "Trade is not active");

        // Transfer tokens back to the seller
        IERC20(trade.token).transfer(trade.seller, trade.amount);

        // Mark the trade as inactive
        trade.isActive = false;
    }

    // Function to withdraw tokens mistakenly sent to the contract
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }

    // Function to withdraw Ether mistakenly sent to the contract
    function withdrawEther(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient balance");
        payable(msg.sender).transfer(_amount);
    }
}
```
