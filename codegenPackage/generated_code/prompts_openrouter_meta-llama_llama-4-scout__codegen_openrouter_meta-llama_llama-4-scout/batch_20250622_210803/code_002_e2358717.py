"""
Generated Code Metadata:
========================
Original URL: https://param-35r.pages.dev
Prompt: Generate a smart contract code for a gaming platform that utilizes Param Network's staking and rewards mechanism.
Generated: DETERMINISTIC_e2358717acbd7ab5
Batch ID: 20250622_210803
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

/**
 * @title Param Gaming Platform Staking Contract
 * @author [Your Name]
 * @notice This contract manages the staking and rewards mechanism for the Param Gaming Platform
 */
contract ParamGamingStaking is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfo;

    // Mapping of reward token balances
    mapping (address => uint256) public rewardBalances;

    // Param Network staking contract address
    address public paramStakingContract;

    // Reward token contract address
    address public rewardToken;

    // Staking token contract address
    address public stakingToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked amount
    uint256 public totalStakedAmount;

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
     * @dev Struct to store user staking information
     */
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakeBlock;
    }

    /**
     * @dev Constructor
     * @param _paramStakingContract Param Network staking contract address
     * @param _rewardToken Reward token contract address
     * @param _stakingToken Staking token contract address
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        address _paramStakingContract,
        address _rewardToken,
        address _stakingToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        paramStakingContract = _paramStakingContract;
        rewardToken = _rewardToken;
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period is over");

        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        uint256 newStakedAmount = userInfo.stakedAmount.add(_amount);

        // Transfer staking tokens from user to contract
        IERC20(stakingToken).transferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userInfo.stakedAmount = newStakedAmount;
        userInfo.lastStakeBlock = block.number;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfo[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];
        uint256 newStakedAmount = userInfo.stakedAmount.sub(_amount);

        // Transfer staking tokens from contract to user
        IERC20(stakingToken).transfer(msg.sender, _amount);

        // Update user staking information
        userInfo.stakedAmount = newStakedAmount;
        userInfo.rewardDebt = getRewardDebt(msg.sender);

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public {
        UserStakingInfo storage userInfo = userStakingInfo[msg.sender];

        // Calculate reward
        uint256 reward = getReward(msg.sender);

        // Update user reward debt
        userInfo.rewardDebt = getRewardDebt(msg.sender);

        // Transfer reward tokens to user
        IERC20(rewardToken).transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Get reward debt
     * @param _user User address
     * @return Reward debt
     */
    function getRewardDebt(address _user) internal view returns (uint256) {
        UserStakingInfo storage userInfo = userStakingInfo[_user];
        uint256 blocksStaked = block.number.sub(userInfo.lastStakeBlock);
        uint256 reward = blocksStaked.mul(rewardPerBlock).mul(userInfo.stakedAmount).div(totalStakedAmount);
        return userInfo.rewardDebt.add(reward);
    }

    /**
     * @dev Get reward
     * @param _user User address
     * @return Reward
     */
    function getReward(address _user) internal view returns (uint256) {
        UserStakingInfo storage userInfo = userStakingInfo[_user];
        uint256 blocksStaked = block.number.sub(userInfo.lastStakeBlock);
        uint256 reward = blocksStaked.mul(rewardPerBlock).mul(userInfo.stakedAmount).div(totalStakedAmount);
        return reward.sub(userInfo.rewardDebt);
    }

    /**
     * @dev Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @dev Update staking end block
     * @param _newStakingEndBlock New staking end block
     */
    function updateStakingEndBlock(uint256 _newStakingEndBlock) public onlyOwner {
        stakingEndBlock = _newStakingEndBlock;
    }

    /**
     * @dev Withdraw tokens from contract
     * @param _token Token contract address
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) public onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
