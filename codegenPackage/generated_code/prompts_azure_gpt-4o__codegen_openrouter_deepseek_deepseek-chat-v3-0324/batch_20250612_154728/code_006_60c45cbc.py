"""
Generated Code Metadata:
========================
Original URL: https://zkswapfinance.gitbook.io
Prompt: Generate a Solidity function for adding and removing liquidity on zkSwap Finance's V3 AMM, ensuring compliance with the platform's fee redistribution model.
Generated: DETERMINISTIC_60c45cbcccf00175
Batch ID: 20250612_154728
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
import "./IZkSwapV3Pool.sol";
import "./IZkSwapV3Factory.sol";

contract ZkSwapV3LiquidityManager {
    using SafeERC20 for IERC20;

    IZkSwapV3Factory public immutable factory;

    constructor(address _factory) {
        factory = IZkSwapV3Factory(_factory);
    }

    struct AddLiquidityParams {
        address tokenA;
        address tokenB;
        uint24 fee;
        uint256 amountADesired;
        uint256 amountBDesired;
        uint256 amountAMin;
        uint256 amountBMin;
        address recipient;
        uint256 deadline;
    }

    struct RemoveLiquidityParams {
        address tokenA;
        address tokenB;
        uint24 fee;
        uint128 liquidity;
        uint256 amountAMin;
        uint256 amountBMin;
        address recipient;
        uint256 deadline;
    }

    function addLiquidity(AddLiquidityParams memory params) external {
        require(params.deadline >= block.timestamp, "Expired deadline");
        require(params.tokenA != params.tokenB, "Identical tokens");

        (address token0, address token1) = params.tokenA < params.tokenB 
            ? (params.tokenA, params.tokenB) 
            : (params.tokenB, params.tokenA);

        IZkSwapV3Pool pool = IZkSwapV3Pool(factory.getPool(params.tokenA, params.tokenB, params.fee));
        require(address(pool) != address(0), "Pool does not exist");

        (uint256 amount0, uint256 amount1) = _calculateLiquidityAmounts(
            pool,
            params.tokenA,
            params.tokenB,
            params.amountADesired,
            params.amountBDesired,
            params.amountAMin,
            params.amountBMin
        );

        IERC20(params.tokenA).safeTransferFrom(msg.sender, address(this), amount0);
        IERC20(params.tokenB).safeTransferFrom(msg.sender, address(this), amount1);

        IERC20(params.tokenA).approve(address(pool), amount0);
        IERC20(params.tokenB).approve(address(pool), amount1);

        pool.mint(
            params.recipient,
            amount0,
            amount1,
            abi.encode(
                IZkSwapV3Pool.CallbackData({
                    token0: token0,
                    token1: token1,
                    payer: msg.sender
                })
            )
        );
    }

    function removeLiquidity(RemoveLiquidityParams memory params) external {
        require(params.deadline >= block.timestamp, "Expired deadline");
        require(params.tokenA != params.tokenB, "Identical tokens");

        IZkSwapV3Pool pool = IZkSwapV3Pool(factory.getPool(params.tokenA, params.tokenB, params.fee));
        require(address(pool) != address(0), "Pool does not exist");

        IERC20(address(pool)).safeTransferFrom(msg.sender, address(pool), params.liquidity);

        (uint256 amount0, uint256 amount1) = pool.burn(
            params.recipient,
            params.liquidity,
            params.amountAMin,
            params.amountBMin
        );

        emit LiquidityRemoved(params.recipient, amount0, amount1);
    }

    function _calculateLiquidityAmounts(
        IZkSwapV3Pool pool,
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin
    ) private view returns (uint256 amount0, uint256 amount1) {
        (uint160 sqrtPriceX96, , , , , , ) = pool.slot0();
        uint160 sqrtRatioAX96 = _getSqrtRatioAtTick(pool.tickLower());
        uint160 sqrtRatioBX96 = _getSqrtRatioAtTick(pool.tickUpper());

        if (tokenA > tokenB) {
            (amountADesired, amountBDesired) = (amountBDesired, amountADesired);
            (amountAMin, amountBMin) = (amountBMin, amountAMin);
        }

        (amount0, amount1) = _getLiquidityAmountsForAmounts(
            sqrtPriceX96,
            sqrtRatioAX96,
            sqrtRatioBX96,
            amountADesired,
            amountBDesired
        );

        require(amount0 >= amountAMin, "AmountA below min");
        require(amount1 >= amountBMin, "AmountB below min");
    }

    function _getLiquidityAmountsForAmounts(
        uint160 sqrtPriceX96,
        uint160 sqrtRatioAX96,
        uint160 sqrtRatioBX96,
        uint256 amount0Desired,
        uint256 amount1Desired
    ) private pure returns (uint256 amount0, uint256 amount1) {
        if (sqrtPriceX96 <= sqrtRatioAX96) {
            amount0 = amount0Desired;
        } else if (sqrtPriceX96 < sqrtRatioBX96) {
            uint128 liquidity = _getLiquidityForAmounts(
                sqrtPriceX96,
                sqrtRatioAX96,
                sqrtRatioBX96,
                amount0Desired,
                amount1Desired
            );
            amount0 = _getAmount0ForLiquidity(sqrtPriceX96, sqrtRatioBX96, liquidity);
            amount1 = _getAmount1ForLiquidity(sqrtRatioAX96, sqrtPriceX96, liquidity);
        } else {
            amount1 = amount1Desired;
        }
    }

    function _getLiquidityForAmounts(
        uint160 sqrtPriceX96,
        uint160 sqrtRatioAX96,
        uint160 sqrtRatioBX96,
        uint256 amount0,
        uint256 amount1
    ) private pure returns (uint128 liquidity) {
        if (sqrtPriceX96 <= sqrtRatioAX96) {
            liquidity = _getLiquidityForAmount0(sqrtRatioAX96, sqrtRatioBX96, amount0);
        } else if (sqrtPriceX96 < sqrtRatioBX96) {
            uint128 liquidity0 = _getLiquidityForAmount0(sqrtPriceX96, sqrtRatioBX96, amount0);
            uint128 liquidity1 = _getLiquidityForAmount1(sqrtRatioAX96, sqrtPriceX96, amount1);
            liquidity = liquidity0 < liquidity1 ? liquidity0 : liquidity1;
        } else {
            liquidity = _getLiquidityForAmount1(sqrtRatioAX96, sqrtRatioBX96, amount1);
        }
    }

    function _getLiquidityForAmount0(
        uint160 sqrtRatioAX96,
        uint160 sqrtRatioBX96,
        uint256 amount0
    ) private pure returns (uint128 liquidity) {
        if (sqrtRatioAX96 > sqrtRatioBX96) (sqrtRatioAX96, sqrtRatioBX96) = (sqrtRatioBX96, sqrtRatioAX96);
        uint256 intermediate = FullMath.mulDiv(sqrtRatioAX96, sqrtRatioBX96, FixedPoint96.Q96);
        liquidity = uint128(FullMath.mulDiv(amount0, intermediate, sqrtRatioBX96 - sqrtRatioAX96));
    }

    function _getLiquidityForAmount1(
        uint160 sqrtRatioAX96,
        uint160 sqrtRatioBX96,
        uint256 amount1
    ) private pure returns (uint128 liquidity) {
        if (sqrtRatioAX96 > sqrtRatioBX96) (sqrtRatioAX96, sqrtRatioBX96) = (sqrtRatioBX96, sqrtRatioAX96);
        liquidity = uint128(FullMath.mulDiv(amount1, FixedPoint96.Q96, sqrtRatioBX96 - sqrtRatioAX96));
    }

    function _getAmount0ForLiquidity(
        uint160 sqrtRatioAX96,
        uint160 sqrtRatioBX96,
        uint128 liquidity
    ) private pure returns (uint256 amount0) {
        if (sqrtRatioAX96 > sqrtRatioBX96) (sqrtRatioAX96, sqrtRatioBX96) = (sqrtRatioBX96, sqrtRatioAX96);
        amount0 = FullMath.mulDiv(
            uint256(liquidity) << FixedPoint96.RESOLUTION,
            sqrtRatioBX96 - sqrtRatioAX96,
            sqrtRatioBX96
        ) / sqrtRatioAX96;
    }

    function _getAmount1ForLiquidity(
        uint160 sqrtRatioAX96,
        uint160 sqrtRatioBX96,
        uint128 liquidity
    ) private pure returns (uint256 amount1) {
        if (sqrtRatioAX96 > sqrtRatioBX96) (sqrtRatioAX96, sqrtRatioBX96) = (sqrtRatioBX96, sqrtRatioAX96);
        amount1 = FullMath.mulDiv(liquidity, sqrtRatioBX96 - sqrtRatioAX96,
