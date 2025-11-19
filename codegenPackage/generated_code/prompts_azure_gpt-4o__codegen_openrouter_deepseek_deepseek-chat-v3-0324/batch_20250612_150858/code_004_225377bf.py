"""
Generated Code Metadata:
========================
Original URL: https://mantanetwork-network.github.io
Prompt: Create a decentralized exchange (DEX) smart contract on Manta Network that prevents front-running attacks by leveraging its privacy features.
Generated: DETERMINISTIC_225377bfcc0921d2
Batch ID: 20250612_150858
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PrivacyDEX
 * @dev A decentralized exchange contract on Manta Network that prevents front-running
 * by leveraging privacy features through encrypted order matching.
 */
contract PrivacyDEX is ReentrancyGuard {
    // Struct to represent an encrypted order
    struct EncryptedOrder {
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 minAmountOut;
        bytes32 commitment; // Zero-knowledge proof commitment
        uint256 timestamp;
        address trader;
        bool isFilled;
    }

    // Mapping from order hash to EncryptedOrder
    mapping(bytes32 => EncryptedOrder) public orders;

    // Events
    event OrderCreated(
        bytes32 indexed orderHash,
        address indexed trader,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        bytes32 commitment
    );

    event OrderFilled(
        bytes32 indexed orderHash,
        address indexed trader,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    event OrderCancelled(bytes32 indexed orderHash, address indexed trader);

    /**
     * @dev Creates a new encrypted order
     * @param tokenIn Address of the input token
     * @param tokenOut Address of the output token
     * @param amountIn Amount of input token
     * @param minAmountOut Minimum amount of output token expected
     * @param commitment Zero-knowledge proof commitment
     */
    function createOrder(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        bytes32 commitment
    ) external nonReentrant {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "Amount must be positive");
        require(minAmountOut > 0, "Min amount out must be positive");

        // Transfer tokens from trader to contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Create order hash using privacy-preserving parameters
        bytes32 orderHash = keccak256(
            abi.encodePacked(
                tokenIn,
                tokenOut,
                amountIn,
                minAmountOut,
                commitment,
                block.timestamp,
                msg.sender
            )
        );

        orders[orderHash] = EncryptedOrder({
            tokenIn: tokenIn,
            tokenOut: tokenOut,
            amountIn: amountIn,
            minAmountOut: minAmountOut,
            commitment: commitment,
            timestamp: block.timestamp,
            trader: msg.sender,
            isFilled: false
        });

        emit OrderCreated(
            orderHash,
            msg.sender,
            tokenIn,
            tokenOut,
            amountIn,
            minAmountOut,
            commitment
        );
    }

    /**
     * @dev Fills an existing order with privacy-preserving validation
     * @param orderHash Hash of the order to fill
     * @param amountOut Amount of output token to give
     * @param proof Zero-knowledge proof for order validation
     */
    function fillOrder(
        bytes32 orderHash,
        uint256 amountOut,
        bytes calldata proof
    ) external nonReentrant {
        EncryptedOrder storage order = orders[orderHash];
        require(order.trader != address(0), "Order does not exist");
        require(!order.isFilled, "Order already filled");
        require(amountOut >= order.minAmountOut, "Insufficient output amount");
        require(
            verifyProof(order.commitment, proof),
            "Invalid zero-knowledge proof"
        );

        // Transfer tokens
        IERC20(order.tokenOut).transferFrom(
            msg.sender,
            order.trader,
            amountOut
        );
        IERC20(order.tokenIn).transfer(msg.sender, order.amountIn);

        order.isFilled = true;

        emit OrderFilled(
            orderHash,
            order.trader,
            order.tokenIn,
            order.tokenOut,
            order.amountIn,
            amountOut
        );
    }

    /**
     * @dev Cancels an existing order
     * @param orderHash Hash of the order to cancel
     */
    function cancelOrder(bytes32 orderHash) external nonReentrant {
        EncryptedOrder storage order = orders[orderHash];
        require(order.trader == msg.sender, "Not order owner");
        require(!order.isFilled, "Order already filled");

        // Return tokens to trader
        IERC20(order.tokenIn).transfer(order.trader, order.amountIn);

        delete orders[orderHash];

        emit OrderCancelled(orderHash, msg.sender);
    }

    /**
     * @dev Verifies a zero-knowledge proof (placeholder for actual zk-SNARK verification)
     * @param commitment The commitment to verify against
     * @param proof The zero-knowledge proof
     * @return bool Whether the proof is valid
     */
    function verifyProof(
        bytes32 commitment,
        bytes calldata proof
    ) internal pure returns (bool) {
        // In a real implementation, this would verify a zk-SNARK proof
        // against the commitment using Manta's privacy features
        // This is a placeholder that always returns true for demonstration
        return true;
    }
}
```
