"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://navigatorsonic.exchange
Prompt: Provide an example of how to use Navigator Exchange's open-source smart contracts to ensure transparency and security in trading operations.
Generated: DETERMINISTIC_0af558d640d97236
Batch ID: 20250612_154029
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

// Importing the required libraries and contracts from Navigator Exchange
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for managing trades on the Navigator Exchange
contract NavigatorExchange is Ownable {
    using SafeMath for uint256; // Using SafeMath for safe arithmetic

    // Event emitted when a trade is created
    event TradeCreated(
        address indexed trader,
        uint256 indexed tradeId,
        address indexed token,
        uint256 amount,
        uint256 price
    );

    // Event emitted when a trade is executed
    event TradeExecuted(
        address indexed trader,
        uint256 indexed tradeId,
        address indexed token,
        uint256 amount,
        uint256 price
    );

    // Struct to represent a trade
    struct Trade {
        address trader;
        address token;
        uint256 amount;
        uint256 price; // Price per token in wei
        bool isActive;
    }

    // Mapping of trade ID to trade details
    mapping(uint256 => Trade) public trades;
    uint256 public tradeCounter; // Counter to keep track of trade IDs

    // Modifier to check if the trade exists
    modifier tradeExists(uint256 _tradeId) {
        require(trades[_tradeId].trader != address(0), "Trade does not exist");
        _;
    }

    // Function to create a trade
    function createTrade(address _token, uint256 _amount, uint256 _price) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_price > 0, "Price must be greater than 0");

        // Transfer tokens from trader to contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Increment trade counter and create new trade
        tradeCounter++;
        trades[tradeCounter] = Trade({
            trader: msg.sender,
            token: _token,
            amount: _amount,
            price: _price,
            isActive: true
        });

        emit TradeCreated(msg.sender, tradeCounter, _token, _amount, _price);
    }

    // Function to execute a trade
    function executeTrade(uint256 _tradeId) external tradeExists(_tradeId) {
        Trade storage trade = trades[_tradeId];
        
        require(trade.isActive, "Trade is not active");
        require(msg.sender != trade.trader, "Trader cannot execute their own trade");

        // Calculate total cost
        uint256 totalCost = trade.amount.mul(trade.price);

        // Transfer the amount of tokens to the trader
        IERC20(trade.token).transfer(msg.sender, trade.amount);
        // Transfer ETH to the trader's address
        payable(trade.trader).transfer(totalCost);

        // Mark the trade as inactive
        trade.isActive = false;

        emit TradeExecuted(msg.sender, _tradeId, trade.token, trade.amount, trade.price);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
