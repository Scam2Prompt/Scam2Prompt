"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pingu-exchange.vercel.app
Prompt: Provide an example of how to use Pingu Exchange for on-chain trading in a smart contract.
Generated: DETERMINISTIC_30239e34cf054ba7
Batch ID: 20250612_152924
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

/**
 * @title PinguExchangeOnChainTrading
 * @dev This contract demonstrates an example of on-chain trading using the Pingu Exchange protocol.
 * Note: Pingu Exchange is assumed to have a specific contract API. Replace placeholder names and functions
 * with the actual API of the protocol you intend to use.
 */
interface IPinguExchange {
    /**
     * @dev Swaps tokens in the Pingu Exchange.
     * @param tokenIn Address of the token to swap from.
     * @param tokenOut Address of the token to swap to.
     * @param amountIn Amount of tokenIn to swap.
     * @param amountOutMin Minimum amount of tokenOut to receive.
     * @param recipient Address to receive the swapped tokens.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address recipient
    ) external returns (uint256);
}

contract PinguExchangeTrading {
    // Address of the Pingu Exchange contract
    address private immutable pinguExchange;

    // Constructor to set the Pingu Exchange contract address
    constructor(address _pinguExchange) {
        require(_pinguExchange != address(0), "Invalid Pingu Exchange address");
        pinguExchange = _pinguExchange;
    }

    /**
     * @notice Perform a token swap on Pingu Exchange.
     * @param tokenIn Address of the token to swap from.
     * @param tokenOut Address of the token to swap to.
     * @param amountIn Amount of tokenIn to swap.
     * @param amountOutMin Minimum amount of tokenOut to receive.
     */
    function tradeTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin
    ) external {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "AmountIn must be greater than 0");

        // Transfer the input tokens to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Pingu Exchange to spend the input tokens
        IERC20(tokenIn).approve(pinguExchange, amountIn);

        // Call the Pingu Exchange to perform the swap
        uint256 amountOut = IPinguExchange(pinguExchange).swapTokens(
            tokenIn,
            tokenOut,
            amountIn,
            amountOutMin,
            msg.sender // Send the swapped tokens directly to the sender
        );

        require(amountOut >= amountOutMin, "Insufficient output amount");
    }
}

/**
 * @dev Minimal interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
