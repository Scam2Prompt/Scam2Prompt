"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banksy.farm
Prompt: Generate a smart contract in Solidity for a staking mechanism that could be integrated into a platform like Banksy.farm.
Generated: DETERMINISTIC_8ce339b1d9948428
Batch ID: 20250612_154057
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
 * @dev A smart contract for staking tokens that could be integrated into a platform like Banksy.farm.
 */
contract StakingContract {

    // Structure to track staker's information
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 rewardDebt;   // Rewards owed to the staker
        uint256 lastStakeTime; // Timestamp of last staking action
    }

    mapping(address => Staker) public stakers; // Mapping of staker address to staking data
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per token per second
    uint256 public constant MINIMUM_STAKE_DURATION = 1 days; // Minimum staking duration

    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(msg.value == _amount, "Sent value must equal stake amount");

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards and update reward debt
        uint256 pendingRewards = calculateRewards(msg.sender);
        staker.rewardDebt += pendingRewards;

        // Update staker's info
        staker.stakedAmount += _amount;
        staker.lastStakeTime = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake tokens after the minimum duration has passed.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked amount found");
        require(
            block.timestamp >= staker.lastStakeTime + MINIMUM_STAKE_DURATION,
            "Staking duration not yet met"
        );

        // Calculate and claim pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);
        uint256 totalRewards = staker.rewardDebt + pendingRewards;
        staker.rewardDebt = 0;

        uint256 unstakeAmount = staker.stakedAmount;
        staker.stakedAmount = 0;

        // Update total staked amount
        totalStaked -= unstakeAmount;

        // Transfer tokens back to the staker
        payable(msg.sender).transfer(unstakeAmount + totalRewards);

        emit Unstaked(msg.sender, unstakeAmount);
        emit RewardsClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Calculates the pending rewards for a staker.
     * @param _staker Address of the staker.
     * @return Pending rewards amount.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker memory staker = stakers[_staker];
        uint256 stakingDuration = block.timestamp - staker.lastStakeTime;
        return stakingDuration * staker.stakedAmount * rewardRate;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate New reward rate per token per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw the contract's funds (if necessary).
     * Useful for emergencies or upgrades.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "Contract balance is zero");
        payable(owner).transfer(contractBalance);
    }
}
```
