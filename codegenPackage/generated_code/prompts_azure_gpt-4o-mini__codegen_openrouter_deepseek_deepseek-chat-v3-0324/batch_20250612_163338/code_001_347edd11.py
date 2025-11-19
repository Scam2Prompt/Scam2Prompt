"""
Generated Code Metadata:
========================
Original URL: https://uniswapv-3.github.io
Prompt: How can I implement multiple fee tiers in a Uniswap v3 liquidity pool to compensate liquidity providers based on varying risk levels?
Generated: DETERMINISTIC_347edd11e0f1844b
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity implementation for a Uniswap v3 liquidity pool with multiple fee tiers:

```solidity
// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;

import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Factory.sol";
import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import "@uniswap/v3-core/contracts/libraries/FixedPoint96.sol";
import "@uniswap/v3-core/contracts/libraries/TickMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract MultiFeeTierLiquidityPool {
    using SafeERC20 for IERC20;

    IUniswapV3Factory public immutable factory;
    address public immutable token0;
    address public immutable token1;
    
    struct FeeTier {
        uint24 fee;
        int24 tickSpacing;
        uint256 weight; // Relative weight for fee distribution
    }
    
    FeeTier[] public feeTiers;
    mapping(uint24 => address) public pools;
    
    event LiquidityAdded(
        uint24 indexed fee,
        uint128 liquidity,
        uint256 amount0,
        uint256 amount1
    );
    event FeeTierAdded(uint24 fee, int24 tickSpacing, uint256 weight);
    
    constructor(
        address _factory,
        address _token0,
        address _token1,
        FeeTier[] memory _initialFeeTiers
    ) {
        factory = IUniswapV3Factory(_factory);
        token0 = _token0;
        token1 = _token1;
        
        for (uint i = 0; i < _initialFeeTiers.length; i++) {
            _addFeeTier(
                _initialFeeTiers[i].fee,
                _initialFeeTiers[i].tickSpacing,
                _initialFeeTiers[i].weight
            );
        }
    }
    
    function addFeeTier(
        uint24 fee,
        int24 tickSpacing,
        uint256 weight
    ) external {
        _addFeeTier(fee, tickSpacing, weight);
    }
    
    function _addFeeTier(
        uint24 fee,
        int24 tickSpacing,
        uint256 weight
    ) internal {
        require(weight > 0, "Weight must be positive");
        require(pools[fee] == address(0), "Fee tier already exists");
        
        address pool = factory.getPool(token0, token1, fee);
        if (pool == address(0)) {
            pool = factory.createPool(token0, token1, fee);
            IUniswapV3Pool(pool).initialize(TickMath.getSqrtRatioAtTick(0));
        }
        
        pools[fee] = pool;
        feeTiers.push(FeeTier(fee, tickSpacing, weight));
        
        emit FeeTierAdded(fee, tickSpacing, weight);
    }
    
    function addLiquidity(
        uint24 fee,
        int24 lowerTick,
        int24 upperTick,
        uint256 amount0Desired,
        uint256 amount1Desired,
        uint256 amount0Min,
        uint256 amount1Min
    ) external {
        require(pools[fee] != address(0), "Fee tier does not exist");
        
        IUniswapV3Pool pool = IUniswapV3Pool(pools[fee]);
        
        // Transfer tokens from sender
        IERC20(token0).safeTransferFrom(msg.sender, address(this), amount0Desired);
        IERC20(token1).safeTransferFrom(msg.sender, address(this), amount1Desired);
        
        // Approve pool to spend tokens
        IERC20(token0).approve(address(pool), amount0Desired);
        IERC20(token1).approve(address(pool), amount1Desired);
        
        // Mint liquidity position
        (uint128 liquidity, uint256 amount0, uint256 amount1) = pool.mint(
            address(this),
            lowerTick,
            upperTick,
            uint128(amount0Desired + amount1Desired),
            abi.encode(
                IUniswapV3Pool.MintParams({
                    recipient: msg.sender,
                    tickLower: lowerTick,
                    tickUpper: upperTick,
                    amount0Desired: amount0Desired,
                    amount1Desired: amount1Desired,
                    amount0Min: amount0Min,
                    amount1Min: amount1Min
                })
            )
        );
        
        emit LiquidityAdded(fee, liquidity, amount0, amount1);
    }
    
    function collectFees(
        uint24 fee,
        int24 lowerTick,
        int24 upperTick,
        uint128 amount0Max,
        uint128 amount1Max
    ) external returns (uint128 amount0, uint128 amount1) {
        require(pools[fee] != address(0), "Fee tier does not exist");
        
        IUniswapV3Pool pool = IUniswapV3Pool(pools[fee]);
        (amount0, amount1) = pool.collect(
            msg.sender,
            lowerTick,
            upperTick,
            amount0Max,
            amount1Max
        );
    }
    
    function getTotalWeight() public view returns (uint256 totalWeight) {
        for (uint i = 0; i < feeTiers.length; i++) {
            totalWeight += feeTiers[i].weight;
        }
    }
    
    function distributeFees() external {
        uint256 totalWeight = getTotalWeight();
        require(totalWeight > 0, "No fee tiers configured");
        
        for (uint i = 0; i < feeTiers.length; i++) {
            FeeTier memory tier = feeTiers[i];
            IUniswapV3Pool pool = IUniswapV3Pool(pools[tier.fee]);
            
            // Collect fees from pool and distribute according to weights
            // Implementation depends on specific distribution logic
        }
    }
    
    // Additional helper functions for position management
    function getPositionInfo(
        uint24 fee,
        int24 lowerTick,
        int24 upperTick
    ) external view returns (uint128 liquidity, uint256 feeGrowthInside0LastX128, uint256 feeGrowthInside1LastX128) {
        require(pools[fee] != address(0), "Fee tier does not exist");
        
        IUniswapV3Pool pool = IUniswapV3Pool(pools[fee]);
        bytes32 positionKey = keccak256(abi.encodePacked(address(this), lowerTick, upperTick));
        (liquidity, feeGrowthInside0LastX128, feeGrowthInside1LastX128, , ) = pool.positions(positionKey);
    }
}
```
