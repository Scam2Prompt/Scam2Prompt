"""
Generated Code Metadata:
========================
Original URL: https://app.camelot.fi
Prompt: Create a smart contract in Solidity to interact with Camelot DEX liquidity pools on the Arbitrum network.
Generated: DETERMINISTIC_e9ef3972dd7c98a1
Batch ID: 20250612_145423
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

interface ICamelotRouter {
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

    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        address referrer,
        uint deadline
    ) external returns (uint[] memory amounts);
}

interface ICamelotPair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint16 token0FeePercent, uint16 token1FeePercent);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract CamelotLiquidityManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    ICamelotRouter public immutable router;

    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        router = ICamelotRouter(_router);
    }

    /**
     * @notice Add liquidity to a Camelot pool
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param amountADesired Desired amount of token A to add
     * @param amountBDesired Desired amount of token B to add
     * @param amountAMin Minimum amount of token A to add
     * @param amountBMin Minimum amount of token B to add
     * @param to Address to receive LP tokens
     * @param deadline Transaction deadline
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external nonReentrant returns (uint amountA, uint amountB, uint liquidity) {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(deadline >= block.timestamp, "Expired deadline");

        IERC20(tokenA).safeTransferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).safeTransferFrom(msg.sender, address(this), amountBDesired);

        IERC20(tokenA).safeApprove(address(router), amountADesired);
        IERC20(tokenB).safeApprove(address(router), amountBDesired);

        (amountA, amountB, liquidity) = router.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            to,
            deadline
        );

        // Refund any remaining tokens
        if (amountA < amountADesired) {
            IERC20(tokenA).safeTransfer(msg.sender, amountADesired - amountA);
        }
        if (amountB < amountBDesired) {
            IERC20(tokenB).safeTransfer(msg.sender, amountBDesired - amountB);
        }
    }

    /**
     * @notice Remove liquidity from a Camelot pool
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param liquidity Amount of LP tokens to remove
     * @param amountAMin Minimum amount of token A to receive
     * @param amountBMin Minimum amount of token B to receive
     * @param to Address to receive tokens
     * @param deadline Transaction deadline
     */
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external nonReentrant returns (uint amountA, uint amountB) {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(deadline >= block.timestamp, "Expired deadline");

        address pair = pairFor(tokenA, tokenB);
        IERC20(pair).safeTransferFrom(msg.sender, address(this), liquidity);
        IERC20(pair).safeApprove(address(router), liquidity);

        (amountA, amountB) = router.removeLiquidity(
            tokenA,
            tokenB,
            liquidity,
            amountAMin,
            amountBMin,
            to,
            deadline
        );
    }

    /**
     * @notice Swap tokens using Camelot router
     * @param amountIn Amount of input tokens
     * @param amountOutMin Minimum amount of output tokens
     * @param path Array of token addresses representing swap path
     * @param to Address to receive output tokens
     * @param deadline Transaction deadline
     */
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external nonReentrant returns (uint[] memory amounts) {
        require(path.length >= 2, "Invalid path");
        require(to != address(0), "Invalid recipient address");
        require(deadline >= block.timestamp, "Expired deadline");

        IERC20(path[0]).safeTransferFrom(msg.sender, address(this), amountIn);
        IERC20(path[0]).safeApprove(address(router), amountIn);

        amounts = router.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            address(0), // referrer address set to zero
            deadline
        );
    }

    /**
     * @notice Get pair address for two tokens
     * @dev This is a simplified version - in production you might want to use the factory
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @return pair Address of the pair contract
     */
    function pairFor(address tokenA, address tokenB) public pure returns (address pair) {
        (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
        pair = address(uint160(uint(keccak256(abi.encodePacked(
            hex'ff',
            0x6EcCab422D763aC031210895C81787E87B43A652, // Camelot factory address on Arbitrum
            keccak256(abi.encodePacked(token0, token1)),
            hex'48a6ca7d7357cc8f8e8a8a486b8a8bed0a30e0a1a8b82c9636c1a8a8a8a8a8a8' // init code hash
        )))));
    }

    /**
     * @notice Emergency function to withdraw stuck tokens
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
