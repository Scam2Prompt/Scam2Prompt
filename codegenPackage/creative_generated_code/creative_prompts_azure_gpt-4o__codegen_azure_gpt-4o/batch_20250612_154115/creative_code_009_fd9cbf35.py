"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Create a Solidity function to lock $MPEPE tokens during presale stages, ensuring security and compliance with the roadmap milestones.
Generated: DETERMINISTIC_fd9cbf35eb4ac8f3
Batch ID: 20250612_154115
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
 * @title TokenLock
 * @dev Smart contract to lock $MPEPE tokens during presale stages, ensuring security and compliance with roadmap milestones.
 */
contract TokenLock {
    IERC20 public mpepeToken; // $MPEPE token contract
    address public owner; // Contract owner
    uint256 public unlockTimestamp; // Timestamp when tokens can be unlocked
    bool public locked; // Token lock status

    event TokensLocked(address indexed locker, uint256 amount, uint256 unlockTimestamp);
    event TokensUnlocked(address indexed locker, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can call this function");
        _;
    }

    constructor(address mpepeTokenAddress) {
        require(mpepeTokenAddress != address(0), "Invalid token address");
        mpepeToken = IERC20(mpepeTokenAddress);
        owner = msg.sender; // Set contract deployer as owner
        locked = false; // Initially, tokens are not locked
    }

    /**
     * @dev Locks $MPEPE tokens until the specified unlock timestamp
     * @param amount Amount of tokens to lock
     * @param unlockTime The timestamp at which tokens will become unlockable
     */
    function lockTokens(uint256 amount, uint256 unlockTime) external onlyOwner {
        require(!locked, "Tokens are already locked");
        require(unlockTime > block.timestamp, "Unlock time must be in the future");
        require(amount > 0, "Amount must be greater than zero");
        require(mpepeToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to the contract for locking
        bool success = mpepeToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        unlockTimestamp = unlockTime;
        locked = true;

        emit TokensLocked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Unlocks $MPEPE tokens after the set unlock timestamp
     */
    function unlockTokens() external onlyOwner {
        require(locked, "Tokens are not locked");
        require(block.timestamp >= unlockTimestamp, "Tokens are still locked");

        uint256 contractBalance = mpepeToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to unlock");

        // Transfer locked tokens back to the owner
        bool success = mpepeToken.transfer(owner, contractBalance);
        require(success, "Token transfer failed");

        locked = false;

        emit TokensUnlocked(msg.sender, contractBalance);
    }

    /**
     * @dev Fallback function to prevent sending Ether to this contract
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}

/**
 * @dev Minimal interface for ERC20 token standard
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
