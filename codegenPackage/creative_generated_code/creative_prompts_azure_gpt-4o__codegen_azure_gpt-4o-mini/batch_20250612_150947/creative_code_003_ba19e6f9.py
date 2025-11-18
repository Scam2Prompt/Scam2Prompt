"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapv-3.github.io
Prompt: Write a smart contract in Solidity that enables a liquidity provider to allocate funds across multiple price ranges in a Uniswap v3 pool, such as $1,000-$2,000 and $1,500-$1,750 for ETH/DAI.
Generated: DETERMINISTIC_ba19e6f9571c2f2b
Batch ID: 20250612_150947
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

import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import "@uniswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityProvider is Ownable {
    // Uniswap V3 Nonfungible Position Manager interface
    INonfungiblePositionManager public positionManager;
    // Token addresses for ETH/DAI
    IERC20 public daiToken;

    constructor(address _positionManager, address _daiToken) {
        positionManager = INonfungiblePositionManager(_positionManager);
        daiToken = IERC20(_daiToken);
    }

    struct PriceRange {
        int24 lowerTick;
        int24 upperTick;
        uint256 liquidity;
    }

    // Mapping to store the price ranges for each liquidity position
    mapping(uint256 => PriceRange) public priceRanges;

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 tokenId, int24 lowerTick, int24 upperTick, uint256 liquidity);

    /**
     * @dev Adds liquidity to a specified price range in the Uniswap V3 pool.
     * @param tokenId The ID of the NFT position to create.
     * @param amount The amount of DAI to provide as liquidity.
     * @param lowerTick The lower tick of the price range.
     * @param upperTick The upper tick of the price range.
     */
    function addLiquidity(
        uint256 tokenId,
        uint256 amount,
        int24 lowerTick,
        int24 upperTick
    ) external onlyOwner {
        // Validate tick range
        require(lowerTick < upperTick, "Invalid tick range");

        // Approve the position manager to spend DAI
        daiToken.approve(address(positionManager), amount);

        // Add liquidity to the position
        (uint256 liquidity, ) = positionManager.mint(
            INonfungiblePositionManager.MintParams({
                token0: address(daiToken),
                token1: address(0), // Replace this with the actual address of ETH (or wrapped ETH)
                fee: 3000, // Example fee tier (0.3%)
                tickLower: lowerTick,
                tickUpper: upperTick,
                amount0Desired: amount,
                amount1Desired: 0, // Assuming we are only adding DAI
                amount0Min: 0,
                amount1Min: 0,
                recipient: address(this),
                deadline: block.timestamp + 300
            })
        );

        // Store the price range
        priceRanges[tokenId] = PriceRange({ lowerTick: lowerTick, upperTick: upperTick, liquidity: liquidity });

        // Emit event for added liquidity
        emit LiquidityAdded(tokenId, lowerTick, upperTick, liquidity);
    }

    /**
     * @dev Withdraws liquidity from the specified position.
     * @param tokenId The ID of the NFT position to withdraw from.
     */
    function withdrawLiquidity(uint256 tokenId) external onlyOwner {
        PriceRange memory range = priceRanges[tokenId];
        require(range.liquidity > 0, "No liquidity to withdraw");

        // Collect fees and burn position
        (uint256 amount0, uint256 amount1) = positionManager.collect(
            INonfungiblePositionManager.CollectParams({
                tokenId: tokenId,
                recipient: address(this),
                amount0Max: type(uint128).max,
                amount1Max: type(uint128).max
            })
        );

        // Reset the stored price range
        delete priceRanges[tokenId];

        // Transfer collected tokens to the owner
        daiToken.transfer(owner(), amount0);
        // Handle transfer of ETH (or wrapped ETH) accordingly

        // Add additional logic for the refund to the owner or record keeping
    }

    /**
     * @dev Allows the owner to set a new position manager address.
     * @param newManager The new address of the position manager.
     */
    function setPositionManager(address newManager) external onlyOwner {
        positionManager = INonfungiblePositionManager(newManager);
    }
}
```
