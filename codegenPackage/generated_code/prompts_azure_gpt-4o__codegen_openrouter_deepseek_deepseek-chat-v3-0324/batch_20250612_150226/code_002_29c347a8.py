"""
Generated Code Metadata:
========================
Original URL: https://pushdtoken.pages.dev
Prompt: Generate code to integrate a voting system into a decentralized governance model for a blockchain platform like Pushd, allowing token holders to propose and vote on changes to platform features and policies.
Generated: DETERMINISTIC_29c347a88b600116
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title PushdGovernance
 * @dev A decentralized governance contract allowing token holders to propose and vote on changes
 */
contract PushdGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public governanceToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private _whitelistedTokens;

    uint256 public constant MIN_PROPOSAL_DURATION = 1 days;
    uint256 public constant MIN_VOTING_DURATION = 3 days;
    uint256 public constant MIN_VOTING_POWER = 1000 * 10**18; // 1000 tokens

    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event WhitelistTokenAdded(address indexed token);
    event WhitelistTokenRemoved(address indexed token);

    modifier onlyTokenHolder() {
        require(
            governanceToken.balanceOf(msg.sender) >= MIN_VOTING_POWER,
            "Insufficient voting power"
        );
        _;
    }

    constructor(address _governanceToken) {
        require(
            _governanceToken != address(0),
            "Governance token cannot be zero address"
        );
        governanceToken = IERC20(_governanceToken);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration of voting period in seconds
     */
    function createProposal(
        string memory _description,
        uint256 _duration
    ) external onlyTokenHolder {
        require(
            _duration >= MIN_VOTING_DURATION,
            "Voting duration too short"
        );
        require(
            bytes(_description).length > 0,
            "Description cannot be empty"
        );

        uint256 startTime = block.timestamp + MIN_PROPOSAL_DURATION;
        uint256 endTime = startTime + _duration;

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            _description,
            startTime,
            endTime
        );
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support True for yes, false for no
     */
    function vote(
        uint256 _proposalId,
        bool _support
    ) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(
            block.timestamp >= proposal.startTime,
            "Voting not started"
        );
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(
            !proposal.hasVoted[msg.sender],
            "Already voted"
        );

        uint256 votingPower = governanceToken.balanceOf(msg.sender);
        proposal.hasVoted[msg.sender] = true;

        if (_support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit VoteCast(msg.sender, _proposalId, _support, votingPower);
    }

    /**
     * @dev Execute a proposal if voting succeeded
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id == _proposalId, "Proposal does not exist");
        require(
            block.timestamp > proposal.endTime,
            "Voting not ended"
        );
        require(!proposal.executed, "Already executed");
        require(
            proposal.forVotes > proposal.againstVotes,
            "Proposal rejected"
        );

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Add a token to the whitelist (onlyOwner)
     * @param _token Address of the token to whitelist
     */
    function addWhitelistedToken(address _token) external onlyOwner {
        require(_token != address(0), "Token cannot be zero address");
        require(_whitelistedTokens.add(_token), "Token already whitelisted");
        emit WhitelistTokenAdded(_token);
    }

    /**
     * @dev Remove a token from the whitelist (onlyOwner)
     * @param _token Address of the token to remove
     */
    function removeWhitelistedToken(address _token) external onlyOwner {
        require(_whitelistedTokens.remove(_token), "Token not whitelisted");
        emit WhitelistTokenRemoved(_token);
    }

    /**
     * @dev Check if a token is whitelisted
     * @param _token Address of the token to check
     * @return bool True if whitelisted
     */
    function isTokenWhitelisted(address _token) external view returns (bool) {
        return _whitelistedTokens.contains(_token);
    }

    /**
     * @dev Get list of whitelisted tokens
     * @return address[] Array of whitelisted token addresses
     */
    function getWhitelistedTokens() external view returns (address[] memory) {
        return _whitelistedTokens.values();
    }

    /**
     * @dev Get voting power of an address
     * @param _voter Address to check
     * @return uint256 Voting power in tokens
     */
    function getVotingPower(address _voter) external view returns (uint256) {
        return governanceToken.balanceOf(_voter);
    }
}
```
