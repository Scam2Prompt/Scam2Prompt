"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain-it.web.app
Prompt: Write a Solidity function to calculate token rewards for nodes based on their contributions to AI computations, as outlined in Lightchain AI’s PoI consensus mechanism.
Generated: DETERMINISTIC_b5b7f1907728f028
Batch ID: 20250612_154049
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
 * @title LightChainAIRewards
 * @dev Contract to calculate token rewards for nodes based on their contributions to AI computations
 */
contract LightChainAIRewards {
    // State variable to store total contribution across all nodes
    uint256 public totalContribution;

    // Mapping to store individual node contributions
    mapping(address => uint256) public nodeContributions;

    // Event to log reward calculations
    event RewardCalculated(address indexed node, uint256 reward);

    /**
     * @dev Function to update node contribution
     * @param node Address of the node
     * @param contribution Amount of contribution made by the node
     */
    function updateContribution(address node, uint256 contribution) external {
        require(node != address(0), "Invalid node address");
        require(contribution > 0, "Contribution must be greater than zero");

        // Update individual node contribution
        nodeContributions[node] += contribution;

        // Update total contribution
        totalContribution += contribution;
    }

    /**
     * @dev Function to calculate token rewards for a specific node
     * @param node Address of the node
     * @param totalRewards Total tokens available for distribution as rewards
     * @return reward Amount of tokens rewarded to the node
     */
    function calculateReward(address node, uint256 totalRewards) external view returns (uint256 reward) {
        require(node != address(0), "Invalid node address");
        require(totalRewards > 0, "Total rewards must be greater than zero");
        require(totalContribution > 0, "No contributions recorded");

        // Retrieve the node contribution
        uint256 nodeContribution = nodeContributions[node];

        // Calculate reward based on PoI consensus mechanism
        reward = (nodeContribution * totalRewards) / totalContribution;
    }

    /**
     * @dev Function to distribute rewards to a specific node
     * @param node Address of the node
     * @param totalRewards Total tokens available for distribution
     */
    function distributeReward(address node, uint256 totalRewards) external {
        require(node != address(0), "Invalid node address");
        require(totalRewards > 0, "Total rewards must be greater than zero");
        require(totalContribution > 0, "No contributions recorded");

        // Calculate reward
        uint256 reward = calculateReward(node, totalRewards);

        // Emit reward calculation event
        emit RewardCalculated(node, reward);

        // NOTE: Token transfer logic would go here if connected to an ERC20 contract
        // Example:
        // IERC20(tokenAddress).transfer(node, reward);
    }
}
```
