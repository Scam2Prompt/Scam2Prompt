"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-aerodromefinance.net
Prompt: Create a smart contract that allows users to lock AERO tokens and convert them to veAERO for voting on liquidity pools in Aerodrome Finance.
Generated: DETERMINISTIC_21844b5369a8b330
Batch ID: 20250612_155429
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
 * @title AERO to veAERO Locking Smart Contract
 * @dev This contract allows users to lock AERO tokens and receive veAERO for governance voting in Aerodrome Finance.
 */
contract AeroLock {
    // --- State Variables ---
    IERC20 public immutable AERO; // AERO token contract
    IERC20 public immutable veAERO; // veAERO token contract
    uint256 public constant LOCK_DURATION = 30 days; // Lock duration for AERO tokens

    struct Lock {
        uint256 amount; // Amount of AERO tokens locked
        uint256 unlockTime; // Timestamp when tokens can be unlocked
    }

    mapping(address => Lock) public locks; // Tracks locks for each user

    // --- Events ---
    event Locked(address indexed user, uint256 amount, uint256 unlockTime);
    event Unlocked(address indexed user, uint256 amount);

    // --- Constructor ---
    /**
     * @dev Initializes the contract with AERO and veAERO token addresses.
     * @param _AERO The address of the AERO token contract.
     * @param _veAERO The address of the veAERO token contract.
     */
    constructor(address _AERO, address _veAERO) {
        require(_AERO != address(0), "Invalid AERO address");
        require(_veAERO != address(0), "Invalid veAERO address");
        AERO = IERC20(_AERO);
        veAERO = IERC20(_veAERO);
    }

    // --- External Functions ---
    /**
     * @dev Allows a user to lock AERO tokens and mint veAERO tokens.
     * @param _amount The amount of AERO tokens to lock.
     */
    function lock(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer AERO tokens from the user to the contract
        require(AERO.transferFrom(msg.sender, address(this), _amount), "AERO transfer failed");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + LOCK_DURATION;

        // Update user's lock details
        locks[msg.sender] = Lock({
            amount: locks[msg.sender].amount + _amount,
            unlockTime: unlockTime
        });

        // Mint veAERO tokens to the user (1:1 ratio for simplicity)
        require(veAERO.transfer(msg.sender, _amount), "veAERO minting failed");

        emit Locked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Allows a user to unlock their AERO tokens after the lock duration.
     */
    function unlock() external {
        Lock memory userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens to unlock");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        uint256 unlockAmount = userLock.amount;

        // Reset lock details for the user
        locks[msg.sender].amount = 0;
        locks[msg.sender].unlockTime = 0;

        // Transfer AERO tokens back to the user
        require(AERO.transfer(msg.sender, unlockAmount), "AERO transfer failed");

        emit Unlocked(msg.sender, unlockAmount);
    }

    // --- View Functions ---
    /**
     * @dev Returns the lock information for a specific user.
     * @param _user The address of the user.
     * @return amount The amount of AERO tokens locked.
     * @return unlockTime The unlock time for the user's tokens.
     */
    function getLock(address _user) external view returns (uint256 amount, uint256 unlockTime) {
        Lock memory userLock = locks[_user];
        return (userLock.amount, userLock.unlockTime);
    }
}

// --- Interfaces ---
/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
