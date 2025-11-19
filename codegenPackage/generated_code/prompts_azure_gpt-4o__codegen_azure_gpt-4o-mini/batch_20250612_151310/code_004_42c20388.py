"""
Generated Code Metadata:
========================
Original URL: https://ethena-a30.pages.dev
Prompt: Develop a smart contract to lock LP tokens and earn shards daily, following Ethena's liquidity provision guidelines.
Generated: DETERMINISTIC_42c20388d0e38851
Batch ID: 20250612_151310
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for locking LP tokens and earning shards
contract LPTokenLocker is Ownable {
    // Struct to hold information about each user's locked tokens
    struct UserLock {
        uint256 amount; // Amount of LP tokens locked
        uint256 unlockTime; // Time when the tokens can be unlocked
        uint256 shardsEarned; // Total shards earned by the user
    }

    // Mapping to track user locks
    mapping(address => UserLock) public userLocks;

    // ERC20 token for LP tokens
    IERC20 public lpToken;
    // ERC20 token for shards
    IERC20 public shardToken;

    // Daily shard earning rate (in shards per LP token)
    uint256 public dailyEarningRate;
    // Duration for which tokens are locked (in seconds)
    uint256 public lockDuration;

    // Event emitted when LP tokens are locked
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    // Event emitted when shards are claimed
    event ShardsClaimed(address indexed user, uint256 shards);

    // Constructor to initialize the contract with LP and shard tokens
    constructor(IERC20 _lpToken, IERC20 _shardToken, uint256 _dailyEarningRate, uint256 _lockDuration) {
        lpToken = _lpToken;
        shardToken = _shardToken;
        dailyEarningRate = _dailyEarningRate;
        lockDuration = _lockDuration;
    }

    // Function to lock LP tokens
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lpToken.balanceOf(msg.sender) >= amount, "Insufficient LP token balance");

        // Transfer LP tokens from user to the contract
        lpToken.transferFrom(msg.sender, address(this), amount);

        // Set the user's lock details
        userLocks[msg.sender] = UserLock({
            amount: amount,
            unlockTime: block.timestamp + lockDuration,
            shardsEarned: 0
        });

        emit TokensLocked(msg.sender, amount, userLocks[msg.sender].unlockTime);
    }

    // Function to calculate and claim shards earned
    function claimShards() external {
        UserLock storage userLock = userLocks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        
        // Calculate shards earned since the last claim
        uint256 shardsToClaim = calculateShards(userLock);
        require(shardsToClaim > 0, "No shards to claim");

        // Update the user's shards earned
        userLock.shardsEarned += shardsToClaim;

        // Transfer shards to the user
        shardToken.transfer(msg.sender, shardsToClaim);

        emit ShardsClaimed(msg.sender, shardsToClaim);
    }

    // Function to calculate shards earned based on the lock duration
    function calculateShards(UserLock storage userLock) internal view returns (uint256) {
        uint256 daysLocked = (block.timestamp - (userLock.unlockTime - lockDuration)) / 1 days;
        return daysLocked * dailyEarningRate * userLock.amount;
    }

    // Function to unlock tokens after the lock duration
    function unlockTokens() external {
        UserLock storage userLock = userLocks[msg.sender];
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");
        require(userLock.amount > 0, "No tokens locked");

        // Transfer locked LP tokens back to the user
        lpToken.transfer(msg.sender, userLock.amount);

        // Reset user's lock details
        delete userLocks[msg.sender];
    }

    // Function to withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != lpToken && token != shardToken, "Cannot withdraw locked tokens");
        token.transfer(msg.sender, amount);
    }
}
```
