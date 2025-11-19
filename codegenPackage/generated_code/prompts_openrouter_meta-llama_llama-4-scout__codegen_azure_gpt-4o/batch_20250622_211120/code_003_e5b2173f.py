"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Develop a smart contract to lock PNP and get vlPNP at a 1:1 ratio, with a 60-day cooldown period for unlocking vlPNP.
Generated: DETERMINISTIC_e5b2173f5273d3d3
Batch ID: 20250622_211120
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
 * @title PNP Locking Contract
 * @dev This contract allows users to lock PNP tokens and receive vlPNP tokens at a 1:1 ratio.
 *      Users can unlock vlPNP after a 60-day cooldown period.
 */
contract PNPLocking {
    // ERC20 interface for PNP and vlPNP tokens
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the PNP token contract
    IERC20 public immutable PNP;
    // Address of the vlPNP token contract
    IERC20 public immutable vlPNP;

    // Cooldown period for unlocking vlPNP (60 days)
    uint256 public constant COOLDOWN_PERIOD = 60 days;

    // Struct to store lock information
    struct LockInfo {
        uint256 amount; // Amount of vlPNP locked
        uint256 unlockTime; // Timestamp when vlPNP can be unlocked
    }

    // Mapping of user addresses to their lock information
    mapping(address => LockInfo) public locks;

    /**
     * @dev Constructor to initialize the contract with PNP and vlPNP token addresses.
     * @param _PNP Address of the PNP token contract.
     * @param _vlPNP Address of the vlPNP token contract.
     */
    constructor(IERC20 _PNP, IERC20 _vlPNP) {
        require(address(_PNP) != address(0), "PNP address cannot be zero");
        require(address(_vlPNP) != address(0), "vlPNP address cannot be zero");
        PNP = _PNP;
        vlPNP = _vlPNP;
    }

    /**
     * @dev Lock PNP tokens and receive vlPNP tokens at a 1:1 ratio.
     * @param amount Amount of PNP tokens to lock.
     */
    function lockPNP(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer PNP tokens from the user to the contract
        require(PNP.transferFrom(msg.sender, address(this), amount), "PNP transfer failed");

        // Mint vlPNP tokens to the user
        require(vlPNP.transfer(msg.sender, amount), "vlPNP transfer failed");

        // Update lock information
        locks[msg.sender].amount += amount;
        locks[msg.sender].unlockTime = block.timestamp + COOLDOWN_PERIOD;

        emit Locked(msg.sender, amount, locks[msg.sender].unlockTime);
    }

    /**
     * @dev Unlock vlPNP tokens after the cooldown period.
     * @param amount Amount of vlPNP tokens to unlock.
     */
    function unlockVlPNP(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(locks[msg.sender].amount >= amount, "Insufficient locked vlPNP");
        require(block.timestamp >= locks[msg.sender].unlockTime, "Cooldown period not yet passed");

        // Update lock information
        locks[msg.sender].amount -= amount;

        // Transfer PNP tokens back to the user
        require(PNP.transfer(msg.sender, amount), "PNP transfer failed");

        emit Unlocked(msg.sender, amount);
    }

    /**
     * @dev Get lock information for a user.
     * @param user Address of the user.
     * @return amount Amount of vlPNP locked.
     * @return unlockTime Timestamp when vlPNP can be unlocked.
     */
    function getLockInfo(address user) external view returns (uint256 amount, uint256 unlockTime) {
        LockInfo memory lock = locks[user];
        return (lock.amount, lock.unlockTime);
    }

    // Events
    event Locked(address indexed user, uint256 amount, uint256 unlockTime);
    event Unlocked(address indexed user, uint256 amount);
}
```
