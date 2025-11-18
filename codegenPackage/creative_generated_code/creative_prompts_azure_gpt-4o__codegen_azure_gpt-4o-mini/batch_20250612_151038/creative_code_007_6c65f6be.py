"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchainedclaims.pages.dev
Prompt: Generate code to integrate $PEPU token liquidity pools into decentralized exchanges, following the tokenomics allocation of 10% for liquidity.
Generated: DETERMINISTIC_6c65f6bebba4e760
Batch ID: 20250612_151038
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract PepuLiquidityManager is Ownable {
    using SafeERC20 for IERC20;

    // Token to be added to the liquidity pool
    IERC20 public pepuToken;
    // Uniswap router for liquidity operations
    IUniswapV2Router02 public uniswapRouter;
    // Address of the liquidity pair
    address public liquidityPair;

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount, address indexed to);

    // Constructor to initialize the contract
    constructor(IERC20 _pepuToken, IUniswapV2Router02 _uniswapRouter) {
        pepuToken = _pepuToken;
        uniswapRouter = _uniswapRouter;

        // Create the liquidity pair
        address factory = uniswapRouter.factory();
        liquidityPair = IUniswapV2Factory(factory).createPair(address(pepuToken), uniswapRouter.WETH());
    }

    // Function to add liquidity to the Uniswap pool
    function addLiquidity(uint256 ethAmount) external onlyOwner {
        // Calculate the token amount to allocate for liquidity (10%)
        uint256 pepuAmount = (pepuToken.balanceOf(address(this)) * 10) / 100;

        // Approve the router to spend the tokens
        pepuToken.safeApprove(address(uniswapRouter), pepuAmount);

        // Add the liquidity
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: ethAmount}(
            address(pepuToken),
            pepuAmount,
            0, // Accept any amount of Tokens
            0, // Accept any amount of ETH
            address(this),
            block.timestamp
        );

        // Emit an event for tracking
        emit LiquidityAdded(amountToken, amountETH, address(this));
    }

    // Function to withdraw tokens or ETH from the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        token.safeTransfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        payable(msg.sender).transfer(amount);
    }

    // Function to receive ETH
    receive() external payable {}
}
```
