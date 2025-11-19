"""
Generated Code Metadata:
========================
Original URL: https://ethereumcv.io
Prompt: Develop a Solidity-based decentralized exchange smart contract for Ethereum Classic Vision, incorporating features mentioned in the ETCV white paper.
Generated: DETERMINISTIC_c55a8ab80f997f1b
Batch ID: 20250612_151847
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Decentralized Exchange Smart Contract for Ethereum Classic Vision (ETCV)
 * @author [Your Name]
 * @notice This contract enables decentralized trading of ETCV tokens.
 */
contract DecentralizedExchange {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of token pairs
    mapping(address => mapping(address => Pair)) public tokenPairs;

    // Mapping of user orders
    mapping(address => mapping(uint256 => Order)) public userOrders;

    // Mapping of order IDs to order status
    mapping(uint256 => bool) public orderStatus;

    // Event emitted when a new token pair is created
    event NewTokenPair(address indexed token1, address indexed token2);

    // Event emitted when a new order is created
    event NewOrder(address indexed user, uint256 orderId);

    // Event emitted when an order is filled
    event OrderFilled(uint256 orderId);

    // Event emitted when an order is cancelled
    event OrderCancelled(uint256 orderId);

    // Struct representing a token pair
    struct Pair {
        address token1;
        address token2;
        uint256 reserve1;
        uint256 reserve2;
    }

    // Struct representing an order
    struct Order {
        address user;
        uint256 token1Amount;
        uint256 token2Amount;
        uint256 orderType; // 0: buy, 1: sell
        uint256 status; // 0: open, 1: filled, 2: cancelled
    }

    /**
     * @notice Creates a new token pair
     * @param token1 Address of the first token
     * @param token2 Address of the second token
     */
    function createTokenPair(address token1, address token2) public {
        require(token1 != token2, "Tokens must be different");
        require(tokenPairs[token1][token2].token1 == address(0), "Token pair already exists");

        tokenPairs[token1][token2] = Pair(token1, token2, 0, 0);
        tokenPairs[token2][token1] = Pair(token2, token1, 0, 0);

        emit NewTokenPair(token1, token2);
    }

    /**
     * @notice Creates a new order
     * @param token1 Address of the first token
     * @param token2 Address of the second token
     * @param token1Amount Amount of the first token
     * @param token2Amount Amount of the second token
     * @param orderType Type of the order (0: buy, 1: sell)
     */
    function createOrder(address token1, address token2, uint256 token1Amount, uint256 token2Amount, uint256 orderType) public {
        require(tokenPairs[token1][token2].token1 != address(0), "Token pair does not exist");
        require(token1Amount > 0 && token2Amount > 0, "Amounts must be greater than zero");
        require(orderType == 0 || orderType == 1, "Invalid order type");

        uint256 orderId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        userOrders[msg.sender][orderId] = Order(msg.sender, token1Amount, token2Amount, orderType, 0);
        orderStatus[orderId] = true;

        emit NewOrder(msg.sender, orderId);
    }

    /**
     * @notice Fills an order
     * @param orderId ID of the order to fill
     */
    function fillOrder(uint256 orderId) public {
        require(orderStatus[orderId], "Order does not exist");
        require(userOrders[msg.sender][orderId].status == 0, "Order is not open");

        Order memory order = userOrders[msg.sender][orderId];

        if (order.orderType == 0) {
            // Buy order
            require(tokenPairs[order.token1][order.token2].reserve1 >= order.token1Amount, "Insufficient reserve");
            require(tokenPairs[order.token1][order.token2].reserve2 >= order.token2Amount, "Insufficient reserve");

            tokenPairs[order.token1][order.token2].reserve1 = tokenPairs[order.token1][order.token2].reserve1.sub(order.token1Amount);
            tokenPairs[order.token1][order.token2].reserve2 = tokenPairs[order.token1][order.token2].reserve2.sub(order.token2Amount);

            IERC20(order.token1).safeTransfer(order.user, order.token1Amount);
            IERC20(order.token2).safeTransfer(msg.sender, order.token2Amount);
        } else {
            // Sell order
            require(tokenPairs[order.token1][order.token2].reserve1 >= order.token2Amount, "Insufficient reserve");
            require(tokenPairs[order.token1][order.token2].reserve2 >= order.token1Amount, "Insufficient reserve");

            tokenPairs[order.token1][order.token2].reserve1 = tokenPairs[order.token1][order.token2].reserve1.sub(order.token2Amount);
            tokenPairs[order.token1][order.token2].reserve2 = tokenPairs[order.token1][order.token2].reserve2.sub(order.token1Amount);

            IERC20(order.token1).safeTransfer(msg.sender, order.token1Amount);
            IERC20(order.token2).safeTransfer(order.user, order.token2Amount);
        }

        userOrders[msg.sender][orderId].status = 1;
        orderStatus[orderId] = false;

        emit OrderFilled(orderId);
    }

    /**
     * @notice Cancels an order
     * @param orderId ID of the order to cancel
     */
    function cancelOrder(uint256 orderId) public {
        require(orderStatus[orderId], "Order does not exist");
        require(userOrders[msg.sender][orderId].status == 0, "Order is not open");

        userOrders[msg.sender][orderId].status = 2;
        orderStatus[orderId] = false;

        emit OrderCancelled(orderId);
    }

    /**
     * @notice Adds liquidity to a token pair
     * @param token1 Address of the first token
     * @param token2 Address of the second token
     * @param token1Amount Amount of the first token
     * @param token2Amount Amount of the second token
     */
    function addLiquidity(address token1, address token2, uint256 token1Amount, uint256 token2Amount) public {
        require(tokenPairs[token1][token2].token1 != address(0), "Token pair does not exist");
        require(token1Amount > 0 && token2Amount > 0, "Amounts must be greater than zero");

        tokenPairs[token1][token2].reserve1 = tokenPairs[token1][token2].reserve1.add(token1Amount);
        tokenPairs[token1][token2].reserve2 = tokenPairs[token1][token2].reserve2.add(token2Amount);

        IERC20(token1).safeTransferFrom(msg.sender, address(this), token1Amount);
        IERC20(token2).safeTransferFrom(msg.sender, address(this), token2Amount);
    }

    /**
     * @notice Removes liquidity from a token pair
     * @param token1 Address of the first token
     * @param token2 Address of the second token
     * @param token1Amount Amount of the first token
     * @param token2Amount Amount of the second token
     */
    function removeLiquidity(address token1, address token2, uint256 token1Amount, uint256 token2Amount) public {
        require(tokenPairs[token1][token2].token1 != address(0), "Token pair does not exist");
        require(token1Amount > 0 && token2Amount > 0, "Amounts must be greater than zero");

        require(tokenPairs[token1][token2].reserve1 >= token1Amount, "Insufficient reserve");
        require(tokenPairs[token1][token2].reserve2 >= token2Amount, "Insufficient reserve");

        tokenPairs[token1][token2].reserve1 = tokenPairs[token1][token2].reserve1.sub(token1Amount);
        tokenPairs[token1][token2].reserve2 = tokenPairs[token1][token2].reserve2.sub(token2Amount);

        IERC20(token1).safeTransfer(msg.sender, token1Amount);
        IERC20(token2).safeTransfer(msg.sender, token2Amount);
    }
}
```
