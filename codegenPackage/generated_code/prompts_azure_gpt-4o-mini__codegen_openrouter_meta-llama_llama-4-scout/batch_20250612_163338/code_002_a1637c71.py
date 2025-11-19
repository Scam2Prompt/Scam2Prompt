"""
Generated Code Metadata:
========================
Original URL: https://daddysunversity.com
Prompt: Create a Solidity smart contract that allows users to stake $DADDY tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_a1637c71fada9b6f
Batch ID: 20250612_163338
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Daddy Staking Contract
 * @author [Your Name]
 * @notice Allows users to stake $DADDY tokens and earn rewards based on their holdings.
 */
contract DaddyStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // $DADDY token contract
    IERC20 public daddyToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Reward accumulator
    uint256 public accRewardPerShare;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _daddyToken $DADDY token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _daddyToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) public {
        daddyToken = IERC20(_daddyToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Updates the reward accumulator and distributes rewards to users
     */
    function updateRewardAccumulator() public {
        uint256 currentBlock = block.number;
        if (currentBlock <= lastRewardBlock) {
            return;
        }

        uint256 stakingBalance = totalStakingBalance;
        if (stakingBalance == 0) {
            lastRewardBlock = currentBlock;
            return;
        }

        uint256 reward = rewardPerBlock.mul(currentBlock.sub(lastRewardBlock));
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(stakingBalance));
        lastRewardBlock = currentBlock;
    }

    /**
     * @dev Calculates the user's reward
     * @param _user User address
     * @return User's reward
     */
    function getUserReward(address _user) public view returns (uint256) {
        uint256 userStakingBalance = stakingBalances[_user];
        if (userStakingBalance == 0) {
            return 0;
        }

        uint256 userRewardDebt = rewardDebt[_user];
        uint256 pendingReward = userStakingBalance.mul(accRewardPerShare).div(1e18).sub(userRewardDebt);
        return pendingReward;
    }

    /**
     * @dev Stakes $DADDY tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        daddyToken.safeTransferFrom(msg.sender, address(this), _amount);
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);
        rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes $DADDY tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        updateRewardAccumulator();
        uint256 pendingReward = getUserReward(msg.sender);
        if (pendingReward > 0) {
            rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);
            rewardToken.safeTransfer(msg.sender, pendingReward);
            emit RewardsDistributed(msg.sender, pendingReward);
        }

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);
        daddyToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claims rewards
     */
    function claimRewards() public nonReentrant {
        updateRewardAccumulator();
        uint256 pendingReward = getUserReward(msg.sender);
        require(pendingReward > 0, "No pending rewards");

        rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);
        rewardToken.safeTransfer(msg.sender, pendingReward);
        emit RewardsDistributed(msg.sender, pendingReward);
    }
}
```
