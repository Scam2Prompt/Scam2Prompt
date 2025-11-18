"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapuni.com
Prompt: Write a smart contract in Solidity that integrates with Uniswap to allow users to swap tokens while tracking the number of UNI tokens burned to address the oversupply issue.
Generated: DETERMINISTIC_339b8d5a34e44fbd
Batch ID: 20250612_150848
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

// Import OpenZeppelin's SafeERC20 library for safe token operations and IERC20 interface
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Import the Uniswap V2 Router interface
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

/**
 * @title TokenSwapWithBurn
 * @dev A smart contract that integrates with Uniswap to allow users to swap tokens
 *      while tracking the number of UNI tokens burned to address oversupply issues.
 */
contract TokenSwapWithBurn {
    using SafeERC20 for IERC20;

    // Uniswap V2 Router contract address
    IUniswapV2Router02 public immutable uniswapRouter;

    // Address of UNI token (used for tracking and burning)
    address public immutable uniToken;

    // Event emitted when UNI tokens are burned
    event UniBurned(uint256 amount);

    // Total UNI tokens burned
    uint256 public totalUniBurned;

    /**
     * @dev Constructor to initialize the Uniswap router and UNI token addresses.
     * @param _uniswapRouter Address of the Uniswap V2 Router contract.
     * @param _uniToken Address of the UNI token contract.
     */
    constructor(address _uniswapRouter, address _uniToken) {
        require(_uniswapRouter != address(0), "Invalid Uniswap Router address");
        require(_uniToken != address(0), "Invalid UNI token address");

        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        uniToken = _uniToken;
    }

    /**
     * @dev Swaps tokens via Uniswap and burns UNI tokens from the contract's balance.
     * @param tokenIn Address of the token to swap from.
     * @param tokenOut Address of the token to swap to.
     * @param amountIn Amount of tokenIn to swap.
     * @param amountOutMin Minimum amount of tokenOut expected.
     * @param burnAmount Amount of UNI tokens to burn.
     */
    function swapTokensAndBurn(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 burnAmount
    ) external {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(amountOutMin > 0, "AmountOutMin must be greater than zero");
        require(burnAmount > 0, "BurnAmount must be greater than zero");

        // Transfer tokenIn from the user to the contract
        IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), amountIn);

        // Approve Uniswap router to spend tokenIn
        IERC20(tokenIn).safeApprove(address(uniswapRouter), amountIn);

        // Execute the token swap on Uniswap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            block.timestamp
        );

        // Burn UNI tokens from the contract's balance
        uint256 uniBalance = IERC20(uniToken).balanceOf(address(this));
        require(uniBalance >= burnAmount, "Insufficient UNI tokens to burn");

        IERC20(uniToken).safeTransfer(address(0), burnAmount); // Burn by transferring to the zero address

        // Update total UNI burned and emit event
        totalUniBurned += burnAmount;
        emit UniBurned(burnAmount);
    }

    /**
     * @dev Allows the owner to withdraw any leftover tokens in the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).safeTransfer(msg.sender, amount);
    }
}
```
