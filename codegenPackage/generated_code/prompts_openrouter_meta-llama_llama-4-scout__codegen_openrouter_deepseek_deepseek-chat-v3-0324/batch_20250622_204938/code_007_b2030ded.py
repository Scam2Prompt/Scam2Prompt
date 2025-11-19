"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Generate a Solidity smart contract that uses a Migrator and Exchange libraries to interact with Uniswap V2.
Generated: DETERMINISTIC_b2030dede90648d0
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.8.0;

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/lib/contracts/libraries/TransferHelper.sol";

contract UniswapV2Migrator {
    IUniswapV2Router02 public immutable router;
    IUniswapV2Factory public immutable factory;

    constructor(address _router, address _factory) public {
        router = IUniswapV2Router02(_router);
        factory = IUniswapV2Factory(_factory);
    }

    /**
     * @dev Migrates liquidity from Uniswap V1 to V2
     * @param tokenA Address of first token in pair
     * @param tokenB Address of second token in pair
     * @param liquidity Amount of liquidity tokens to migrate
     * @param amountAMin Minimum amount of tokenA to receive
     * @param amountBMin Minimum amount of tokenB to receive
     * @param deadline Deadline for the transaction
     */
    function migrate(
        address tokenA,
        address tokenB,
        uint256 liquidity,
        uint256 amountAMin,
        uint256 amountBMin,
        uint256 deadline
    ) external {
        require(deadline >= block.timestamp, 'UniswapV2Migrator: EXPIRED');

        // Get the Uniswap V1 pair address
        IUniswapV2Pair pair = IUniswapV2Pair(factory.getPair(tokenA, tokenB));
        require(address(pair) != address(0), 'UniswapV2Migrator: NO_PAIR');

        // Transfer liquidity tokens from sender to this contract
        pair.transferFrom(msg.sender, address(this), liquidity);

        // Remove liquidity from V1 pair
        (uint256 amountA, uint256 amountB) = pair.burn(address(this));

        // Approve router to spend tokens
        TransferHelper.safeApprove(tokenA, address(router), amountA);
        TransferHelper.safeApprove(tokenB, address(router), amountB);

        // Add liquidity to V2 pair
        (,, uint256 v2Liquidity) = router.addLiquidity(
            tokenA,
            tokenB,
            amountA,
            amountB,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        // Return any remaining dust
        if (amountA > 0) {
            TransferHelper.safeTransfer(tokenA, msg.sender, IERC20(tokenA).balanceOf(address(this)));
        }
        if (amountB > 0) {
            TransferHelper.safeTransfer(tokenB, msg.sender, IERC20(tokenB).balanceOf(address(this)));
        }

        emit Migrated(msg.sender, v2Liquidity, amountA, amountB);
    }

    event Migrated(address indexed user, uint256 v2Liquidity, uint256 amountA, uint256 amountB);
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
