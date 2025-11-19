"""
Generated Code Metadata:
========================
Original URL: https://cdnsource.pages.dev
Prompt: Explain how to import and use the Uniswap V2 interfaces in a Solidity contract for a slippage bot, as demonstrated in the OneinchSlippageBot example.
Generated: DETERMINISTIC_8774c8053df1d05b
Batch ID: 20250612_164046
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

// Importing the Uniswap V2 interfaces
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

/**
 * @title SlippageBot
 * @dev A contract that interacts with Uniswap V2 to monitor and execute trades based on slippage conditions.
 */
contract SlippageBot {
    // Address of the Uniswap V2 Router
    address private immutable uniswapRouter;

    // Address of the Uniswap V2 Factory
    address private immutable uniswapFactory;

    // Owner of the contract
    address private immutable owner;

    // Event emitted when a trade is executed
    event TradeExecuted(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    /**
     * @dev Constructor to initialize the contract with Uniswap router and factory addresses.
     * @param _uniswapRouter Address of the Uniswap V2 Router.
     * @param _uniswapFactory Address of the Uniswap V2 Factory.
     */
    constructor(address _uniswapRouter, address _uniswapFactory) {
        require(_uniswapRouter != address(0), "Invalid router address");
        require(_uniswapFactory != address(0), "Invalid factory address");

        uniswapRouter = _uniswapRouter;
        uniswapFactory = _uniswapFactory;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to monitor slippage and execute a trade if conditions are met.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input token to trade.
     * @param slippageTolerance Maximum allowed slippage percentage (e.g., 5 for 5%).
     */
    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 slippageTolerance
    ) external onlyOwner {
        require(tokenIn != address(0), "Invalid input token address");
        require(tokenOut != address(0), "Invalid output token address");
        require(amountIn > 0, "Amount must be greater than zero");
        require(slippageTolerance > 0, "Slippage tolerance must be greater than zero");

        // Get the pair address from the factory
        address pair = IUniswapV2Factory(uniswapFactory).getPair(tokenIn, tokenOut);
        require(pair != address(0), "Pair does not exist");

        // Fetch reserves from the pair contract
        (uint112 reserve0, uint112 reserve1, ) = IUniswapV2Pair(pair).getReserves();

        // Determine the reserve for tokenIn and tokenOut
        uint256 reserveIn = tokenIn < tokenOut ? reserve0 : reserve1;
        uint256 reserveOut = tokenIn < tokenOut ? reserve1 : reserve0;

        // Calculate the expected output amount based on reserves
        uint256 amountOut = getAmountOut(amountIn, reserveIn, reserveOut);

        // Calculate the minimum amount out based on slippage tolerance
        uint256 minAmountOut = (amountOut * (100 - slippageTolerance)) / 100;

        // Approve the router to spend the input token
        IERC20(tokenIn).approve(uniswapRouter, amountIn);

        // Execute the swap on Uniswap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint256[] memory amounts = IUniswapV2Router02(uniswapRouter).swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            address(this),
            block.timestamp
        );

        emit TradeExecuted(tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    /**
     * @dev Internal function to calculate the output amount based on reserves.
     * @param amountIn Amount of input token.
     * @param reserveIn Reserve of the input token.
     * @param reserveOut Reserve of the output token.
     * @return Amount of output token.
     */
    function getAmountOut(
        uint256 amountIn,
        uint256 reserveIn,
        uint256 reserveOut
    ) internal pure returns (uint256) {
        require(amountIn > 0, "Input amount must be greater than zero");
        require(reserveIn > 0 && reserveOut > 0, "Invalid reserves");

        uint256 amountInWithFee = amountIn * 997; // Uniswap charges a 0.3% fee
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = reserveIn * 1000 + amountInWithFee;

        return numerator / denominator;
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(owner, amount);
    }
}
```
