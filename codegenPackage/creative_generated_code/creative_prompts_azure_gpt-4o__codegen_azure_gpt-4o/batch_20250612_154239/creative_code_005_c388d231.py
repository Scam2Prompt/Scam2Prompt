"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Develop a voting system smart contract in Solidity that allows BDOGITO holders to propose and vote on which companies should join the B2B Booster ecosystem.
Generated: DETERMINISTIC_c388d2312d84466d
Batch ID: 20250612_154239
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
 * @title VotingSystem
 * @dev A smart contract for BDOGITO token holders to propose and vote on companies joining the B2B Booster ecosystem.
 */
contract VotingSystem {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string companyName;
        string companyDetails;
        address proposer;
        uint256 voteCount;
        bool executed;
    }

    // State variables
    uint256 public proposalCount; // Counter for proposals
    mapping(uint256 => Proposal) public proposals; // Mapping to store proposals
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted for a specific proposal

    address public BDOGITOTokenAddress; // Address of BDOGITO token contract
    uint256 public votingDuration; // Duration of voting in seconds
    mapping(uint256 => uint256) public proposalDeadline; // Tracks the deadline for voting on each proposal

    // Modifier to check if the caller is a BDOGITO token holder
    modifier onlyTokenHolder() {
        require(getBDOGITOBalance(msg.sender) > 0, "Not a BDOGITO token holder");
        _;
    }

    // Event declarations
    event ProposalCreated(
        uint256 proposalId,
        string companyName,
        string companyDetails,
        address proposer,
        uint256 deadline
    );
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to initialize the contract.
     * @param _BDOGITOTokenAddress Address of the BDOGITO token contract.
     * @param _votingDuration Duration of voting period in seconds.
     */
    constructor(address _BDOGITOTokenAddress, uint256 _votingDuration) {
        BDOGITOTokenAddress = _BDOGITOTokenAddress;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _companyName Name of the company being proposed.
     * @param _companyDetails Additional details about the company.
     */
    function createProposal(string memory _companyName, string memory _companyDetails) external onlyTokenHolder {
        proposalCount++;
        uint256 deadline = block.timestamp + votingDuration;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            companyName: _companyName,
            companyDetails: _companyDetails,
            proposer: msg.sender,
            voteCount: 0,
            executed: false
        });
        proposalDeadline[proposalCount] = deadline;

        emit ProposalCreated(proposalCount, _companyName, _companyDetails, msg.sender, deadline);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external onlyTokenHolder {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        require(block.timestamp <= proposalDeadline[proposalId], "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        proposals[proposalId].voteCount++;
        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Function to execute a proposal after the voting period ends.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyTokenHolder {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        require(block.timestamp > proposalDeadline[proposalId], "Voting period has not ended");
        require(!proposals[proposalId].executed, "Proposal already executed");

        // For simplicity, only mark the proposal as executed. In a real-world scenario, you'd implement logic 
        // to onboard the company into the ecosystem.
        proposals[proposalId].executed = true;

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Function to get the BDOGITO token balance of an address.
     * @param account Address to check the balance for.
     * @return uint256 Balance of BDOGITO tokens.
     */
    function getBDOGITOBalance(address account) internal view returns (uint256) {
        (bool success, bytes memory data) = BDOGITOTokenAddress.call(
            abi.encodeWithSignature("balanceOf(address)", account)
        );
        require(success, "Failed to fetch token balance");
        return abi.decode(data, (uint256));
    }
}
```
