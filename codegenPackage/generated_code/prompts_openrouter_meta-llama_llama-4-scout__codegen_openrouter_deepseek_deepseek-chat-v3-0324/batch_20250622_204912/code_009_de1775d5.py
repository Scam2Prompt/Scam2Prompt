"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: Design a smart contract on Ethereum or BSC that integrates with MDEX's API to create a custom DeFi application.
Generated: DETERMINISTIC_de1775d5011a1402
Batch ID: 20250622_204912
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

interface IMDEXRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
}

contract MDEXIntegration is Ownable, ReentrancyGuard {
    IMDEXRouter public mdexRouter;
    address public mdexRouterAddress;
    
    event TokensSwapped(
        address indexed user,
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOut
    );
    
    event RouterUpdated(address newRouter);
    
    constructor(address _mdexRouter) {
        require(_mdexRouter != address(0), "Invalid router address");
        mdexRouterAddress = _mdexRouter;
        mdexRouter = IMDEXRouter(_mdexRouter);
    }
    
    /**
     * @dev Update the MDEX router address
     * @param _newRouter Address of the new MDEX router
     */
    function updateRouter(address _newRouter) external onlyOwner {
        require(_newRouter != address(0), "Invalid router address");
        mdexRouterAddress = _newRouter;
        mdexRouter = IMDEXRouter(_newRouter);
        emit RouterUpdated(_newRouter);
    }
    
    /**
     * @dev Swap tokens using MDEX
     * @param _amountIn Amount of input tokens to swap
     * @param _amountOutMin Minimum amount of output tokens expected
     * @param _path Array of token addresses representing swap path
     * @param _deadline Unix timestamp after which the transaction will revert
     */
    function swapTokens(
        uint _amountIn,
        uint _amountOutMin,
        address[] calldata _path,
        uint _deadline
    ) external nonReentrant {
        require(_path.length >= 2, "Invalid path");
        require(_amountIn > 0, "Amount must be greater than 0");
        require(_deadline >= block.timestamp, "Expired deadline");
        
        IERC20 inputToken = IERC20(_path[0]);
        
        // Transfer tokens from user to this contract
        require(inputToken.transferFrom(msg.sender, address(this), _amountIn), "Transfer failed");
        
        // Approve MDEX router to spend tokens
        require(inputToken.approve(mdexRouterAddress, _amountIn), "Approval failed");
        
        // Execute swap
        uint[] memory amounts = mdexRouter.swapExactTokensForTokens(
            _amountIn,
            _amountOutMin,
            _path,
            msg.sender,
            _deadline
        );
        
        emit TokensSwapped(
            msg.sender,
            _path[0],
            _path[_path.length - 1],
            _amountIn,
            amounts[amounts.length - 1]
        );
    }
    
    /**
     * @dev Get the estimated amount of output tokens for a given input
     * @param _amountIn Amount of input tokens
     * @param _path Array of token addresses representing swap path
     * @return amounts Array of amounts at each step of the path
     */
    function getEstimatedOutput(
        uint _amountIn,
        address[] calldata _path
    ) external view returns (uint[] memory amounts) {
        require(_path.length >= 2, "Invalid path");
        amounts = mdexRouter.getAmountsOut(_amountIn, _path);
    }
    
    /**
     * @dev Emergency withdraw tokens sent to this contract by mistake
     * @param _token Address of the token to withdraw
     */
    function emergencyWithdraw(address _token) external onlyOwner {
        IERC20 token = IERC20(_token);
        uint balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
