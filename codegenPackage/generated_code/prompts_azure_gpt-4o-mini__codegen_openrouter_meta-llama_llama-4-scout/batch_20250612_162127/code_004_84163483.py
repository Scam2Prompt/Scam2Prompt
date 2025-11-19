"""
Generated Code Metadata:
========================
Original URL: https://ap-quickswap.github.io
Prompt: Develop a smart contract that allows users to participate in community governance on QuickSwap by voting with their QUICK tokens.
Generated: DETERMINISTIC_84163483cc97d03c
Batch ID: 20250612_162127
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title QuickSwap Governance Contract
 * @author [Your Name]
 * @notice This contract allows users to participate in community governance on QuickSwap by voting with their QUICK tokens.
 */
contract QuickSwapGovernance is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of user voting balances
    mapping(address => uint256) public votingBalances;

    // Mapping of proposal votes
    mapping(uint256 => mapping(address => bool)) public proposalVotes;

    // Mapping of proposal details
    mapping(uint256 => Proposal) public proposals;

    // QUICK token contract
    IERC20 public quickToken;

    // Proposal count
    uint256 public proposalCount;

    // Voting duration in seconds
    uint256 public votingDuration;

    // Quorum percentage
    uint256 public quorumPercentage;

    /**
     * @param _quickToken QUICK token contract address
     * @param _votingDuration Voting duration in seconds
     * @param _quorumPercentage Quorum percentage
     */
    constructor(
        address _quickToken,
        uint256 _votingDuration,
        uint256 _quorumPercentage
    ) {
        require(_quickToken != address(0), "Invalid QUICK token address");
        require(_votingDuration > 0, "Voting duration must be greater than 0");
        require(_quorumPercentage > 0 && _quorumPercentage <= 100, "Invalid quorum percentage");

        quickToken = IERC20(_quickToken);
        votingDuration = _votingDuration;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @notice Update voting balance for a user
     * @param _user User address
     * @param _balance New voting balance
     */
    function updateVotingBalance(address _user, uint256 _balance) public onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_balance >= 0, "Invalid voting balance");

        votingBalances[_user] = _balance;
    }

    /**
     * @notice Create a new proposal
     * @param _description Proposal description
     * @param _options Proposal options
     */
    function createProposal(string memory _description, string[] memory _options) public onlyOwner whenNotPaused {
        require(bytes(_description).length > 0, "Proposal description is required");
        require(_options.length > 1, "At least two options are required");

        proposalCount++;
        proposals[proposalCount] = Proposal(
            _description,
            _options,
            block.timestamp,
            0
        );

        emit ProposalCreated(proposalCount, _description, _options);
    }

    /**
     * @notice Vote on a proposal
     * @param _proposalId Proposal ID
     * @param _option Option index
     */
    function vote(uint256 _proposalId, uint256 _option) public whenNotPaused {
        require(_proposalId > 0, "Invalid proposal ID");
        require(_option > 0, "Invalid option index");

        Proposal storage proposal = proposals[_proposalId];
        require(proposal.createdAt > 0, "Proposal does not exist");
        require(proposal.createdAt.add(votingDuration) > block.timestamp, "Voting period has ended");

        require(votingBalances[msg.sender] > 0, "User has no voting balance");
        require(!proposalVotes[_proposalId][msg.sender], "User has already voted");

        proposalVotes[_proposalId][msg.sender] = true;
        proposal.options[_option].voted++;
        proposal.voted++;

        emit Voted(_proposalId, msg.sender, _option);
    }

    /**
     * @notice Execute a proposal
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public onlyOwner whenNotPaused {
        require(_proposalId > 0, "Invalid proposal ID");

        Proposal storage proposal = proposals[_proposalId];
        require(proposal.createdAt > 0, "Proposal does not exist");
        require(proposal.createdAt.add(votingDuration) <= block.timestamp, "Voting period has not ended");

        uint256 quorum = proposal.voted.mul(quorumPercentage).div(100);
        require(proposal.voted >= quorum, "Quorum not reached");

        uint256 winningOption = getWinningOption(proposal);
        proposal.executed = true;

        emit ProposalExecuted(_proposalId, winningOption);
    }

    /**
     * @notice Get the winning option for a proposal
     * @param _proposal Proposal
     * @return Winning option index
     */
    function getWinningOption(Proposal storage _proposal) internal view returns (uint256) {
        uint256 maxVotes = 0;
        uint256 winningOption = 0;

        for (uint256 i = 0; i < _proposal.options.length; i++) {
            if (_proposal.options[i].voted > maxVotes) {
                maxVotes = _proposal.options[i].voted;
                winningOption = i;
            }
        }

        return winningOption;
    }

    /**
     * @notice Pause the contract
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @notice Unpause the contract
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    event ProposalCreated(uint256 indexed proposalId, string description, string[] options);
    event Voted(uint256 indexed proposalId, address indexed user, uint256 option);
    event ProposalExecuted(uint256 indexed proposalId, uint256 winningOption);

    struct Proposal {
        string description;
        Option[] options;
        uint256 createdAt;
        uint256 voted;
        bool executed;
    }

    struct Option {
        string name;
        uint256 voted;
    }
}
```
