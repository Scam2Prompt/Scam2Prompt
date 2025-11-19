"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Provide an example of a smart contract that could be used in a project developed during the ETHBerlin04 hackathon, focusing on community initiatives.
Generated: DETERMINISTIC_d0766ced5c652c2f
Batch ID: 20250612_162710
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
 * @title CommunityFund
 * @dev A smart contract for managing community-driven initiatives and funding.
 * The contract allows users to contribute funds and propose initiatives,
 * while the community votes to approve or reject them.
 */
contract CommunityFund {
    // Event emitted when a new initiative is proposed
    event InitiativeProposed(uint256 initiativeId, string description, address proposer);
    
    // Event emitted when funds are contributed
    event FundContributed(address contributor, uint256 amount);
    
    // Event emitted when an initiative is approved
    event InitiativeApproved(uint256 initiativeId, uint256 totalVotes);

    // Structure to define an initiative
    struct Initiative {
        string description;
        address proposer;
        uint256 votes;
        bool approved;
    }

    // State variables
    Initiative[] public initiatives;
    mapping(address => uint256) public contributions; // Tracks contributions per address
    uint256 public totalFunds; // Total funds available for initiatives

    // Modifier to ensure a valid initiative ID
    modifier validInitiative(uint256 _initiativeId) {
        require(_initiativeId < initiatives.length, "Invalid initiative ID");
        _;
    }

    /**
     * @notice Function to contribute funds to the community initiative pool
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than 0");

        // Update contributions and total funds
        contributions[msg.sender] += msg.value;
        totalFunds += msg.value;

        emit FundContributed(msg.sender, msg.value);
    }

    /**
     * @notice Function to propose a new initiative
     * @param _description A description of the initiative
     */
    function proposeInitiative(string calldata _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");

        // Create and store the initiative
        initiatives.push(Initiative({
            description: _description,
            proposer: msg.sender,
            votes: 0,
            approved: false
        }));

        emit InitiativeProposed(initiatives.length - 1, _description, msg.sender);
    }

    /**
     * @notice Function to vote on a proposed initiative
     * @param _initiativeId The ID of the initiative to vote for
     */
    function voteForInitiative(uint256 _initiativeId) external validInitiative(_initiativeId) {
        Initiative storage initiative = initiatives[_initiativeId];
        require(!initiative.approved, "Initiative already approved");

        // Increment vote count
        initiative.votes++;

        // Check if the initiative has been approved (simple majority vote logic)
        if (initiative.votes > (totalFunds / 2)) {
            initiative.approved = true;
            emit InitiativeApproved(_initiativeId, initiative.votes);
        }
    }

    /**
     * @notice Function to withdraw funds for an approved initiative
     * @param _initiativeId The ID of the initiative to withdraw funds for
     */
    function withdrawFunds(uint256 _initiativeId) external validInitiative(_initiativeId) {
        Initiative storage initiative = initiatives[_initiativeId];
        require(initiative.approved, "Initiative not approved");
        require(initiative.proposer == msg.sender, "Only proposer can withdraw funds");

        uint256 fundsToWithdraw = totalFunds;
        totalFunds = 0;

        // Transfer funds to the proposer
        (bool success, ) = msg.sender.call{value: fundsToWithdraw}("");
        require(success, "Fund withdrawal failed");
    }

    /**
     * @notice Function to get the details of an initiative
     * @param _initiativeId The ID of the initiative to fetch details for
     * @return description The description of the initiative
     * @return proposer The address of the proposer
     * @return votes The number of votes cast for the initiative
     * @return approved Whether the initiative has been approved
     */
    function getInitiativeDetails(uint256 _initiativeId)
        external
        view
        validInitiative(_initiativeId)
        returns (string memory description, address proposer, uint256 votes, bool approved)
    {
        Initiative storage initiative = initiatives[_initiativeId];
        return (initiative.description, initiative.proposer, initiative.votes, initiative.approved);
    }
}
```
