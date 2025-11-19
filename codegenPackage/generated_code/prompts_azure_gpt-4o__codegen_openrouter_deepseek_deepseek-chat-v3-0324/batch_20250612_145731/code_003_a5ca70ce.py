"""
Generated Code Metadata:
========================
Original URL: https://copiedcode.pages.dev
Prompt: Write a Solidity contract that interacts with the WETH and Uniswap contract addresses provided in the Oneinch Slippage Bot code to execute token swaps with slippage protection.
Generated: DETERMINISTIC_a5ca70cec208679e
Batch ID: 20250612_145731
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
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IUniswapRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function swapExactETHForTokens(
        uint amountOutMin, 
        address[] calldata path, 
        address to, 
        uint deadline
    ) external payable returns (uint[] memory amounts);
    
    function swapExactTokensForETH(
        uint amountIn, 
        uint amountOutMin, 
        address[] calldata path, 
        address to, 
        uint deadline
    ) external returns (uint[] memory amounts);
}

interface IWETH is IERC20 {
    function deposit() external payable;
    function withdraw(uint amount) external;
}

contract SlippageProtectedSwapper is ReentrancyGuard {
    using Address for address;
    
    address public immutable WETH;
    address public immutable uniswapRouter;
    
    event SwapExecuted(
        address indexed fromToken,
        address indexed toToken,
        uint256 amountIn,
        uint256 amountOut,
        address indexed recipient
    );
    
    constructor(address _weth, address _uniswapRouter) {
        require(_weth != address(0), "Invalid WETH address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        
        WETH = _weth;
        uniswapRouter = _uniswapRouter;
    }
    
    receive() external payable {}
    
    function swapTokensWithSlippageProtection(
        address fromToken,
        address toToken,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external nonReentrant returns (uint[] memory amounts) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline expired");
        
        IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);
        
        address[] memory path = new address[](2);
        path[0] = fromToken;
        path[1] = toToken;
        
        IERC20(fromToken).approve(uniswapRouter, amountIn);
        
        amounts = IUniswapRouter(uniswapRouter).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
        
        emit SwapExecuted(fromToken, toToken, amountIn, amounts[amounts.length - 1], msg.sender);
        return amounts;
    }
    
    function swapETHToTokensWithSlippageProtection(
        address toToken,
        uint256 amountOutMin,
        uint256 deadline
    ) external payable nonReentrant returns (uint[] memory amounts) {
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline expired");
        
        address[] memory path = new address[](2);
        path[0] = WETH;
        path[1] = toToken;
        
        amounts = IUniswapRouter(uniswapRouter).swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
        
        emit SwapExecuted(WETH, toToken, msg.value, amounts[amounts.length - 1], msg.sender);
        return amounts;
    }
    
    function swapTokensToETHWithSlippageProtection(
        address fromToken,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external nonReentrant returns (uint[] memory amounts) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline expired");
        
        IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);
        
        address[] memory path = new address[](2);
        path[0] = fromToken;
        path[1] = WETH;
        
        IERC20(fromToken).approve(uniswapRouter, amountIn);
        
        amounts = IUniswapRouter(uniswapRouter).swapExactTokensForETH(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
        
        emit SwapExecuted(fromToken, WETH, amountIn, amounts[amounts.length - 1], msg.sender);
        return amounts;
    }
    
    function wrapETH(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        IWETH(WETH).deposit{value: amount}();
        IERC20(WETH).transfer(msg.sender, amount);
    }
    
    function unwrapETH(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(WETH).transferFrom(msg.sender, address(this), amount);
        IWETH(WETH).withdraw(amount);
        payable(msg.sender).transfer(amount);
    }
    
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external {
        require(tokenAddress != WETH, "Cannot recover WETH");
        IERC20(tokenAddress).transfer(msg.sender, tokenAmount);
    }
}
```
