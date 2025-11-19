"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqnetwork.io
Prompt: How can I implement a voting mechanism for governance proposals using the IQ token on the BrainDAO ecosystem?
Generated: DETERMINISTIC_6e676e6a8f0275fd
Batch ID: 20250612_163506
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
 * @title GovernanceVoting
 * @dev Implements a voting mechanism for governance proposals using the IQ token on the BrainDAO ecosystem.
 *      This contract allows users to vote on proposals, where votes are weighted by the number of IQ tokens staked.
 */
interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract GovernanceVoting {
    // IQ token contract address
    IERC20 public iqToken;

    // Proposal structure
    struct Proposal {
        string description;
        uint256 voteCount;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Array to store proposals
    Proposal[] public proposals;

    // Mapping to track staked tokens per voter
    mapping(address => uint256) public stakedTokens;

    // Mapping to track if a voter has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter, bool vote, uint256 weight);
    event ProposalExecuted(uint256 proposalId, bool success);

    /**
     * @dev Constructor to set the IQ token address.
     * @param _iqToken Address of the IQ token contract.
     */
    constructor(IERC20 _iqToken) {
        require(address(_iqToken) != address(0), "Invalid IQ token address");
        iqToken = _iqToken;
    }

    /**
     * @dev Stake IQ tokens to participate in voting.
     * @param _amount Amount of IQ tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Stake amount should be greater than zero");
        require(iqToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        stakedTokens[msg.sender] += _amount;
    }

    /**
     * @dev Unstake IQ tokens and withdraw them back to the voter.
     * @param _amount Amount of IQ tokens to unstake.
     */
    function unstakeTokens(uint256 _amount) external {
        require(_amount > 0, "Unstake amount should be greater than zero");
        require(stakedTokens[msg.sender] >= _amount, "Insufficient staked tokens");
        stakedTokens[msg.sender] -= _amount;
        require(iqToken.transfer(msg.sender, _amount), "Token transfer failed");
    }

    /**
     * @dev Create a new governance proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _vote True for yes, false for no.
     */
    function vote(uint256 _proposalId, bool _vote) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(stakedTokens[msg.sender] > 0, "No staked tokens to vote");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");

        Proposal storage proposal = proposals[_proposalId];
        hasVoted[_proposalId][msg.sender] = true;

        uint256 voterWeight = stakedTokens[msg.sender];
        proposal.voteCount += voterWeight;

        if (_vote) {
            proposal.yesVotes += voterWeight;
        } else {
            proposal.noVotes += voterWeight;
        }

        emit Voted(_proposalId, msg.sender, _vote, voterWeight);
    }

    /**
     * @dev Execute the proposal after voting has concluded.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");

        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes cast on this proposal");

        proposal.executed = true;

        // Logic to execute the proposal (e.g., updating system settings) would go here
        bool success = proposal.yesVotes > proposal.noVotes; // Example: Pass if yesVotes > noVotes

        emit ProposalExecuted(_proposalId, success);
    }

    /**
     * @dev Get the total number of proposals.
     * @return Total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get details of a proposal.
     * @param _proposalId ID of the proposal to retrieve.
     * @return Proposal details.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory, uint256, uint256, uint256, bool) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.yesVotes, proposal.noVotes, proposal.executed);
    }
}
```
