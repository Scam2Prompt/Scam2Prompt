"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eursj.com
Prompt: Generate a Solidity smart contract compatible with Ethereum 2.0 that implements a basic staking mechanism with reward distribution.
Generated: DETERMINISTIC_27dcfc15d2f1bfa7
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title StakingContract
 * @notice A simple staking contract with reward distribution.
 */
contract StakingContract {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardPool; // Total reward pool distributed to stakers

    struct Stake {
        uint256 amount; // Amount staked by the user
        uint256 rewardDebt; // Rewards already credited to the user
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake

    // Events
    event StakeDeposited(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardsAdded(uint256 amount);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor that initializes the contract with the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to add rewards to the reward pool.
     * @param _amount Amount of rewards to add.
     */
    function addRewards(uint256 _amount) external payable onlyOwner {
        require(msg.value == _amount, "Sent value does not match amount");
        rewardPool += _amount;
        emit RewardsAdded(_amount);
    }

    /**
     * @dev Allows users to stake Ether into the contract.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");
        
        Stake storage userStake = stakes[msg.sender];
        
        // Update the user's stake
        userStake.amount += msg.value;
        userStake.rewardDebt = calculatePendingReward(msg.sender);
        
        // Update total staked amount
        totalStaked += msg.value;

        emit StakeDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Calculates pending rewards for a staker.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function calculatePendingReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0 || totalStaked == 0) {
            return 0;
        }
        return (rewardPool * userStake.amount) / totalStaked - userStake.rewardDebt;
    }

    /**
     * @dev Allows users to claim their pending rewards.
     */
    function claimRewards() external {
        uint256 pendingReward = calculatePendingReward(msg.sender);
        require(pendingReward > 0, "No rewards to claim");

        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += pendingReward;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: pendingReward}("");
        require(success, "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Allows users to withdraw their staked Ether.
     */
    function withdrawStake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Claim any pending rewards before withdrawing
        claimRewards();

        // Update user's stake
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer the staked amount back to the user
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Stake withdrawal failed");

        emit StakeWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Unsupported operation");
    }

    /**
     * @dev Receive function to allow reward deposits.
     */
    receive() external payable {
        rewardPool += msg.value;
        emit RewardsAdded(msg.value);
    }
}
```
