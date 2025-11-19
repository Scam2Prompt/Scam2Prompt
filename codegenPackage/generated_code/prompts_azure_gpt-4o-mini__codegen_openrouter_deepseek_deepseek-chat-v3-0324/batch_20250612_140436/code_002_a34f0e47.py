"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: Generate a tutorial on how to create a liquidity pool on MDEX, including the steps for adding liquidity and earning MDX rewards.
Generated: DETERMINISTIC_a34f0e475bdb1852
Batch ID: 20250612_140436
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

interface IMdexRouter {
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

interface IMdexPair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

interface IMdexFactory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

contract MdexLiquidityProvider is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;
    
    IMdexRouter public immutable router;
    IMdexFactory public immutable factory;
    address public immutable mdxToken;
    
    constructor(address _router, address _factory, address _mdxToken) {
        router = IMdexRouter(_router);
        factory = IMdexFactory(_factory);
        mdxToken = _mdxToken;
    }
    
    /**
     * @dev Creates a new liquidity pool if it doesn't exist
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     */
    function createPool(address tokenA, address tokenB) external onlyOwner {
        require(tokenA != tokenB, "Identical tokens");
        require(tokenA != address(0) && tokenB != address(0), "Zero address");
        
        address pair = factory.getPair(tokenA, tokenB);
        if (pair == address(0)) {
            factory.createPair(tokenA, tokenB);
        }
    }
    
    /**
     * @dev Adds liquidity to an existing pool
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @param amountADesired Amount of tokenA to add
     * @param amountBDesired Amount of tokenB to add
     * @param amountAMin Minimum amount of tokenA to add
     * @param amountBMin Minimum amount of tokenB to add
     * @param deadline Transaction deadline
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external nonReentrant {
        require(tokenA != tokenB, "Identical tokens");
        require(deadline >= block.timestamp, "Expired deadline");
        
        // Transfer tokens from user to this contract
        IERC20(tokenA).safeTransferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).safeTransferFrom(msg.sender, address(this), amountBDesired);
        
        // Approve router to spend tokens
        IERC20(tokenA).safeApprove(address(router), amountADesired);
        IERC20(tokenB).safeApprove(address(router), amountBDesired);
        
        // Add liquidity
        (uint amountA, uint amountB, uint liquidity) = router.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );
        
        // Return any remaining tokens
        if (amountA < amountADesired) {
            IERC20(tokenA).safeTransfer(msg.sender, amountADesired - amountA);
        }
        if (amountB < amountBDesired) {
            IERC20(tokenB).safeTransfer(msg.sender, amountBDesired - amountB);
        }
        
        emit LiquidityAdded(msg.sender, tokenA, tokenB, amountA, amountB, liquidity);
    }
    
    /**
     * @dev Removes liquidity from a pool
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @param liquidity Amount of LP tokens to remove
     * @param amountAMin Minimum amount of tokenA to receive
     * @param amountBMin Minimum amount of tokenB to receive
     * @param deadline Transaction deadline
     */
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external nonReentrant {
        require(tokenA != tokenB, "Identical tokens");
        require(deadline >= block.timestamp, "Expired deadline");
        
        address pair = factory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pool doesn't exist");
        
        // Transfer LP tokens from user to this contract
        IERC20(pair).safeTransferFrom(msg.sender, address(this), liquidity);
        
        // Approve router to spend LP tokens
        IERC20(pair).safeApprove(address(router), liquidity);
        
        // Remove liquidity
        (uint amountA, uint amountB) = router.removeLiquidity(
            tokenA,
            tokenB,
            liquidity,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );
        
        emit LiquidityRemoved(msg.sender, tokenA, tokenB, amountA, amountB);
    }
    
    /**
     * @dev Claims MDX rewards (implementation depends on MDEX's reward mechanism)
     */
    function claimMdxRewards() external {
        // Implementation depends on MDEX's specific reward contract
        // This is a placeholder for the actual reward claiming logic
        emit RewardsClaimed(msg.sender, 0); // Replace with actual reward amount
    }
    
    // Events
    event LiquidityAdded(
        address indexed provider,
        address indexed tokenA,
        address indexed tokenB,
        uint amountA,
        uint amountB,
        uint liquidity
    );
    
    event LiquidityRemoved(
        address indexed provider,
        address indexed tokenA,
        address indexed tokenB,
        uint amountA,
        uint amountB
    );
    
    event RewardsClaimed(address indexed user, uint amount);
}
```
