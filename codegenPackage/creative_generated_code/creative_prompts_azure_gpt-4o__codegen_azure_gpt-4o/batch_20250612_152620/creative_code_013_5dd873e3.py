"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydrofinance-dapp.pages.dev
Prompt: Write a Solidity contract to allow HDRO token holders to vote on asset admission for Hydro Protocol's Real Yield Asset (RYA) basket.
Generated: DETERMINISTIC_5dd873e3b5f94f10
Batch ID: 20250612_152620
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
 * @title HDRO Token Holder Voting Contract
 * @dev Allows HDRO token holders to vote on asset admission for Hydro Protocol's RYA basket.
 */
contract AssetAdmissionVoting {
    struct Proposal {
        address asset; // The asset proposed for admission
        string description; // A brief description of the asset
        uint256 votesFor; // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        bool executed; // Whether the proposal has been executed
    }

    address public owner;
    IERC20 public hdroToken; // Reference to the HDRO token contract
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    event ProposalCreated(uint256 proposalId, address indexed asset, string description);
    event Voted(uint256 proposalId, address indexed voter, bool inFavor);
    event ProposalExecuted(uint256 proposalId, address indexed asset, bool accepted);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier hasHDROBalance() {
        require(hdroToken.balanceOf(msg.sender) > 0, "Must hold HDRO tokens to participate");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposals.length, "Proposal does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the HDRO token address.
     * @param _hdroToken Address of the HDRO token contract.
     */
    constructor(address _hdroToken) {
        require(_hdroToken != address(0), "Invalid HDRO token address");
        owner = msg.sender;
        hdroToken = IERC20(_hdroToken);
    }

    /**
     * @dev Creates a new proposal for asset admission.
     * @param _asset Address of the proposed asset.
     * @param _description Description of the proposed asset.
     */
    function createProposal(address _asset, string memory _description) external onlyOwner {
        require(_asset != address(0), "Invalid asset address");
        proposals.push(
            Proposal({
                asset: _asset,
                description: _description,
                votesFor: 0,
                votesAgainst: 0,
                executed: false
            })
        );
        emit ProposalCreated(proposals.length - 1, _asset, _description);
    }

    /**
     * @dev Allows HDRO token holders to vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param inFavor Boolean indicating whether the vote is in favor or against.
     */
    function vote(uint256 proposalId, bool inFavor) external hasHDROBalance proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!hasVoted[proposalId][msg.sender], "Already voted on this proposal");
        require(!proposal.executed, "Proposal has already been executed");

        // Mark voter as having voted
        hasVoted[proposalId][msg.sender] = true;

        if (inFavor) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit Voted(proposalId, msg.sender, inFavor);
    }

    /**
     * @dev Executes a proposal after voting has concluded.
     * Only the contract owner can execute proposals.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal has already been executed");

        // Determine if proposal is accepted based on votes
        bool accepted = proposal.votesFor > proposal.votesAgainst;

        // Mark proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(proposalId, proposal.asset, accepted);

        // If accepted, implement logic for asset admission (out of scope for this contract)
        // For instance, adding the asset to the RYA basket.
        if (accepted) {
            // Asset admission logic goes here (e.g., updating a state variable, interacting with other contracts, etc.)
        }
    }

    /**
     * @dev Returns the total number of proposals created.
     * @return The number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Returns details of a specific proposal.
     * @param proposalId ID of the proposal to fetch.
     * @return asset Address of the asset.
     * @return description Description of the asset.
     * @return votesFor Number of votes in favor.
     * @return votesAgainst Number of votes against.
     * @return executed Whether the proposal has been executed.
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (
            address asset,
            string memory description,
            uint256 votesFor,
            uint256 votesAgainst,
            bool executed
        )
    {
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.asset,
            proposal.description,
            proposal.votesFor,
            proposal.votesAgainst,
            proposal.executed
        );
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
