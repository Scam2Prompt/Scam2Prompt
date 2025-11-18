"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexalote.org
Prompt: Create a smart contract that interacts with Dexalot to execute trades across multiple blockchains while ensuring non-custodial asset management.
Generated: DETERMINISTIC_cb4a1baecefc5d84
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title CrossChainDexalotTrader
 * @notice A smart contract for non-custodial trading across multiple blockchains using Dexalot.
 *         This contract ensures user funds are never held in custody and executes trades efficiently.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IDexalot {
    function trade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external returns (uint256 actualAmountOut);
}

interface IBridge {
    function transferTokens(
        address token,
        address recipient,
        uint256 amount,
        uint256 destinationChainId
    ) external;
}

contract CrossChainDexalotTrader is Ownable, ReentrancyGuard {
    // Dexalot trading interface
    IDexalot public dexalot;

    // Bridge interface for cross-chain token transfer
    IBridge public bridge;

    /**
     * @notice Event emitted when a trade is executed.
     * @param user Address of the user who initiated the trade.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input tokens traded.
     * @param amountOut Amount of output tokens received.
     */
    event TradeExecuted(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @notice Event emitted when tokens are sent to another blockchain.
     * @param user Address of the user who initiated the transfer.
     * @param token Address of the token transferred.
     * @param amount Amount of tokens transferred.
     * @param destinationChainId ID of the destination blockchain.
     */
    event TokensBridged(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 destinationChainId
    );

    /**
     * @notice Constructor to initialize Dexalot and bridge interfaces.
     * @param _dexalot Address of the Dexalot smart contract.
     * @param _bridge Address of the bridge smart contract.
     */
    constructor(address _dexalot, address _bridge) {
        dexalot = IDexalot(_dexalot);
        bridge = IBridge(_bridge);
    }

    /**
     * @notice Allow the owner to update the Dexalot contract address.
     * @param _dexalot New Dexalot contract address.
     */
    function setDexalot(address _dexalot) external onlyOwner {
        require(_dexalot != address(0), "Invalid Dexalot address");
        dexalot = IDexalot(_dexalot);
    }

    /**
     * @notice Allow the owner to update the bridge contract address.
     * @param _bridge New bridge contract address.
     */
    function setBridge(address _bridge) external onlyOwner {
        require(_bridge != address(0), "Invalid bridge address");
        bridge = IBridge(_bridge);
    }

    /**
     * @notice Execute a trade on Dexalot.
     * @param tokenIn Address of the token to sell.
     * @param tokenOut Address of the token to buy.
     * @param amountIn Amount of the input token to sell.
     * @param minAmountOut Minimum amount of the output token to receive.
     */
    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external nonReentrant {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "AmountIn must be greater than zero");

        // Transfer input tokens from user to contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve Dexalot to spend the input tokens
        IERC20(tokenIn).approve(address(dexalot), amountIn);

        // Execute the trade
        uint256 amountOut = dexalot.trade(tokenIn, tokenOut, amountIn, minAmountOut);
        require(amountOut >= minAmountOut, "Insufficient output amount");

        // Transfer output tokens to the user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit trade executed event
        emit TradeExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @notice Bridge tokens to another blockchain.
     * @param token Address of the token to bridge.
     * @param amount Amount of the token to bridge.
     * @param destinationChainId ID of the destination blockchain.
     */
    function bridgeTokens(
        address token,
        uint256 amount,
        uint256 destinationChainId
    ) external nonReentrant {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve bridge to spend the tokens
        IERC20(token).approve(address(bridge), amount);

        // Call the bridge contract to transfer tokens
        bridge.transferTokens(token, msg.sender, amount, destinationChainId);

        // Emit tokens bridged event
        emit TokensBridged(msg.sender, token, amount, destinationChainId);
    }

    /**
     * @notice Recover tokens sent to the contract by mistake.
     * @param token Address of the token to recover.
     * @param to Address to send the recovered tokens.
     * @param amount Amount of tokens to recover.
     */
    function recoverTokens(
        address token,
        address to,
        uint256 amount
    ) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(to, amount);
    }
}
```
