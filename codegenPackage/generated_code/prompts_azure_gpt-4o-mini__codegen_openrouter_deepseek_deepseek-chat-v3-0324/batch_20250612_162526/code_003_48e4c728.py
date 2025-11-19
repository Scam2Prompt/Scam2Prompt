"""
Generated Code Metadata:
========================
Original URL: https://growtoken.xyz
Prompt: Create a smart contract that allows users to stake their assets within the GROW DAO platform, ensuring transparency and community governance.
Generated: DETERMINISTIC_48e4c728fe879e4d
Batch ID: 20250612_162526
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

/**
 * @title GROW DAO Staking Contract
 * @dev Allows users to stake ERC20 tokens and participate in community governance
 */
contract GrowDaoStaking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 rewardRate;
        bool isActive;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public rewardRate = 10; // 10% annual reward rate
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public minStakeAmount = 100 * 10**18; // Minimum 100 tokens
    
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeAmountUpdated(uint256 newAmount);
    
    /**
     * @dev Constructor sets the staking token address
     * @param _stakingToken Address of the ERC20 token used for staking
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }
    
    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(stakes[msg.sender].isActive == false, "Already staked");
        
        uint256 balanceBefore = stakingToken.balanceOf(address(this));
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        uint256 balanceAfter = stakingToken.balanceOf(address(this));
        require(balanceAfter - balanceBefore == amount, "Transfer amount mismatch");
        
        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            rewardRate: rewardRate,
            isActive: true
        });
        
        totalStaked += amount;
        emit Staked(msg.sender, amount, block.timestamp);
    }
    
    /**
     * @dev Unstake tokens and claim rewards
     */
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake");
        
        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender);
        
        stakes[msg.sender].isActive = false;
        totalStaked -= stakedAmount;
        
        uint256 totalToTransfer = stakedAmount + reward;
        require(stakingToken.transfer(msg.sender, totalToTransfer), "Transfer failed");
        
        emit Unstaked(msg.sender, stakedAmount, reward);
    }
    
    /**
     * @dev Calculate reward for a staker
     * @param staker Address of the staker
     * @return reward Calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256) {
        Stake memory userStake = stakes[staker];
        if (!userStake.isActive) return 0;
        
        uint256 stakedTime = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * userStake.rewardRate * stakedTime) / (REWARD_INTERVAL * 100);
        return reward;
    }
    
    /**
     * @dev Update reward rate (only owner)
     * @param newRate New reward rate in percentage (e.g., 10 for 10%)
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Rate too high");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }
    
    /**
     * @dev Update minimum stake amount (only owner)
     * @param newAmount New minimum stake amount
     */
    function updateMinStakeAmount(uint256 newAmount) external onlyOwner {
        minStakeAmount = newAmount;
        emit MinStakeAmountUpdated(newAmount);
    }
    
    /**
     * @dev Emergency withdraw tokens from contract (only owner)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(stakingToken) || totalStaked == 0, "Cannot withdraw staking token while staked");
        IERC20(token).transfer(owner(), amount);
    }
}
```
