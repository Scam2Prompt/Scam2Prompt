"""
Generated Code Metadata:
========================
Original URL: https://navigatorsonic.exchange
Prompt: Provide an example of how to use Navigator Exchange's open-source smart contracts to ensure transparency and security in trading operations.
Generated: DETERMINISTIC_0af558d640d97236
Batch ID: 20250612_154029
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title TransparentExchange
 * @dev A transparent and secure trading contract using Navigator Exchange principles
 */
contract TransparentExchange is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Order {
        address maker;
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 amountOut;
        uint256 expiry;
        bool filled;
    }

    mapping(bytes32 => Order) public orders;
    mapping(address => uint256) public feesCollected;
    uint256 public feeBasisPoints = 10; // 0.1% fee

    event OrderCreated(
        bytes32 orderId,
        address indexed maker,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 expiry
    );

    event OrderFilled(
        bytes32 orderId,
        address indexed maker,
        address indexed taker,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 feeAmount
    );

    event FeeWithdrawn(address indexed token, uint256 amount);

    /**
     * @dev Create a new order
     * @param tokenIn The token being offered
     * @param tokenOut The token requested
     * @param amountIn Amount of tokenIn offered
     * @param amountOut Amount of tokenOut requested
     * @param expiry Order expiry timestamp
     */
    function createOrder(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 expiry
    ) external {
        require(amountIn > 0, "AmountIn must be positive");
        require(amountOut > 0, "AmountOut must be positive");
        require(expiry > block.timestamp, "Expiry must be in the future");

        bytes32 orderId = keccak256(
            abi.encodePacked(
                msg.sender,
                tokenIn,
                tokenOut,
                amountIn,
                amountOut,
                expiry,
                block.timestamp
            )
        );

        orders[orderId] = Order({
            maker: msg.sender,
            tokenIn: tokenIn,
            tokenOut: tokenOut,
            amountIn: amountIn,
            amountOut: amountOut,
            expiry: expiry,
            filled: false
        });

        IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), amountIn);

        emit OrderCreated(
            orderId,
            msg.sender,
            tokenIn,
            tokenOut,
            amountIn,
            amountOut,
            expiry
        );
    }

    /**
     * @dev Fill an existing order
     * @param orderId The ID of the order to fill
     */
    function fillOrder(bytes32 orderId) external nonReentrant {
        Order storage order = orders[orderId];
        require(order.maker != address(0), "Order does not exist");
        require(!order.filled, "Order already filled");
        require(block.timestamp < order.expiry, "Order expired");

        uint256 feeAmount = (order.amountOut * feeBasisPoints) / 10000;
        uint256 amountOutAfterFee = order.amountOut - feeAmount;

        IERC20(order.tokenOut).safeTransferFrom(
            msg.sender,
            order.maker,
            amountOutAfterFee
        );
        IERC20(order.tokenOut).safeTransferFrom(
            msg.sender,
            address(this),
            feeAmount
        );
        IERC20(order.tokenIn).safeTransfer(msg.sender, order.amountIn);

        feesCollected[order.tokenOut] += feeAmount;
        order.filled = true;

        emit OrderFilled(
            orderId,
            order.maker,
            msg.sender,
            order.tokenIn,
            order.tokenOut,
            order.amountIn,
            order.amountOut,
            feeAmount
        );
    }

    /**
     * @dev Withdraw collected fees (owner only)
     * @param token The token to withdraw fees for
     */
    function withdrawFees(address token) external onlyOwner {
        uint256 amount = feesCollected[token];
        require(amount > 0, "No fees to withdraw");

        feesCollected[token] = 0;
        IERC20(token).safeTransfer(msg.sender, amount);

        emit FeeWithdrawn(token, amount);
    }

    /**
     * @dev Update the fee basis points (owner only)
     * @param newFeeBasisPoints New fee basis points (1 = 0.01%)
     */
    function setFeeBasisPoints(uint256 newFeeBasisPoints) external onlyOwner {
        require(newFeeBasisPoints <= 100, "Fee cannot exceed 1%");
        feeBasisPoints = newFeeBasisPoints;
    }
}
```
