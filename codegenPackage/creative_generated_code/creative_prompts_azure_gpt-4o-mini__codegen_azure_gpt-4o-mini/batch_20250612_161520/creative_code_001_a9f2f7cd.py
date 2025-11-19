"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-lido-7fd.pages.dev
Prompt: How can I implement a liquidity pool rebalance function for stETH rewards using UniswapV2 ETH-stETH?
Generated: DETERMINISTIC_a9f2f7cd1d6f3180
Batch ID: 20250612_161520
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract LiquidityPoolRebalance {
    IUniswapV2Router02 public uniswapRouter;
    IERC20 public stETH;
    IERC20 public WETH;
    IUniswapV2Pair public pair;

    // Events for logging purposes
    event Rebalanced(uint256 stETHAmount, uint256 ETHAmount);

    constructor(address _uniswapRouter, address _stETH, address _WETH, address _pair) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        stETH = IERC20(_stETH);
        WETH = IERC20(_WETH);
        pair = IUniswapV2Pair(_pair);
    }

    /**
     * @notice Rebalances the liquidity pool by swapping a specified amount of stETH for ETH and vice versa.
     * @param stETHAmount The amount of stETH to swap for ETH.
     * @param ethAmount The amount of ETH to swap for stETH.
     */
    function rebalance(uint256 stETHAmount, uint256 ethAmount) external {
        require(stETHAmount > 0 || ethAmount > 0, "Must swap at least one asset");

        // Swap stETH for ETH if stETHAmount is specified
        if (stETHAmount > 0) {
            // Transfer stETH from sender to this contract
            require(stETH.transferFrom(msg.sender, address(this), stETHAmount), "Transfer failed");

            // Approve Uniswap to spend stETH
            require(stETH.approve(address(uniswapRouter), stETHAmount), "Approval failed");

            // Execute the swap
            address[] memory path = new address[](2);
            path[0] = address(stETH);
            path[1] = address(WETH);

            uniswapRouter.swapExactTokensForETH(
                stETHAmount,
                0, // Accept any amount of ETH
                path,
                address(this),
                block.timestamp
            );
        }

        // Swap ETH for stETH if ethAmount is specified
        if (ethAmount > 0) {
            // Ensure the contract has enough ETH
            require(address(this).balance >= ethAmount, "Insufficient ETH balance");

            // Execute the swap
            address[] memory path = new address[](2);
            path[0] = address(WETH);
            path[1] = address(stETH);

            uniswapRouter.swapExactETHForTokens{value: ethAmount}(
                0, // Accept any amount of stETH
                path,
                address(this),
                block.timestamp
            );
        }

        emit Rebalanced(stETHAmount, ethAmount);
    }

    // Allow the contract to receive ETH
    receive() external payable {}

    /**
     * @notice Withdraws stETH to the sender's address.
     * @param amount The amount of stETH to withdraw.
     */
    function withdrawSTETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stETH.balanceOf(address(this)) >= amount, "Insufficient stETH balance");
        
        require(stETH.transfer(msg.sender, amount), "Withdrawal failed");
    }

    /**
     * @notice Withdraws ETH to the sender's address.
     * @param amount The amount of ETH to withdraw.
     */
    function withdrawETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(address(this).balance >= amount, "Insufficient ETH balance");
        
        payable(msg.sender).transfer(amount);
    }
}
```
