"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-org.vercel.app
Prompt: Write a smart contract that utilizes Uniswap for token swaps and flash swaps.
Generated: DETERMINISTIC_4cecf9d35e387e5e
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title UniswapTokenSwap
 * @dev A smart contract that interacts with Uniswap V2 for token swaps and flash swaps.
 *      This contract is designed to enable token swapping between two ERC20 tokens
 *      and execute flash swaps (borrowing tokens with no upfront cost).
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

contract UniswapTokenSwap {
    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public immutable uniswapRouter;

    // Address of the Uniswap V2 Factory
    address public immutable uniswapFactory;

    // Event emitted when a swap occurs
    event TokenSwap(
        address indexed sender,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    /**
     * @dev Sets the Uniswap V2 Router and Factory addresses.
     * @param _uniswapRouter Address of the Uniswap V2 Router.
     * @param _uniswapFactory Address of the Uniswap V2 Factory.
     */
    constructor(address _uniswapRouter, address _uniswapFactory) {
        require(
            _uniswapRouter != address(0) && _uniswapFactory != address(0),
            "Invalid address"
        );
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        uniswapFactory = _uniswapFactory;
    }

    /**
     * @dev Performs a token swap on Uniswap V2.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of the input token to swap.
     * @param amountOutMin Minimum amount of the output token expected.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin
    ) external {
        require(amountIn > 0, "AmountIn must be greater than 0");
        require(
            IERC20(tokenIn).balanceOf(msg.sender) >= amountIn,
            "Insufficient token balance"
        );

        // Transfer the input token to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend the input token
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Get the path for the swap (tokenIn -> tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender, // Send the output tokens to the sender
            block.timestamp // Deadline for the swap
        );

        emit TokenSwap(msg.sender, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    /**
     * @dev Executes a flash swap using a Uniswap pair contract.
     *      This example assumes no special logic for utilizing borrowed tokens; it simply repays the loan.
     * @param pairAddress Address of the Uniswap V2 Pair contract.
     * @param tokenBorrow Address of the token to borrow.
     * @param amountBorrow Amount of the token to borrow.
     */
    function executeFlashSwap(
        address pairAddress,
        address tokenBorrow,
        uint256 amountBorrow
    ) external {
        require(amountBorrow > 0, "Borrow amount must be greater than 0");

        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

        // Determine which token in the pair is being borrowed
        address token0 = pair.token0();
        address token1 = pair.token1();
        require(
            tokenBorrow == token0 || tokenBorrow == token1,
            "Invalid token for flash swap"
        );

        address tokenOther = tokenBorrow == token0 ? token1 : token0;

        // Perform the flash swap
        pair.swap(
            tokenBorrow == token0 ? amountBorrow : 0,
            tokenBorrow == token1 ? amountBorrow : 0,
            address(this),
            abi.encode(amountBorrow, tokenBorrow, tokenOther)
        );
    }

    /**
     * @dev Callback function required for Uniswap flash swaps.
     *      This function is triggered by the Uniswap pair contract when a flash swap is initiated.
     * @param sender Address initiating the flash swap.
     * @param amount0 Amount of token0 being swapped.
     * @param amount1 Amount of token1 being swapped.
     * @param data Encoded data containing flash swap parameters.
     */
    function uniswapV2Call(
        address sender,
        uint256 amount0,
        uint256 amount1,
        bytes calldata data
    ) external {
        require(sender == address(this), "Unauthorized sender");

        // Decode the data passed to the flash swap
        (uint256 amountBorrow, address tokenBorrow, address tokenOther) = abi
            .decode(data, (uint256, address, address));

        // Compute the repayment amount (including fees)
        uint256 fee = (amountBorrow * 3) / 997 + 1; // Uniswap charges a 0.3% fee
        uint256 amountToRepay = amountBorrow + fee;

        // Perform any custom logic here with the borrowed tokens
        // For example, arbitrage or liquidation

        // Ensure the contract has enough balance to repay
        IERC20(tokenBorrow).transfer(msg.sender, amountToRepay);
    }
}
```
