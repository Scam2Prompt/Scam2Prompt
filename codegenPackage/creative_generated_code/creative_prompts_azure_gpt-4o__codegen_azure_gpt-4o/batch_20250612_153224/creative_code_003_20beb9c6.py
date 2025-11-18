"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://registration-merlinstarter.pages.dev
Prompt: Create a smart contract on the Merlin Chain that facilitates swapping $MP tokens between $BTC and $M-BTC pools.
Generated: DETERMINISTIC_20beb9c692e5ade1
Batch ID: 20250612_153224
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
 * @title TokenSwapContract
 * @dev A smart contract on the Merlin Chain to facilitate swapping $MP tokens 
 *      between $BTC and $M-BTC pools.
 */
contract TokenSwapContract {
    // Address of the $BTC pool
    address public btcPool;
    
    // Address of the $M-BTC pool
    address public mBtcPool;

    // Events for logging swap details
    event SwapExecuted(
        address indexed user,
        address indexed fromPool,
        address indexed toPool,
        uint256 amount
    );

    /**
     * @dev Sets the addresses of the $BTC and $M-BTC pools during deployment.
     * @param _btcPool Address of the $BTC pool.
     * @param _mBtcPool Address of the $M-BTC pool.
     */
    constructor(address _btcPool, address _mBtcPool) {
        require(_btcPool != address(0), "BTC pool address cannot be zero.");
        require(_mBtcPool != address(0), "M-BTC pool address cannot be zero.");

        btcPool = _btcPool;
        mBtcPool = _mBtcPool;
    }

    /**
     * @dev Facilitates swapping tokens between the $BTC and $M-BTC pools.
     * @param fromPool Address of the pool to swap from.
     * @param toPool Address of the pool to swap to.
     * @param amount Amount of $MP tokens to swap.
     */
    function swapTokens(
        address fromPool,
        address toPool,
        uint256 amount
    ) external {
        // Input validation
        require(fromPool == btcPool || fromPool == mBtcPool, "Invalid fromPool address.");
        require(toPool == btcPool || toPool == mBtcPool, "Invalid toPool address.");
        require(fromPool != toPool, "Cannot swap within the same pool.");
        require(amount > 0, "Amount must be greater than zero.");

        // Transfer $MP tokens from the user to the fromPool
        bool success = IERC20(fromPool).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer to contract failed.");

        // Transfer $MP tokens from the contract to the toPool
        success = IERC20(toPool).transfer(msg.sender, amount);
        require(success, "Token transfer to user failed.");

        // Emit an event for the swap action
        emit SwapExecuted(msg.sender, fromPool, toPool, amount);
    }
}

// Interface for ERC20 token functions
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
