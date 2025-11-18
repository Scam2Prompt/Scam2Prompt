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

/**
 * @title UPRINTRoadmap
 * @dev A smart contract to track and manage milestones for the $UPRINT roadmap phases.
 */
contract UPRINTRoadmap {
    // Enum to represent different roadmap phases
    enum Phase {
        CommunityGrowth,
        CoinGeckoListing,
        CMCListing,
        ExchangePartnership
    }

    // Struct to store details about a milestone
    struct Milestone {
        string description; // Description of the milestone
        bool completed;     // Status of the milestone
        uint256 timestamp;  // Timestamp when the milestone was completed
    }

    // Mapping from roadmap phase to milestones
    mapping(Phase => Milestone[]) public milestones;

    // Owner of the contract
    address public owner;

    // Events
    event MilestoneAdded(Phase phase, string description);
    event MilestoneCompleted(Phase phase, uint256 milestoneIndex, uint256 timestamp);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "UPRINTRoadmap: Caller is not the owner.");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new milestone to a roadmap phase.
     * @param phase The phase to which the milestone belongs.
     * @param description A description of the milestone.
     */
    function addMilestone(Phase phase, string memory description) external onlyOwner {
        milestones[phase].push(Milestone({
            description: description,
            completed: false,
            timestamp: 0
        }));
        emit MilestoneAdded(phase, description);
    }

    /**
     * @dev Mark a milestone as completed.
     * @param phase The phase to which the milestone belongs.
     * @param milestoneIndex The index of the milestone to mark as completed.
     */
    function completeMilestone(Phase phase, uint256 milestoneIndex) external onlyOwner {
        require(milestoneIndex < milestones[phase].length, "UPRINTRoadmap: Invalid milestone index.");
        Milestone storage milestone = milestones[phase][milestoneIndex];
        require(!milestone.completed, "UPRINTRoadmap: Milestone already completed.");

        milestone.completed = true;
        milestone.timestamp = block.timestamp;

        emit MilestoneCompleted(phase, milestoneIndex, block.timestamp);
    }

    /**
     * @dev Get the details of a milestone.
     * @param phase The phase to which the milestone belongs.
     * @param milestoneIndex The index of the milestone.
     * @return description The description of the milestone.
     * @return completed The completion status of the milestone.
     * @return timestamp The timestamp when the milestone was completed.
     */
    function getMilestone(Phase phase, uint256 milestoneIndex)
        external
        view
        returns (string memory description, bool completed, uint256 timestamp)
    {
        require(milestoneIndex < milestones[phase].length, "UPRINTRoadmap: Invalid milestone index.");
        Milestone memory milestone = milestones[phase][milestoneIndex];
        return (milestone.description, milestone.completed, milestone.timestamp);
    }

    /**
     * @dev Get the number of milestones in a phase.
     * @param phase The phase to query.
     * @return The number of milestones in the phase.
     */
    function getMilestoneCount(Phase phase) external view returns (uint256) {
        return milestones[phase].length;
    }
}
```
