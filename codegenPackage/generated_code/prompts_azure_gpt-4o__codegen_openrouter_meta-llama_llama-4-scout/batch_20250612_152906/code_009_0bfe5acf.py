"""
Generated Code Metadata:
========================
Original URL: https://kayentest2.pages.dev
Prompt: Generate a Solidity contract for a staking mechanism that aligns with KAYEN Protocol's sustainable dual-token model and deflationary principles.
Generated: DETERMINISTIC_0bfe5acfd8f30cc2
Batch ID: 20250612_152906
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title KAYEN Staking Contract
 * @author [Your Name]
 * @notice This contract implements a staking mechanism for KAYEN Protocol's sustainable dual-token model and deflationary principles.
 */
contract KayenStaking is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping of user staking start time
    mapping(address => uint256) public stakingStartTime;

    // Total staking amount
    uint256 public totalStakingAmount;

    // KAYEN token contract
    IERC20 public kayenToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Reward distribution start block
    uint256 public rewardDistributionStartBlock;

    // Reward distribution end block
    uint256 public rewardDistributionEndBlock;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _kayenToken KAYEN token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     * @param _rewardDistributionStartBlock Reward distribution start block
     * @param _rewardDistributionEndBlock Reward distribution end block
     */
    constructor(
        address _kayenToken,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock,
        uint256 _rewardDistributionStartBlock,
        uint256 _rewardDistributionEndBlock
    ) public {
        kayenToken = IERC20(_kayenToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        rewardDistributionStartBlock = _rewardDistributionStartBlock;
        rewardDistributionEndBlock = _rewardDistributionEndBlock;
        lastRewardBlock = _stakingStartBlock;
    }

    /**
     * @notice Stake KAYEN tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "staker address cannot be 0");
        require(_amount > 0, "stake amount must be greater than 0");
        require(stakingStartBlock <= block.number && block.number <= stakingEndBlock, "staking period has ended");

        // Transfer KAYEN tokens to contract
        require(kayenToken.transferFrom(msg.sender, address(this), _amount), "KAYEN token transfer failed");

        // Update user's staking balance
        if (stakingBalances[msg.sender] == 0) {
            stakingStartTime[msg.sender] = block.timestamp;
        }
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingAmount = totalStakingAmount.add(_amount);

        // Update user's reward debt
        updateRewardDebt(msg.sender);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake KAYEN tokens
     */
    function unstake() external nonReentrant {
        require(msg.sender != address(0), "staker address cannot be 0");
        require(stakingBalances[msg.sender] > 0, "user has no staking balance");

        // Calculate user's reward
        uint256 reward = getReward(msg.sender);

        // Update user's staking balance and reward debt
        uint256 stakingBalance = stakingBalances[msg.sender];
        stakingBalances[msg.sender] = 0;
        rewardDebt[msg.sender] = 0;
        totalStakingAmount = totalStakingAmount.sub(stakingBalance);

        // Transfer KAYEN tokens and reward tokens to user
        require(kayenToken.transfer(msg.sender, stakingBalance), "KAYEN token transfer failed");
        if (reward > 0) {
            require(rewardToken.transfer(msg.sender, reward), "reward token transfer failed");
            emit RewardDistributed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, stakingBalance);
    }

    /**
     * @notice Update reward debt for user
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        if (stakingBalances[_user] > 0) {
            uint256 pendingReward = getPendingReward(_user);
            rewardDebt[_user] = rewardDebt[_user].add(pendingReward);
        }
    }

    /**
     * @notice Get pending reward for user
     * @param _user User address
     * @return Pending reward
     */
    function getPendingReward(address _user) public view returns (uint256) {
        uint256 currentBlock = block.number;
        if (currentBlock <= lastRewardBlock) {
            return 0;
        }

        uint256 stakingBalance = stakingBalances[_user];
        if (stakingBalance == 0) {
            return 0;
        }

        uint256 reward = stakingBalance.mul(currentBlock.sub(lastRewardBlock)).mul(rewardPerBlock).div(1e18);
        return reward;
    }

    /**
     * @notice Get reward for user
     * @param _user User address
     * @return Reward
     */
    function getReward(address _user) public view returns (uint256) {
        uint256 pendingReward = getPendingReward(_user);
        uint256 rewardDebtValue = rewardDebt[_user];
        if (pendingReward > rewardDebtValue) {
            return pendingReward.sub(rewardDebtValue);
        } else {
            return 0;
        }
    }

    /**
     * @notice Update last reward block and distribute reward
     */
    function updateLastRewardBlock() external onlyOwner {
        require(block.number > lastRewardBlock, "last reward block is up-to-date");

        uint256 currentBlock = block.number;
        if (currentBlock > rewardDistributionEndBlock) {
            currentBlock = rewardDistributionEndBlock;
        }

        uint256 reward = totalStakingAmount.mul(currentBlock.sub(lastRewardBlock)).mul(rewardPerBlock).div(1e18);
        if (reward > 0) {
            require(rewardToken.transfer(msg.sender, reward), "reward token transfer failed");
        }

        lastRewardBlock = currentBlock;
    }
}
```
