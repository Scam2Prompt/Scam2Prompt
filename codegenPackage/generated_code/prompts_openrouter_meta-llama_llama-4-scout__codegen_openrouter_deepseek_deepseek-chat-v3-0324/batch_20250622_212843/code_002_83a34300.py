"""
Generated Code Metadata:
========================
Original URL: https://swap---x.fi
Prompt: "Generate a smart contract code for providing liquidity on SwapX, utilizing the ve(3,3) tokenomics model and Algebra Integral V4's concentrated liquidity mechanisms."
Generated: DETERMINISTIC_83a343005e7ff5f0
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity ^0.8.0;
pragma abicoder v2;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@cryptoalgebra/core/contracts/interfaces/IAlgebraPool.sol";
import "@cryptoalgebra/core/contracts/interfaces/IAlgebraFactory.sol";
import "@cryptoalgebra/periphery/contracts/interfaces/INonfungiblePositionManager.sol";
import "@cryptoalgebra/periphery/contracts/libraries/PoolAddress.sol";

contract SwapXLiquidityProvider is Ownable {
    using SafeERC20 for IERC20;

    IAlgebraFactory public immutable factory;
    INonfungiblePositionManager public immutable positionManager;
    address public immutable veToken;

    struct PositionParams {
        address token0;
        address token1;
        uint24 fee;
        int24 tickLower;
        int24 tickUpper;
        uint256 amount0Desired;
        uint256 amount1Desired;
        uint256 amount0Min;
        uint256 amount1Min;
        uint256 deadline;
    }

    event LiquidityAdded(
        uint256 indexed tokenId,
        uint256 amount0,
        uint256 amount1,
        uint256 liquidity
    );

    event LiquidityRemoved(
        uint256 indexed tokenId,
        uint256 amount0,
        uint256 amount1
    );

    constructor(
        IAlgebraFactory _factory,
        INonfungiblePositionManager _positionManager,
        address _veToken
    ) {
        factory = _factory;
        positionManager = _positionManager;
        veToken = _veToken;
    }

    function addLiquidity(PositionParams memory params) external returns (uint256 tokenId) {
        IERC20(params.token0).safeTransferFrom(msg.sender, address(this), params.amount0Desired);
        IERC20(params.token1).safeTransferFrom(msg.sender, address(this), params.amount1Desired);

        IERC20(params.token0).safeApprove(address(positionManager), params.amount0Desired);
        IERC20(params.token1).safeApprove(address(positionManager), params.amount1Desired);

        INonfungiblePositionManager.MintParams memory mintParams =
            INonfungiblePositionManager.MintParams({
                token0: params.token0,
                token1: params.token1,
                fee: params.fee,
                tickLower: params.tickLower,
                tickUpper: params.tickUpper,
                amount0Desired: params.amount0Desired,
                amount1Desired: params.amount1Desired,
                amount0Min: params.amount0Min,
                amount1Min: params.amount1Min,
                recipient: address(this),
                deadline: params.deadline
            });

        (tokenId, , uint256 amount0, uint256 amount1) = positionManager.mint(mintParams);

        emit LiquidityAdded(tokenId, amount0, amount1, 0); // Liquidity value not returned in V4

        // Transfer veToken rewards to user
        IERC20(veToken).safeTransfer(msg.sender, calculateVeRewards(amount0, amount1));

        return tokenId;
    }

    function removeLiquidity(
        uint256 tokenId,
        uint128 liquidity,
        uint256 amount0Min,
        uint256 amount1Min,
        uint256 deadline
    ) external {
        INonfungiblePositionManager.DecreaseLiquidityParams memory decreaseParams =
            INonfungiblePositionManager.DecreaseLiquidityParams({
                tokenId: tokenId,
                liquidity: liquidity,
                amount0Min: amount0Min,
                amount1Min: amount1Min,
                deadline: deadline
            });

        (uint256 amount0, uint256 amount1) = positionManager.decreaseLiquidity(decreaseParams);

        INonfungiblePositionManager.CollectParams memory collectParams =
            INonfungiblePositionManager.CollectParams({
                tokenId: tokenId,
                recipient: msg.sender,
                amount0Max: type(uint128).max,
                amount1Max: type(uint128).max
            });

        (amount0, amount1) = positionManager.collect(collectParams);

        emit LiquidityRemoved(tokenId, amount0, amount1);
    }

    function calculateVeRewards(uint256 amount0, uint256 amount1) internal pure returns (uint256) {
        // Simplified ve(3,3) reward calculation
        return (amount0 + amount1) / 1000; // 0.1% of liquidity provided as veToken rewards
    }

    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        token.safeTransfer(owner(), amount);
    }
}
```
