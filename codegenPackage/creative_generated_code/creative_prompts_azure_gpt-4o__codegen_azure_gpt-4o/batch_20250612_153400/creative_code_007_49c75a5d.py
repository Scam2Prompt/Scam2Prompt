"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-mstar-merlinstarter.pages.dev
Prompt: Develop a smart contract that interacts with MerlinSwap to enable automatic token swaps between $BTC and $M-BTC pools.
Generated: DETERMINISTIC_49c75a5d8ca4c6c8
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a Solidity smart contract that interacts with MerlinSwap to enable automatic token swaps between `$BTC` and `$M-BTC` pools. It adheres to the requirements specified.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Interface for the MerlinSwap Router (Assume MerlinSwap uses a Uniswap-like router interface)
interface IMerlinSwapRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function getAmountsOut(
        uint256 amountIn,
        address[] calldata path
    ) external view returns (uint256[] memory amounts);
}

// Interface for ERC20 tokens
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AutoTokenSwap {
    // State variables
    address public immutable owner;
    IMerlinSwapRouter public immutable merlinSwapRouter;

    // Token addresses
    address public immutable BTC;     // Address of the BTC token
    address public immutable M_BTC;   // Address of the M-BTC token

    // Events
    event TokenSwapped(
        address indexed user,
        uint256 amountIn,
        uint256 amountOut,
        address tokenIn,
        address tokenOut
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(
        address _merlinSwapRouter,
        address _BTC,
        address _M_BTC
    ) {
        owner = msg.sender;
        merlinSwapRouter = IMerlinSwapRouter(_merlinSwapRouter);
        BTC = _BTC;
        M_BTC = _M_BTC;
    }

    /**
     * @dev Approves the MerlinSwap router to spend tokens on behalf of this contract.
     * @param token The token to approve.
     * @param amount The amount to approve.
     */
    function approveToken(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).approve(address(merlinSwapRouter), amount), "Approval failed");
    }

    /**
     * @dev Swaps tokens between BTC and M-BTC pools.
     * @param amountIn The amount of BTC or M-BTC to swap.
     * @param amountOutMin The minimum amount of tokens to receive.
     * @param tokenIn The address of the token being swapped (BTC or M-BTC).
     * @param tokenOut The address of the token to receive (BTC or M-BTC).
     * @param deadline The timestamp after which the swap is invalid.
     */
    function swapTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address tokenIn,
        address tokenOut,
        uint256 deadline
    ) external {
        require(
            tokenIn == BTC || tokenIn == M_BTC,
            "Invalid input token"
        );
        require(
            tokenOut == BTC || tokenOut == M_BTC,
            "Invalid output token"
        );
        require(
            tokenIn != tokenOut,
            "Input and output tokens must differ"
        );

        // Transfer tokens from the user to this contract
        require(
            IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn),
            "Token transfer failed"
        );

        // Define the swap path (tokenIn -> tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Perform the swap
        uint256[] memory amounts = merlinSwapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit event for successful swap
        emit TokenSwapped(msg.sender, amountIn, amounts[1], tokenIn, tokenOut);
    }

    /**
     * @dev Gets the estimated output amount for a given input amount.
     * @param amountIn The amount of tokens to swap.
     * @param tokenIn The address of the token being swapped (BTC or M-BTC).
     * @param tokenOut The address of the token to receive (BTC or M-BTC).
     * @return The estimated amount of tokens to receive.
     */
    function getSwapEstimate(
        uint256 amountIn,
        address tokenIn,
        address tokenOut
    ) external view returns (uint256) {
        require(
            tokenIn == BTC || tokenIn == M_BTC,
            "Invalid input token"
        );
        require(
            tokenOut == BTC || tokenOut == M_BTC,
            "Invalid output token"
        );
        require(
            tokenIn != tokenOut,
            "Input and output tokens must differ"
        );

        // Define the swap path (tokenIn -> tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Get estimated amounts out
        uint256[] memory amounts = merlinSwapRouter.getAmountsOut(amountIn, path);
        return amounts[1];
    }
}
```
