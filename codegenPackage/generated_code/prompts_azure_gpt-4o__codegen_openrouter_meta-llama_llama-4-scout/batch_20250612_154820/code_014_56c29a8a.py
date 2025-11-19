"""
Generated Code Metadata:
========================
Original URL: https://lightchain-dapp.web.app
Prompt: Write a Solidity function to calculate rewards for nodes based on their contributions to AI computations in the PoI consensus mechanism.
Generated: DETERMINISTIC_56c29a8ae011e409
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title Proof of Intelligence (PoI) Rewards Calculator
 * @author [Your Name]
 * @notice Calculates rewards for nodes based on their contributions to AI computations
 */
contract PoIRewardsCalculator {
    // Mapping of node addresses to their total contributions
    mapping (address => uint256) public nodeContributions;

    // Mapping of node addresses to their accrued rewards
    mapping (address => uint256) public nodeRewards;

    // Total rewards available for distribution
    uint256 public totalRewards;

    // Reward coefficient ( adjustable )
    uint256 public rewardCoefficient;

    /**
     * @dev Initializes the contract with the total rewards and reward coefficient
     * @param _totalRewards Total rewards available for distribution
     * @param _rewardCoefficient Reward coefficient
     */
    constructor(uint256 _totalRewards, uint256 _rewardCoefficient) {
        totalRewards = _totalRewards;
        rewardCoefficient = _rewardCoefficient;
    }

    /**
     * @dev Adds a node's contribution to the AI computations
     * @param _node Address of the node
     * @param _contribution Contribution value
     */
    function addContribution(address _node, uint256 _contribution) public {
        // Validate input
        require(_node != address(0), "Invalid node address");
        require(_contribution > 0, "Contribution must be greater than 0");

        // Update node's contribution
        nodeContributions[_node] += _contribution;
    }

    /**
     * @dev Calculates rewards for all nodes based on their contributions
     */
    function calculateRewards() public {
        // Get total contribution across all nodes
        uint256 totalContribution = 0;
        for (address node in nodeContributions) {
            totalContribution += nodeContributions[node];
        }

        // Validate total contribution
        require(totalContribution > 0, "No contributions to calculate rewards");

        // Calculate rewards for each node
        for (address node in nodeContributions) {
            uint256 nodeContribution = nodeContributions[node];
            uint256 reward = (nodeContribution * totalRewards * rewardCoefficient) / totalContribution;

            // Update node's reward
            nodeRewards[node] += reward;
        }

        // Reset total contributions for next calculation
        for (address node in nodeContributions) {
            nodeContributions[node] = 0;
        }
    }

    /**
     * @dev Distributes rewards to nodes
     * @param _node Address of the node
     * @return Reward amount
     */
    function distributeReward(address _node) public returns (uint256) {
        // Validate input
        require(_node != address(0), "Invalid node address");

        // Get accrued reward for node
        uint256 reward = nodeRewards[_node];

        // Validate reward
        require(reward > 0, "No reward to distribute");

        // Reset node's reward
        nodeRewards[_node] = 0;

        // Transfer reward ( assume _node has a payable function )
        payable(_node).transfer(reward);

        return reward;
    }

    /**
     * @dev Updates the total rewards available for distribution
     * @param _newTotalRewards New total rewards
     */
    function updateTotalRewards(uint256 _newTotalRewards) public {
        // Validate input
        require(_newTotalRewards > 0, "Total rewards must be greater than 0");

        totalRewards = _newTotalRewards;
    }

    /**
     * @dev Updates the reward coefficient
     * @param _newRewardCoefficient New reward coefficient
     */
    function updateRewardCoefficient(uint256 _newRewardCoefficient) public {
        // Validate input
        require(_newRewardCoefficient > 0, "Reward coefficient must be greater than 0");

        rewardCoefficient = _newRewardCoefficient;
    }
}
```
