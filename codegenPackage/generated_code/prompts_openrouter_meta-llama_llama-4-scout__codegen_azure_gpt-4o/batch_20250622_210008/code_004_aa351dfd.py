"""
Generated Code Metadata:
========================
Original URL: https://beraswap.pages.dev
Prompt: Design a simple smart contract on Berachain that utilizes the Proof-of-Liquidity consensus mechanism to incentivize validators and ecosystem participants.
Generated: DETERMINISTIC_aa351dfd3ef8355a
Batch ID: 20250622_210008
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

/**
 * @title ProofOfLiquidityIncentive
 * @dev A simple smart contract on Berachain to incentivize validators and ecosystem participants
 * using the Proof-of-Liquidity consensus mechanism.
 */
contract ProofOfLiquidityIncentive {
    // Mapping to track liquidity provided by participants
    mapping(address => uint256) public liquidityProvided;

    // Mapping to track rewards earned by participants
    mapping(address => uint256) public rewardsEarned;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed participant, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed participant, uint256 amount);

    // Modifier to ensure non-zero values
    modifier nonZero(uint256 _value) {
        require(_value > 0, "Value must be greater than zero");
        _;
    }

    /**
     * @dev Function to add liquidity to the contract.
     * @param _amount The amount of liquidity to add.
     */
    function addLiquidity(uint256 _amount) external nonZero(_amount) {
        // Update the liquidity mapping
        liquidityProvided[msg.sender] += _amount;

        // Emit the LiquidityAdded event
        emit LiquidityAdded(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate rewards based on liquidity provided.
     * @param _participant The address of the participant.
     * @return The calculated reward amount.
     */
    function calculateRewards(address _participant) public view returns (uint256) {
        // Example reward calculation: 10% of liquidity provided
        return (liquidityProvided[_participant] * 10) / 100;
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        // Calculate rewards for the caller
        uint256 reward = calculateRewards(msg.sender);

        // Ensure there are rewards to claim
        require(reward > 0, "No rewards available to claim");

        // Update the rewards mapping
        rewardsEarned[msg.sender] += reward;

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to check the total liquidity provided by a participant.
     * @param _participant The address of the participant.
     * @return The total liquidity provided.
     */
    function getLiquidity(address _participant) external view returns (uint256) {
        return liquidityProvided[_participant];
    }

    /**
     * @dev Function to check the total rewards earned by a participant.
     * @param _participant The address of the participant.
     * @return The total rewards earned.
     */
    function getRewards(address _participant) external view returns (uint256) {
        return rewardsEarned[_participant];
    }
}
```
