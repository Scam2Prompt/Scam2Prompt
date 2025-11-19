"""
Generated Code Metadata:
========================
Original URL: https://jh1.xuexi02.top
Prompt: Create a Solidity contract that implements a basic arbitrage strategy similar to the one used by NAKA-Miner's arbitrage robot.
Generated: DETERMINISTIC_96dec98537509efc
Batch ID: 20250612_155705
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract ArbitrageBot is Ownable {
    IUniswapV2Router02 public router1;
    IUniswapV2Router02 public router2;
    
    event ArbitrageExecuted(
        address indexed token,
        uint256 amountIn,
        uint256 profit
    );
    
    constructor(address _router1, address _router2) {
        router1 = IUniswapV2Router02(_router1);
        router2 = IUniswapV2Router02(_router2);
    }
    
    function executeArbitrage(
        address token,
        uint256 amountIn,
        uint256 minProfit
    ) external onlyOwner {
        require(amountIn > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amountIn);
        IERC20(token).approve(address(router1), amountIn);
        IERC20(token).approve(address(router2), amountIn);
        
        address[] memory path = new address[](2);
        path[0] = token;
        path[1] = router1.WETH();
        
        // Get expected output from first exchange
        uint256[] memory amountsOut1 = router1.getAmountsOut(amountIn, path);
        uint256 expectedOut1 = amountsOut1[amountsOut1.length - 1];
        
        // Get expected output from second exchange
        uint256[] memory amountsOut2 = router2.getAmountsOut(amountIn, path);
        uint256 expectedOut2 = amountsOut2[amountsOut2.length - 1];
        
        if (expectedOut1 > expectedOut2) {
            // Buy low on router2, sell high on router1
            uint256[] memory amounts = router2.swapExactTokensForTokens(
                amountIn,
                0,
                path,
                address(this),
                block.timestamp + 300
            );
            
            uint256 amountOut = amounts[amounts.length - 1];
            
            path[0] = router1.WETH();
            path[1] = token;
            
            amounts = router1.swapExactTokensForTokens(
                amountOut,
                0,
                path,
                address(this),
                block.timestamp + 300
            );
            
            uint256 finalAmount = amounts[amounts.length - 1];
            require(finalAmount > amountIn + minProfit, "Insufficient profit");
            
            emit ArbitrageExecuted(token, amountIn, finalAmount - amountIn);
        } else if (expectedOut2 > expectedOut1) {
            // Buy low on router1, sell high on router2
            uint256[] memory amounts = router1.swapExactTokensForTokens(
                amountIn,
                0,
                path,
                address(this),
                block.timestamp + 300
            );
            
            uint256 amountOut = amounts[amounts.length - 1];
            
            path[0] = router2.WETH();
            path[1] = token;
            
            amounts = router2.swapExactTokensForTokens(
                amountOut,
                0,
                path,
                address(this),
                block.timestamp + 300
            );
            
            uint256 finalAmount = amounts[amounts.length - 1];
            require(finalAmount > amountIn + minProfit, "Insufficient profit");
            
            emit ArbitrageExecuted(token, amountIn, finalAmount - amountIn);
        } else {
            revert("No arbitrage opportunity");
        }
    }
    
    function withdrawTokens(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(token).transfer(msg.sender, balance);
    }
    
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).transfer(balance);
    }
    
    receive() external payable {}
}
```
