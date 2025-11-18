"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-staging.org
Prompt: Develop a smart contract that interacts with Uniswap V3 to add liquidity to a pool, ensuring compliance with the protocol's specifications.
Generated: DETERMINISTIC_5c307f329bd48f2d
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces from Uniswap V3
import "@uniswap/v3-periphery/contracts/interfaces/ISwapRouter.sol";
import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import "@uniswap/v3-periphery/contracts/libraries/TransferHelper.sol";
import "@uniswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";

contract UniswapV3LiquidityAdder {
    // Uniswap V3 Nonfungible Position Manager address
    INonfungiblePositionManager public immutable positionManager;

    // Constructor to initialize the position manager
    constructor(address _positionManager) {
        require(_positionManager != address(0), "Invalid position manager address");
        positionManager = INonfungiblePositionManager(_positionManager);
    }

    /**
     * @notice Add liquidity to a Uniswap V3 pool
     * @param token0 Address of the first token in the pool
     * @param token1 Address of the second token in the pool
     * @param fee Fee tier of the pool (e.g., 500, 3000, or 10000)
     * @param amount0Desired Desired amount of token0 to add to the pool
     * @param amount1Desired Desired amount of token1 to add to the pool
     * @param amount0Min Minimum acceptable amount of token0 to add (slippage control)
     * @param amount1Min Minimum acceptable amount of token1 to add (slippage control)
     * @param recipient Address to receive the liquidity position NFT
     * @return tokenId ID of the liquidity position NFT
     */
    function addLiquidity(
        address token0,
        address token1,
        uint24 fee,
        uint256 amount0Desired,
        uint256 amount1Desired,
        uint256 amount0Min,
        uint256 amount1Min,
        address recipient
    ) external returns (uint256 tokenId) {
        require(token0 != address(0) && token1 != address(0), "Invalid token addresses");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer the desired amounts of tokens from the user to the contract
        TransferHelper.safeTransferFrom(token0, msg.sender, address(this), amount0Desired);
        TransferHelper.safeTransferFrom(token1, msg.sender, address(this), amount1Desired);

        // Approve the position manager to spend the tokens
        TransferHelper.safeApprove(token0, address(positionManager), amount0Desired);
        TransferHelper.safeApprove(token1, address(positionManager), amount1Desired);

        // Set parameters for the add liquidity call
        INonfungiblePositionManager.MintParams memory params = INonfungiblePositionManager.MintParams({
            token0: token0,
            token1: token1,
            fee: fee,
            tickLower: -887220, // Default tick lower - Uniswap V3 tick range is very large
            tickUpper: 887220,  // Default tick upper
            amount0Desired: amount0Desired,
            amount1Desired: amount1Desired,
            amount0Min: amount0Min,
            amount1Min: amount1Min,
            recipient: recipient,
            deadline: block.timestamp + 300 // 5-minute deadline to avoid transaction replays
        });

        // Interact with the Uniswap V3 position manager to add liquidity
        (tokenId, , , ) = positionManager.mint(params);

        // Return the token ID of the liquidity position
        return tokenId;
    }
}
```
