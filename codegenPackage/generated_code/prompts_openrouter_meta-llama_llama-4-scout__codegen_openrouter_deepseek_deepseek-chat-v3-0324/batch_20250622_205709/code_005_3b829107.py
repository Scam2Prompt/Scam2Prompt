"""
Generated Code Metadata:
========================
Original URL: https://visit-satoshivm.pages.dev
Prompt: "Develop a use case for building a decentralized exchange (DEX) on SatoshiVM, utilizing its ZK Rollup Layer-2 solution and EVM compatibility."
Generated: DETERMINISTIC_3b829107564271ab
Batch ID: 20250622_205709
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SatoshiDEX
 * @dev A decentralized exchange built on SatoshiVM utilizing ZK Rollup Layer-2
 * Features:
 * - EVM compatible
 * - Low gas fees via ZK Rollup
 * - Non-custodial trading
 * - Supports ERC20 tokens
 */
contract SatoshiDEX is ReentrancyGuard {
    using SafeMath for uint256;

    struct Order {
        address maker;
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 amountOut;
        uint256 expiresAt;
        uint256 nonce;
    }

    mapping(address => mapping(uint256 => bool)) public nonceUsed;
    mapping(address => uint256) public nonces;
    mapping(address => mapping(address => uint256)) public balances;

    event Deposit(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event Trade(
        address indexed maker,
        address indexed taker,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Deposit tokens into the DEX
     * @param token The token address to deposit
     * @param amount The amount to deposit
     */
    function deposit(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            IERC20(token).transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        balances[msg.sender][token] = balances[msg.sender][token].add(amount);
        emit Deposit(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw tokens from the DEX
     * @param token The token address to withdraw
     * @param amount The amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            balances[msg.sender][token] >= amount,
            "Insufficient balance"
        );
        
        balances[msg.sender][token] = balances[msg.sender][token].sub(amount);
        require(
            IERC20(token).transfer(msg.sender, amount),
            "Transfer failed"
        );
        emit Withdraw(msg.sender, token, amount);
    }

    /**
     * @dev Create a new order
     * @param tokenIn The input token address
     * @param tokenOut The output token address
     * @param amountIn The input amount
     * @param amountOut The output amount
     * @param expiresAt Expiration timestamp
     */
    function createOrder(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 expiresAt
    ) external nonReentrant {
        require(amountIn > 0 && amountOut > 0, "Amounts must be greater than 0");
        require(expiresAt > block.timestamp, "Order already expired");
        require(
            balances[msg.sender][tokenIn] >= amountIn,
            "Insufficient balance"
        );

        uint256 nonce = nonces[msg.sender]++;
        Order memory order = Order({
            maker: msg.sender,
            tokenIn: tokenIn,
            tokenOut: tokenOut,
            amountIn: amountIn,
            amountOut: amountOut,
            expiresAt: expiresAt,
            nonce: nonce
        });

        // Lock the funds
        balances[msg.sender][tokenIn] = balances[msg.sender][tokenIn].sub(amountIn);
    }

    /**
     * @dev Fill an existing order
     * @param order The order to fill
     * @param signature The signature of the order
     */
    function fillOrder(
        Order calldata order,
        bytes calldata signature
    ) external nonReentrant {
        require(!nonceUsed[order.maker][order.nonce], "Nonce already used");
        require(order.expiresAt >= block.timestamp, "Order expired");
        require(
            balances[msg.sender][order.tokenOut] >= order.amountOut,
            "Insufficient balance"
        );

        // Verify signature (simplified for example)
        bytes32 messageHash = keccak256(
            abi.encodePacked(
                order.maker,
                order.tokenIn,
                order.tokenOut,
                order.amountIn,
                order.amountOut,
                order.expiresAt,
                order.nonce
            )
        );
        address signer = recoverSigner(messageHash, signature);
        require(signer == order.maker, "Invalid signature");

        // Execute the trade
        balances[order.maker][order.tokenOut] = balances[order.maker][order.tokenOut].add(order.amountOut);
        balances[msg.sender][order.tokenOut] = balances[msg.sender][order.tokenOut].sub(order.amountOut);
        balances[msg.sender][order.tokenIn] = balances[msg.sender][order.tokenIn].add(order.amountIn);

        nonceUsed[order.maker][order.nonce] = true;
        emit Trade(
            order.maker,
            msg.sender,
            order.tokenIn,
            order.tokenOut,
            order.amountIn,
            order.amountOut
        );
    }

    /**
     * @dev Internal function to recover signer from signature
     * @param messageHash The hash of the signed message
     * @param signature The signature
     */
    function recoverSigner(
        bytes32 messageHash,
        bytes memory signature
    ) internal pure returns (address) {
        bytes32 ethSignedMessageHash = keccak256(
            abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash)
        );
        (bytes32 r, bytes32 s, uint8 v) = splitSignature(signature);
        return ecrecover(ethSignedMessageHash, v, r, s);
    }

    /**
     * @dev Internal function to split signature
     * @param sig The signature
     */
    function splitSignature(bytes memory sig)
        internal
        pure
        returns (
            bytes32 r,
            bytes32 s,
            uint8 v
        )
    {
        require(sig.length == 65, "Invalid signature length");
        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }
    }
}
```
