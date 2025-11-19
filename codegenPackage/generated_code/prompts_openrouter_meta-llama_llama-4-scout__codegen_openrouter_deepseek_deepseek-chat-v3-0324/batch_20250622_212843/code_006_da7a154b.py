"""
Generated Code Metadata:
========================
Original URL: https://holdexofficial.com
Prompt: "Develop a plan for integrating Holdex AI with a DeFi protocol for liquidity provision and yield farming, including smart contract code."
Generated: DETERMINISTIC_da7a154b525ad37c
Batch ID: 20250622_212843
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

interface IHoldexAI {
    function predictOptimalPair(address tokenA, address tokenB) external view returns (uint256, uint256);
    function getOptimalYieldStrategy(address lpToken) external view returns (address, uint256);
}

interface IDexRouter {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountA, uint256 amountB, uint256 liquidity);
    
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint256 liquidity,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountA, uint256 amountB);
}

interface IFarm {
    function deposit(uint256 pid, uint256 amount, address to) external;
    function withdraw(uint256 pid, uint256 amount, address to) external;
    function harvest(uint256 pid, address to) external;
}

contract HoldexDeFiIntegrator is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IHoldexAI public holdexAI;
    address public dexRouter;
    address public farm;

    struct UserPosition {
        address tokenA;
        address tokenB;
        uint256 liquidity;
        uint256 farmPid;
    }

    mapping(address => UserPosition[]) public userPositions;

    event LiquidityAdded(address indexed user, address tokenA, address tokenB, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(address indexed user, address tokenA, address tokenB, uint256 amountA, uint256 amountB);
    event YieldFarmed(address indexed user, uint256 farmPid, uint256 amount);
    event YieldHarvested(address indexed user, uint256 farmPid, uint256 amount);

    constructor(address _holdexAI, address _dexRouter, address _farm) {
        require(_holdexAI != address(0), "Invalid HoldexAI address");
        require(_dexRouter != address(0), "Invalid DEX router address");
        require(_farm != address(0), "Invalid farm address");
        
        holdexAI = IHoldexAI(_holdexAI);
        dexRouter = _dexRouter;
        farm = _farm;
    }

    function addLiquidityAndFarm(
        address tokenA,
        address tokenB,
        uint256 amountA,
        uint256 amountB,
        uint256 minAmountA,
        uint256 minAmountB,
        uint256 deadline,
        uint256 farmPid
    ) external nonReentrant {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(amountA > 0 && amountB > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline passed");

        // Transfer tokens from user
        IERC20(tokenA).safeTransferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).safeTransferFrom(msg.sender, address(this), amountB);

        // Approve router to spend tokens
        IERC20(tokenA).safeApprove(dexRouter, amountA);
        IERC20(tokenB).safeApprove(dexRouter, amountB);

        // Get optimal amounts from Holdex AI
        (uint256 optimalAmountA, uint256 optimalAmountB) = holdexAI.predictOptimalPair(tokenA, tokenB);
        
        // Adjust amounts to optimal ratios
        uint256 adjustedAmountA = amountA > optimalAmountA ? optimalAmountA : amountA;
        uint256 adjustedAmountB = amountB > optimalAmountB ? optimalAmountB : amountB;

        // Add liquidity
        (uint256 usedAmountA, uint256 usedAmountB, uint256 liquidity) = IDexRouter(dexRouter).addLiquidity(
            tokenA,
            tokenB,
            adjustedAmountA,
            adjustedAmountB,
            minAmountA,
            minAmountB,
            address(this),
            deadline
        );

        // Store LP token address (assuming it's the pair address)
        address lpToken = pairFor(tokenA, tokenB);

        // Deposit to farm
        IERC20(lpToken).safeApprove(farm, liquidity);
        IFarm(farm).deposit(farmPid, liquidity, msg.sender);

        // Store user position
        userPositions[msg.sender].push(UserPosition({
            tokenA: tokenA,
            tokenB: tokenB,
            liquidity: liquidity,
            farmPid: farmPid
        }));

        // Refund any unused tokens
        if (amountA > usedAmountA) {
            IERC20(tokenA).safeTransfer(msg.sender, amountA - usedAmountA);
        }
        if (amountB > usedAmountB) {
            IERC20(tokenB).safeTransfer(msg.sender, amountB - usedAmountB);
        }

        emit LiquidityAdded(msg.sender, tokenA, tokenB, usedAmountA, usedAmountB, liquidity);
    }

    function removeLiquidityAndClaim(
        uint256 positionIndex,
        uint256 minAmountA,
        uint256 minAmountB,
        uint256 deadline
    ) external nonReentrant {
        require(positionIndex < userPositions[msg.sender].length, "Invalid position index");
        require(deadline >= block.timestamp, "Deadline passed");

        UserPosition storage position = userPositions[msg.sender][positionIndex];
        address lpToken = pairFor(position.tokenA, position.tokenB);

        // Withdraw from farm
        IFarm(farm).withdraw(position.farmPid, position.liquidity, msg.sender);

        // Approve router to spend LP tokens
        IERC20(lpToken).safeApprove(dexRouter, position.liquidity);

        // Remove liquidity
        (uint256 amountA, uint256 amountB) = IDexRouter(dexRouter).removeLiquidity(
            position.tokenA,
            position.tokenB,
            position.liquidity,
            minAmountA,
            minAmountB,
            msg.sender,
            deadline
        );

        // Harvest any remaining yield
        IFarm(farm).harvest(position.farmPid, msg.sender);

        // Remove position
        _removePosition(msg.sender, positionIndex);

        emit LiquidityRemoved(msg.sender, position.tokenA, position.tokenB, amountA, amountB);
    }

    function harvestYield(uint256 positionIndex) external nonReentrant {
        require(positionIndex < userPositions[msg.sender].length, "Invalid position index");
        
        UserPosition storage position = userPositions[msg.sender][positionIndex];
        IFarm(farm).harvest(position.farmPid, msg.sender);
        
        emit YieldHarvested(msg.sender, position.farmPid, position.liquidity);
    }

    function _removePosition(address user, uint256 index) private {
        uint256 lastIndex = userPositions[user].length - 1;
        if (index != lastIndex) {
            userPositions[user][index] = userPositions[user][lastIndex];
        }
        userPositions[user].pop();
    }

    // Helper function to get pair address (implementation depends on DEX)
    function pairFor(address tokenA, address tokenB) public view returns (address) {
        // This should be implemented based on the specific DEX's pair address calculation
        // For example, UniswapV2 uses a factory to create pairs
        revert("Pair address calculation not implemented");
    }

    function updateHoldexAI(address _holdexAI) external onlyOwner {
        require(_holdexAI != address(0), "Invalid address");
        holdexAI = IHoldexAI(_holdexAI);
    }

    function updateDexRouter(address _dexRouter) external onlyOwner {
        require(_dexRouter != address(0), "Invalid address");
        dexRouter = _dexRouter;
    }

    function updateFarm(address _farm) external onlyOwner {
        require(_farm != address(0), "Invalid address");
        farm = _farm;
    }

    function getUserPositions(address user) external view returns (UserPosition[] memory) {
        return userPositions[user];
    }
}
```
