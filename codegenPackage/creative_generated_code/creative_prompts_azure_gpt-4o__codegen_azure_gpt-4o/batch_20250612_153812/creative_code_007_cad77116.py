"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: Write a smart contract that leverages Ethereum's Pectra upgrade for staking, based on insights shared in Consensys' blog.
Generated: DETERMINISTIC_cad771160badb17b
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready smart contract for staking on Ethereum, leveraging the "Pectra upgrade." Note: As of my knowledge cutoff in October 2023, there is no "Pectra upgrade" officially recognized in Ethereum. If this is a future or hypothetical development, the contract implements staking functionality based on standard Ethereum features (e.g., `revert`, events, and best practices for staking contracts).

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev A contract for staking Ether, leveraging Ethereum's upgrades and best practices.
 */
contract StakingContract {
    // Mapping to store staked balances of users.
    mapping(address => uint256) private stakedBalances;

    // Mapping to store timestamps of when users staked their funds.
    mapping(address => uint256) private stakingTimestamps;

    // Total amount of Ether staked in the contract.
    uint256 private totalStaked;

    // Staking reward rate (e.g., 5% annualized).
    uint256 public constant REWARD_RATE = 5; // Annual rate in percentage.

    // Minimum staking duration for rewards (in seconds, e.g., 30 days).
    uint256 public constant MINIMUM_STAKING_DURATION = 30 days;

    // Address of the contract owner.
    address public owner;

    // Events for logging staking and withdrawal activity.
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure non-zero values are passed.
     * @param _value The value to check.
     */
    modifier nonZero(uint256 _value) {
        require(_value > 0, "Value must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to stake Ether in the contract.
     * Users can call this function to deposit their Ether for staking.
     */
    function stake() external payable nonZero(msg.value) {
        // Update the staked balance and timestamp for the user.
        stakedBalances[msg.sender] += msg.value;
        stakingTimestamps[msg.sender] = block.timestamp;

        // Update the total amount of Ether staked.
        totalStaked += msg.value;

        // Emit the Staked event.
        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Function to calculate staking rewards for a user.
     * Rewards are based on the staking duration and the reward rate.
     * @param _user The address of the user whose rewards are to be calculated.
     * @return Reward amount in Wei.
     */
    function calculateReward(address _user) public view returns (uint256) {
        // Ensure the user has staked funds.
        uint256 stakedAmount = stakedBalances[_user];
        if (stakedAmount == 0) {
            return 0;
        }

        // Calculate staking duration.
        uint256 stakingDuration = block.timestamp - stakingTimestamps[_user];
        if (stakingDuration < MINIMUM_STAKING_DURATION) {
            return 0; // No rewards for staking less than the minimum duration.
        }

        // Calculate annualized reward based on the staking duration.
        uint256 reward = (stakedAmount * REWARD_RATE * stakingDuration) / (365 days * 100);
        return reward;
    }

    /**
     * @dev Function to withdraw staked funds along with rewards.
     * Users can call this function to retrieve their staked Ether and any earned rewards.
     */
    function withdraw() external {
        // Ensure the user has staked funds.
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No funds to withdraw");

        // Calculate the reward.
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's staked balance and timestamp.
        stakedBalances[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Update the total amount of Ether staked.
        totalStaked -= stakedAmount;

        // Transfer the staked amount and reward to the user.
        uint256 totalWithdrawal = stakedAmount + reward;
        (bool success, ) = msg.sender.call{value: totalWithdrawal}("");
        require(success, "Withdrawal failed");

        // Emit the Withdrawn event.
        emit Withdrawn(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Function to get the total staked balance of a user.
     * @param _user The address of the user.
     * @return The total staked balance in Wei.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Function to get the total amount of Ether staked in the contract.
     * @return Total staked Ether in Wei.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Use the stake function to deposit funds");
    }
}
```
