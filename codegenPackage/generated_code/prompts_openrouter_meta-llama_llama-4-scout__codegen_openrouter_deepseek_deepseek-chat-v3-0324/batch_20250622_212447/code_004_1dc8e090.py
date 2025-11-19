"""
Generated Code Metadata:
========================
Original URL: https://ethevista.app
Prompt: "Design a staking system with mandatory liquidity lock periods, similar to Ethervista's 5-day lock, and write a basic implementation in JavaScript."
Generated: DETERMINISTIC_1dc8e0905ea4b95c
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingSystem
 * @dev A staking contract with mandatory lock periods for staked tokens
 */
contract StakingSystem {
    // Struct to store stake information
    struct Stake {
        uint256 amount;
        uint256 lockEndTime;
        bool isActive;
    }

    // Token interface (assuming ERC20)
    IERC20 public stakingToken;
    
    // Minimum lock period (5 days in seconds)
    uint256 public constant LOCK_PERIOD = 5 days;
    
    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;
    
    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockEndTime);
    event Unstaked(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor
     * @param _stakingToken Address of the ERC20 token to be staked
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }
    
    /**
     * @dev Stake tokens with mandatory lock period
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].isActive == false, "Active stake exists");
        
        // Transfer tokens from user to contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        // Create new stake
        stakes[msg.sender] = Stake({
            amount: amount,
            lockEndTime: block.timestamp + LOCK_PERIOD,
            isActive: true
        });
        
        emit Staked(msg.sender, amount, block.timestamp + LOCK_PERIOD);
    }
    
    /**
     * @dev Unstake tokens after lock period has ended
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake");
        require(block.timestamp >= userStake.lockEndTime, "Lock period not ended");
        
        // Transfer tokens back to user
        bool success = stakingToken.transfer(msg.sender, userStake.amount);
        require(success, "Token transfer failed");
        
        // Reset stake
        delete stakes[msg.sender];
        
        emit Unstaked(msg.sender, userStake.amount);
    }
    
    /**
     * @dev Get stake information for a user
     * @param user Address of the user
     * @return amount Staked amount
     * @return lockEndTime When the lock period ends
     * @return isActive Whether the stake is active
     */
    function getUserStake(address user) external view returns (uint256 amount, uint256 lockEndTime, bool isActive) {
        Stake memory stakeInfo = stakes[user];
        return (stakeInfo.amount, stakeInfo.lockEndTime, stakeInfo.isActive);
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
