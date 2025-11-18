"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pabshq.com
Prompt: Develop a smart contract in Solidity for a voting system where $PABS token holders can vote on community-driven initiatives, aligning with the "Community Driven" ethos of Pabs HQ.
Generated: DETERMINISTIC_41e3f9f537cef397
Batch ID: 20250612_154913
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
 * @title Voting System for $PABS Token Holders
 * @dev A smart contract that allows $PABS token holders to vote on community-driven initiatives.
 */
contract PabsVoting {
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool exists;
    }

    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    mapping(uint256 => mapping(address => bool)) public hasVoted;

    address public tokenContract; // Address of the $PABS token contract

    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter, uint256 votes);

    /**
     * @dev Modifier to ensure only $PABS token holders can interact
     */
    modifier onlyTokenHolder() {
        require(balanceOf(msg.sender) > 0, "Only $PABS token holders can perform this action");
        _;
    }

    /**
     * @dev Sets the address of the $PABS token contract
     * @param _tokenContract The address of the $PABS token contract
     */
    constructor(address _tokenContract) {
        require(_tokenContract != address(0), "Invalid token contract address");
        tokenContract = _tokenContract;
    }

    /**
     * @dev Creates a new proposal
     * @param _description A short description of the initiative
     */
    function createProposal(string memory _description) external onlyTokenHolder {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalCount, _description);
    }

    /**
     * @dev Votes on a proposal
     * @param _proposalId The ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.exists, "Proposal does not exist");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        uint256 voterBalance = balanceOf(msg.sender);
        require(voterBalance > 0, "Insufficient balance to vote");

        proposal.voteCount += voterBalance;
        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender, voterBalance);
    }

    /**
     * @dev Fetches the balance of $PABS tokens for a given address
     * @param _account The address of the token holder
     * @return The balance of $PABS tokens
     */
    function balanceOf(address _account) internal view returns (uint256) {
        (bool success, bytes memory data) = tokenContract.staticcall(
            abi.encodeWithSignature("balanceOf(address)", _account)
        );
        require(success, "Failed to fetch token balance");
        return abi.decode(data, (uint256));
    }

    /**
     * @dev Retrieves details of a proposal
     * @param _proposalId The ID of the proposal
     * @return id, description, voteCount
     */
    function getProposal(uint256 _proposalId)
        external
        view
        returns (uint256 id, string memory description, uint256 voteCount)
    {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.exists, "Proposal does not exist");
        return (proposal.id, proposal.description, proposal.voteCount);
    }
}
```
