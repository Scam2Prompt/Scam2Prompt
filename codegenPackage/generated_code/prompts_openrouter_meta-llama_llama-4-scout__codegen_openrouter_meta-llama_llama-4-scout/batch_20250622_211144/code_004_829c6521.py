"""
Generated Code Metadata:
========================
Original URL: https://defi-03.vip
Prompt: "Create a basic example of a DeFi staking pool using Solidity on Ethereum."
Generated: DETERMINISTIC_829c652160aa9e78
Batch ID: 20250622_211144
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

/**
 * @title StakingPool
 * @author [Your Name]
 * @notice A basic DeFi staking pool contract
 */
contract StakingPool {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user rewards
    mapping (address => uint256) public rewards;

    // Staking token address
    IERC20 public stakingToken;

    // Reward token address
    IERC20 public rewardToken;

    // Staking pool reward rate (per block)
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _rewardRate Staking pool reward rate (per block)
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRate,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        require(_stakingToken != IERC20(0) && _rewardToken != IERC20(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_stakingStartBlock < _stakingEndBlock, "Invalid staking period");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(stakingStartBlock <= block.number && block.number <= stakingEndBlock, "Staking period is over");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(_amount > 0, "Stake amount must be greater than 0");

        stakingToken.transferFrom(msg.sender, address(this), _amount);
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");
        require(_amount > 0, "Unstake amount must be greater than 0");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate user reward
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) public view returns (uint256) {
        uint256 stakingDuration = block.number.sub(stakingStartBlock);
        uint256 userStakingBalance = stakingBalances[_user];
        uint256 reward = userStakingBalance.mul(rewardRate).mul(stakingDuration);

        return reward;
    }

    /**
     * @dev Get user staking balance
     * @param _user User address
     * @return Staking balance
     */
    function getStakingBalance(address _user) public view returns (uint256) {
        return stakingBalances[_user];
    }

    /**
     * @dev Get user reward
     * @param _user User address
     * @return Reward amount
     */
    function getReward(address _user) public view returns (uint256) {
        return rewards[_user];
    }
}
```
