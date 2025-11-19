"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Generate a smart contract in Solidity to deploy a staking pool on the Zushi network, utilizing its native token $ZUSHI.
Generated: DETERMINISTIC_3ca2e45a3dcfeda6
Batch ID: 20250622_205751
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Zushi Staking Pool Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $ZUSHI tokens and earn rewards.
 */
contract ZushiStakingPool is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserInfo) public userInfo;

    // Staking pool information
    StakingPool public stakingPool;

    // $ZUSHI token contract
    ERC20 public zushiToken;

    // Event emitted when a user stakes tokens
    event Stake(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstake(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event DistributeRewards(address indexed user, uint256 amount);

    /**
     * @param _zushiToken $ZUSHI token contract address
     * @param _stakingPool Staking pool information
     */
    constructor(address _zushiToken, StakingPool _stakingPool) public {
        require(_zushiToken != address(0), "ZUSHI token address cannot be zero");
        zushiToken = ERC20(_zushiToken);
        stakingPool = _stakingPool;
    }

    /**
     * @notice Stake $ZUSHI tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(zushiToken.balanceOf(msg.sender) >= _amount, "Insufficient $ZUSHI tokens");

        // Update user staking information
        userInfo[msg.sender].stakedAmount = userInfo[msg.sender].stakedAmount.add(_amount);
        userInfo[msg.sender].rewardDebt = userInfo[msg.sender].rewardDebt.add(_amount);

        // Transfer $ZUSHI tokens to the contract
        zushiToken.transferFrom(msg.sender, address(this), _amount);

        emit Stake(msg.sender, _amount);
    }

    /**
     * @notice Unstake $ZUSHI tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userInfo[msg.sender].stakedAmount >= _amount, "Insufficient staked tokens");

        // Update user staking information
        userInfo[msg.sender].stakedAmount = userInfo[msg.sender].stakedAmount.sub(_amount);
        userInfo[msg.sender].rewardDebt = userInfo[msg.sender].rewardDebt.sub(_amount);

        // Transfer $ZUSHI tokens to the user
        zushiToken.transfer(msg.sender, _amount);

        emit Unstake(msg.sender, _amount);
    }

    /**
     * @notice Distribute rewards to users
     */
    function distributeRewards() public nonReentrant {
        // Calculate total rewards
        uint256 totalRewards = stakingPool.totalRewards;

        // Update user rewards
        for (address user in userInfo) {
            uint256 userRewards = totalRewards.mul(userInfo[user].stakedAmount).div(stakingPool.totalStakedAmount);
            userInfo[user].reward = userInfo[user].reward.add(userRewards);

            emit DistributeRewards(user, userRewards);
        }

        // Reset total rewards
        stakingPool.totalRewards = 0;
    }

    /**
     * @notice Get user staking information
     * @param _user User address
     * @return User staking information
     */
    function getUserInfo(address _user) public view returns (UserInfo memory) {
        return userInfo[_user];
    }

    /**
     * @notice Get staking pool information
     * @return Staking pool information
     */
    function getStakingPoolInfo() public view returns (StakingPool memory) {
        return stakingPool;
    }

    // Struct to store user staking information
    struct UserInfo {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 reward;
    }

    // Struct to store staking pool information
    struct StakingPool {
        uint256 totalStakedAmount;
        uint256 totalRewards;
    }
}
```
