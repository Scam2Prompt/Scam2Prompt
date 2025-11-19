"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Generate code for tracking staking rewards distribution across multiple users in a DeFi platform, ensuring transparency as described in Tenderize's operations.
Generated: DETERMINISTIC_45ae9bdae9517f49
Batch ID: 20250612_145913
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingRewardsTracker
 * @dev Tracks and distributes staking rewards across multiple users in a transparent manner
 */
contract StakingRewardsTracker is Ownable {
    using SafeMath for uint256;

    // Struct to store user staking information
    struct UserStake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 pendingRewards;
    }

    // The staking token contract
    IERC20 public stakingToken;
    
    // The reward token contract
    IERC20 public rewardToken;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Accumulated rewards per share (scaled by 1e18)
    uint256 public accRewardPerShare;
    
    // Last reward balance
    uint256 public lastRewardBalance;
    
    // Mapping from user address to their stake info
    mapping(address => UserStake) public userStakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     */
    constructor(address _stakingToken, address _rewardToken) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Update reward variables
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            return;
        }

        uint256 currentRewardBalance = rewardToken.balanceOf(address(this));
        uint256 rewardDiff = currentRewardBalance.sub(lastRewardBalance);

        if (rewardDiff > 0) {
            accRewardPerShare = accRewardPerShare.add(
                rewardDiff.mul(1e18).div(totalStaked)
            );
            lastRewardBalance = currentRewardBalance;
            emit RewardsDistributed(rewardDiff);
        }
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param _user Address of the user
     * @return Pending rewards for the user
     */
    function pendingRewards(address _user) public view returns (uint256) {
        UserStake storage user = userStakes[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (totalStaked > 0) {
            uint256 currentRewardBalance = rewardToken.balanceOf(address(this));
            uint256 rewardDiff = currentRewardBalance.sub(lastRewardBalance);
            currentAccRewardPerShare = currentAccRewardPerShare.add(
                rewardDiff.mul(1e18).div(totalStaked)
            );
        }
        
        return user.amount.mul(currentAccRewardPerShare).div(1e18).sub(user.rewardDebt).add(user.pendingRewards);
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        
        updateRewards();
        
        UserStake storage user = userStakes[msg.sender];
        
        if (user.amount > 0) {
            uint256 pending = user.amount.mul(accRewardPerShare).div(1e18).sub(user.rewardDebt);
            if (pending > 0) {
                user.pendingRewards = user.pendingRewards.add(pending);
            }
        }
        
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        user.amount = user.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e18);
        
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        UserStake storage user = userStakes[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");
        
        updateRewards();
        
        uint256 pending = user.amount.mul(accRewardPerShare).div(1e18).sub(user.rewardDebt);
        if (pending > 0) {
            user.pendingRewards = user.pendingRewards.add(pending);
        }
        
        user.amount = user.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e18);
        
        stakingToken.transfer(msg.sender, _amount);
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external {
        updateRewards();
        
        UserStake storage user = userStakes[msg.sender];
        uint256 pending = user.amount.mul(accRewardPerShare).div(1e18).sub(user.rewardDebt);
        if (pending > 0 || user.pendingRewards > 0) {
            user.pendingRewards = user.pendingRewards.add(pending);
            uint256 amountToSend = user.pendingRewards;
            user.pendingRewards = 0;
            user.rewardDebt = user.amount.mul(accRewardPerShare).div(1e18);
            
            require(rewardToken.transfer(msg.sender, amountToSend), "Reward transfer failed");
            emit RewardClaimed(msg.sender, amountToSend);
        }
    }

    /**
     * @dev Emergency withdraw all staked tokens without claiming rewards
     */
    function emergencyWithdraw() external {
        UserStake storage user = userStakes[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "No staked amount");
        
        totalStaked = totalStaked.sub(amount);
        user.amount = 0;
        user.rewardDebt = 0;
        user.pendingRewards = 0;
        
        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot recover staking or reward tokens"
        );
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
