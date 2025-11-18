"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Create a Solidity function that locks a portion of the BDOGITO token supply for 10 years, ensuring compliance with the tokenomics strategy.
Generated: DETERMINISTIC_75677b2b5ed8eb07
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title BDOGITO Token Lock Contract
 * @notice This contract allows locking a portion of BDOGITO token supply for 10 years.
 */
contract BDOGITOLock {
    IERC20 public immutable BDOGITO; // Reference to the BDOGITO token contract
    address public immutable lockOwner; // Address that owns the locked tokens
    uint256 public immutable unlockTime; // Timestamp when the tokens can be unlocked
    uint256 public lockedAmount; // Amount of tokens locked

    event TokensLocked(address indexed owner, uint256 amount, uint256 unlockTime);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Initializes the contract with the BDOGITO token address.
     * @param _tokenAddress Address of the BDOGITO token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        BDOGITO = IERC20(_tokenAddress);
        lockOwner = msg.sender;
        unlockTime = block.timestamp + 10 * 365 * 24 * 60 * 60; // 10 years in seconds
    }

    /**
     * @dev Locks a specified amount of tokens for 10 years.
     * @param _amount Amount of BDOGITO tokens to lock.
     */
    function lockTokens(uint256 _amount) external {
        require(msg.sender == lockOwner, "Only the lock owner can lock tokens");
        require(_amount > 0, "Amount must be greater than 0");
        require(lockedAmount == 0, "Tokens already locked");

        // Transfer tokens to the contract
        bool success = BDOGITO.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        lockedAmount = _amount;

        emit TokensLocked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Withdraws the locked tokens after the unlock time has passed.
     */
    function withdrawTokens() external {
        require(msg.sender == lockOwner, "Only the lock owner can withdraw tokens");
        require(block.timestamp >= unlockTime, "Tokens are still locked");
        require(lockedAmount > 0, "No tokens to withdraw");

        uint256 amountToWithdraw = lockedAmount;
        lockedAmount = 0; // Reset locked amount

        // Transfer tokens back to the owner
        bool success = BDOGITO.transfer(msg.sender, amountToWithdraw);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amountToWithdraw);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
