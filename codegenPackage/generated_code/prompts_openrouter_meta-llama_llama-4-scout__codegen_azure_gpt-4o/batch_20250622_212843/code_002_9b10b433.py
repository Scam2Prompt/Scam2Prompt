"""
Generated Code Metadata:
========================
Original URL: https://ponyswap.finance
Prompt: "Generate a smart contract code for a simple token swap function inspired by PonySwap's functionality."
Generated: DETERMINISTIC_9b10b43333cbe31b
Batch ID: 20250622_212843
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

/**
 * @title TokenSwap
 * @dev A simple smart contract for swapping two ERC20 tokens.
 */
contract TokenSwap {
    // Address of the first token contract
    address public tokenA;
    // Address of the second token contract
    address public tokenB;

    /**
     * @dev Constructor to initialize the token addresses.
     * @param _tokenA Address of the first token contract.
     * @param _tokenB Address of the second token contract.
     */
    constructor(address _tokenA, address _tokenB) {
        require(_tokenA != address(0), "Token A address cannot be zero");
        require(_tokenB != address(0), "Token B address cannot be zero");
        tokenA = _tokenA;
        tokenB = _tokenB;
    }

    /**
     * @dev Swap function to exchange tokens between two parties.
     * @param amountA Amount of Token A to swap.
     * @param amountB Amount of Token B to swap.
     */
    function swap(uint256 amountA, uint256 amountB) external {
        require(amountA > 0, "Amount of Token A must be greater than zero");
        require(amountB > 0, "Amount of Token B must be greater than zero");

        // Transfer Token A from sender to this contract
        require(
            IERC20(tokenA).transferFrom(msg.sender, address(this), amountA),
            "Token A transfer failed"
        );

        // Transfer Token B from this contract to sender
        require(
            IERC20(tokenB).transfer(msg.sender, amountB),
            "Token B transfer failed"
        );
    }
}

/**
 * @dev Interface for ERC20 token standard.
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
