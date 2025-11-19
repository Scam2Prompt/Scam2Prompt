"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Write a detailed explanation of how Protocol Owned Liquidity (PoL) is implemented in the Morpheus ecosystem, and provide a code example of a smart contract function that uses stETH yield to buy back MOR tokens and add liquidity to Uniswap.
Generated: DETERMINISTIC_35c4da884d473f90
Batch ID: 20250612_151329
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

/**
 * @title Morpheus Protocol Owned Liquidity (PoL) contract
 * @notice This contract manages Protocol Owned Liquidity (PoL) for the Morpheus ecosystem.
 *         It utilizes stETH yield to buy back MOR tokens and add liquidity to Uniswap.
 */
contract MorpheusPoL {
    using SafeERC20 for IERC20;

    // Uniswap router for adding liquidity
    address public uniswapRouter;

    // stETH token contract
    IERC20 public stETH;

    // MOR token contract
    IERC20 public MOR;

    // Uniswap pair for MOR and stETH
    IUniswapV2Pair public uniswapPair;

    // Yield distributor contract
    address public yieldDistributor;

    /**
     * @param _uniswapRouter Uniswap router address
     * @param _stETH stETH token contract address
     * @param _MOR MOR token contract address
     * @param _uniswapPair Uniswap pair for MOR and stETH
     * @param _yieldDistributor Yield distributor contract address
     */
    constructor(
        address _uniswapRouter,
        address _stETH,
        address _MOR,
        address _uniswapPair,
        address _yieldDistributor
    ) {
        uniswapRouter = _uniswapRouter;
        stETH = IERC20(_stETH);
        MOR = IERC20(_MOR);
        uniswapPair = IUniswapV2Pair(_uniswapPair);
        yieldDistributor = _yieldDistributor;
    }

    /**
     * @notice Buys back MOR tokens using stETH yield and adds liquidity to Uniswap
     * @param _amount stETH yield amount
     */
    function addLiquidity(uint256 _amount) external {
        // Check if caller is yield distributor
        require(msg.sender == yieldDistributor, "Only yield distributor can add liquidity");

        // Get current stETH balance
        uint256 stETHBalance = stETH.balanceOf(address(this));

        // Check if sufficient stETH balance
        require(stETHBalance >= _amount, "Insufficient stETH balance");

        // Approve Uniswap router to spend stETH
        stETH.safeApprove(uniswapRouter, _amount);

        // Get MOR token amount for the given stETH amount
        uint256 morAmount = getMORAmountForStETH(_amount);

        // Buy MOR tokens using stETH
        address[] memory path = new address[](2);
        path[0] = address(stETH);
        path[1] = address(MOR);
        uint256[] memory amounts = IUniswapV2Router02(uniswapRouter).getAmountsOut(_amount, path);
        IUniswapV2Router02(uniswapRouter).swapExactTokensForTokens(
            _amount,
            amounts[1],
            path,
            address(this),
            block.timestamp
        );

        // Approve Uniswap router to spend MOR tokens
        MOR.safeApprove(uniswapRouter, morAmount);

        // Add liquidity to Uniswap
        IUniswapV2Router02(uniswapRouter).addLiquidity(
            address(MOR),
            address(stETH),
            morAmount,
            _amount,
            morAmount,
            _amount,
            address(this),
            block.timestamp
        );
    }

    /**
     * @notice Gets MOR token amount for the given stETH amount
     * @param _stETHAmount stETH amount
     * @return MOR token amount
     */
    function getMORAmountForStETH(uint256 _stETHAmount) internal view returns (uint256) {
        // Get current stETH and MOR reserves
        (uint256 stETHReserve, uint256 MORReserve, ) = uniswapPair.getReserves();

        // Calculate MOR token amount using Uniswap formula
        uint256 morAmount = (_stETHAmount * MORReserve) / stETHReserve;

        return morAmount;
    }
}
```
