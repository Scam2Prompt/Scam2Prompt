"""
Generated Code Metadata:
========================
Original URL: https://0xblast.com
Prompt: Provide code examples for integrating DexKit functionality into a decentralized application, as described on 0xBlast.
Generated: DETERMINISTIC_8a5535cd0258b8c0
Batch ID: 20250612_152527
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

interface IDexKit {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
}

contract DexKitIntegration is Ownable, ReentrancyGuard {
    IDexKit public dexKitRouter;
    address public constant WETH = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    
    event SwapExecuted(
        address indexed user,
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOut
    );
    
    constructor(address _dexKitRouter) {
        require(_dexKitRouter != address(0), "Invalid router address");
        dexKitRouter = IDexKit(_dexKitRouter);
    }
    
    function setDexKitRouter(address _dexKitRouter) external onlyOwner {
        require(_dexKitRouter != address(0), "Invalid router address");
        dexKitRouter = IDexKit(_dexKitRouter);
    }
    
    function swapTokens(
        address _tokenIn,
        address _tokenOut,
        uint _amountIn,
        uint _amountOutMin,
        uint _deadline
    ) external nonReentrant {
        require(_amountIn > 0, "Amount must be greater than 0");
        require(_deadline > block.timestamp, "Deadline has passed");
        
        IERC20 tokenIn = IERC20(_tokenIn);
        require(tokenIn.transferFrom(msg.sender, address(this), _amountIn), "Transfer failed");
        
        tokenIn.approve(address(dexKitRouter), _amountIn);
        
        address[] memory path;
        if (_tokenIn == WETH || _tokenOut == WETH) {
            path = new address[](2);
            path[0] = _tokenIn;
            path[1] = _tokenOut;
        } else {
            path = new address[](3);
            path[0] = _tokenIn;
            path[1] = WETH;
            path[2] = _tokenOut;
        }
        
        uint[] memory amounts = dexKitRouter.swapExactTokensForTokens(
            _amountIn,
            _amountOutMin,
            path,
            msg.sender,
            _deadline
        );
        
        emit SwapExecuted(
            msg.sender,
            _tokenIn,
            _tokenOut,
            _amountIn,
            amounts[amounts.length - 1]
        );
    }
    
    function getEstimatedOut(
        address _tokenIn,
        address _tokenOut,
        uint _amountIn
    ) external view returns (uint[] memory) {
        require(_amountIn > 0, "Amount must be greater than 0");
        
        address[] memory path;
        if (_tokenIn == WETH || _tokenOut == WETH) {
            path = new address[](2);
            path[0] = _tokenIn;
            path[1] = _tokenOut;
        } else {
            path = new address[](3);
            path[0] = _tokenIn;
            path[1] = WETH;
            path[2] = _tokenOut;
        }
        
        return dexKitRouter.getAmountsOut(_amountIn, path);
    }
    
    function rescueTokens(address _token) external onlyOwner {
        IERC20 token = IERC20(_token);
        uint balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to rescue");
        require(token.transfer(msg.sender, balance), "Transfer failed");
    }
}
```
