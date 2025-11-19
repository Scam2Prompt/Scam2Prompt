"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://or-22s.pages.dev
Prompt: Provide an example of a smart contract that integrates with the $ENTS rewards event.
Generated: DETERMINISTIC_949d32cdf1f48002
Batch ID: 20250612_163432
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
 * @title ENTSRewardContract
 * @dev This smart contract listens for $ENTS rewards events and handles the distribution of rewards.
 */
contract ENTSRewardContract {
    // Address of the $ENTS token contract
    address public entsTokenAddress;

    // Mapping to track user balances
    mapping(address => uint256) public rewardBalances;

    // Event emitted when rewards are received
    event RewardReceived(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to check if the caller is the $ENTS token contract
    modifier onlyEntsToken() {
        require(msg.sender == entsTokenAddress, "Caller is not the ENTS token contract");
        _;
    }

    /**
     * @dev Constructor to set the $ENTS token contract address.
     * @param _entsTokenAddress The address of the $ENTS token contract.
     */
    constructor(address _entsTokenAddress) {
        require(_entsTokenAddress != address(0), "Invalid ENTS token address");
        entsTokenAddress = _entsTokenAddress;
    }

    /**
     * @dev Function to update rewards when the $ENTS token contract triggers an event.
     * @param user The address of the user receiving rewards.
     * @param amount The amount of rewards to credit to the user.
     */
    function updateReward(address user, uint256 amount) external onlyEntsToken {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update reward balance
        rewardBalances[user] += amount;

        // Emit RewardReceived event
        emit RewardReceived(user, amount);
    }

    /**
     * @dev Function to allow users to claim their rewards.
     */
    function claimReward() external {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards available for claiming");

        // Reset reward balance before transfer to prevent reentrancy attack
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to the user (assuming $ENTS supports transfer method)
        (bool success, ) = entsTokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, reward)
        );
        require(success, "Reward transfer failed");

        // Emit RewardClaimed event
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to check the reward balance of a user.
     * @param user The address of the user.
     * @return The reward balance of the user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }
}
```
