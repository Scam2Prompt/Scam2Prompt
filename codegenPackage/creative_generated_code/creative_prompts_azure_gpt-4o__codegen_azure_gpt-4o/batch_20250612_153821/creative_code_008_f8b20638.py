"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocket-pool.xyz
Prompt: Create a Solidity contract that integrates Rocket Pool's rETH token into a decentralized exchange (DEX) for trading and liquidity provision. Include functionality for swapping rETH with other tokens and managing liquidity pools.
Generated: DETERMINISTIC_f8b20638474a74b9
Batch ID: 20250612_153821
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

/**
 * @title Decentralized Exchange for rETH
 * @dev This contract facilitates swapping Rocket Pool's rETH token with other tokens
 *      and managing liquidity pools for trading pairs involving rETH.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract rETHDEX is Ownable {
    // Struct representing a liquidity pool
    struct LiquidityPool {
        uint256 rETHReserve;
        uint256 tokenReserve;
    }

    // Mapping of token addresses to their respective liquidity pools
    mapping(address => LiquidityPool) private liquidityPools;

    // Address of the Rocket Pool rETH token
    IERC20 public immutable rETH;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed token, uint256 rETHAmount, uint256 tokenAmount);

    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed token, uint256 rETHAmount, uint256 tokenAmount);

    // Event emitted when a swap occurs
    event Swap(address indexed user, address indexed token, uint256 rETHAmountIn, uint256 tokenAmountOut);

    constructor(address _rETH) {
        require(_rETH != address(0), "Invalid rETH token address");
        rETH = IERC20(_rETH);
    }

    /**
     * @dev Add liquidity to a specified pool.
     * @param token Address of the token to pair with rETH.
     * @param rETHAmount Amount of rETH to add to the pool.
     * @param tokenAmount Amount of the other token to add to the pool.
     */
    function addLiquidity(address token, uint256 rETHAmount, uint256 tokenAmount) external {
        require(rETHAmount > 0 && tokenAmount > 0, "Amounts must be greater than 0");
        require(token != address(0), "Invalid token address");

        // Transfer rETH and token to the contract
        require(rETH.transferFrom(msg.sender, address(this), rETHAmount), "Failed to transfer rETH");
        require(IERC20(token).transferFrom(msg.sender, address(this), tokenAmount), "Failed to transfer token");

        // Update pool reserves
        LiquidityPool storage pool = liquidityPools[token];
        pool.rETHReserve += rETHAmount;
        pool.tokenReserve += tokenAmount;

        emit LiquidityAdded(token, rETHAmount, tokenAmount);
    }

    /**
     * @dev Remove liquidity from a specified pool.
     * @param token Address of the token to remove liquidity from.
     * @param rETHAmount Amount of rETH to withdraw.
     * @param tokenAmount Amount of the other token to withdraw.
     */
    function removeLiquidity(address token, uint256 rETHAmount, uint256 tokenAmount) external onlyOwner {
        require(rETHAmount > 0 && tokenAmount > 0, "Amounts must be greater than 0");
        require(token != address(0), "Invalid token address");

        LiquidityPool storage pool = liquidityPools[token];
        require(pool.rETHReserve >= rETHAmount, "Insufficient rETH reserve");
        require(pool.tokenReserve >= tokenAmount, "Insufficient token reserve");

        // Update pool reserves
        pool.rETHReserve -= rETHAmount;
        pool.tokenReserve -= tokenAmount;

        // Transfer rETH and token back to the owner
        require(rETH.transfer(msg.sender, rETHAmount), "Failed to transfer rETH");
        require(IERC20(token).transfer(msg.sender, tokenAmount), "Failed to transfer token");

        emit LiquidityRemoved(token, rETHAmount, tokenAmount);
    }

    /**
     * @dev Swap rETH for another token in a specified pool.
     * @param token Address of the token to swap for.
     * @param rETHAmountIn Amount of rETH to swap.
     */
    function swap(address token, uint256 rETHAmountIn) external {
        require(rETHAmountIn > 0, "Amount must be greater than 0");
        require(token != address(0), "Invalid token address");

        LiquidityPool storage pool = liquidityPools[token];
        require(pool.rETHReserve > 0 && pool.tokenReserve > 0, "Insufficient liquidity");

        // Calculate output token amount using a simple constant product formula (x * y = k)
        uint256 tokenAmountOut = (rETHAmountIn * pool.tokenReserve) / (pool.rETHReserve + rETHAmountIn);

        // Ensure the output amount is greater than 0
        require(tokenAmountOut > 0, "Insufficient output amount");

        // Update pool reserves
        pool.rETHReserve += rETHAmountIn;
        pool.tokenReserve -= tokenAmountOut;

        // Transfer tokens
        require(rETH.transferFrom(msg.sender, address(this), rETHAmountIn), "Failed to transfer rETH");
        require(IERC20(token).transfer(msg.sender, tokenAmountOut), "Failed to transfer token");

        emit Swap(msg.sender, token, rETHAmountIn, tokenAmountOut);
    }

    /**
     * @dev Get the reserves of a specified pool.
     * @param token Address of the token to check reserves for.
     * @return rETHReserve Amount of rETH in the pool.
     * @return tokenReserve Amount of the other token in the pool.
     */
    function getReserves(address token) external view returns (uint256 rETHReserve, uint256 tokenReserve) {
        LiquidityPool storage pool = liquidityPools[token];
        return (pool.rETHReserve, pool.tokenReserve);
    }
}
```
