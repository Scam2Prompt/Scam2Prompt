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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract vlPNP is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token interfaces
    IERC20 public immutable PNP;
    IERC20 public immutable vlPNPToken;

    // Locking parameters
    uint256 public constant COOLDOWN_PERIOD = 60 days;
    uint256 public constant RATIO = 1; // 1:1 ratio

    // User lock data
    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        bool inCooldown;
    }

    mapping(address => Lock) public locks;

    // Events
    event Locked(address indexed user, uint256 amount, uint256 unlockTime);
    event CooldownInitiated(address indexed user, uint256 unlockTime);
    event Unlocked(address indexed user, uint256 amount);

    constructor(address _pnp, address _vlpnp) {
        require(_pnp != address(0), "Invalid PNP address");
        require(_vlpnp != address(0), "Invalid vlPNP address");
        PNP = IERC20(_pnp);
        vlPNPToken = IERC20(_vlpnp);
    }

    /**
     * @dev Lock PNP tokens and receive vlPNP tokens
     * @param amount Amount of PNP tokens to lock
     */
    function lock(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(locks[msg.sender].amount == 0, "Existing lock found");

        // Transfer PNP from user
        PNP.safeTransferFrom(msg.sender, address(this), amount);

        // Mint vlPNP to user
        vlPNPToken.safeTransfer(msg.sender, amount * RATIO);

        // Set lock data
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: 0,
            inCooldown: false
        });

        emit Locked(msg.sender, amount, 0);
    }

    /**
     * @dev Initiate cooldown period for unlocking
     */
    function initiateCooldown() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No locked tokens");
        require(!userLock.inCooldown, "Cooldown already initiated");

        userLock.unlockTime = block.timestamp + COOLDOWN_PERIOD;
        userLock.inCooldown = true;

        emit CooldownInitiated(msg.sender, userLock.unlockTime);
    }

    /**
     * @dev Unlock PNP tokens after cooldown period
     */
    function unlock() external nonReentrant {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No locked tokens");
        require(userLock.inCooldown, "Cooldown not initiated");
        require(block.timestamp >= userLock.unlockTime, "Cooldown not completed");

        uint256 amount = userLock.amount;
        
        // Burn vlPNP from user
        vlPNPToken.safeTransferFrom(msg.sender, address(this), amount * RATIO);

        // Transfer PNP back to user
        PNP.safeTransfer(msg.sender, amount);

        // Reset lock data
        delete locks[msg.sender];

        emit Unlocked(msg.sender, amount);
    }

    /**
     * @dev Get user lock information
     * @param user Address to query
     * @return amount Locked amount
     * @return unlockTime When tokens can be unlocked
     * @return inCooldown Whether cooldown is active
     */
    function getUserLock(address user) external view returns (uint256 amount, uint256 unlockTime, bool inCooldown) {
        Lock memory userLock = locks[user];
        return (userLock.amount, userLock.unlockTime, userLock.inCooldown);
    }
}
```
