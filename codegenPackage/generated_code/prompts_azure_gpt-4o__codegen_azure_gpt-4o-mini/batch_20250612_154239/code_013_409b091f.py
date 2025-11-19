"""
Generated Code Metadata:
========================
Original URL: https://carbondefi.pages.dev
Prompt: Explain how to use Carbon DeFi's custom fee tiers to optimize trading costs for ERC-20 token pairs in a smart contract.
Generated: DETERMINISTIC_409b091f14043516
Batch ID: 20250612_154239
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Carbon DeFi protocol
interface ICarbonDeFi {
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 feeTier
    ) external returns (uint256 amountOut);
}

// Smart contract to interact with Carbon DeFi's custom fee tiers
contract CarbonDeFiTrader is Ownable {
    ICarbonDeFi public carbonDeFi;

    // Event to log successful trades
    event TradeExecuted(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut, uint256 feeTier);

    // Constructor to set the Carbon DeFi contract address
    constructor(address _carbonDeFi) {
        require(_carbonDeFi != address(0), "Invalid Carbon DeFi address");
        carbonDeFi = ICarbonDeFi(_carbonDeFi);
    }

    // Function to execute a trade with custom fee tier
    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 feeTier
    ) external onlyOwner returns (uint256) {
        // Validate input parameters
        require(amountIn > 0, "Amount in must be greater than zero");
        require(minAmountOut > 0, "Minimum amount out must be greater than zero");
        require(feeTier >= 0, "Invalid fee tier");

        // Transfer tokens from the caller to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Carbon DeFi contract to spend the tokens
        IERC20(tokenIn).approve(address(carbonDeFi), amountIn);

        // Execute the trade
        uint256 amountOut = carbonDeFi.swap(tokenIn, tokenOut, amountIn, minAmountOut, feeTier);

        // Emit event for successful trade
        emit TradeExecuted(tokenIn, tokenOut, amountIn, amountOut, feeTier);

        // Return the amount of tokens received
        return amountOut;
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
