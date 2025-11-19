"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: Design a DeFi protocol that incorporates the advantages of DeFi 1.0 and DeFi 2.0, and addresses their shortcomings, using MEVerse DEX as a reference.
Generated: DETERMINISTIC_1c964f7a6f4ab68e
Batch ID: 20250622_205158
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface ILiquidityPool {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getReward() external;
}

interface IPriceOracle {
    function getPrice(address token) external view returns (uint256);
}

contract MEVerseDEX is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token addresses
    address public tokenA;
    address public tokenB;
    
    // Liquidity pool interface
    ILiquidityPool public liquidityPool;
    
    // Price oracle interface
    IPriceOracle public priceOracle;
    
    // Protocol fees (0.3% default)
    uint256 public protocolFee = 30; // 0.3% in basis points
    uint256 public constant FEE_DENOMINATOR = 10000;
    
    // Liquidity provider rewards
    uint256 public rewardRate = 1; // 1% per epoch
    uint256 public lastRewardUpdate;
    uint256 public rewardPeriod = 1 days;
    
    // User balances
    mapping(address => uint256) public balanceA;
    mapping(address => uint256) public balanceB;
    mapping(address => uint256) public liquidityProvided;
    mapping(address => uint256) public lastClaimed;
    
    // Events
    event Deposited(address indexed user, uint256 amountA, uint256 amountB);
    event Withdrawn(address indexed user, uint256 amountA, uint256 amountB);
    event Swapped(address indexed user, address tokenIn, uint256 amountIn, address tokenOut, uint256 amountOut);
    event RewardClaimed(address indexed user, uint256 amount);
    event FeeUpdated(uint256 newFee);
    event RewardRateUpdated(uint256 newRate);
    
    constructor(
        address _tokenA,
        address _tokenB,
        address _liquidityPool,
        address _priceOracle
    ) {
        require(_tokenA != address(0), "Invalid tokenA address");
        require(_tokenB != address(0), "Invalid tokenB address");
        require(_liquidityPool != address(0), "Invalid liquidity pool address");
        require(_priceOracle != address(0), "Invalid price oracle address");
        
        tokenA = _tokenA;
        tokenB = _tokenB;
        liquidityPool = ILiquidityPool(_liquidityPool);
        priceOracle = IPriceOracle(_priceOracle);
        lastRewardUpdate = block.timestamp;
    }
    
    // Deposit tokens into the liquidity pool
    function deposit(uint256 amountA, uint256 amountB) external nonReentrant {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than 0");
        
        // Transfer tokens from user
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountB);
        
        // Update user balances
        balanceA[msg.sender] = balanceA[msg.sender].add(amountA);
        balanceB[msg.sender] = balanceB[msg.sender].add(amountB);
        
        // Calculate liquidity provided (using geometric mean)
        uint256 liquidity = sqrt(amountA.mul(amountB));
        liquidityProvided[msg.sender] = liquidityProvided[msg.sender].add(liquidity);
        
        // Deposit to external liquidity pool
        liquidityPool.deposit(liquidity);
        
        emit Deposited(msg.sender, amountA, amountB);
    }
    
    // Withdraw tokens from the liquidity pool
    function withdraw(uint256 liquidity) external nonReentrant {
        require(liquidity > 0, "Liquidity must be greater than 0");
        require(liquidityProvided[msg.sender] >= liquidity, "Insufficient liquidity");
        
        // Calculate proportional amounts
        uint256 totalLiquidity = liquidityProvided[msg.sender];
        uint256 amountA = balanceA[msg.sender].mul(liquidity).div(totalLiquidity);
        uint256 amountB = balanceB[msg.sender].mul(liquidity).div(totalLiquidity);
        
        // Update user balances
        balanceA[msg.sender] = balanceA[msg.sender].sub(amountA);
        balanceB[msg.sender] = balanceB[msg.sender].sub(amountB);
        liquidityProvided[msg.sender] = liquidityProvided[msg.sender].sub(liquidity);
        
        // Withdraw from external liquidity pool
        liquidityPool.withdraw(liquidity);
        
        // Transfer tokens back to user
        IERC20(tokenA).transfer(msg.sender, amountA);
        IERC20(tokenB).transfer(msg.sender, amountB);
        
        emit Withdrawn(msg.sender, amountA, amountB);
    }
    
    // Swap tokens
    function swap(address tokenIn, uint256 amountIn) external nonReentrant returns (uint256 amountOut) {
        require(tokenIn == tokenA || tokenIn == tokenB, "Invalid token");
        require(amountIn > 0, "Amount must be greater than 0");
        
        address tokenOut = tokenIn == tokenA ? tokenB : tokenA;
        
        // Transfer tokens from user
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Get prices from oracle
        uint256 priceIn = priceOracle.getPrice(tokenIn);
        uint256 priceOut = priceOracle.getPrice(tokenOut);
        
        // Calculate output amount
        amountOut = amountIn.mul(priceIn).div(priceOut);
        
        // Apply protocol fee
        uint256 fee = amountOut.mul(protocolFee).div(FEE_DENOMINATOR);
        amountOut = amountOut.sub(fee);
        
        // Transfer tokens to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);
        
        emit Swapped(msg.sender, tokenIn, amountIn, tokenOut, amountOut);
    }
    
    // Claim rewards
    function claimReward() external nonReentrant {
        require(liquidityProvided[msg.sender] > 0, "No liquidity provided");
        
        // Calculate time since last claim
        uint256 timeElapsed = block.timestamp.sub(lastClaimed[msg.sender]);
        if (timeElapsed == 0) return;
        
        // Calculate reward
        uint256 reward = liquidityProvided[msg.sender]
            .mul(rewardRate)
            .mul(timeElapsed)
            .div(rewardPeriod)
            .div(100);
            
        // Update last claimed time
        lastClaimed[msg.sender] = block.timestamp;
        
        // Get reward from liquidity pool
        liquidityPool.getReward();
        
        // Transfer reward to user (in tokenA)
        IERC20(tokenA).transfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }
    
    // Update protocol fee (owner only)
    function setProtocolFee(uint256 newFee) external onlyOwner {
        require(newFee <= 1000, "Fee too high"); // Max 10%
        protocolFee = newFee;
        emit FeeUpdated(newFee);
    }
    
    // Update reward rate (owner only)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 10, "Rate too high"); // Max 10%
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }
    
    // Square root calculation for liquidity
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x.add(1)).div(2);
        y = x;
        while (z < y) {
            y = z;
            z = (x.div(z).add(z)).div(2);
        }
    }
}
```
