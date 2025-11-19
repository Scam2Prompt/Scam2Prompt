"""
Generated Code Metadata:
========================
Original URL: https://growtoken.xyz
Prompt: "Generate a smart contract code for staking and LST utilities on a blockchain platform similar to GROW DAO's offerings."
Generated: DETERMINISTIC_36480e74bc148603
Batch ID: 20250622_212444
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LST Staking Contract
 * @notice Allows users to stake LST tokens and earn rewards
 * @dev Implements staking functionality with reward distribution
 */
contract LSTStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking details
    struct UserStake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // Staking token (LST)
    IERC20 public immutable stakingToken;
    
    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;

    // Reward rate per second
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Last update time for rewards
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // Precision factor for calculations
    uint256 public constant PRECISION = 1e18;

    // Mapping of user addresses to their staking info
    mapping(address => UserStake) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token (LST)
     * @param _rewardToken Address of the reward token
     * @param _rewardRate Initial reward rate per second
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    /**
     * @notice Update reward variables
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userStakes[account].rewardDebt = earned(account);
        }
        _;
    }

    /**
     * @notice Calculate reward per token
     * @return Reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((block.timestamp - lastUpdateTime) * rewardRate * PRECISION) / totalStaked;
    }

    /**
     * @notice Calculate earned rewards for an account
     * @param account User address
     * @return Total earned rewards
     */
    function earned(address account) public view returns (uint256) {
        UserStake memory user = userStakes[account];
        return (user.amount * (rewardPerToken() - user.rewardDebt)) / PRECISION;
    }

    /**
     * @notice Stake LST tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        UserStake storage user = userStakes[msg.sender];
        user.amount += amount;
        user.lastStakeTime = block.timestamp;
        user.rewardDebt = (user.amount * rewardPerTokenStored) / PRECISION;
        
        totalStaked += amount;
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked tokens
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        UserStake storage user = userStakes[msg.sender];
        require(user.amount >= amount, "Insufficient balance");
        
        user.amount -= amount;
        user.rewardDebt = (user.amount * rewardPerTokenStored) / PRECISION;
        
        totalStaked -= amount;
        stakingToken.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            UserStake storage user = userStakes[msg.sender];
            user.rewardDebt = (user.amount * rewardPerTokenStored) / PRECISION;
            
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @notice Withdraw all staked tokens and claim rewards
     */
    function exit() external {
        withdraw(userStakes[msg.sender].amount);
        getReward();
    }

    /**
     * @notice Emergency withdraw without rewards
     */
    function emergencyWithdraw() external nonReentrant {
        UserStake storage user = userStakes[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");
        
        totalStaked -= amount;
        user.amount = 0;
        user.rewardDebt = 0;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @notice Update reward rate
     * @param _rewardRate New reward rate per second
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @notice Recover ERC20 tokens sent by mistake
     * @param tokenAddress Token address
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }

    /**
     * @notice Get user staking info
     * @param user User address
     * @return stakedAmount Amount staked by user
     * @return pendingReward Pending rewards for user
     * @return lastStakeTime Last stake time
     */
    function getUserInfo(address user) external view returns (
        uint256 stakedAmount,
        uint256 pendingReward,
        uint256 lastStakeTime
    ) {
        UserStake memory stakeInfo = userStakes[user];
        return (
            stakeInfo.amount,
            earned(user),
            stakeInfo.lastStakeTime
        );
    }
}
```
