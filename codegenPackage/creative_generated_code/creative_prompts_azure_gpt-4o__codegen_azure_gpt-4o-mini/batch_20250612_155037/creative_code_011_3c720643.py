"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Create a Solidity contract for a community-driven token distribution system that allows users to vote on how $WING tokens should be allocated in future phases.
Generated: DETERMINISTIC_3c7206435c704c84
Batch ID: 20250612_155037
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title CommunityTokenDistribution
 * @dev A contract to manage the distribution of $WING tokens
 * through community voting on allocation phases.
 */
contract CommunityTokenDistribution is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // IERC20 token representing the $WING tokens
    IERC20 public wingToken;

    // Struct representing a voting phase
    struct VotingPhase {
        uint256 startTime;
        uint256 endTime;
        uint256 totalVotes;
        mapping(address => uint256) votes;
        EnumerableSet.AddressSet voters;
    }

    // Mapping of phase ID to VotingPhase
    mapping(uint256 => VotingPhase) public votingPhases;
    
    // Current phase ID
    uint256 public currentPhaseId;

    // Event emitted when a new voting phase is created
    event VotingPhaseCreated(uint256 indexed phaseId, uint256 startTime, uint256 endTime);
    
    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed phaseId, address indexed voter, uint256 amount);

    // Modifier to check if the voting phase is active
    modifier activePhase(uint256 phaseId) {
        require(block.timestamp >= votingPhases[phaseId].startTime, "Voting phase has not started yet.");
        require(block.timestamp <= votingPhases[phaseId].endTime, "Voting phase has ended.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the $WING token address.
     * @param _wingToken Address of the $WING token contract.
     */
    constructor(address _wingToken) {
        require(_wingToken != address(0), "Invalid token address");
        wingToken = IERC20(_wingToken);
    }

    /**
     * @dev Create a new voting phase.
     * @param duration Duration of the voting phase in seconds.
     */
    function createVotingPhase(uint256 duration) external onlyOwner {
        uint256 phaseId = currentPhaseId++;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + duration;

        VotingPhase storage newPhase = votingPhases[phaseId];
        newPhase.startTime = startTime;
        newPhase.endTime = endTime;
        
        emit VotingPhaseCreated(phaseId, startTime, endTime);
    }

    /**
     * @dev Cast a vote in the current active voting phase.
     * @param amount Amount of $WING tokens to vote with.
     */
    function vote(uint256 amount) external activePhase(currentPhaseId) {
        require(amount > 0, "Vote amount must be greater than zero");
        require(wingToken.balanceOf(msg.sender) >= amount, "Insufficient $WING tokens");
        
        // Transfer tokens from the voter to the contract
        wingToken.transferFrom(msg.sender, address(this), amount);
        
        VotingPhase storage phase = votingPhases[currentPhaseId];
        phase.totalVotes += amount;
        phase.votes[msg.sender] += amount;

        if (phase.voters.add(msg.sender)) {
            phase.voters.add(msg.sender);
        }

        emit VoteCast(currentPhaseId, msg.sender, amount);
    }

    /**
     * @dev Retrieve the total votes cast in a specific phase.
     * @param phaseId The ID of the voting phase.
     * @return totalVotes The total amount of votes.
     */
    function getTotalVotes(uint256 phaseId) external view returns (uint256 totalVotes) {
        return votingPhases[phaseId].totalVotes;
    }

    /**
     * @dev Retrieve the amount of votes a specific address has in a phase.
     * @param phaseId The ID of the voting phase.
     * @param voter The address of the voter.
     * @return voterVotes The amount of votes cast by the voter.
     */
    function getVotesByVoter(uint256 phaseId, address voter) external view returns (uint256 voterVotes) {
        return votingPhases[phaseId].votes[voter];
    }
}
```
