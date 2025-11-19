"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Create a simple staking contract for PUNDU tokens, allowing users to stake their tokens and earn rewards in the form of additional PUNDU tokens.
Generated: DETERMINISTIC_2d75208cd2881fba
Batch ID: 20250622_210856
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PUNDU Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake their PUNDU tokens and earn rewards in the form of additional PUNDU tokens.
 */
contract Pundustaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserInfo) public userInfo;

    // PUNDU token contract
    IERC20 public token;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking start block
    uint256 public startBlock;

    // Staking end block
    uint256 public endBlock;

    // Event emitted when user stakes tokens
    event Stake(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstake(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event DistributeRewards(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    /**
     * @notice Constructor
     * @param _token PUNDU token contract
     * @param _rewardPerBlock Reward per block
     * @param _startBlock Staking start block
     * @param _endBlock Staking end block
     */
    constructor(
        IERC20 _token,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) public {
        token = _token;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    /**
     * @notice Stake PUNDU tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(block.number >= startBlock && block.number <= endBlock, "Staking period has not started or has ended");

        UserInfo storage user = userInfo[msg.sender];
        uint256 stakedAmount = user.stakedAmount;

        // Transfer tokens to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staked amount
        user.stakedAmount = stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        // Update user's reward debt
        user.rewardDebt = user.rewardDebt.add(_amount);

        emit Stake(msg.sender, _amount);
    }

    /**
     * @notice Unstake PUNDU tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userInfo[msg.sender].stakedAmount >= _amount, "Insufficient staked tokens");

        UserInfo storage user = userInfo[msg.sender];
        uint256 stakedAmount = user.stakedAmount;

        // Calculate and distribute rewards
        uint256 rewards = getRewards(msg.sender);
        distributeRewards(msg.sender, rewards);

        // Update user's staked amount
        user.stakedAmount = stakedAmount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens to user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        // Update user's reward debt
        user.rewardDebt = user.rewardDebt.sub(_amount);

        emit Unstake(msg.sender, _amount);
    }

    /**
     * @notice Get user's rewards
     * @param _user User address
     * @return Rewards amount
     */
    function getRewards(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 rewards = 0;

        if (user.stakedAmount > 0) {
            uint256 blocksStaked = block.number.sub(startBlock);
            blocksStaked = blocksStaked > endBlock.sub(startBlock) ? endBlock.sub(startBlock) : blocksStaked;
            rewards = user.stakedAmount.mul(blocksStaked).mul(rewardPerBlock).div(1e18);
            rewards = rewards.sub(user.rewardDebt);
        }

        return rewards;
    }

    /**
     * @notice Distribute rewards to user
     * @param _user User address
     * @param _amount Rewards amount
     */
    function distributeRewards(address _user, uint256 _amount) internal {
        if (_amount > 0) {
            UserInfo storage user = userInfo[_user];
            require(token.transfer(_user, _amount), "Token transfer failed");
            user.rewardDebt = user.rewardDebt.add(_amount);
            emit DistributeRewards(_user, _amount);
        }
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public {
        rewardPerBlock = _newRewardPerBlock;
    }
}
```
