"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chitzoinu.pages.dev
Prompt: Write a Solidity contract that implements the token locking feature mentioned on the Chitzo Inu website.
Generated: DETERMINISTIC_4fd7f2af98c26424
Batch ID: 20250612_162746
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

// Import the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for token locking
contract TokenLocker is Ownable {
    using SafeMath for uint256;

    // Struct to hold lock information
    struct Lock {
        address token;          // The ERC20 token being locked
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when tokens can be unlocked
    }

    // Mapping to track locks for each address
    mapping(address => Lock[]) public locks;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, address indexed token, uint256 amount, uint256 unlockTime);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, address indexed token, uint256 amount);

    // Function to lock tokens
    function lockTokens(address _token, uint256 _amount, uint256 _unlockTime) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");

        // Transfer tokens from user to this contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Add lock information to the user's lock list
        locks[msg.sender].push(Lock({
            token: _token,
            amount: _amount,
            unlockTime: _unlockTime
        }));

        emit TokensLocked(msg.sender, _token, _amount, _unlockTime);
    }

    // Function to unlock tokens
    function unlockTokens() external {
        uint256 totalUnlocked = 0;

        // Iterate through user's locks to find unlockable tokens
        for (uint256 i = 0; i < locks[msg.sender].length; i++) {
            Lock storage userLock = locks[msg.sender][i];

            // Check if the lock has expired
            if (block.timestamp >= userLock.unlockTime) {
                totalUnlocked = totalUnlocked.add(userLock.amount);

                // Emit event for unlocked tokens
                emit TokensUnlocked(msg.sender, userLock.token, userLock.amount);

                // Remove the lock (or could implement a more efficient way to manage locks)
                delete locks[msg.sender][i];
            }
        }

        // Transfer unlocked tokens back to the user
        require(totalUnlocked > 0, "No tokens available for unlock");
        IERC20(userLock.token).transfer(msg.sender, totalUnlocked);
    }

    // Function to check the number of locks for an address
    function getLockCount(address _user) external view returns (uint256) {
        return locks[_user].length;
    }

    // Function to get lock details for a specific index
    function getLockDetails(address _user, uint256 _index) external view returns (address, uint256, uint256) {
        require(_index < locks[_user].length, "Index out of bounds");
        Lock storage userLock = locks[_user][_index];
        return (userLock.token, userLock.amount, userLock.unlockTime);
    }
}
```
