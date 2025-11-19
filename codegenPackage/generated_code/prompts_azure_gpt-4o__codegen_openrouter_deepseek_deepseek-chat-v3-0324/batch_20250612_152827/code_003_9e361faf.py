"""
Generated Code Metadata:
========================
Original URL: https://gameswap-org.web.app
Prompt: Develop a yield farming strategy for GameSwap's GSWAP token, ensuring compatibility with Ethereum standards and decentralized finance protocols.
Generated: DETERMINISTIC_9e361fafd30ab49d
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IGameSwapRouter {
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

interface IGameSwapPair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

interface IGameSwapFarm {
    function deposit(uint256 _pid, uint256 _amount) external;
    function withdraw(uint256 _pid, uint256 _amount) external;
    function userInfo(uint256 _pid, address _user) external view returns (uint256 amount, uint256 rewardDebt);
}

contract GameSwapYieldFarm is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token addresses
    address public gswapToken;
    address public wethToken;
    address public lpToken;
    
    // Protocol addresses
    address public router;
    address public farm;
    
    // Farm pool ID
    uint256 public poolId;
    
    // Reward tracking
    uint256 public lastHarvest;
    uint256 public totalHarvested;
    
    // Constants
    uint256 public constant MAX_INT = 2**256 - 1;
    
    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);
    event Harvested(uint256 amount);
    event Rebalanced(uint256 gswapAmount, uint256 ethAmount);
    
    constructor(
        address _gswapToken,
        address _wethToken,
        address _lpToken,
        address _router,
        address _farm,
        uint256 _poolId
    ) {
        gswapToken = _gswapToken;
        wethToken = _wethToken;
        lpToken = _lpToken;
        router = _router;
        farm = _farm;
        poolId = _poolId;
        
        // Approve tokens for router and farm
        IERC20(gswapToken).safeApprove(router, MAX_INT);
        IERC20(wethToken).safeApprove(router, MAX_INT);
        IERC20(lpToken).safeApprove(farm, MAX_INT);
    }
    
    // Main entry point for yield farming strategy
    function deposit(uint256 gswapAmount, uint256 ethAmount) external onlyOwner nonReentrant {
        require(gswapAmount > 0 || ethAmount > 0, "Must deposit something");
        
        // Transfer tokens from owner
        if (gswapAmount > 0) {
            IERC20(gswapToken).safeTransferFrom(msg.sender, address(this), gswapAmount);
        }
        if (ethAmount > 0) {
            IERC20(wethToken).safeTransferFrom(msg.sender, address(this), ethAmount);
        }
        
        _addLiquidityAndStake(gswapAmount, ethAmount);
        
        emit Deposited(gswapAmount.add(ethAmount));
    }
    
    // Withdraw funds from farm and return to owner
    function withdraw(uint256 lpAmount) external onlyOwner nonReentrant {
        require(lpAmount > 0, "Amount must be greater than 0");
        
        // Withdraw from farm
        IGameSwapFarm(farm).withdraw(poolId, lpAmount);
        
        // Remove liquidity
        (uint256 gswapAmount, uint256 ethAmount) = _removeLiquidity(lpAmount);
        
        // Transfer tokens back to owner
        if (gswapAmount > 0) {
            IERC20(gswapToken).safeTransfer(msg.sender, gswapAmount);
        }
        if (ethAmount > 0) {
            IERC20(wethToken).safeTransfer(msg.sender, ethAmount);
        }
        
        emit Withdrawn(lpAmount);
    }
    
    // Harvest rewards from farm
    function harvest() external onlyOwner nonReentrant {
        // Withdraw 0 to trigger reward distribution
        IGameSwapFarm(farm).withdraw(poolId, 0);
        
        uint256 rewardBalance = IERC20(gswapToken).balanceOf(address(this));
        require(rewardBalance > 0, "No rewards to harvest");
        
        // Track harvest
        lastHarvest = block.timestamp;
        totalHarvested = totalHarvested.add(rewardBalance);
        
        // Transfer rewards to owner
        IERC20(gswapToken).safeTransfer(msg.sender, rewardBalance);
        
        emit Harvested(rewardBalance);
    }
    
    // Rebalance the LP position
    function rebalance(uint256 gswapAmountMin, uint256 ethAmountMin) external onlyOwner nonReentrant {
        // Get current LP balance
        (uint256 lpBalance,) = IGameSwapFarm(farm).userInfo(poolId, address(this));
        
        // Withdraw all from farm
        if (lpBalance > 0) {
            IGameSwapFarm(farm).withdraw(poolId, lpBalance);
        }
        
        // Remove all liquidity
        (uint256 gswapAmount, uint256 ethAmount) = _removeLiquidity(lpBalance);
        
        // Add new liquidity with current balances
        _addLiquidityAndStake(gswapAmount, ethAmount);
        
        emit Rebalanced(gswapAmount, ethAmount);
    }
    
    // Internal function to add liquidity and stake in farm
    function _addLiquidityAndStake(uint256 gswapAmount, uint256 ethAmount) internal {
        if (gswapAmount > 0 && ethAmount > 0) {
            // Add liquidity
            (,, uint256 liquidity) = IGameSwapRouter(router).addLiquidity(
                gswapToken,
                wethToken,
                gswapAmount,
                ethAmount,
                1, // Minimum amounts (slippage tolerance)
                1,
                address(this),
                block.timestamp + 1 hours
            );
            
            // Stake in farm
            if (liquidity > 0) {
                IGameSwapFarm(farm).deposit(poolId, liquidity);
            }
        }
    }
    
    // Internal function to remove liquidity
    function _removeLiquidity(uint256 lpAmount) internal returns (uint256, uint256) {
        if (lpAmount == 0) {
            return (0, 0);
        }
        
        // Get token addresses from LP
        address token0 = IGameSwapPair(lpToken).token0();
        address token1 = IGameSwapPair(lpToken).token1();
        
        // Remove liquidity
        (uint256 amount0, uint256 amount1) = IGameSwapRouter(router).removeLiquidity(
            token0,
            token1,
            lpAmount,
            1, // Minimum amounts (slippage tolerance)
            1,
            address(this),
            block.timestamp + 1 hours
        );
        
        // Return amounts in GSWAP/ETH order regardless of LP token order
        if (token0 == gswapToken) {
            return (amount0, amount1);
        } else {
            return (amount1, amount0);
        }
    }
    
    // Emergency withdraw all funds without harvesting
    function emergencyWithdraw() external onlyOwner nonReentrant {
        (uint256 lpBalance,) = IGameSwapFarm(farm).userInfo(poolId, address(this));
        
        if (lpBalance > 0) {
            IGameSwapFarm(farm).withdraw(poolId, lpBalance);
        }
        
        (uint256 gswapAmount, uint256 ethAmount) = _removeLiquidity(lpBalance);
        
        if (gswapAmount > 0) {
            IERC20(gswapToken).safeTransfer(msg.sender, gswapAmount);
        }
        if (ethAmount > 0) {
            IERC20(wethToken).safeTransfer(msg.sender, ethAmount);
        }
    }
    
    // View function to get current position info
    function getPositionInfo() external view returns (
        uint256 gswapBalance,
        uint256 ethBalance,
        uint256 lpBalance,
        uint256 lastHarvestTime,
        uint256 totalHarvestedAmount
    ) {
        (lpBalance,) = IGameSwapFarm(farm).userInfo(poolId, address(this));
        gswapBalance = IERC20(g
