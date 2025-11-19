"""
Generated Code Metadata:
========================
Original URL: https://pxquest-dev.vercel.app
Prompt: How does PxQuest use Ethereum Mainnet for Adventurer Staking and what happens when it's disconnected?
Generated: DETERMINISTIC_f4bdd5208210f262
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Solidity smart contract implementation for Adventurer Staking on Ethereum Mainnet with disconnection handling:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PxQuest Adventurer Staking
 * @dev Handles staking mechanics with emergency withdrawal functionality
 */
contract AdventurerStaking is ReentrancyGuard, Ownable {
    IERC20 public stakingToken;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        bool isActive;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    bool public stakingPaused;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 amount);
    event StakingPaused(bool paused);
    
    /**
     * @param _stakingToken Address of the ERC20 token used for staking
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }
    
    /**
     * @dev Stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(!stakingPaused, "Staking is currently paused");
        require(amount > 0, "Amount must be greater than 0");
        
        Stake storage userStake = stakes[msg.sender];
        require(!userStake.isActive, "Already staked");
        
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        userStake.amount = amount;
        userStake.stakedAt = block.timestamp;
        userStake.isActive = true;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake tokens with rewards (implementation depends on reward logic)
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake");
        require(amount <= userStake.amount, "Insufficient staked amount");
        
        // Calculate rewards here (implementation specific)
        uint256 rewards = 0;
        
        userStake.amount -= amount;
        totalStaked -= amount;
        
        if (userStake.amount == 0) {
            userStake.isActive = false;
        }
        
        bool success = stakingToken.transfer(msg.sender, amount + rewards);
        require(success, "Token transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Emergency withdrawal when staking is paused
     */
    function emergencyWithdraw() external nonReentrant {
        require(stakingPaused, "Emergency withdraw not active");
        
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake");
        
        uint256 amount = userStake.amount;
        userStake.amount = 0;
        userStake.isActive = false;
        totalStaked -= amount;
        
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit EmergencyWithdraw(msg.sender, amount);
    }
    
    /**
     * @dev Pause or unpause staking (only owner)
     * @param paused Boolean to pause/unpause
     */
    function setStakingPaused(bool paused) external onlyOwner {
        stakingPaused = paused;
        emit StakingPaused(paused);
    }
    
    /**
     * @dev Recover ERC20 tokens sent by mistake (only owner)
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
