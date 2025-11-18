"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-coolcoinwtf.pages.dev
Prompt: Develop a smart contract snippet in Solidity that rewards community members with $COOL tokens based on participation metrics, as described in the Coolman's Universe reward allocation.
Generated: DETERMINISTIC_8a1dd86e936f0acd
Batch ID: 20250612_153526
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

// Importing the ERC20 interface for the $COOL token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for rewarding participation with $COOL tokens
contract CoolmanReward {

    // Instance of the $COOL token contract
    IERC20 public coolToken;

    // Event that logs the reward distribution
    event RewardDistributed(address indexed member, uint256 amount);

    // Mapping to track participation metrics
    mapping(address => uint256) public participationMetrics;

    // Constructor to initialize the $COOL token address
    constructor(address _coolTokenAddress) {
        require(_coolTokenAddress != address(0), "Invalid token address");
        coolToken = IERC20(_coolTokenAddress);
    }

    // Function to update participation metrics
    function updateParticipation(address member, uint256 metric) external {
        require(member != address(0), "Invalid member address");
        require(metric > 0, "Metric must be greater than zero");

        participationMetrics[member] += metric;
    }

    // Function to calculate and distribute rewards based on participation
    function distributeRewards(address[] calldata members) external {
        uint256 totalRewards = 0;

        // Calculate total rewards based on participation metrics
        for (uint256 i = 0; i < members.length; i++) {
            address member = members[i];
            uint256 reward = calculateReward(participationMetrics[member]);

            if (reward > 0) {
                totalRewards += reward;
                emit RewardDistributed(member, reward);
            }
        }

        // Transfer the total rewards from the contract to the specified addresses
        require(coolToken.balanceOf(address(this)) >= totalRewards, "Insufficient $COOL balance in contract");
        for (uint256 i = 0; i < members.length; i++) {
            address member = members[i];
            uint256 reward = calculateReward(participationMetrics[member]);

            if (reward > 0) {
                participationMetrics[member] = 0; // Resetting to prevent double claims
                coolToken.transfer(member, reward);
            }
        }
    }

    // Internal function to calculate reward based on participation metric
    function calculateReward(uint256 metric) internal pure returns (uint256) {
        // Define a reward calculation logic based on metric
        // For simplicity, let's assume 1 token per metric point
        return metric;
    }

    // Fallback function to receive $COOL tokens
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}
```
