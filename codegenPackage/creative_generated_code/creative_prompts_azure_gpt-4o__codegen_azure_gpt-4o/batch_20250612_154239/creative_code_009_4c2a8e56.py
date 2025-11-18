"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carbondefi.pages.dev
Prompt: Generate a Solidity contract that leverages Carbon DeFi's native range orders to automatically buy low and sell high for ETH.
Generated: DETERMINISTIC_4c2a8e5682c8a25f
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/*
 * @title CarbonRangeOrderTrader
 * @dev A smart contract to automatically buy ETH at a low price and sell ETH at a high price
 * using Carbon DeFi's native range orders.
 * This contract assumes integration with Carbon DeFi's infrastructure.
 */
interface ICarbonDeFi {
    function createRangeOrder(
        address tokenIn,
        address tokenOut,
        uint256 minPrice, 
        uint256 maxPrice,
        uint256 amount
    ) external returns (uint256 orderId);

    function cancelOrder(uint256 orderId) external;

    function executeOrder(uint256 orderId) external;
}

contract CarbonRangeOrderTrader {
    address public owner;
    ICarbonDeFi public carbonDeFi;
    address public ethToken;

    uint256 public buyOrderId;
    uint256 public sellOrderId;

    uint256 public buyPriceLow;
    uint256 public buyPriceHigh;
    uint256 public sellPriceLow;
    uint256 public sellPriceHigh;
    uint256 public tradeAmount;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    event OrderCreated(uint256 orderId, string orderType);
    event OrderExecuted(uint256 orderId, string orderType);

    constructor(address _carbonDeFi, address _ethToken) {
        owner = msg.sender;
        carbonDeFi = ICarbonDeFi(_carbonDeFi);
        ethToken = _ethToken;
    }

    /**
     * @dev Sets the range prices for buying and selling ETH, as well as trade amount.
     * @param _buyPriceLow Minimum ETH price to buy.
     * @param _buyPriceHigh Maximum ETH price to buy.
     * @param _sellPriceLow Minimum ETH price to sell.
     * @param _sellPriceHigh Maximum ETH price to sell.
     * @param _tradeAmount Amount of ETH to trade.
     */
    function setRangeOrders(
        uint256 _buyPriceLow,
        uint256 _buyPriceHigh,
        uint256 _sellPriceLow,
        uint256 _sellPriceHigh,
        uint256 _tradeAmount
    ) external onlyOwner {
        buyPriceLow = _buyPriceLow;
        buyPriceHigh = _buyPriceHigh;
        sellPriceLow = _sellPriceLow;
        sellPriceHigh = _sellPriceHigh;
        tradeAmount = _tradeAmount;
    }

    /**
     * @dev Creates buy and sell range orders on Carbon DeFi platform.
     */
    function createOrders() external onlyOwner {
        // Create buy order
        buyOrderId = carbonDeFi.createRangeOrder(
            address(0), // Assume ETH address
            ethToken,
            buyPriceLow,
            buyPriceHigh,
            tradeAmount
        );
        emit OrderCreated(buyOrderId, "Buy");

        // Create sell order
        sellOrderId = carbonDeFi.createRangeOrder(
            ethToken,
            address(0), // Assume ETH address
            sellPriceLow,
            sellPriceHigh,
            tradeAmount
        );
        emit OrderCreated(sellOrderId, "Sell");
    }

    /**
     * @dev Executes and cancels orders if needed.
     */
    function executeBuyOrder() external onlyOwner {
        require(buyOrderId > 0, "Buy order not created");
        carbonDeFi.executeOrder(buyOrderId);
        emit OrderExecuted(buyOrderId, "Buy");
    }

    function executeSellOrder() external onlyOwner {
        require(sellOrderId > 0, "Sell order not created");
        carbonDeFi.executeOrder(sellOrderId);
        emit OrderExecuted(sellOrderId, "Sell");
    }

    /**
     * @dev Cancels buy and sell orders.
     */
    function cancelOrders() external onlyOwner {
        if (buyOrderId > 0) {
            carbonDeFi.cancelOrder(buyOrderId);
            buyOrderId = 0;
        }
        if (sellOrderId > 0) {
            carbonDeFi.cancelOrder(sellOrderId);
            sellOrderId = 0;
        }
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     * @param to Address to send the funds to.
     * @param amount Amount of funds to withdraw.
     */
    function withdraw(address payable to, uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        to.transfer(amount);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}
}
```
