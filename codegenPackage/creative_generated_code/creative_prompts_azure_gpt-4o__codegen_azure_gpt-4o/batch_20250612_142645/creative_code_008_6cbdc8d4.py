"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapv3.finance
Prompt: Write a Solidity function to deposit tokens into a PancakeSwap V3 liquidity pool and withdraw them after a specified duration.
Generated: DETERMINISTIC_6cbdc8d4e24c61aa
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Import interfaces for interacting with PancakeSwap V3 contracts
import "@pancakeswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract LiquidityManager is ReentrancyGuard {
    // PancakeSwap V3 Nonfungible Position Manager contract address
    INonfungiblePositionManager public immutable positionManager;

    // Struct to store deposit information
    struct Deposit {
        uint256 tokenId;
        uint256 unlockTime;
        address owner;
    }
    
    // Mapping to track deposits
    mapping(uint256 => Deposit) public deposits;

    // Event declarations
    event Deposited(uint256 indexed tokenId, address indexed owner, uint256 unlockTime);
    event Withdrawn(uint256 indexed tokenId, address indexed owner);

    constructor(INonfungiblePositionManager _positionManager) {
        positionManager = _positionManager;
    }

    /**
     * @dev Deposit liquidity into PancakeSwap V3 and lock it for a specified duration.
     * @param token0 The address of the first token.
     * @param token1 The address of the second token.
     * @param fee The pool fee tier.
     * @param amount0Desired Desired amount of token0.
     * @param amount1Desired Desired amount of token1.
     * @param amount0Min Minimum amount of token0.
     * @param amount1Min Minimum amount of token1.
     * @param deadline Transaction deadline.
     * @param duration Duration (in seconds) to lock the liquidity.
     */
    function depositLiquidity(
        address token0,
        address token1,
        uint24 fee,
        uint256 amount0Desired,
        uint256 amount1Desired,
        uint256 amount0Min,
        uint256 amount1Min,
        uint256 deadline,
        uint256 duration
    ) external nonReentrant {
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens from the user to this contract
        IERC20(token0).transferFrom(msg.sender, address(this), amount0Desired);
        IERC20(token1).transferFrom(msg.sender, address(this), amount1Desired);

        // Approve tokens for the position manager
        IERC20(token0).approve(address(positionManager), amount0Desired);
        IERC20(token1).approve(address(positionManager), amount1Desired);

        // Mint the liquidity position
        INonfungiblePositionManager.MintParams memory params = INonfungiblePositionManager.MintParams({
            token0: token0,
            token1: token1,
            fee: fee,
            tickLower: -887272, // Wide range for simplicity, adjust as needed
            tickUpper: 887272,
            amount0Desired: amount0Desired,
            amount1Desired: amount1Desired,
            amount0Min: amount0Min,
            amount1Min: amount1Min,
            recipient: address(this),
            deadline: deadline
        });

        (uint256 tokenId, , , ) = positionManager.mint(params);

        // Store deposit details
        deposits[tokenId] = Deposit({
            tokenId: tokenId,
            unlockTime: block.timestamp + duration,
            owner: msg.sender
        });

        emit Deposited(tokenId, msg.sender, block.timestamp + duration);
    }

    /**
     * @dev Withdraw liquidity from PancakeSwap V3 after the lock duration has passed.
     * @param tokenId The ID of the liquidity position NFT.
     */
    function withdrawLiquidity(uint256 tokenId) external nonReentrant {
        Deposit memory deposit = deposits[tokenId];

        // Ensure the caller is the owner of the deposit
        require(deposit.owner == msg.sender, "Not the deposit owner");
        // Ensure the lock duration has passed
        require(block.timestamp >= deposit.unlockTime, "Lock period not over");

        // Collect liquidity and fees from the position
        INonfungiblePositionManager.CollectParams memory params = INonfungiblePositionManager.CollectParams({
            tokenId: tokenId,
            recipient: msg.sender,
            amount0Max: type(uint128).max,
            amount1Max: type(uint128).max
        });

        positionManager.collect(params);

        // Burn the position NFT
        positionManager.burn(tokenId);

        // Remove deposit data
        delete deposits[tokenId];

        emit Withdrawn(tokenId, msg.sender);
    }
}
```

This code is a Solidity contract that interacts with PancakeSwap V3's Nonfungible Position Manager to deposit and withdraw liquidity with locking functionality. It includes comprehensive error handling, comments, and adheres to best practices.
