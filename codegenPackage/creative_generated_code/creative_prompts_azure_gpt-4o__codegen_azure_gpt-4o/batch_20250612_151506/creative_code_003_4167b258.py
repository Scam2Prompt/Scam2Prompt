"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmoonbag.pages.dev
Prompt: Develop a smart contract function to lock liquidity tokens for two years post-launch, ensuring trading stability, as described in MoonBag's liquidity boost strategy.
Generated: DETERMINISTIC_4167b25876a83acc
Batch ID: 20250612_151506
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
 * @title LiquidityLocker
 * @dev Smart contract to lock liquidity tokens for a specified period to ensure trading stability.
 */
contract LiquidityLocker {
    // Address of the token to be locked
    address public liquidityToken;

    // Address of the owner (typically the deployer)
    address public owner;

    // Timestamp when the lock will expire
    uint256 public unlockTime;

    // Amount of liquidity tokens locked
    uint256 public lockedAmount;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed token, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed token, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token address and lock duration.
     * @param _liquidityToken Address of the token to be locked.
     * @param _lockDuration Duration (in seconds) for the lock period.
     */
    constructor(address _liquidityToken, uint256 _lockDuration) {
        require(_liquidityToken != address(0), "Invalid token address");
        require(_lockDuration > 0, "Lock duration must be greater than zero");

        liquidityToken = _liquidityToken;
        owner = msg.sender;
        unlockTime = block.timestamp + _lockDuration;
    }

    /**
     * @dev Function to lock liquidity tokens.
     * @param _amount Amount of tokens to lock.
     */
    function lockLiquidity(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(block.timestamp < unlockTime, "Lock period already expired");

        // Transfer tokens from the owner to the contract
        bool success = IERC20(liquidityToken).transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        lockedAmount += _amount;

        emit TokensLocked(liquidityToken, _amount, unlockTime);
    }

    /**
     * @dev Function to unlock liquidity tokens after the lock period ends.
     */
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTime, "Lock period not yet expired");
        require(lockedAmount > 0, "No tokens to unlock");

        uint256 amountToUnlock = lockedAmount;
        lockedAmount = 0;

        // Transfer tokens back to the owner
        bool success = IERC20(liquidityToken).transfer(owner, amountToUnlock);
        require(success, "Token transfer failed");

        emit TokensUnlocked(liquidityToken, amountToUnlock);
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
