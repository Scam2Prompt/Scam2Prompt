"""
Generated Code Metadata:
========================
Original URL: https://cowswap.io
Prompt: "Design a smart contract for a cryptocurrency swap platform inspired by CowSwap's architecture on Ethereum blockchain."
Generated: DETERMINISTIC_9f465a22795a1cdb
Batch ID: 20250622_211541
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

/**
 * @title CryptoSwap
 * @dev A smart contract for swapping cryptocurrencies inspired by CowSwap's architecture.
 *      This contract allows users to create and fulfill swap orders securely.
 */
contract CryptoSwap {
    // Struct to represent a swap order
    struct SwapOrder {
        address maker; // Address of the order creator
        address tokenIn; // Token to be swapped (input token)
        address tokenOut; // Token to be received (output token)
        uint256 amountIn; // Amount of input token
        uint256 amountOutMin; // Minimum amount of output token expected
        uint256 expiration; // Expiration timestamp of the order
        bool fulfilled; // Whether the order has been fulfilled
    }

    // Mapping to store swap orders by ID
    mapping(uint256 => SwapOrder) public orders;

    // Counter for order IDs
    uint256 public orderCounter;

    // Events
    event OrderCreated(
        uint256 indexed orderId,
        address indexed maker,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 expiration
    );
    event OrderFulfilled(uint256 indexed orderId, address indexed fulfiller);
    event OrderCancelled(uint256 indexed orderId);

    /**
     * @dev Creates a new swap order.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input token to swap.
     * @param amountOutMin Minimum amount of output token expected.
     * @param expiration Expiration timestamp of the order.
     */
    function createOrder(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 expiration
    ) external {
        require(expiration > block.timestamp, "Expiration must be in the future");
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(amountOutMin > 0, "AmountOutMin must be greater than zero");

        // Transfer input tokens from the maker to the contract
        require(
            IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn),
            "Token transfer failed"
        );

        // Create a new order
        orders[orderCounter] = SwapOrder({
            maker: msg.sender,
            tokenIn: tokenIn,
            tokenOut: tokenOut,
            amountIn: amountIn,
            amountOutMin: amountOutMin,
            expiration: expiration,
            fulfilled: false
        });

        emit OrderCreated(
            orderCounter,
            msg.sender,
            tokenIn,
            tokenOut,
            amountIn,
            amountOutMin,
            expiration
        );

        // Increment the order counter
        orderCounter++;
    }

    /**
     * @dev Fulfills a swap order.
     * @param orderId ID of the order to fulfill.
     */
    function fulfillOrder(uint256 orderId) external {
        SwapOrder storage order = orders[orderId];

        require(order.maker != address(0), "Order does not exist");
        require(!order.fulfilled, "Order already fulfilled");
        require(order.expiration > block.timestamp, "Order has expired");

        // Transfer output tokens from the fulfiller to the maker
        require(
            IERC20(order.tokenOut).transferFrom(
                msg.sender,
                order.maker,
                order.amountOutMin
            ),
            "Token transfer failed"
        );

        // Transfer input tokens from the contract to the fulfiller
        require(
            IERC20(order.tokenIn).transfer(msg.sender, order.amountIn),
            "Token transfer failed"
        );

        // Mark the order as fulfilled
        order.fulfilled = true;

        emit OrderFulfilled(orderId, msg.sender);
    }

    /**
     * @dev Cancels a swap order.
     * @param orderId ID of the order to cancel.
     */
    function cancelOrder(uint256 orderId) external {
        SwapOrder storage order = orders[orderId];

        require(order.maker == msg.sender, "Only the maker can cancel the order");
        require(!order.fulfilled, "Order already fulfilled");

        // Transfer input tokens back to the maker
        require(
            IERC20(order.tokenIn).transfer(order.maker, order.amountIn),
            "Token transfer failed"
        );

        // Delete the order
        delete orders[orderId];

        emit OrderCancelled(orderId);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
