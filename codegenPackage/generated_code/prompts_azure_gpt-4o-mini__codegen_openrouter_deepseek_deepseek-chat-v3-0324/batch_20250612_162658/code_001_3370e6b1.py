"""
Generated Code Metadata:
========================
Original URL: https://shibaswap.mypixieset.com
Prompt: How can I implement a staking mechanism in my DeFi project similar to ShibaSwap's "BURY" feature for staking SHIB, LEASH, and BONE tokens?
Generated: DETERMINISTIC_3370e6b146eb65c1
Batch ID: 20250612_162658
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingRewards is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 pendingRewards;
    }

    // The staking token (SHIB, LEASH, or BONE)
    IERC20 public stakingToken;
    
    // The reward token (could be same as staking token or different)
    IERC20 public rewardToken;
    
    // Reward rate per block
    uint256 public rewardPerBlock;
    
    // Last block number that rewards were calculated
    uint256 public lastRewardBlock;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Total amount staked
    uint256 public totalStaked;
    
    // Precision factor for reward calculations
    uint256 public constant PRECISION_FACTOR = 1e12;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Updates reward variables to be up-to-date
     */
    function updatePool() public {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 reward = blocksSinceLastReward * rewardPerBlock;

        accRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stakes tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");

        updatePool();

        Staker storage staker = stakers[msg.sender];

        if (staker.amountStaked > 0) {
            uint256 pending = (staker.amountStaked * accRewardPerShare) / 
                PRECISION_FACTOR - staker.rewardDebt;
            if (pending > 0) {
                staker.pendingRewards += pending;
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        staker.amountStaked += _amount;
        totalStaked += _amount;

        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 
            PRECISION_FACTOR;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraws staked tokens and claims rewards
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot withdraw 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Withdraw amount exceeds balance");

        updatePool();

        uint256 pending = (staker.amountStaked * accRewardPerShare) / 
            PRECISION_FACTOR - staker.rewardDebt;

        if (pending > 0) {
            staker.pendingRewards += pending;
        }

        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 
            PRECISION_FACTOR;

        stakingToken.safeTransfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claims accumulated rewards
     */
    function claimRewards() external nonReentrant {
        updatePool();

        Staker storage staker = stakers[msg.sender];
        uint256 pending = (staker.amountStaked * accRewardPerShare) / 
            PRECISION_FACTOR - staker.rewardDebt;

        if (pending > 0 || staker.pendingRewards > 0) {
            staker.pendingRewards += pending;
            uint256 totalRewards = staker.pendingRewards;

            require(totalRewards > 0, "No rewards to claim");
            require(rewardToken.balanceOf(address(this)) >= totalRewards, 
                "Insufficient reward token balance");

            staker.pendingRewards = 0;
            staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 
                PRECISION_FACTOR;

            rewardToken.safeTransfer(msg.sender, totalRewards);
            emit RewardClaimed(msg.sender, totalRewards);
        }
    }

    /**
     * @dev Updates reward rate
     * @param _rewardPerBlock New reward rate per block
     */
    function updateRewardRate(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    /**
     * @dev Emergency withdraw without caring about rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 amount = staker.amountStaked;
        require(amount > 0, "Nothing to withdraw");

        totalStaked -= amount;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;
        staker.pendingRewards = 0;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Returns the pending rewards for a user
     * @param _user Address of the user
     * @return Pending rewards
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 reward = blocksSinceLastReward * rewardPerBlock;
            currentAccRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        }
        
        return staker.pendingRewards + 
            ((staker.amountStaked * currentAccRewardPerShare) / 
                PRECISION_FACTOR - staker.rewardDebt);
    }
}
```
