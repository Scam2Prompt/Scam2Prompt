"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: Provide an example of how to utilize DAO funds for portfolio investments in a DeFi platform like MEVerse DEX.
Generated: DETERMINISTIC_b840dc393d9d1d60
Batch ID: 20250612_135144
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IDEXRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
}

contract DAOInvestmentManager is Ownable, ReentrancyGuard {
    IERC20 public daoToken;
    IDEXRouter public dexRouter;
    
    // Investment portfolio tracking
    struct Investment {
        address token;
        uint amount;
        uint timestamp;
    }
    
    Investment[] public investments;
    
    event FundsInvested(address indexed token, uint amount);
    event LiquidityAdded(address indexed tokenA, address indexed tokenB, uint amountA, uint amountB);
    event FundsWithdrawn(address indexed token, uint amount);
    
    constructor(address _daoToken, address _dexRouter) {
        daoToken = IERC20(_daoToken);
        dexRouter = IDEXRouter(_dexRouter);
    }
    
    /**
     * @dev Invest DAO funds by swapping to another token
     * @param amount Amount of DAO tokens to invest
     * @param tokenOut Target token address
     * @param amountOutMin Minimum amount of tokenOut expected
     * @param deadline Transaction deadline
     */
    function investFunds(
        uint amount,
        address tokenOut,
        uint amountOutMin,
        uint deadline
    ) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(daoToken.balanceOf(address(this)) >= amount, "Insufficient DAO funds");
        
        // Approve router to spend DAO tokens
        daoToken.approve(address(dexRouter), amount);
        
        address[] memory path = new address[](2);
        path[0] = address(daoToken);
        path[1] = tokenOut;
        
        // Execute swap
        uint[] memory amounts = dexRouter.swapExactTokensForTokens(
            amount,
            amountOutMin,
            path,
            address(this),
            deadline
        );
        
        // Record investment
        investments.push(Investment({
            token: tokenOut,
            amount: amounts[1],
            timestamp: block.timestamp
        }));
        
        emit FundsInvested(tokenOut, amounts[1]);
    }
    
    /**
     * @dev Add liquidity to a pool
     * @param tokenA First token address
     * @param tokenB Second token address
     * @param amountA Amount of tokenA to add
     * @param amountB Amount of tokenB to add
     * @param amountAMin Minimum amount of tokenA to add
     * @param amountBMin Minimum amount of tokenB to add
     * @param deadline Transaction deadline
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountA,
        uint amountB,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external onlyOwner nonReentrant {
        IERC20(tokenA).approve(address(dexRouter), amountA);
        IERC20(tokenB).approve(address(dexRouter), amountB);
        
        (uint usedAmountA, uint usedAmountB, ) = dexRouter.addLiquidity(
            tokenA,
            tokenB,
            amountA,
            amountB,
            amountAMin,
            amountBMin,
            address(this),
            deadline
        );
        
        emit LiquidityAdded(tokenA, tokenB, usedAmountA, usedAmountB);
    }
    
    /**
     * @dev Withdraw funds from the contract
     * @param token Token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawFunds(address token, uint amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        IERC20 tokenContract = IERC20(token);
        require(tokenContract.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        bool success = tokenContract.transfer(msg.sender, amount);
        require(success, "Transfer failed");
        
        emit FundsWithdrawn(token, amount);
    }
    
    /**
     * @dev Get total investments count
     * @return count Number of investments
     */
    function getInvestmentsCount() external view returns (uint) {
        return investments.length;
    }
    
    /**
     * @dev Get investment details by index
     * @param index Investment index
     * @return Investment details
     */
    function getInvestment(uint index) external view returns (Investment memory) {
        require(index < investments.length, "Invalid index");
        return investments[index];
    }
}
```
