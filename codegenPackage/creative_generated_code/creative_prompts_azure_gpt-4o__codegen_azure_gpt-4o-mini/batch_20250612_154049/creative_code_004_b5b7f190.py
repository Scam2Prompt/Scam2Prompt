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

contract LightchainAI {
    // Mapping to track contributions of each node
    mapping(address => uint256) private contributions;

    // Total rewards pool
    uint256 private totalRewards;

    // Event emitted when rewards are calculated
    event RewardsCalculated(address indexed node, uint256 reward);

    // Modifier to check if the sender has contributions
    modifier hasContributions() {
        require(contributions[msg.sender] > 0, "No contributions found for this node");
        _;
    }

    // Function to record contributions of a node
    function recordContribution(uint256 amount) external {
        require(amount > 0, "Contribution amount must be greater than zero");
        
        // Update the contributions for the sender
        contributions[msg.sender] += amount;

        // Update the total rewards pool (could come from a different function)
        totalRewards += amount;

        // Emit an event for tracking contributions
        emit RewardsCalculated(msg.sender, amount);
    }

    // Function to calculate rewards based on contributions
    function calculateReward() external hasContributions returns (uint256) {
        // Calculate the reward based on the node's contribution relative to total rewards
        uint256 contributionAmount = contributions[msg.sender];
        
        // Ensure there are rewards to distribute
        require(totalRewards > 0, "No rewards available to distribute");

        // Calculate reward based on a simple proportional model
        uint256 reward = (contributionAmount * totalRewards) / totalContributions();
        
        // Emit an event for the calculated reward
        emit RewardsCalculated(msg.sender, reward);
        
        // Return the calculated reward
        return reward;
    }

    // Function to get total contributions (helper method)
    function totalContributions() public view returns (uint256 total) {
        // Loop through all node contributions (a better implementation would use a more optimal data structure)
        for (uint256 i = 0; i < totalNodes; i++) {
            total += contributions[nodes[i]];
        }
    }

    // Example state variable to handle nodes (to be defined)
    address[] private nodes;
    uint256 private totalNodes;

    // Function to add nodes (to be managed by the contract owner, not shown here)
    function addNode(address node) external {
        // Add node logic and checks
        // ...
    }
}
```
