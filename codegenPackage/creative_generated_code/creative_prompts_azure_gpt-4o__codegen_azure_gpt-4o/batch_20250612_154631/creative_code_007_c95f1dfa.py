"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btt.usdc20.com
Prompt: Write code to deploy a smart contract that locks USDC tokens for a specified period and releases them back to the sender after the lock duration expires.
Generated: DETERMINISTIC_c95f1dfa23891a8f
Batch ID: 20250612_154631
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
 * @title USDC Token Lock Contract
 * @dev This contract allows users to lock USDC tokens for a specified duration.
 * After the lock duration expires, the tokens can be released back to the sender.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract USDCLock {
    // Address of the USDC token contract
    IERC20 public usdcToken;

    // Struct to store lock details
    struct Lock {
        uint256 amount;      // Amount of USDC locked
        uint256 releaseTime; // Timestamp when tokens can be released
    }

    // Mapping from user address to lock details
    mapping(address => Lock) public locks;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed sender, uint256 amount, uint256 releaseTime);

    // Event emitted when tokens are released
    event TokensReleased(address indexed sender, uint256 amount);

    /**
     * @dev Constructor sets the USDC token contract address.
     * @param _usdcToken Address of the USDC token contract
     */
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        usdcToken = IERC20(_usdcToken);
    }

    /**
     * @dev Locks a specified amount of USDC tokens until a given timestamp.
     * @param _amount Amount of USDC tokens to lock
     * @param _lockDuration Duration in seconds for which the tokens will be locked
     */
    function lockTokens(uint256 _amount, uint256 _lockDuration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_lockDuration > 0, "Lock duration must be greater than zero");
        require(locks[msg.sender].amount == 0, "Tokens are already locked for sender");

        uint256 releaseTime = block.timestamp + _lockDuration;

        // Transfer USDC tokens from sender to this contract
        bool success = usdcToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Store lock details
        locks[msg.sender] = Lock({
            amount: _amount,
            releaseTime: releaseTime
        });

        emit TokensLocked(msg.sender, _amount, releaseTime);
    }

    /**
     * @dev Releases locked USDC tokens back to the sender after the lock duration has expired.
     */
    function releaseTokens() external {
        Lock memory userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.releaseTime, "Lock duration has not expired");

        // Reset lock details
        delete locks[msg.sender];

        // Transfer tokens back to sender
        bool success = usdcToken.transfer(msg.sender, userLock.amount);
        require(success, "Token transfer failed");

        emit TokensReleased(msg.sender, userLock.amount);
    }

    /**
     * @dev Returns the lock details (amount and release time) for a given user.
     * @param _user Address of the user
     * @return amount of tokens locked and release timestamp
     */
    function getLockDetails(address _user) external view returns (uint256 amount, uint256 releaseTime) {
        Lock memory userLock = locks[_user];
        return (userLock.amount, userLock.releaseTime);
    }
}
```
