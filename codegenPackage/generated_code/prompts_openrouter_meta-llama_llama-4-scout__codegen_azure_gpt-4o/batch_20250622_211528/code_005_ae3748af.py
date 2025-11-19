"""
Generated Code Metadata:
========================
Original URL: https://chain-sourcesmart.pages.dev
Prompt: Design a smart contract for a DAO-led protocol, similar to Popcorn, that leverages Web3 DeFi for environmental, open-source, and educational initiatives.
Generated: DETERMINISTIC_ae3748af4b47e81f
Batch ID: 20250622_211528
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
 * @title DAOProtocol
 * @dev A smart contract for a DAO-led protocol that supports environmental, open-source, and educational initiatives.
 *      This contract allows members to propose, vote, and fund initiatives using Web3 DeFi principles.
 */
contract DAOProtocol {
    // Struct to represent an initiative proposal
    struct Proposal {
        uint256 id;
        string title;
        string description;
        address proposer;
        uint256 fundingGoal;
        uint256 fundsRaised;
        uint256 votesFor;
        uint256 votesAgainst;
        bool funded;
        bool active;
    }

    // State variables
    uint256 public proposalCount; // Counter for proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal struct
    mapping(address => bool) public members; // Mapping to track DAO members
    mapping(uint256 => mapping(address => bool)) public votes; // Tracks votes per proposal per member
    address public owner; // Owner of the contract
    uint256 public membershipFee; // Fee to become a DAO member

    // Events
    event ProposalCreated(uint256 id, string title, address proposer);
    event Voted(uint256 proposalId, address voter, bool support);
    event FundsDeposited(uint256 proposalId, uint256 amount, address donor);
    event ProposalFunded(uint256 proposalId);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier onlyMember() {
        require(members[msg.sender], "Only DAO members can perform this action");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Constructor
    constructor(uint256 _membershipFee) {
        owner = msg.sender;
        membershipFee = _membershipFee;
    }

    /**
     * @dev Allows a user to join the DAO by paying the membership fee.
     */
    function joinDAO() external payable {
        require(msg.value == membershipFee, "Incorrect membership fee");
        require(!members[msg.sender], "Already a member");
        members[msg.sender] = true;
    }

    /**
     * @dev Allows a DAO member to create a new proposal.
     * @param _title Title of the proposal.
     * @param _description Description of the proposal.
     * @param _fundingGoal Funding goal for the proposal.
     */
    function createProposal(
        string memory _title,
        string memory _description,
        uint256 _fundingGoal
    ) external onlyMember {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            title: _title,
            description: _description,
            proposer: msg.sender,
            fundingGoal: _fundingGoal,
            fundsRaised: 0,
            votesFor: 0,
            votesAgainst: 0,
            funded: false,
            active: true
        });

        emit ProposalCreated(proposalCount, _title, msg.sender);
    }

    /**
     * @dev Allows a DAO member to vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool support)
        external
        onlyMember
        proposalExists(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.active, "Proposal is not active");
        require(!votes[proposalId][msg.sender], "Already voted");

        votes[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @dev Allows anyone to deposit funds to a proposal.
     * @param proposalId ID of the proposal to fund.
     */
    function depositFunds(uint256 proposalId)
        external
        payable
        proposalExists(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.active, "Proposal is not active");
        require(!proposal.funded, "Proposal is already funded");

        proposal.fundsRaised += msg.value;

        emit FundsDeposited(proposalId, msg.value, msg.sender);

        // Check if funding goal is met
        if (proposal.fundsRaised >= proposal.fundingGoal) {
            proposal.funded = true;
            proposal.active = false;
            emit ProposalFunded(proposalId);
        }
    }

    /**
     * @dev Allows the owner to withdraw contract funds.
     */
    function withdraw() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Returns the details of a proposal.
     * @param proposalId ID of the proposal to fetch.
     * @return Proposal details.
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (Proposal memory)
    {
        return proposals[proposalId];
    }
}
```
