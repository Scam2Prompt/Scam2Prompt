"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-site.web.app
Prompt: Write a Solidity contract for a DAO vault system similar to Flockerz's Flock Vault, where community members can vote to allocate funds and earn rewards for participation.
Generated: DETERMINISTIC_825cd69f7524ccf4
Batch ID: 20250612_145223
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
 * @title DAO Vault Contract
 * @notice A decentralized vault system where members can propose, vote, and allocate funds,
 * while earning rewards for participation.
 */
contract DAOVault {
    struct Proposal {
        string description; // Description of the proposal
        uint256 amount;     // Amount requested in the proposal
        address payable recipient; // Recipient address for the funds
        uint256 votesFor;   // Count of votes in favor
        uint256 votesAgainst; // Count of votes against
        bool executed;      // Whether the proposal has been executed
    }

    address public immutable owner; // Contract owner
    uint256 public proposalCount;   // Number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal IDs to Proposal structs
    mapping(address => bool) public members; // Registered members
    mapping(uint256 => mapping(address => bool)) public votes; // Tracks voting per proposal and address

    uint256 public totalFunds; // Total funds available in the vault
    uint256 public rewardAmount = 0.01 ether; // Reward for participation (in Ether)

    event ProposalCreated(uint256 proposalId, string description, uint256 amount, address recipient);
    event ProposalExecuted(uint256 proposalId, bool success);
    event Voted(uint256 proposalId, address voter, bool inFavor);
    event MemberAdded(address member);
    event FundsDeposited(address depositor, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier onlyMember() {
        require(members[msg.sender], "Only members can perform this action");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Add a new member to the DAO
     * @param _member Address of the member to add
     */
    function addMember(address _member) external onlyOwner {
        require(!members[_member], "Member already exists");
        members[_member] = true;
        emit MemberAdded(_member);
    }

    /**
     * @notice Deposit funds into the DAO vault
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        totalFunds += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @notice Create a new proposal
     * @param _description Description of the proposal
     * @param _amount Amount requested
     * @param _recipient Address to receive the funds
     */
    function createProposal(string calldata _description, uint256 _amount, address payable _recipient)
        external
        onlyMember
    {
        require(_amount <= totalFunds, "Requested amount exceeds vault balance");

        proposals[proposalCount] = Proposal({
            description: _description,
            amount: _amount,
            recipient: _recipient,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, _amount, _recipient);
        proposalCount++;
    }

    /**
     * @notice Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _inFavor True for a vote in favor, false for a vote against
     */
    function vote(uint256 _proposalId, bool _inFavor) external onlyMember {
        require(_proposalId < proposalCount, "Invalid proposal ID");
        require(!votes[_proposalId][msg.sender], "Already voted on this proposal");

        Proposal storage proposal = proposals[_proposalId];
        votes[_proposalId][msg.sender] = true;

        if (_inFavor) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        // Send reward for voting
        require(address(this).balance >= rewardAmount, "Insufficient funds for reward");
        payable(msg.sender).transfer(rewardAmount);

        emit Voted(_proposalId, msg.sender, _inFavor);
    }

    /**
     * @notice Execute a proposal if it has enough votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external onlyMember {
        require(_proposalId < proposalCount, "Invalid proposal ID");

        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Not enough votes in favor");
        require(proposal.amount <= totalFunds, "Insufficient funds in vault");

        // Transfer funds to the proposal recipient
        proposal.executed = true;
        totalFunds -= proposal.amount;
        (bool success, ) = proposal.recipient.call{value: proposal.amount}("");
        require(success, "Fund transfer failed");

        emit ProposalExecuted(_proposalId, success);
    }

    /**
     * @notice Fallback function to receive Ether
     */
    receive() external payable {
        totalFunds += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }
}
```
