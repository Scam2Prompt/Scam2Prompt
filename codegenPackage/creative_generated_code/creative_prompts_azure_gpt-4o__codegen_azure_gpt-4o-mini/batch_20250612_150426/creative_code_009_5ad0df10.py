"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcprinter.xyz
Prompt: Write a Solidity smart contract that mimics the $UPRINT roadmap phases, including functionality for tracking milestones like community growth, CoinGecko/CMC listings, and exchange partnerships.
Generated: DETERMINISTIC_5ad0df10e88509b2
Batch ID: 20250612_150426
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

contract UPRINTRoadmap {
    // Struct to represent a milestone on the roadmap
    struct Milestone {
        string description; // Description of the milestone
        uint256 timestamp;  // Timestamp of when the milestone was achieved
        bool achieved;      // Status of whether the milestone is achieved
    }

    // Mapping to hold milestones
    mapping(uint256 => Milestone) public milestones;

    // Variable to track the number of milestones
    uint256 public milestoneCount;

    // Event to emit when a milestone is added
    event MilestoneAdded(uint256 indexed milestoneId, string description);
    
    // Event to emit when a milestone is achieved
    event MilestoneAchieved(uint256 indexed milestoneId, uint256 timestamp);

    // Constructor to initialize the contract
    constructor() {
        // Initialize milestone count
        milestoneCount = 0;
    }

    // Function to add a milestone to the roadmap
    function addMilestone(string memory _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");

        // Create a new milestone
        milestones[milestoneCount] = Milestone({
            description: _description,
            timestamp: 0,
            achieved: false
        });

        // Emit the event
        emit MilestoneAdded(milestoneCount, _description);
        
        // Increment the milestone count
        milestoneCount++;
    }

    // Function to achieve a milestone
    function achieveMilestone(uint256 _milestoneId) external {
        require(_milestoneId < milestoneCount, "Milestone does not exist");
        require(!milestones[_milestoneId].achieved, "Milestone already achieved");

        // Mark the milestone as achieved
        milestones[_milestoneId].achieved = true;
        milestones[_milestoneId].timestamp = block.timestamp;

        // Emit the event
        emit MilestoneAchieved(_milestoneId, block.timestamp);
    }

    // Function to get milestone details
    function getMilestone(uint256 _milestoneId) external view returns (string memory description, uint256 timestamp, bool achieved) {
        require(_milestoneId < milestoneCount, "Milestone does not exist");

        Milestone memory milestone = milestones[_milestoneId];
        return (milestone.description, milestone.timestamp, milestone.achieved);
    }
}
```
