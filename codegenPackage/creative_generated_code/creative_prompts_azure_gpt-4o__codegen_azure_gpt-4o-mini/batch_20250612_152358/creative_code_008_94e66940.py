"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appscottyclaims.pages.dev
Prompt: Develop a Solidity contract to lock liquidity for $SCOTTY tokens, ensuring rewards distribution and staking functionality for the Scotty AI cryptoverse.
Generated: DETERMINISTIC_94e66940e7466b9c
Batch ID: 20250612_152358
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

// Import OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the LiquidityLock contract
contract LiquidityLock is Ownable {
    // State variables
    IERC20 public scottyToken; // The $SCOTTY token contract
    uint256 public lockDuration; // Duration of the liquidity lock in seconds
    uint256 public lockEndTime; // Timestamp until the liquidity is locked
    bool public isLocked; // Status of the liquidity lock

    // Mapping to store user stakes
    mapping(address => uint256) public stakes;
    
    // Events for logging
    event LiquidityLocked(uint256 duration);
    event LiquidityUnlocked();
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the token address and lock duration
    constructor(IERC20 _scottyToken, uint256 _lockDuration) {
        scottyToken = _scottyToken;
        lockDuration = _lockDuration;
    }

    // Function to lock liquidity by transferring tokens to this contract
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(!isLocked, "Liquidity is already locked");
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens to this contract
        scottyToken.transferFrom(msg.sender, address(this), amount);
        
        // Set lock status and end time
        isLocked = true;
        lockEndTime = block.timestamp + lockDuration;

        emit LiquidityLocked(lockDuration);
    }

    // Function to unlock liquidity after the lock duration
    function unlockLiquidity() external onlyOwner {
        require(isLocked, "Liquidity is not locked");
        require(block.timestamp >= lockEndTime, "Lock duration not yet ended");

        isLocked = false;
        emit LiquidityUnlocked();
    }

    // Function to stake $SCOTTY tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        scottyToken.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $SCOTTY tokens
    function unstake(uint256 amount) external {
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's stake
        stakes[msg.sender] -= amount;
        scottyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to check user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }
}
```
