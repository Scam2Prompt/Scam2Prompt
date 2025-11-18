"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dinamikaplus.ru
Prompt: Write a smart contract in Solidity to enable staking of BELT tokens and distribute rewards based on the mechanisms described in Belt Finance.
Generated: DETERMINISTIC_1845eac8f9ec3e5e
Batch ID: 20250612_155024
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
 * @title BELT Token Staking Smart Contract
 * @dev Enables staking BELT tokens and distributing rewards based on staking mechanisms.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BeltStaking {
    // BELT token interface
    IERC20 public immutable beltToken;

    // Reward distribution variables
    uint256 public rewardRate; // Rewards per second per staked token
    uint256 public lastUpdateTime;
    uint256 public totalRewardsDistributed;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // User staking and reward data
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 pendingRewards;
    }
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    // Constructor
    constructor(IERC20 _beltToken, uint256 _rewardRate) {
        beltToken = _beltToken;
        rewardRate = _rewardRate; // Set reward rate
    }

    /**
     * @dev Modifier to update rewards before any state-changing action.
     */
    modifier updateRewards(address _staker) {
        if (_staker != address(0)) {
            Staker storage staker = stakers[_staker];
            staker.pendingRewards += calculateRewards(_staker);
            staker.rewardDebt = staker.stakedAmount * rewardRate;
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Stake BELT tokens in the contract.
     * @param _amount Amount of BELT tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");

        Staker storage staker = stakers[msg.sender];
        beltToken.transferFrom(msg.sender, address(this), _amount);

        staker.stakedAmount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked BELT tokens.
     * @param _amount Amount of BELT tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= _amount, "Insufficient staked balance");

        staker.stakedAmount -= _amount;
        totalStaked -= _amount;

        beltToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        uint256 rewardsToClaim = staker.pendingRewards;

        require(rewardsToClaim > 0, "No rewards to claim");

        staker.pendingRewards = 0;
        totalRewardsDistributed += rewardsToClaim;

        beltToken.transfer(msg.sender, rewardsToClaim);

        emit Claimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Calculate rewards for a given staker since last update.
     * @param _staker Address of the staker.
     * @return Pending rewards.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 accumulatedRewards = (staker.stakedAmount * rewardRate * (block.timestamp - lastUpdateTime)) / 1e18;
        return accumulatedRewards - staker.rewardDebt;
    }

    /**
     * @dev View function to check pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 calculatedRewards = calculateRewards(_user);
        return staker.pendingRewards + calculatedRewards;
    }
}
```
