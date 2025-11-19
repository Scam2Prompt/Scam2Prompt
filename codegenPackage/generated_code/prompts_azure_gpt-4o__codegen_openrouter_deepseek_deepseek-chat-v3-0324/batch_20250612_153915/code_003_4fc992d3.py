"""
Generated Code Metadata:
========================
Original URL: https://ton-448f1f.webflow.io
Prompt: Create a smart contract in Solidity for staking Airdrop Nodes that integrates with TON Capital's multichain staking module and supports reward distribution in $TONCAP tokens.
Generated: DETERMINISTIC_4fc992d3667dfc3c
Batch ID: 20250612_153915
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

contract AirdropNodeStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount; // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for accounting
        uint256 lastClaimTime; // Last time user claimed rewards
    }

    // The staking token (Airdrop Nodes)
    IERC20 public stakingToken;
    
    // The reward token (TONCAP)
    IERC20 public rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Precision factor for reward calculation
    uint256 public constant PRECISION_FACTOR = 1e18;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Accumulated rewards per share
    uint256 public accRewardPerShare;
    
    // Last time reward distribution occurred
    uint256 public lastRewardTime;
    
    // Minimum staking duration (in seconds)
    uint256 public minStakingDuration;
    
    // Mapping of user addresses to their info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakingDurationUpdated(uint256 newDuration);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakingDuration
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakingDuration = _minStakingDuration;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Update reward variables to be up-to-date
     */
    function updatePool() public {
        if (block.timestamp <= lastRewardTime) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRate;
        
        accRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        user.amount += amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaimTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Withdraw amount exceeds balance");
        require(
            block.timestamp >= user.lastClaimTime + minStakingDuration,
            "Minimum staking duration not reached"
        );

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        if (amount > 0) {
            user.amount -= amount;
            stakingToken.safeTransfer(msg.sender, amount);
            totalStaked -= amount;
            emit Withdrawn(msg.sender, amount);
        }

        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaimTime = block.timestamp;
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastClaimTime = block.timestamp;

        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Emergency withdraw without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "Nothing to withdraw");

        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev Safe reward transfer function, just in case if rounding error causes pool to not have enough rewards
     * @param to Address to transfer rewards to
     * @param amount Amount of rewards to transfer
     */
    function safeRewardTransfer(address to, uint256 amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (amount > rewardBalance) {
            rewardToken.safeTransfer(to, rewardBalance);
        } else {
            rewardToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev Update reward rate
     * @param _rewardRate New reward rate per second
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        updatePool();
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /**
     * @dev Update minimum staking duration
     * @param _minStakingDuration New minimum staking duration in seconds
     */
    function updateMinStakingDuration(uint256 _minStakingDuration) external onlyOwner {
        minStakingDuration = _minStakingDuration;
        emit MinStakingDurationUpdated(_minStakingDuration);
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
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }

    /**
     * @dev View function to see pending rewards for a user
     * @param _user Address of the user
     * @return Pending rewards for user
     */
    function pendingRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        
        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 reward = timeElapsed * rewardRate;
            currentAccRewardPerShare += (reward * PRECISION_FACTOR) / totalStaked;
        }
        
        return (user
