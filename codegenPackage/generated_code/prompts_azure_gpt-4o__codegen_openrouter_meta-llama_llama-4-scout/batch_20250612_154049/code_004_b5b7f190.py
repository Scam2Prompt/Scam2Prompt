"""
Generated Code Metadata:
========================
Original URL: https://lightchain-it.web.app
Prompt: Write a Solidity function to calculate token rewards for nodes based on their contributions to AI computations, as outlined in Lightchain AI’s PoI consensus mechanism.
Generated: DETERMINISTIC_b5b7f1907728f028
Batch ID: 20250612_154049
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

contract LightchainAI {
    // Mapping of node addresses to their contribution scores
    mapping (address => uint256) public nodeContributions;

    // Mapping of node addresses to their reward balances
    mapping (address => uint256) public nodeRewards;

    // Total tokens allocated for rewards
    uint256 public totalRewardTokens;

    // Token contract instance
    IERC20 public token;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed node, uint256 rewardAmount);

    /**
     * Constructor for the LightchainAI contract
     * @param _token Address of the token contract
     * @param _totalRewardTokens Total tokens to allocate for rewards
     */
    constructor(address _token, uint256 _totalRewardTokens) {
        require(_token != address(0), "Token address cannot be zero");
        require(_totalRewardTokens > 0, "Total reward tokens must be greater than zero");

        token = IERC20(_token);
        totalRewardTokens = _totalRewardTokens;
    }

    /**
     * Updates the contribution score for a node
     * @param _node Address of the node
     * @param _contribution Contribution score to add
     */
    function updateNodeContribution(address _node, uint256 _contribution) public {
        require(_node != address(0), "Node address cannot be zero");
        require(_contribution > 0, "Contribution must be greater than zero");

        nodeContributions[_node] += _contribution;
    }

    /**
     * Calculates and distributes rewards to nodes based on their contributions
     */
    function distributeRewards() public {
        // Calculate total contribution score across all nodes
        uint256 totalContribution = 0;
        for (address node in nodeContributions) {
            totalContribution += nodeContributions[node];
        }

        // Distribute rewards to nodes
        for (address node in nodeContributions) {
            uint256 nodeContribution = nodeContributions[node];
            uint256 rewardAmount = (nodeContribution * totalRewardTokens) / totalContribution;

            // Update node's reward balance
            nodeRewards[node] += rewardAmount;

            // Transfer tokens to node
            require(token.transfer(node, rewardAmount), "Token transfer failed");

            // Emit event
            emit RewardsDistributed(node, rewardAmount);
        }

        // Reset contribution scores and total reward tokens
        for (address node in nodeContributions) {
            nodeContributions[node] = 0;
        }
        totalRewardTokens = 0;
    }

    /**
     * Allows a node to claim their reward tokens
     * @param _node Address of the node
     */
    function claimReward(address _node) public {
        require(_node != address(0), "Node address cannot be zero");
        require(nodeRewards[_node] > 0, "Node has no reward to claim");

        uint256 rewardAmount = nodeRewards[_node];
        nodeRewards[_node] = 0;

        require(token.transfer(_node, rewardAmount), "Token transfer failed");
    }
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
