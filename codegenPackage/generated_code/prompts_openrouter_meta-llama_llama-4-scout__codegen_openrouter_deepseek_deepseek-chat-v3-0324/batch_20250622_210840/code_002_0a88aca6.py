"""
Generated Code Metadata:
========================
Original URL: https://agora-ai.market
Prompt: Develop a smart contract in Solidity for staking and liquidity provision on the Agora AI platform, considering the tokenomics and total supply of 1,000,000,000 AGAI.
Generated: DETERMINISTIC_0a88aca6a75b0419
Batch ID: 20250622_210840
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

contract AgoraAIStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct StakeInfo {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // AGAI token contract
    IERC20 public agaiToken;

    // Total AGAI staked
    uint256 public totalStaked;

    // Reward rate per block (in wei)
    uint256 public rewardPerBlock;

    // Precision factor for reward calculation
    uint256 private constant PRECISION_FACTOR = 1e12;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Last reward calculation block
    uint256 public lastRewardBlock;

    // Mapping of user to their stake info
    mapping(address => StakeInfo) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor
     * @param _agaiToken Address of AGAI token
     * @param _rewardPerBlock Reward rate per block
     */
    constructor(address _agaiToken, uint256 _rewardPerBlock) {
        require(_agaiToken != address(0), "Invalid token address");
        agaiToken = IERC20(_agaiToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Update reward variables
     */
    function updatePool() internal {
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
     * @dev Stake AGAI tokens
     * @param amount Amount of AGAI to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        updatePool();

        StakeInfo storage user = userStakes[msg.sender];

        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
            if (pending > 0) {
                safeAgaiTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        agaiToken.safeTransferFrom(msg.sender, address(this), amount);
        user.amount += amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        user.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake AGAI tokens
     * @param amount Amount of AGAI to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        StakeInfo storage user = userStakes[msg.sender];
        require(user.amount >= amount, "Insufficient staked balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        if (pending > 0) {
            safeAgaiTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        user.amount -= amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        totalStaked -= amount;

        agaiToken.safeTransfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        StakeInfo storage user = userStakes[msg.sender];
        require(user.amount > 0, "No staked balance");

        updatePool();

        uint256 pending = (user.amount * accRewardPerShare) / PRECISION_FACTOR - user.rewardDebt;
        require(pending > 0, "No rewards to claim");

        user.rewardDebt = (user.amount * accRewardPerShare) / PRECISION_FACTOR;
        safeAgaiTransfer(msg.sender, pending);

        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safe AGAI transfer function
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function safeAgaiTransfer(address to, uint256 amount) internal {
        uint256 agaiBalance = agaiToken.balanceOf(address(this));
        if (amount > agaiBalance) {
            agaiToken.safeTransfer(to, agaiBalance);
        } else {
            agaiToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev Update reward rate
     * @param _rewardPerBlock New reward rate per block
     */
    function updateRewardRate(uint256 _rewardPerBlock) external onlyOwner {
        updatePool();
        rewardPerBlock = _rewardPerBlock;
        emit RewardRateUpdated(_rewardPerBlock);
    }

    /**
     * @dev Get pending rewards for a user
     * @param user User address
     * @return Pending rewards
     */
    function pendingRewards(address user) external view returns (uint256) {
        StakeInfo storage stakeInfo = userStakes[user];
        uint256 tempAccRewardPerShare = accRewardPerShare;
        uint256 tempTotalStaked = totalStaked;

        if (block.number > lastRewardBlock && tempTotalStaked != 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 reward = blocksSinceLastReward * rewardPerBlock;
            tempAccRewardPerShare += (reward * PRECISION_FACTOR) / tempTotalStaked;
        }

        return (stakeInfo.amount * tempAccRewardPerShare) / PRECISION_FACTOR - stakeInfo.rewardDebt;
    }

    /**
     * @dev Emergency withdraw all staked tokens without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        StakeInfo storage user = userStakes[msg.sender];
        uint256 amount = user.amount;
        require(amount > 0, "No staked balance");

        user.amount = 0;
        user.rewardDebt = 0;
        totalStaked -= amount;

        agaiToken.safeTransfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }
}
```
