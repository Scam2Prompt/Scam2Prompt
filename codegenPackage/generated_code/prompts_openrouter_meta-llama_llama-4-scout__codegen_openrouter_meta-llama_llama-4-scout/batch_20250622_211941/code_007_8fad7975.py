"""
Generated Code Metadata:
========================
Original URL: https://testuser.usdtddex.com
Prompt: "How can I implement a staking feature similar to USDTD using Solidity, considering the 100% decentralized, transparent, and secure requirements?"
Generated: DETERMINISTIC_8fad7975c9a913a3
Batch ID: 20250622_211941
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
 * @title Staking Contract
 * @author [Your Name]
 * @notice A decentralized, transparent, and secure staking feature similar to USDTD
 */
contract StakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // Mapping of reward distribution
    mapping (address => uint256) public rewards;

    // Staking token address
    address public stakingToken;

    // Reward token address
    address public rewardToken;

    // Staking start timestamp
    uint256 public stakingStart;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _stakingStart Timestamp when staking starts
     * @param _stakingEnd Timestamp when staking ends
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingStart,
        uint256 _stakingEnd,
        uint256 _rewardPerBlock
    ) public {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        stakingStart = _stakingStart;
        stakingEnd = _stakingEnd;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(msg.sender != address(0), "Invalid address");
        require(_amount > 0, "Invalid amount");
        require(block.timestamp >= stakingStart && block.timestamp <= stakingEnd, "Staking period has not started or has ended");
        require(ERC20(stakingToken).balanceOf(msg.sender) >= _amount, "Insufficient balance");

        stakers[msg.sender].amount = stakers[msg.sender].amount.add(_amount);
        stakers[msg.sender].lastRewardBlock = block.number;
        totalStaked = totalStaked.add(_amount);

        // Transfer staking tokens to contract
        ERC20(stakingToken).transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() external nonReentrant {
        require(msg.sender != address(0), "Invalid address");
        require(stakers[msg.sender].amount > 0, "No staked amount");

        uint256 stakedAmount = stakers[msg.sender].amount;
        stakers[msg.sender].amount = 0;
        totalStaked = totalStaked.sub(stakedAmount);

        // Transfer staking tokens back to user
        ERC20(stakingToken).transfer(msg.sender, stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Get reward
     */
    function getReward() external nonReentrant {
        require(msg.sender != address(0), "Invalid address");
        require(stakers[msg.sender].amount > 0, "No staked amount");

        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] = rewards[msg.sender].add(reward);

        // Transfer reward tokens to user
        ERC20(rewardToken).transfer(msg.sender, reward);

        stakers[msg.sender].lastRewardBlock = block.number;

        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 stakedAmount = stakers[_user].amount;
        uint256 blocksElapsed = block.number.sub(stakers[_user].lastRewardBlock);
        return stakedAmount.mul(rewardPerBlock).mul(blocksElapsed);
    }

    // Struct to hold staker information
    struct Staker {
        uint256 amount;
        uint256 lastRewardBlock;
    }
}
```
