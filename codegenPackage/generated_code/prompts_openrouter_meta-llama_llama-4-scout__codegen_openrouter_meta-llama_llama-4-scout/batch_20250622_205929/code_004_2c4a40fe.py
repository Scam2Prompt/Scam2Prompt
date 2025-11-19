"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Write a smart contract in Solidity that enables staking, unstaking, and reward distribution for a token, with features like emergency withdrawal and reward tracking.
Generated: DETERMINISTIC_2c4a40fe13fec1da
Batch ID: 20250622_205929
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
 * @title Staking Contract
 * @author [Your Name]
 * @notice This contract enables staking, unstaking, and reward distribution for a token.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // Total staked tokens
    uint256 public totalStaked;

    // Total reward tokens
    uint256 public totalRewards;

    // Reward per block
    uint256 public rewardPerBlock;

    // Staking token address
    IERC20 public stakingToken;

    // Reward token address
    IERC20 public rewardToken;

    // Flag for emergency withdrawal
    bool public emergencyWithdrawal;

    /**
     * @notice Constructor
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        rewardBalances[msg.sender] = rewardBalances[msg.sender].add(rewards);
        totalRewards = totalRewards.add(rewards);

        require(rewardToken.transfer(msg.sender, rewards), "Token transfer failed");
    }

    /**
     * @notice Emergency withdrawal
     */
    function emergencyWithdraw() external {
        require(emergencyWithdrawal, "Emergency withdrawal not enabled");
        require(stakingBalances[msg.sender] > 0, "No staked tokens");

        uint256 stakedAmount = stakingBalances[msg.sender];
        stakingBalances[msg.sender] = 0;
        totalStaked = totalStaked.sub(stakedAmount);

        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");
    }

    /**
     * @notice Calculate rewards for a user
     * @param _user User address
     * @return Rewards for the user
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        // Implement your reward calculation logic here
        // For simplicity, this example uses a basic calculation
        return stakingBalances[_user].mul(rewardPerBlock).div(1e18);
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Enable/disable emergency withdrawal
     * @param _enabled Flag to enable/disable emergency withdrawal
     */
    function toggleEmergencyWithdrawal(bool _enabled) external onlyOwner {
        emergencyWithdrawal = _enabled;
    }

    /**
     * @notice Withdraw tokens from the contract
     * @param _token Token address
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_token);
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }
}
```
