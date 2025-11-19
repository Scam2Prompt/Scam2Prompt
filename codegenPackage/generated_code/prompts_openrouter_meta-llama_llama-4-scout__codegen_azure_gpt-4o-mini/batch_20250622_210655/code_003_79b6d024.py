"""
Generated Code Metadata:
========================
Original URL: https://futureswap.pages.dev
Prompt: Develop a simple smart contract in Solidity to facilitate low-slippage stablecoin swaps on a blockchain platform like Ethereum, inspired by the Future Swap use case.
Generated: DETERMINISTIC_79b6d024e79bf744
Batch ID: 20250622_210655
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

// Importing OpenZeppelin's SafeERC20 for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// FutureSwap contract for low-slippage stablecoin swaps
contract FutureSwap is Ownable {
    using SafeERC20 for IERC20;

    // Event emitted when a swap occurs
    event SwapExecuted(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to store the exchange rates for stablecoins
    mapping(address => mapping(address => uint256)) public exchangeRates;

    // Function to set exchange rates for stablecoin pairs
    function setExchangeRate(address tokenA, address tokenB, uint256 rate) external onlyOwner {
        require(rate > 0, "Exchange rate must be greater than zero");
        exchangeRates[tokenA][tokenB] = rate;
    }

    // Function to swap stablecoins
    function swap(address tokenIn, address tokenOut, uint256 amountIn) external {
        require(exchangeRates[tokenIn][tokenOut] > 0, "Exchange rate not set for this pair");

        // Calculate the amount of tokenOut based on the exchange rate
        uint256 amountOut = (amountIn * exchangeRates[tokenIn][tokenOut]) / 1e18; // Assuming rate is scaled by 1e18

        // Transfer tokenIn from the user to the contract
        IERC20(tokenIn).safeTransferFrom(msg.sender, address(this), amountIn);

        // Transfer tokenOut from the contract to the user
        IERC20(tokenOut).safeTransfer(msg.sender, amountOut);

        // Emit the swap event
        emit SwapExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (for owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).safeTransfer(msg.sender, amount);
    }
}
```
