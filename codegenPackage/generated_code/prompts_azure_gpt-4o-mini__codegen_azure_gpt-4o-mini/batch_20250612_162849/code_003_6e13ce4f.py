"""
Generated Code Metadata:
========================
Original URL: https://arbinu.app
Prompt: Develop a smart contract in Solidity that implements the community-led initiatives mentioned on the Arbinu site, ensuring decentralized management of token holders.
Generated: DETERMINISTIC_6e13ce4f8bf1cea0
Batch ID: 20250612_162849
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CommunityInitiative
 * @dev A smart contract for managing community-led initiatives with decentralized governance.
 */
contract CommunityInitiative is Ownable {
    using Counters for Counters.Counter;

    // Structure to hold initiative details
    struct Initiative {
        string description;
        address proposer;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Mapping of initiative ID to Initiative
    mapping(uint256 => Initiative) public initiatives;
    Counters.Counter private initiativeIdCounter;

    // Event emitted when a new initiative is proposed
    event InitiativeProposed(uint256 indexed initiativeId, string description, address indexed proposer);
    
    // Event emitted when a vote is cast
    event Voted(uint256 indexed initiativeId, address indexed voter, bool support);
    
    // Event emitted when an initiative is executed
    event InitiativeExecuted(uint256 indexed initiativeId);

    /**
     * @dev Propose a new initiative.
     * @param _description A brief description of the initiative.
     */
    function proposeInitiative(string memory _description) external onlyOwner {
        initiativeIdCounter.increment();
        uint256 newInitiativeId = initiativeIdCounter.current();

        Initiative storage newInitiative = initiatives[newInitiativeId];
        newInitiative.description = _description;
        newInitiative.proposer = msg.sender;
        newInitiative.votesFor = 0;
        newInitiative.votesAgainst = 0;
        newInitiative.executed = false;

        emit InitiativeProposed(newInitiativeId, _description, msg.sender);
    }

    /**
     * @dev Vote on an initiative.
     * @param _initiativeId The ID of the initiative to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function vote(uint256 _initiativeId, bool _support) external {
        Initiative storage initiative = initiatives[_initiativeId];

        require(!initiative.executed, "Initiative already executed");
        require(!initiative.hasVoted[msg.sender], "You have already voted");

        initiative.hasVoted[msg.sender] = true;

        if (_support) {
            initiative.votesFor++;
        } else {
            initiative.votesAgainst++;
        }

        emit Voted(_initiativeId, msg.sender, _support);
    }

    /**
     * @dev Execute an initiative if it has enough votes.
     * @param _initiativeId The ID of the initiative to execute.
     */
    function executeInitiative(uint256 _initiativeId) external onlyOwner {
        Initiative storage initiative = initiatives[_initiativeId];

        require(!initiative.executed, "Initiative already executed");
        require(initiative.votesFor > initiative.votesAgainst, "Not enough votes in favor");

        initiative.executed = true;

        // Logic to execute the initiative can be added here

        emit InitiativeExecuted(_initiativeId);
    }

    /**
     * @dev Get the details of an initiative.
     * @param _initiativeId The ID of the initiative.
     * @return description The description of the initiative.
     * @return proposer The address of the proposer.
     * @return votesFor The number of votes in favor.
     * @return votesAgainst The number of votes against.
     * @return executed Whether the initiative has been executed.
     */
    function getInitiativeDetails(uint256 _initiativeId) external view returns (
        string memory description,
        address proposer,
        uint256 votesFor,
        uint256 votesAgainst,
        bool executed
    ) {
        Initiative storage initiative = initiatives[_initiativeId];
        return (
            initiative.description,
            initiative.proposer,
            initiative.votesFor,
            initiative.votesAgainst,
            initiative.executed
        );
    }
}
```
