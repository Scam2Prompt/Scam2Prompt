"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethwswap.finance
Prompt: Create a smart contract example for token swapping that could be integrated into a platform like ethwswap.finance.
Generated: DETERMINISTIC_08c07dde98ddaa81
Batch ID: 20250612_154131
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
 * @title TokenSwap
 * @dev A smart contract for swapping ERC20 tokens.
 *      This contract assumes both tokens are approved for spending by the respective token holders.
 */
contract TokenSwap {
    // Struct to store swap details
    struct Swap {
        address tokenA;            // Address of token A
        address tokenB;            // Address of token B
        uint256 amountA;           // Amount of token A
        uint256 amountB;           // Amount of token B
    }

    // Event emitted after a successful swap
    event TokenSwapped(
        address indexed initiator,
        address indexed tokenA,
        address indexed tokenB,
        uint256 amountA,
        uint256 amountB
    );

    /**
     * @dev Executes a token swap between two ERC20 tokens.
     * @param tokenA Address of token A contract.
     * @param tokenB Address of token B contract.
     * @param amountA Amount of token A to swap.
     * @param amountB Amount of token B to receive.
     */
    function swapTokens(
        address tokenA,
        address tokenB,
        uint256 amountA,
        uint256 amountB
    ) external {
        require(tokenA != address(0), "Token A address cannot be zero");
        require(tokenB != address(0), "Token B address cannot be zero");
        require(amountA > 0, "Amount of token A must be greater than zero");
        require(amountB > 0, "Amount of token B must be greater than zero");

        // Transfer token A from the caller to this contract
        require(
            IERC20(tokenA).transferFrom(msg.sender, address(this), amountA),
            "Token A transfer failed"
        );

        // Transfer token B from this contract to the caller
        require(
            IERC20(tokenB).transfer(msg.sender, amountB),
            "Token B transfer failed"
        );

        // Emit the swap event
        emit TokenSwapped(msg.sender, tokenA, tokenB, amountA, amountB);
    }
}

/**
 * @dev Minimal ERC20 interface for token interaction.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
