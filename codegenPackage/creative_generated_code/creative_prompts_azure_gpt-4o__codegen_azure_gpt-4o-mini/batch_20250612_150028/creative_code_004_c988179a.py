"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismsio.vercel.app
Prompt: Write a smart contract that integrates with Optimism’s Retroactive Public Goods Funding (RetroPGF) mechanism to reward contributors based on community impact.
Generated: DETERMINISTIC_c988179a7c04354e
Batch ID: 20250612_150028
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Define the Smart Contract
contract RetroPGFReward is Ownable {
    using SafeMath for uint256;

    struct Contributor {
        address contributorAddress;
        uint256 impactPoints;
    }

    // Mapping to store contributors and their respective impact points
    mapping(address => Contributor) public contributors;

    // Total impact points for distribution
    uint256 public totalImpactPoints;

    // Event to log rewards
    event RewardDistributed(address indexed contributor, uint256 amount);

    // Function to record contributor impact points
    function recordContribution(address _contributor, uint256 _points) external onlyOwner {
        require(_contributor != address(0), "Invalid contributor address");
        require(_points > 0, "Points must be greater than zero");

        // Update contributor's impact points
        contributors[_contributor].contributorAddress = _contributor;
        contributors[_contributor].impactPoints = contributors[_contributor].impactPoints.add(_points);
        totalImpactPoints = totalImpactPoints.add(_points);
    }

    // Function to distribute rewards based on impact points
    function distributeRewards(uint256 totalRewardAmount) external onlyOwner {
        require(totalRewardAmount > 0, "Total reward amount must be greater than zero");
        require(totalImpactPoints > 0, "No impact points recorded");

        // Distributing rewards to each contributor based on their impact points
        for (uint256 i = 0; i < contributors.length; i++) {
            Contributor memory contributor = contributors[contributors[i]];
            uint256 rewardAmount = (contributor.impactPoints.mul(totalRewardAmount)).div(totalImpactPoints);

            // Transfer the reward (assuming the contract has enough Ether)
            (bool success, ) = contributor.contributorAddress.call{value: rewardAmount}("");
            require(success, "Reward transfer failed");

            emit RewardDistributed(contributor.contributorAddress, rewardAmount);
        }

        // Reset total impact points after distribution
        totalImpactPoints = 0;
    }

    // Function to receive Ether; msg.value will be used for rewards
    receive() external payable {}

    // Fallback function to accept any incoming transfers
    fallback() external payable {}
}
```
