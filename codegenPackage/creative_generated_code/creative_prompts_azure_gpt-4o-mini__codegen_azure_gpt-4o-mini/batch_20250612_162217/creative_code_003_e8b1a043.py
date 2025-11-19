"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-26dec.vercel.app
Prompt: Generate an example of a smart contract that interacts with Uniswap for token swaps.
Generated: DETERMINISTIC_e8b1a04398648266
Batch ID: 20250612_162217
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

// Import the Uniswap interface
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract UniswapTokenSwap {
    // Uniswap router address (Mainnet)
    IUniswapV2Router02 public uniswapRouter;
    
    // Address of the token to be swapped
    address public tokenAddress;

    /**
     * @dev Constructor to set the Uniswap router and token address.
     * @param _uniswapRouter Address of the Uniswap router.
     * @param _tokenAddress Address of the token to be swapped.
     */
    constructor(address _uniswapRouter, address _tokenAddress) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Swaps a specific amount of ETH for the specified token.
     * @param tokenAmountOut Minimum amount of tokens to receive.
     * @param to Address to send the tokens to.
     * @param deadline Time by which the transaction must be completed.
     */
    function swapExactETHForTokens(uint256 tokenAmountOut, address to, uint256 deadline) external payable {
        // Validate input parameters
        require(msg.value > 0, "ETH amount must be greater than zero");
        require(to != address(0), "Invalid recipient address");

        // Define the path for the swap (ETH -> Token)
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // Wrapped ETH address
        path[1] = tokenAddress; // Token address

        // Execute the swap
        uniswapRouter.swapExactETHForTokens{ value: msg.value }(
            tokenAmountOut,
            path,
            to,
            deadline
        );
    }

    /**
     * @dev Swaps a specific amount of tokens for ETH.
     * @param tokenAmountIn Amount of tokens to swap.
     * @param to Address to send the ETH to.
     * @param deadline Time by which the transaction must be completed.
     */
    function swapExactTokensForETH(uint256 tokenAmountIn, address to, uint256 deadline) external {
        // Validate input parameters
        require(tokenAmountIn > 0, "Token amount must be greater than zero");
        require(to != address(0), "Invalid recipient address");

        // Transfer the tokens from the sender to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmountIn);

        // Approve the Uniswap router to spend the tokens
        IERC20(tokenAddress).approve(address(uniswapRouter), tokenAmountIn);

        // Define the path for the swap (Token -> ETH)
        address[] memory path = new address[](2);
        path[0] = tokenAddress; // Token address
        path[1] = uniswapRouter.WETH(); // Wrapped ETH address

        // Execute the swap
        uniswapRouter.swapExactTokensForETH(
            tokenAmountIn,
            0, // Accept any amount of ETH
            path,
            to,
            deadline
        );
    }

    /**
     * @dev Withdraws any remaining ETH in the contract to the owner.
     * @param to Address to send the ETH to.
     */
    function withdrawETH(address payable to) external {
        require(to != address(0), "Invalid recipient address");
        // Transfer the remaining ETH to the specified address
        (bool success, ) = to.call{ value: address(this).balance }("");
        require(success, "Transfer failed.");
    }

    /**
     * @dev Withdraws any ERC20 tokens held by the contract to the owner.
     * @param token Address of the token to withdraw.
     * @param to Address to send the tokens to.
     */
    function withdrawTokens(address token, address to) external {
        require(to != address(0), "Invalid recipient address");
        uint256 tokenBalance = IERC20(token).balanceOf(address(this));
        require(tokenBalance > 0, "No tokens to withdraw");

        // Transfer the tokens to the specified address
        IERC20(token).transfer(to, tokenBalance);
    }
}
```
