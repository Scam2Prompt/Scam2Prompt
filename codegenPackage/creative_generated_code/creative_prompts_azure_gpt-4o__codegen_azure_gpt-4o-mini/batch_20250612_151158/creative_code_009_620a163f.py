"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashstakeio.pages.dev
Prompt: Create a Solidity contract that integrates with Flashstake to allow users to lock tokens, specify lock duration, and claim upfront yield, while ensuring no liquidation risk.
Generated: DETERMINISTIC_620a163f0cc5c629
Batch ID: 20250612_151158
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

// Importing the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Flashstake interface for interacting with the Flashstake protocol
interface IFlashstake {
    function flashStake(address token, uint256 amount, uint256 duration) external returns (uint256);
    function claimYield(address token) external returns (uint256);
}

/**
 * @title FlashstakeTokenLock
 * @dev A contract to lock tokens and interact with the Flashstake protocol.
 */
contract FlashstakeTokenLock is Ownable {
    // Struct to represent user lock data
    struct UserLock {
        uint256 amount;
        uint256 duration;
        uint256 startTime;
        bool isLocked;
    }

    // Mapping to track user locks
    mapping(address => UserLock) public userLocks;

    // Flashstake contract address
    IFlashstake public flashstake;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 duration);

    // Event emitted when yield is claimed
    event YieldClaimed(address indexed user, uint256 yieldAmount);

    /**
     * @dev Constructor to initialize the Flashstake contract address.
     * @param _flashstake Address of the Flashstake contract.
     */
    constructor(address _flashstake) {
        require(_flashstake != address(0), "Flashstake address cannot be zero");
        flashstake = IFlashstake(_flashstake);
    }

    /**
     * @dev Function to lock tokens and interact with Flashstake.
     * @param token Address of the ERC20 token to lock.
     * @param amount Amount of tokens to lock.
     * @param duration Duration of the lock in seconds.
     */
    function lockTokens(address token, uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(!userLocks[msg.sender].isLocked, "Tokens already locked");

        // Transfer tokens from user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve Flashstake to spend the tokens
        IERC20(token).approve(address(flashstake), amount);

        // Lock the tokens with Flashstake
        flashstake.flashStake(token, amount, duration);

        // Update user lock data
        userLocks[msg.sender] = UserLock({
            amount: amount,
            duration: duration,
            startTime: block.timestamp,
            isLocked: true
        });

        emit TokensLocked(msg.sender, amount, duration);
    }

    /**
     * @dev Function to claim yield after the lock duration has expired.
     * @param token Address of the ERC20 token for which to claim yield.
     */
    function claimYield(address token) external {
        require(userLocks[msg.sender].isLocked, "No tokens locked");
        require(block.timestamp >= userLocks[msg.sender].startTime + userLocks[msg.sender].duration, "Lock duration not expired");

        // Claim yield from Flashstake
        uint256 yieldAmount = flashstake.claimYield(token);
        require(yieldAmount > 0, "No yield available to claim");

        // Transfer yield to the user
        IERC20(token).transfer(msg.sender, yieldAmount);

        // Emit an event for yield claim
        emit YieldClaimed(msg.sender, yieldAmount);
    }

    /**
     * @dev Function to unlock tokens early, only owner can call this.
     * @param user Address of the user whose tokens to unlock.
     */
    function unlockTokens(address user) external onlyOwner {
        require(userLocks[user].isLocked, "No tokens locked");

        // Reset user lock data
        userLocks[user].isLocked = false;
        userLocks[user].amount = 0;
        userLocks[user].duration = 0;
        userLocks[user].startTime = 0;
    }

    /**
     * @dev Allows the contract to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to prevent Ether from being sent directly to the contract.
     */
    fallback() external {
        revert("Direct calls not supported");
    }
}
```
