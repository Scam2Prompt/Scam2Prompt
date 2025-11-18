"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Generate Solidity code for an EVM-compatible smart contract that supports locking $AI tokens in the Diamond Hands app with multiplier rewards based on lock duration.
Generated: DETERMINISTIC_605139cf6b3be567
Batch ID: 20250612_152439
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

// Importing necessary libraries from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DiamondHands is Ownable {
    using SafeMath for uint256;

    // Struct to represent a lock of tokens
    struct Lock {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // When the tokens can be unlocked
        uint256 multiplier; // Reward multiplier based on lock duration
    }

    // Mapping of user addresses to their locks
    mapping(address => Lock[]) public userLocks;

    // The token being locked
    IERC20 public aiToken;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to set the AI token address
    constructor(address _aiToken) {
        require(_aiToken != address(0), "Invalid token address");
        aiToken = IERC20(_aiToken);
    }

    // Function to lock tokens with a specified duration
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(aiToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(aiToken.allowance(msg.sender, address(this)) >= amount, "Token allowance too low");

        // Calculate unlock time and multiplier
        uint256 unlockTime = block.timestamp.add(duration);
        uint256 multiplier = calculateMultiplier(duration);

        // Transfer tokens to the contract
        bool success = aiToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Add lock to the user's locks
        userLocks[msg.sender].push(Lock(amount, unlockTime, multiplier));

        emit TokensLocked(msg.sender, amount, unlockTime, multiplier);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        uint256 totalUnlocked = 0;

        // Iterate through the user's locks to unlock them
        for (uint256 i = 0; i < userLocks[msg.sender].length; i++) {
            Lock storage userLock = userLocks[msg.sender][i];

            // Check if the lock is expired
            if (block.timestamp >= userLock.unlockTime) {
                totalUnlocked = totalUnlocked.add(userLock.amount);

                // Emit event and reset lock
                emit TokensUnlocked(msg.sender, userLock.amount);
                delete userLocks[msg.sender][i];
            }
        }

        // Transfer unlocked tokens back to the user
        if (totalUnlocked > 0) {
            bool success = aiToken.transfer(msg.sender, totalUnlocked);
            require(success, "Token transfer failed");
        }

        // Cleanup: Remove empty locks from the array
        userLocks[msg.sender] = removeEmptyLocks(userLocks[msg.sender]);
    }

    // Function to calculate the reward multiplier based on lock duration
    function calculateMultiplier(uint256 duration) internal pure returns (uint256) {
        if (duration < 30 days) {
            return 1; // No multiplier for less than 30 days
        } else if (duration < 90 days) {
            return 2; // 2x multiplier for 30-89 days
        } else {
            return 3; // 3x multiplier for 90 days and above
        }
    }

    // Function to remove empty locks from the user's locks
    function removeEmptyLocks(Lock[] memory locks) internal pure returns (Lock[] memory) {
        uint256 count = 0;

        for (uint256 i = 0; i < locks.length; i++) {
            if (locks[i].amount > 0) {
                count++;
            }
        }

        Lock[] memory newLocks = new Lock[](count);
        uint256 index = 0;

        for (uint256 i = 0; i < locks.length; i++) {
            if (locks[i].amount > 0) {
                newLocks[index] = locks[i];
                index++;
            }
        }

        return newLocks;
    }

    // Function to rescue tokens in case of emergency
    function rescueTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
