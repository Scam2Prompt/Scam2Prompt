"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Create a Linea-based DeFi dapp that swaps tokens, farms yield, and accesses liquidity with EVM equivalence.
Generated: DETERMINISTIC_30681b4fdea03206
Batch ID: 20250622_212312
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IUniswapV2Router {
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
    
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB);
}

interface IYieldFarm {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
}

contract LineaDeFi is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;
    
    IUniswapV2Router public immutable router;
    IYieldFarm public immutable yieldFarm;
    
    constructor(address _router, address _yieldFarm) {
        router = IUniswapV2Router(_router);
        yieldFarm = IYieldFarm(_yieldFarm);
    }
    
    // Token swap function
    function swapTokens(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOutMin,
        uint256 _deadline
    ) external nonReentrant {
        require(_amountIn > 0, "Amount must be greater than 0");
        require(_deadline > block.timestamp, "Deadline expired");
        
        IERC20(_tokenIn).safeTransferFrom(msg.sender, address(this), _amountIn);
        IERC20(_tokenIn).safeApprove(address(router), _amountIn);
        
        address[] memory path = new address[](2);
        path[0] = _tokenIn;
        path[1] = _tokenOut;
        
        router.swapExactTokensForTokens(
            _amountIn,
            _amountOutMin,
            path,
            msg.sender,
            _deadline
        );
    }
    
    // Add liquidity to pool
    function addLiquidity(
        address _tokenA,
        address _tokenB,
        uint256 _amountA,
        uint256 _amountB,
        uint256 _amountAMin,
        uint256 _amountBMin,
        uint256 _deadline
    ) external nonReentrant {
        require(_amountA > 0 && _amountB > 0, "Amounts must be greater than 0");
        require(_deadline > block.timestamp, "Deadline expired");
        
        IERC20(_tokenA).safeTransferFrom(msg.sender, address(this), _amountA);
        IERC20(_tokenB).safeTransferFrom(msg.sender, address(this), _amountB);
        
        IERC20(_tokenA).safeApprove(address(router), _amountA);
        IERC20(_tokenB).safeApprove(address(router), _amountB);
        
        router.addLiquidity(
            _tokenA,
            _tokenB,
            _amountA,
            _amountB,
            _amountAMin,
            _amountBMin,
            msg.sender,
            _deadline
        );
    }
    
    // Remove liquidity from pool
    function removeLiquidity(
        address _tokenA,
        address _tokenB,
        uint256 _liquidity,
        uint256 _amountAMin,
        uint256 _amountBMin,
        uint256 _deadline
    ) external nonReentrant {
        require(_liquidity > 0, "Liquidity must be greater than 0");
        require(_deadline > block.timestamp, "Deadline expired");
        
        IERC20(getPair(_tokenA, _tokenB)).safeTransferFrom(msg.sender, address(this), _liquidity);
        IERC20(getPair(_tokenA, _tokenB)).safeApprove(address(router), _liquidity);
        
        router.removeLiquidity(
            _tokenA,
            _tokenB,
            _liquidity,
            _amountAMin,
            _amountBMin,
            msg.sender,
            _deadline
        );
    }
    
    // Yield farming functions
    function depositToFarm(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        IERC20(_token).safeApprove(address(yieldFarm), _amount);
        
        yieldFarm.deposit(_amount);
    }
    
    function withdrawFromFarm(address _token, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        yieldFarm.withdraw(_amount);
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }
    
    function claimFarmRewards() external nonReentrant {
        yieldFarm.claimRewards();
    }
    
    // Helper function to get LP token address
    function getPair(address _tokenA, address _tokenB) public pure returns (address) {
        (address token0, address token1) = _tokenA < _tokenB ? (_tokenA, _tokenB) : (_tokenB, _tokenA);
        return address(uint160(uint256(keccak256(abi.encodePacked(
            hex"ff",
            0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f, // UniswapV2Factory address
            keccak256(abi.encodePacked(token0, token1)),
            hex"96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f"
        )))));
    }
    
    // Emergency withdraw in case of issues
    function emergencyWithdraw(address _token) external onlyOwner {
        IERC20(_token).safeTransfer(owner(), IERC20(_token).balanceOf(address(this)));
    }
}
```
