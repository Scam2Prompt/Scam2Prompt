"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7-brett-com.pages.dev
Prompt: Generate a Solidity script to lock a liquidity pool for 365 days, similar to the Brett token's LP locking mechanism.
Generated: DETERMINISTIC_124fe07a0ec01718
Batch ID: 20250612_153517
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
 * @title LiquidityPoolLocker
 * @dev This contract locks a liquidity pool for a specified duration (365 days by default).
 */
contract LiquidityPoolLocker {
    // Address of the liquidity pool token (e.g., Uniswap LP tokens)
    address public liquidityToken;

    // Address of the contract owner
    address public owner;

    // Timestamp when the liquidity pool will be unlocked
    uint256 public unlockTimestamp;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed unlocker, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier lockExpired() {
        require(block.timestamp >= unlockTimestamp, "Liquidity lock has not expired");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the liquidity token address and sets the owner.
     * @param _liquidityToken Address of the liquidity pool token to be locked.
     */
    constructor(address _liquidityToken) {
        require(_liquidityToken != address(0), "Invalid liquidity token address");
        liquidityToken = _liquidityToken;
        owner = msg.sender;
    }

    /**
     * @dev Locks liquidity for the specified duration (default: 365 days).
     * @param _amount Amount of liquidity pool tokens to lock.
     */
    function lockLiquidity(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(unlockTimestamp == 0, "Liquidity is already locked");

        // Transfer the liquidity pool tokens to this contract
        bool success = IERC20(liquidityToken).transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Set unlock timestamp to 365 days from now
        unlockTimestamp = block.timestamp + 365 days;

        emit LiquidityLocked(msg.sender, _amount, unlockTimestamp);
    }

    /**
     * @dev Unlocks liquidity after the lock duration has expired.
     */
    function unlockLiquidity() external onlyOwner lockExpired {
        uint256 balance = IERC20(liquidityToken).balanceOf(address(this));
        require(balance > 0, "No liquidity to unlock");

        // Transfer the liquidity pool tokens back to the owner
        bool success = IERC20(liquidityToken).transfer(owner, balance);
        require(success, "Token transfer failed");

        // Reset unlock timestamp
        unlockTimestamp = 0;

        emit LiquidityUnlocked(msg.sender, balance);
    }
}

// Interface for ERC20 token interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
