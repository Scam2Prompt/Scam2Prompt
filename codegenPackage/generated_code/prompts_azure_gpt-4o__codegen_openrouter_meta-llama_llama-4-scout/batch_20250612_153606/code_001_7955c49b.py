"""
Generated Code Metadata:
========================
Original URL: https://moonbootsdao.web.app
Prompt: Create a smart contract in Solidity that facilitates staking $MBDAO tokens and calculates ecosystem rewards based on Moonboots DAO's enhanced staking/voting rights.
Generated: DETERMINISTIC_7955c49b8d868a0e
Batch ID: 20250612_153606
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Moonboots DAO Staking Contract
 * @author [Your Name]
 * @notice This contract facilitates staking $MBDAO tokens and calculates ecosystem rewards based on Moonboots DAO's enhanced staking/voting rights.
 */
contract MoonbootsDAOSTaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping of user staking start time
    mapping(address => uint256) public stakingStartTime;

    // Total staking amount
    uint256 public totalStakingAmount;

    // $MBDAO token contract
    IERC20 public mbdaoToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last block number that reward was distributed
    uint256 public lastRewardBlock;

    // Reward accumulator
    uint256 public accRewardPerShare;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _mbdaoToken $MBDAO token contract address
     * @param _rewardPerBlock Reward per block
     */
    constructor(IERC20 _mbdaoToken, uint256 _rewardPerBlock) {
        mbdaoToken = _mbdaoToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake $MBDAO tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid staking amount");
        require(mbdaoToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        mbdaoToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        if (stakingBalances[msg.sender] == 0) {
            stakingStartTime[msg.sender] = block.timestamp;
        }
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Update total staking amount
        totalStakingAmount = totalStakingAmount.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $MBDAO tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstaking amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Update total staking amount
        totalStakingAmount = totalStakingAmount.sub(_amount);

        // Transfer tokens from contract to user
        mbdaoToken.safeTransfer(msg.sender, _amount);

        // Emit event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Get user's reward
     * @return Reward amount
     */
    function getReward() external {
        uint256 _reward = getUserReward(msg.sender);
        require(_reward > 0, "No reward available");

        // Update user's reward debt
        rewardDebt[msg.sender] = getCurrentRewardPerShare();

        // Transfer reward to user
        mbdaoToken.safeTransfer(msg.sender, _reward);

        // Emit event
        emit RewardDistributed(msg.sender, _reward);
    }

    /**
     * @notice Get user's reward
     * @param _user User address
     * @return Reward amount
     */
    function getUserReward(address _user) internal view returns (uint256) {
        uint256 _currentRewardPerShare = getCurrentRewardPerShare();
        uint256 _userRewardDebt = rewardDebt[_user];

        // Calculate user's reward
        uint256 _reward = stakingBalances[_user].mul(_currentRewardPerShare.sub(_userRewardDebt)).div(1e18);

        return _reward;
    }

    /**
     * @notice Get current reward per share
     * @return Reward per share
     */
    function getCurrentRewardPerShare() internal view returns (uint256) {
        uint256 _totalReward = rewardPerBlock.mul(block.number.sub(lastRewardBlock));
        uint256 _currentRewardPerShare = accRewardPerShare.add(_totalReward.mul(1e18).div(totalStakingAmount));

        return _currentRewardPerShare;
    }

    /**
     * @notice Update reward accumulator
     */
    function updateRewardAccumulator() internal {
        uint256 _totalReward = rewardPerBlock.mul(block.number.sub(lastRewardBlock));
        accRewardPerShare = accRewardPerShare.add(_totalReward.mul(1e18).div(totalStakingAmount));
        lastRewardBlock = block.number;
    }
}
```
