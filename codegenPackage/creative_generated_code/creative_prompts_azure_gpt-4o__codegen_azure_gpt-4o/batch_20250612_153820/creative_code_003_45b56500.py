"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.staderlabs.fi
Prompt: Create a Solidity smart contract that integrates Stader Labs' staking solutions for BNB Chain, ensuring secure delegation and reward distribution.
Generated: DETERMINISTIC_45b565008fd9ce1e
Batch ID: 20250612_153820
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
 * @title BNB Delegation Smart Contract
 * @dev This contract integrates with Stader Labs' staking solutions for BNB Chain to securely delegate BNB and distribute rewards.
 */
interface IStaderBNBStake {
    function stake() external payable;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
    function getUserReward(address user) external view returns (uint256);
}

contract BNBDelegation {
    // Address of the Stader Labs staking contract on BNB Chain
    address public immutable staderBNBStakeAddress;

    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;

    // Event emitted when a user stakes BNB
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws BNB
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the Stader Labs staking contract address.
     * @param _staderBNBStakeAddress Address of the Stader Labs staking contract.
     */
    constructor(address _staderBNBStakeAddress) {
        require(_staderBNBStakeAddress != address(0), "Invalid staking contract address");
        staderBNBStakeAddress = _staderBNBStakeAddress;
    }

    /**
     * @dev Stake BNB into Stader Labs' staking contract.
     * Emits a {Staked} event.
     */
    function stakeBNB() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Delegate BNB to Stader Labs staking contract
        IStaderBNBStake(staderBNBStakeAddress).stake{value: msg.value}();

        // Update user stake balance
        userStakes[msg.sender] += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw staked BNB from Stader Labs' staking contract.
     * Emits a {Withdrawn} event.
     * @param amount Amount of BNB to withdraw.
     */
    function withdrawBNB(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Withdraw BNB from Stader Labs staking contract
        IStaderBNBStake(staderBNBStakeAddress).withdraw(amount);

        // Update user stake balance
        userStakes[msg.sender] -= amount;

        // Transfer withdrawn BNB back to user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards from Stader Labs' staking contract.
     * Emits a {RewardsClaimed} event.
     */
    function claimRewards() external {
        // Get the user's reward from the staking contract
        uint256 reward = IStaderBNBStake(staderBNBStakeAddress).getUserReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Claim rewards from the staking contract
        IStaderBNBStake(staderBNBStakeAddress).claimRewards();

        // Transfer rewards to user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Fallback function to receive BNB.
     */
    receive() external payable {}

    /**
     * @dev Retrieve the total reward for a user from Stader Labs' staking contract.
     * @param user Address of the user.
     * @return Reward amount.
     */
    function getUserReward(address user) external view returns (uint256) {
        return IStaderBNBStake(staderBNBStakeAddress).getUserReward(user);
    }
}
```
