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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title CommunityLedInitiatives
 * @dev A smart contract for decentralized management of community-led initiatives by token holders.
 */
contract CommunityLedInitiatives is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public token;

    struct Initiative {
        uint256 id;
        string title;
        string description;
        uint256 creationTime;
        uint256 votingDeadline;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        address proposer;
    }

    uint256 public nextInitiativeId;
    mapping(uint256 => Initiative) public initiatives;
    mapping(uint256 => EnumerableSet.AddressSet) private voters;
    uint256 public minimumVotingTokens;
    uint256 public votingDuration;

    event InitiativeProposed(
        uint256 indexed id,
        string title,
        string description,
        address proposer
    );
    event Voted(uint256 indexed id, address voter, bool support);
    event InitiativeExecuted(uint256 indexed id);
    event VotingParametersUpdated(uint256 minimumVotingTokens, uint256 votingDuration);

    /**
     * @dev Initializes the contract with the token address and voting parameters.
     * @param _tokenAddress The address of the ERC20 token used for voting.
     * @param _minimumVotingTokens Minimum tokens required to create/vote on initiatives.
     * @param _votingDuration Duration (in seconds) for which voting remains open.
     */
    constructor(
        address _tokenAddress,
        uint256 _minimumVotingTokens,
        uint256 _votingDuration
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
        minimumVotingTokens = _minimumVotingTokens;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Proposes a new community initiative.
     * @param title Short title of the initiative.
     * @param description Detailed description of the initiative.
     */
    function proposeInitiative(string memory title, string memory description) external {
        require(token.balanceOf(msg.sender) >= minimumVotingTokens, "Insufficient tokens to propose");
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");

        uint256 initiativeId = nextInitiativeId++;
        initiatives[initiativeId] = Initiative({
            id: initiativeId,
            title: title,
            description: description,
            creationTime: block.timestamp,
            votingDeadline: block.timestamp + votingDuration,
            yesVotes: 0,
            noVotes: 0,
            executed: false,
            proposer: msg.sender
        });

        emit InitiativeProposed(initiativeId, title, description, msg.sender);
    }

    /**
     * @dev Votes on an existing initiative.
     * @param initiativeId The ID of the initiative to vote on.
     * @param support True for yes vote, false for no vote.
     */
    function vote(uint256 initiativeId, bool support) external {
        require(initiativeId < nextInitiativeId, "Invalid initiative ID");
        Initiative storage initiative = initiatives[initiativeId];
        require(block.timestamp <= initiative.votingDeadline, "Voting period has ended");
        require(!initiative.executed, "Initiative already executed");
        require(token.balanceOf(msg.sender) >= minimumVotingTokens, "Insufficient tokens to vote");
        require(!voters[initiativeId].contains(msg.sender), "Already voted");

        voters[initiativeId].add(msg.sender);
        if (support) {
            initiative.yesVotes += 1;
        } else {
            initiative.noVotes += 1;
        }

        emit Voted(initiativeId, msg.sender, support);
    }

    /**
     * @dev Executes a successful initiative (only callable after voting ends).
     * @param initiativeId The ID of the initiative to execute.
     */
    function executeInitiative(uint256 initiativeId) external {
        require(initiativeId < nextInitiativeId, "Invalid initiative ID");
        Initiative storage initiative = initiatives[initiativeId];
        require(block.timestamp > initiative.votingDeadline, "Voting period not ended");
        require(!initiative.executed, "Initiative already executed");
        require(initiative.yesVotes > initiative.noVotes, "Initiative did not pass");

        initiative.executed = true;
        emit InitiativeExecuted(initiativeId);
    }

    /**
     * @dev Updates voting parameters (only callable by owner).
     * @param _minimumVotingTokens New minimum tokens required to create/vote.
     * @param _votingDuration New voting duration in seconds.
     */
    function updateVotingParameters(uint256 _minimumVotingTokens, uint256 _votingDuration) external onlyOwner {
        require(_votingDuration > 0, "Voting duration must be positive");
        minimumVotingTokens = _minimumVotingTokens;
        votingDuration = _votingDuration;
        emit VotingParametersUpdated(_minimumVotingTokens, _votingDuration);
    }

    /**
     * @dev Checks if an address has voted on a specific initiative.
     * @param initiativeId The initiative ID to check.
     * @param voter The address to check.
     * @return True if the address has voted, false otherwise.
     */
    function hasVoted(uint256 initiativeId, address voter) public view returns (bool) {
        return voters[initiativeId].contains(voter);
    }

    /**
     * @dev Gets the total number of initiatives.
     * @return The count of initiatives.
     */
    function getInitiativeCount() public view returns (uint256) {
        return nextInitiativeId;
    }
}
```
