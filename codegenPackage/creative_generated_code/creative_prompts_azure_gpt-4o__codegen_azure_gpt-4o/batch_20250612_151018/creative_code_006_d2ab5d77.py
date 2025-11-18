"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dex-3kl6ea5or-thorswap.vercel.app
Prompt: Develop a smart contract that interacts with THORChain to facilitate decentralized token swaps via THORSwap.
Generated: DETERMINISTIC_d2ab5d77751baecc
Batch ID: 20250612_151018
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
 * @title ThorSwapTokenSwap
 * @dev A smart contract to interact with THORChain to facilitate token swaps via THORSwap.
 * @notice This contract allows users to perform decentralized token swaps by interacting with THORChain.
 */
contract ThorSwapTokenSwap {
    // Address of the THORChain router contract
    address public immutable thorRouter;

    // Event emitted when a swap is successfully initiated
    event SwapInitiated(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        bytes memo
    );

    /**
     * @dev Constructor sets the THORChain router address.
     * @param _thorRouter Address of the THORChain router contract.
     */
    constructor(address _thorRouter) {
        require(_thorRouter != address(0), "Invalid router address");
        thorRouter = _thorRouter;
    }

    /**
     * @dev Perform a token swap on THORChain via THORSwap.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the desired output token.
     * @param amountIn Amount of input token to swap.
     * @param amountOutMin Minimum acceptable amount of output token to receive.
     * @param memo A memo for THORChain detailing the swap specifics.
     */
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        bytes calldata memo
    ) external payable {
        require(tokenIn != address(0), "Invalid input token address");
        require(tokenOut != address(0), "Invalid output token address");
        require(amountIn > 0, "Amount must be greater than zero");
        require(bytes(memo).length > 0, "Memo cannot be empty");

        // Transfer the input tokens from the sender to the contract
        require(
            IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn),
            "Token transfer failed"
        );

        // Approve the THORChain router to spend the tokens
        require(
            IERC20(tokenIn).approve(thorRouter, amountIn),
            "Token approval failed"
        );

        // Call THORChain router contract to initiate the swap
        (bool success, ) = thorRouter.call{value: msg.value}(
            abi.encodeWithSignature(
                "swap(address,address,uint256,uint256,bytes)",
                tokenIn,
                tokenOut,
                amountIn,
                amountOutMin,
                memo
            )
        );

        require(success, "Swap failed");

        // Emit event for successful swap initiation
        emit SwapInitiated(
            msg.sender,
            tokenIn,
            tokenOut,
            amountIn,
            amountOutMin,
            memo
        );
    }

    /**
     * @dev Fallback function to receive native tokens (e.g., RUNE).
     */
    receive() external payable {
        // Accept native tokens sent to the contract
    }
}

/**
 * @dev Interface for ERC20 tokens.
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
