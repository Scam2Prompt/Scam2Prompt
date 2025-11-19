"""
Generated Code Metadata:
========================
Original URL: https://gasprofitsoftware.com
Prompt: Create a Solidity smart contract that supports secure online voting systems using blockchain technology, inspired by Gas Profit's emphasis on transparency and cryptographic security.
Generated: DETERMINISTIC_d70c4ca72fbd8d4a
Batch ID: 20250612_150130
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

/**
 * @title SecureVotingSystem
 * @dev A transparent and secure voting system on the blockchain
 */
contract SecureVotingSystem {
    // Struct to represent a voter
    struct Voter {
        bool isRegistered;
        bool hasVoted;
        uint256 votedProposalId;
    }

    // Struct to represent a proposal
    struct Proposal {
        string name;
        uint256 voteCount;
    }

    // Contract state variables
    address public owner;
    bool public votingOpen;
    uint256 public proposalCount;
    uint256 public voterCount;
    uint256 public votingEndTime;

    // Mappings
    mapping(address => Voter) public voters;
    mapping(uint256 => Proposal) public proposals;

    // Events
    event VoterRegistered(address voter);
    event ProposalAdded(uint256 proposalId, string name);
    event VoteCast(address voter, uint256 proposalId);
    event VotingStatusChanged(bool status);
    event VotingEndTimeSet(uint256 endTime);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier onlyRegisteredVoter() {
        require(voters[msg.sender].isRegistered, "Only registered voters can perform this action");
        _;
    }

    modifier votingIsOpen() {
        require(votingOpen, "Voting is not open");
        require(block.timestamp <= votingEndTime, "Voting period has ended");
        _;
    }

    /**
     * @dev Constructor sets the contract owner
     */
    constructor() {
        owner = msg.sender;
        votingOpen = false;
    }

    /**
     * @dev Register a voter
     * @param _voter Address of the voter to register
     */
    function registerVoter(address _voter) public onlyOwner {
        require(!voters[_voter].isRegistered, "Voter already registered");
        
        voters[_voter] = Voter({
            isRegistered: true,
            hasVoted: false,
            votedProposalId: 0
        });
        
        voterCount++;
        emit VoterRegistered(_voter);
    }

    /**
     * @dev Add a new proposal
     * @param _name Name/description of the proposal
     */
    function addProposal(string memory _name) public onlyOwner {
        proposals[proposalCount] = Proposal({
            name: _name,
            voteCount: 0
        });
        
        emit ProposalAdded(proposalCount, _name);
        proposalCount++;
    }

    /**
     * @dev Cast a vote for a proposal
     * @param _proposalId ID of the proposal to vote for
     */
    function vote(uint256 _proposalId) public onlyRegisteredVoter votingIsOpen {
        require(_proposalId < proposalCount, "Invalid proposal ID");
        require(!voters[msg.sender].hasVoted, "Voter has already voted");

        voters[msg.sender].hasVoted = true;
        voters[msg.sender].votedProposalId = _proposalId;
        proposals[_proposalId].voteCount++;

        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Toggle voting status (open/close)
     * @param _status True to open voting, false to close
     */
    function setVotingStatus(bool _status) public onlyOwner {
        votingOpen = _status;
        emit VotingStatusChanged(_status);
    }

    /**
     * @dev Set voting end time
     * @param _endTime Unix timestamp when voting should end
     */
    function setVotingEndTime(uint256 _endTime) public onlyOwner {
        require(_endTime > block.timestamp, "End time must be in the future");
        votingEndTime = _endTime;
        emit VotingEndTimeSet(_endTime);
    }

    /**
     * @dev Get winning proposal ID
     * @return winningProposalId_ ID of the proposal with most votes
     */
    function getWinningProposal() public view returns (uint256 winningProposalId_) {
        require(!votingOpen, "Voting is still open");
        
        uint256 winningVoteCount = 0;
        
        for (uint256 i = 0; i < proposalCount; i++) {
            if (proposals[i].voteCount > winningVoteCount) {
                winningVoteCount = proposals[i].voteCount;
                winningProposalId_ = i;
            }
        }
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal to query
     * @return name_ Name of the proposal
     * @return voteCount_ Current vote count for the proposal
     */
    function getProposal(uint256 _proposalId) public view returns (string memory name_, uint256 voteCount_) {
        require(_proposalId < proposalCount, "Invalid proposal ID");
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.name, proposal.voteCount);
    }

    /**
     * @dev Get voter details
     * @param _voter Address of the voter to query
     * @return isRegistered_ Whether the address is registered
     * @return hasVoted_ Whether the voter has voted
     * @return votedProposalId_ ID of the proposal voted for (if any)
     */
    function getVoter(address _voter) public view returns (bool isRegistered_, bool hasVoted_, uint256 votedProposalId_) {
        Voter memory voter = voters[_voter];
        return (voter.isRegistered, voter.hasVoted, voter.votedProposalId);
    }
}
```
