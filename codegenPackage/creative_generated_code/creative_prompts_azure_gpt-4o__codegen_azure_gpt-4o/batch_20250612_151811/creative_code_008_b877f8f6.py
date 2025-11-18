"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.cz
Prompt: Write a Solidity smart contract to interact with PancakeSwap liquidity pools and automate token swaps based on predefined conditions.
Generated: DETERMINISTIC_b877f8f6148ae992
Batch ID: 20250612_151811
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
 * @title PancakeSwap AutoSwap Contract
 * @dev Automates token swaps on PancakeSwap based on predefined conditions.
 *      This contract interacts with PancakeSwap liquidity pools via their router.
 */

interface IPancakeRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

    function getAmountsOut(uint amountIn, address[] calldata path)
        external
        view
        returns (uint[] memory amounts);
}

interface IERC20 {
    function approve(address spender, uint amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint amount) external returns (bool);
    function balanceOf(address account) external view returns (uint);
}

contract PancakeSwapAutoSwap {
    address public owner;
    IPancakeRouter public router;

    event SwapExecuted(
        address indexed user,
        address indexed fromToken,
        address indexed toToken,
        uint amountIn,
        uint amountOut
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the PancakeSwap router address.
     * @param _router Address of the PancakeSwap router contract.
     */
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        owner = msg.sender;
        router = IPancakeRouter(_router);
    }

    /**
     * @dev Allows the owner to automate token swaps based on predefined conditions.
     * @param fromToken Address of the token to swap from.
     * @param toToken Address of the token to swap to.
     * @param amountIn Amount of input tokens to swap.
     * @param minAmountOut Minimum amount of output tokens required (slippage protection).
     * @param deadline Time limit for the swap transaction.
     */
    function swapTokens(
        address fromToken,
        address toToken,
        uint amountIn,
        uint minAmountOut,
        uint deadline
    ) external onlyOwner {
        require(fromToken != address(0) && toToken != address(0), "Invalid token addresses");
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Approve the router to spend the tokens
        IERC20(fromToken).approve(address(router), amountIn);

        // Define the swap path (direct swap, fromToken -> toToken)
        address[] memory path = new address[](2);
        path[0] = fromToken;
        path[1] = toToken;

        // Execute the swap
        uint[] memory amounts = router.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            address(this),
            deadline
        );

        emit SwapExecuted(msg.sender, fromToken, toToken, amountIn, amounts[1]);
    }

    /**
     * @dev Allows the owner to withdraw any tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to transfer contract ownership.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
