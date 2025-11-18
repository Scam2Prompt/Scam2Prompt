"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: Develop a grant proposal for building a new dApp on Flare that utilizes its Web2 connectivity feature to trigger smart contracts based on external API data.
Generated: DETERMINISTIC_0f87008b137f5365
Batch ID: 20250612_153848
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
 * @title GrantProposalDApp
 * @dev A decentralized application (dApp) on the Flare blockchain that
 *      utilizes Web2 connectivity to trigger smart contracts based on external API data.
 */
contract GrantProposalDApp {
    // Owner of the contract
    address public owner;

    // Struct to represent a grant proposal
    struct Proposal {
        uint256 id;
        string title;
        string description;
        uint256 timestamp;
        bool approved;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Counter for proposal IDs
    uint256 private proposalCounter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string title, string description, uint256 timestamp);

    // Event emitted when a proposal is approved
    event ProposalApproved(uint256 id);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to set the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new grant proposal.
     * @param _title Title of the grant proposal.
     * @param _description Description of the grant proposal.
     */
    function createProposal(string memory _title, string memory _description) public onlyOwner {
        proposalCounter++;
        proposals[proposalCounter] = Proposal(proposalCounter, _title, _description, block.timestamp, false);
        emit ProposalCreated(proposalCounter, _title, _description, block.timestamp);
    }

    /**
     * @dev Function to approve a grant proposal.
     * @param proposalId ID of the proposal to be approved.
     */
    function approveProposal(uint256 proposalId) public onlyOwner {
        require(proposals[proposalId].id != 0, "Proposal does not exist.");
        require(!proposals[proposalId].approved, "Proposal is already approved.");
        proposals[proposalId].approved = true;
        emit ProposalApproved(proposalId);
    }

    /**
     * @dev Function to connect with Web2 APIs to trigger actions.
     * @notice This function is a placeholder for integration with Flare's Web2 connectivity feature.
     * @param apiUrl The API endpoint to retrieve external data.
     * @param proposalId ID of the proposal to be updated based on external data.
     */
    function triggerFromAPI(string memory apiUrl, uint256 proposalId) public onlyOwner {
        // Note: Actual Web2 connectivity and API calls are handled off-chain through Flare's FTSO/State Connector.
        // Example logic demonstrating the concept:
        require(proposals[proposalId].id != 0, "Proposal does not exist.");

        // Simulate external API data influencing proposal approval
        // (In production, this would be handled by off-chain services interacting with the Flare State Connector.)
        bool externalApproval = true; // Placeholder for API call result

        if (externalApproval) {
            proposals[proposalId].approved = true;
            emit ProposalApproved(proposalId);
        }
    }

    /**
     * @dev Function to retrieve proposal details.
     * @param proposalId ID of the proposal to retrieve details for.
     * @return The proposal details.
     */
    function getProposalDetails(uint256 proposalId) public view returns (Proposal memory) {
        require(proposals[proposalId].id != 0, "Proposal does not exist.");
        return proposals[proposalId];
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address.");
        owner = newOwner;
    }
}
```
