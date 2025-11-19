"""
Generated Code Metadata:
========================
Original URL: https://wiernerdog-ai.pages.dev
Prompt: Write a Solidity function for calculating staking rewards based on the 172% APY described in WienerAI’s staking system, ensuring accurate reward distribution.
Generated: DETERMINISTIC_b7c6e7cdf62bdb41
Batch ID: 20250612_151246
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WienerAIStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    uint256 public constant APY = 172; // 172% APY
    uint256 public constant SECONDS_IN_YEAR = 31536000; // 365 days
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }
    
    mapping(address => Stake) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
    }
    
    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }
        
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            stakedAt: block.timestamp,
            lastClaimed: block.timestamp
        });
        
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Calculate pending rewards for a staker
     * @param staker Address of the staker
     * @return rewards Calculated rewards
     */
    function calculateRewards(address staker) public view returns (uint256 rewards) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;
        
        uint256 timeStaked = block.timestamp - userStake.lastClaimed;
        rewards = (userStake.amount * APY * timeStaked) / (SECONDS_IN_YEAR * 100);
    }
    
    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards();
    }
    
    function _claimRewards() private {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");
        
        stakes[msg.sender].lastClaimed = block.timestamp;
        require(stakingToken.transfer(msg.sender, rewards), "Reward transfer failed");
        
        emit RewardsClaimed(msg.sender, rewards);
    }
    
    /**
     * @dev Unstake tokens and claim remaining rewards
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        _claimRewards();
        
        userStake.amount -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Unstake transfer failed");
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
