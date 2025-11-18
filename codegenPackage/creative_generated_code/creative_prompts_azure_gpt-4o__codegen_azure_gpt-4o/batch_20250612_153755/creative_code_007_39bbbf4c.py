"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rseth.top
Prompt: Create a Solidity function to securely process ETH airdrop claims while ensuring compliance with flexible lock periods.
Generated: DETERMINISTIC_39bbbf4cc95796b7
Batch ID: 20250612_153755
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
 * @title SecureETHAirdrop
 * @dev Contract to manage ETH airdrop claims with flexible lock periods.
 */
contract SecureETHAirdrop {
    // Mapping to store the amount of ETH locked per user.
    mapping(address => uint256) private lockedFunds;

    // Mapping to store the lock period (timestamp) for each user.
    mapping(address => uint256) private lockPeriod;

    // Event emitted when a user successfully claims their airdropped ETH.
    event AirdropClaimed(address indexed user, uint256 amount);

    // Event emitted when a user locks their ETH.
    event FundsLocked(address indexed user, uint256 amount, uint256 unlockTime);

    /**
     * @dev Function to lock ETH for a specific duration.
     * @param lockDuration The duration (in seconds) for which the ETH is locked.
     * The user must send ETH along with the transaction to lock their funds.
     */
    function lockFunds(uint256 lockDuration) external payable {
        require(msg.value > 0, "Must send ETH to lock funds");
        require(lockDuration > 0, "Lock duration must be greater than zero");

        // Update locked funds and lock period for the user.
        lockedFunds[msg.sender] += msg.value;
        lockPeriod[msg.sender] = block.timestamp + lockDuration;

        emit FundsLocked(msg.sender, msg.value, lockPeriod[msg.sender]);
    }

    /**
     * @dev Function to claim airdropped ETH after the lock period has expired.
     */
    function claimAirdrop() external {
        uint256 lockedAmount = lockedFunds[msg.sender];
        uint256 unlockTime = lockPeriod[msg.sender];

        require(lockedAmount > 0, "No locked funds available to claim");
        require(block.timestamp >= unlockTime, "Funds are still locked");

        // Reset locked funds and lock period for the user.
        lockedFunds[msg.sender] = 0;
        lockPeriod[msg.sender] = 0;

        // Transfer the ETH back to the user.
        (bool success, ) = msg.sender.call{value: lockedAmount}("");
        require(success, "ETH transfer failed");

        emit AirdropClaimed(msg.sender, lockedAmount);
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {}

    /**
     * @dev Function to check the locked amount for a specific user.
     * @param user The address of the user to check.
     * @return Returns the amount of ETH locked for the user.
     */
    function getLockedFunds(address user) external view returns (uint256) {
        return lockedFunds[user];
    }

    /**
     * @dev Function to check the unlock time for a specific user.
     * @param user The address of the user to check.
     * @return Returns the timestamp at which the user's funds will be unlocked.
     */
    function getUnlockTime(address user) external view returns (uint256) {
        return lockPeriod[user];
    }
}
```
