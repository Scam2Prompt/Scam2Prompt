"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Create a smart contract in Solidity that incorporates staking and yield farming mechanisms, aligning with Yeti Ouro's tokenomics and roadmap goals.
Generated: DETERMINISTIC_5c8aa914ae22c75a
Batch ID: 20250612_154752
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
 * @title YetiOuroStakingContract
 * @author [Your Name]
 * @notice This contract provides staking and yield farming mechanisms for Yeti Ouro's tokenomics.
 */
contract YetiOuroStakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping of user staking start time
    mapping(address => uint256) public stakingStartTime;

    // Total staking amount
    uint256 public totalStakingAmount;

    // Yeti Ouro token contract
    IERC20 public yetiOuroToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Total reward
    uint256 public totalReward;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _yetiOuroToken Yeti Ouro token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        address _yetiOuroToken,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        yetiOuroToken = IERC20(_yetiOuroToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        lastRewardBlock = _stakingStartBlock;
    }

    /**
     * @notice Stake Yeti Ouro tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(
            block.number >= stakingStartBlock && block.number <= stakingEndBlock,
            "Staking period has not started or has ended"
        );

        // Transfer Yeti Ouro tokens to contract
        yetiOuroToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Update total staking amount
        totalStakingAmount = totalStakingAmount.add(_amount);

        // Update user's staking start time
        if (stakingStartTime[msg.sender] == 0) {
            stakingStartTime[msg.sender] = block.number;
        }

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake Yeti Ouro tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Update total staking amount
        totalStakingAmount = totalStakingAmount.sub(_amount);

        // Transfer Yeti Ouro tokens to user
        yetiOuroToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward
     */
    function updateReward() public {
        uint256 currentBlock = block.number;
        if (currentBlock > lastRewardBlock && totalStakingAmount > 0) {
            uint256 reward = rewardPerBlock.mul(currentBlock.sub(lastRewardBlock));
            totalReward = totalReward.add(reward);
            lastRewardBlock = currentBlock;
        }
    }

    /**
     * @notice Distribute reward to user
     */
    function distributeReward() external nonReentrant {
        updateReward();

        // Calculate user's reward
        uint256 userReward = calculateUserReward(msg.sender);

        // Update user's reward debt
        rewardDebt[msg.sender] = rewardDebt[msg.sender].add(userReward);

        // Transfer reward to user
        rewardToken.transfer(msg.sender, userReward);

        emit RewardDistributed(msg.sender, userReward);
    }

    /**
     * @notice Calculate user's reward
     * @param _user User address
     * @return User's reward
     */
    function calculateUserReward(address _user) internal view returns (uint256) {
        uint256 stakingBalance = stakingBalances[_user];
        uint256 reward = stakingBalance.mul(totalReward).div(totalStakingAmount);
        return reward;
    }

    /**
     * @notice Get user's staking information
     * @param _user User address
     * @return User's staking balance, reward debt, and staking start time
     */
    function getUserStakingInfo(address _user)
        external
        view
        returns (
            uint256,
            uint256,
            uint256
        )
    {
        return (
            stakingBalances[_user],
            rewardDebt[_user],
            stakingStartTime[_user]
        );
    }
}
```
