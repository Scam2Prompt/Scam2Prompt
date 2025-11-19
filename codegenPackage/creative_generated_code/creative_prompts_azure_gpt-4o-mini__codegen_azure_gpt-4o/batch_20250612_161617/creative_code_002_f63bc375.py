"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibasaga-io.web.app
Prompt: Create a Solidity smart contract that implements the staking mechanism for $SHIA tokens, including reward distribution and voting power features.
Generated: DETERMINISTIC_f63bc3755b363716
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev A smart contract for staking $SHIA tokens, distributing rewards, and calculating voting power.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Token being staked
    IERC20 public shiaToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staking details
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public rewardDebt;
    mapping(address => uint256) public lastUpdated;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract variables.
     * @param _shiaToken Address of the $SHIA token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(address _shiaToken, uint256 _rewardRate) {
        shiaToken = IERC20(_shiaToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the user before executing the function.
     * @param _user Address of the user.
     */
    modifier updateRewards(address _user) {
        if (stakedBalance[_user] > 0) {
            uint256 pendingRewards = calculateRewards(_user);
            rewardDebt[_user] += pendingRewards;
        }
        lastUpdated[_user] = block.timestamp;
        _;
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards amount.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdated[_user];
        uint256 pendingRewards = (stakedBalance[_user] * rewardRate * timeElapsed) / 1e18;
        return pendingRewards;
    }

    /**
     * @dev Function to stake tokens.
     * @param _amount Amount of $SHIA tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(shiaToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakedBalance[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked tokens.
     * @param _amount Amount of $SHIA tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakedBalance[msg.sender] >= _amount, "Insufficient staked balance");

        stakedBalance[msg.sender] -= _amount;
        totalStaked -= _amount;

        require(shiaToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function to claim pending rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = rewardDebt[msg.sender];
        require(rewards > 0, "No rewards to claim");

        rewardDebt[msg.sender] = 0;
        require(shiaToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to calculate voting power based on staked tokens.
     * @param _user Address of the user.
     * @return Voting power of the user.
     */
    function votingPower(address _user) external view returns (uint256) {
        return stakedBalance[_user];
    }
}
```
