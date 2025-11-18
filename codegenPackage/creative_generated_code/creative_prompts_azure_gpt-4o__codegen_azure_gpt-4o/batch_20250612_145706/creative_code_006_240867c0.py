"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Write code to implement RetroPGF funding mechanisms for public goods in an on-chain governance system, referencing Optimism Agora's approach.
Generated: DETERMINISTIC_240867c0b6da1cba
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RetroPGF (Retroactive Public Goods Funding) Mechanism
 * @notice Implements a funding mechanism inspired by Optimism Agora for rewarding public goods retroactively.
 */
contract RetroPGFFunding {
    // --- Structs ---
    
    struct Proposal {
        uint256 id; // Unique ID for the proposal
        address proposer; // Address of the proposer
        string description; // Description of the public good or project
        uint256 fundingReceived; // Total funding received
        bool executed; // Whether the proposal has been executed
    }

    // --- State Variables ---

    uint256 public nextProposalId; // Counter for proposal IDs
    uint256 public totalFundingPool; // Total amount of funds available for RetroPGF
    address public governance; // Address of the governance contract or admin

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal struct
    mapping(address => uint256) public votes; // Tracks votes from each address
    mapping(address => bool) public hasVoted; // Tracks whether an address has voted

    // --- Events ---

    event ProposalCreated(uint256 indexed id, address indexed proposer, string description);
    event Funded(uint256 indexed id, uint256 amount);
    event VoteCasted(address indexed voter, uint256 votes);

    // --- Modifiers ---

    modifier onlyGovernance() {
        require(msg.sender == governance, "Only governance can call this function");
        _;
    }

    modifier validProposal(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Invalid proposal ID");
        _;
    }

    // --- Constructor ---

    /**
     * @dev Initializes the contract with governance address and initial funding pool.
     * @param _governance Address of the governance contract or admin.
     */
    constructor(address _governance) {
        require(_governance != address(0), "Invalid governance address");
        governance = _governance;
        nextProposalId = 1; // Start proposal IDs from 1 for better readability
    }

    // --- Governance Functions ---
    
    /**
     * @notice Governance can deposit funds into the RetroPGF funding pool.
     */
    function depositFunding() external payable onlyGovernance {
        require(msg.value > 0, "Deposit value must be greater than zero");
        totalFundingPool += msg.value;
    }

    // --- Proposal Management ---

    /**
     * @notice Allows anyone to propose a public good for funding.
     * @param _description Description of the public good or project.
     */
    function createProposal(string calldata _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");

        // Create the proposal
        uint256 proposalId = nextProposalId++;
        proposals[proposalId] = Proposal({
            id: proposalId,
            proposer: msg.sender,
            description: _description,
            fundingReceived: 0,
            executed: false
        });

        emit ProposalCreated(proposalId, msg.sender, _description);
    }

    // --- RetroPGF Funding Distribution ---

    /**
     * @notice Governance allocates funding to an approved proposal.
     * @param proposalId The ID of the proposal to fund.
     * @param amount The amount of funds to allocate to the proposal.
     */
    function fundProposal(uint256 proposalId, uint256 amount) external onlyGovernance validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(amount <= totalFundingPool, "Insufficient funding pool");

        // Transfer the funds
        totalFundingPool -= amount;
        proposal.fundingReceived += amount;
        proposal.executed = true;

        payable(proposal.proposer).transfer(amount);
        emit Funded(proposalId, amount);
    }

    // --- Voting Mechanism ---

    /**
     * @notice Allows participants to cast votes for RetroPGF funding decisions.
     * @dev This is a simple voting mechanism; a more sophisticated system could be implemented.
     * @param numVotes The number of votes being cast.
     */
    function castVotes(uint256 numVotes) external payable {
        require(numVotes > 0, "Number of votes must be greater than zero");
        require(msg.value == numVotes * 1 ether, "1 ETH per vote required"); // Example cost per vote

        votes[msg.sender] += numVotes;
        hasVoted[msg.sender] = true;

        emit VoteCasted(msg.sender, numVotes);
    }

    // --- Emergency Functions ---

    /**
     * @notice Allows governance to withdraw unused funds in case of an emergency.
     * @param amount The amount of funds to withdraw.
     * @param recipient The address to send the funds to.
     */
    function emergencyWithdraw(uint256 amount, address recipient) external onlyGovernance {
        require(amount <= totalFundingPool, "Insufficient funding pool");
        require(recipient != address(0), "Invalid recipient address");

        totalFundingPool -= amount;
        payable(recipient).transfer(amount);
    }
}
```
