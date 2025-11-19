"""
Generated Code Metadata:
========================
Original URL: https://uni-store-info.at
Prompt: Develop a smart contract using Solidity to interact with Uniswap's automated market maker (AMM) model for liquidity provision.
Generated: DETERMINISTIC_340b7a30f1b6be13
Batch ID: 20250622_212208
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

// Importing the necessary interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LiquidityProvider {
    // State variables
    IUniswapV2Router02 public uniswapRouter;
    address public immutable WETH; // Wrapped Ether address

    // Events
    event LiquidityAdded(address indexed provider, uint256 amountToken, uint256 amountETH, uint256 liquidity);

    // Constructor to set the Uniswap router and WETH address
    constructor(address _router) {
        uniswapRouter = IUniswapV2Router02(_router);
        WETH = uniswapRouter.WETH();
    }

    // Function to add liquidity to Uniswap
    function addLiquidity(
        address token,
        uint256 tokenAmount,
        uint256 ethAmount,
        uint256 minTokenAmount,
        uint256 minEthAmount,
        address to,
        uint256 deadline
    ) external payable {
        require(msg.value == ethAmount, "Incorrect ETH amount sent");

        // Transfer the specified token amount from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), tokenAmount);

        // Approve the Uniswap router to spend the token
        IERC20(token).approve(address(uniswapRouter), tokenAmount);

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: ethAmount}(
            token,
            tokenAmount,
            minTokenAmount,
            minEthAmount,
            to,
            deadline
        );

        // Emit an event for the liquidity addition
        emit LiquidityAdded(msg.sender, amountToken, amountETH, liquidity);
    }

    // Function to withdraw tokens and ETH from the contract
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
