"""
Generated Code Metadata:
========================
Original URL: https://app-explorer.pages.dev
Prompt: Generate a smart contract template for a decentralized application that ensures censorship resistance and immutability, leveraging the principles outlined in the Dapp Protocol's decentralized architecture.
Generated: DETERMINISTIC_85f57b09d264c4bc
Batch ID: 20250612_145459
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title CensorshipResistantDapp
 * @author [Your Name]
 * @notice A decentralized application template ensuring censorship resistance and immutability.
 */
contract CensorshipResistantDapp {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user addresses to their respective balances
    mapping (address => uint256) public balances;

    // Mapping of proposal IDs to their respective details
    mapping (uint256 => Proposal) public proposals;

    // Mapping of user addresses to their respective voting powers
    mapping (address => uint256) public votingPowers;

    // Total supply of voting power
    uint256 public totalVotingPower;

    // Proposal counter
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed creator, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        address creator;
        string description;
        uint256 votingPowerRequired;
        bool executed;
        mapping (address => bool) votes;
    }

    /**
     * @dev Initializes the contract with the total supply of voting power.
     * @param _totalVotingPower The total supply of voting power.
     */
    constructor(uint256 _totalVotingPower) public {
        totalVotingPower = _totalVotingPower;
    }

    /**
     * @dev Creates a new proposal.
     * @param _description The description of the proposal.
     * @param _votingPowerRequired The voting power required to execute the proposal.
     */
    function createProposal(string memory _description, uint256 _votingPowerRequired) public {
        require(votingPowers[msg.sender] > 0, "Only users with voting power can create proposals");
        require(_votingPowerRequired > 0, "Voting power required must be greater than zero");

        Proposal memory proposal;
        proposal.id = proposalCount++;
        proposal.creator = msg.sender;
        proposal.description = _description;
        proposal.votingPowerRequired = _votingPowerRequired;
        proposal.executed = false;

        proposals[proposal.id] = proposal;

        emit NewProposal(proposal.id, proposal.creator, proposal.description);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param _proposalId The ID of the proposal.
     * @param _support Whether to support or not the proposal.
     */
    function castVote(uint256 _proposalId, bool _support) public {
        require(proposals[_proposalId].id > 0, "Proposal does not exist");
        require(votingPowers[msg.sender] > 0, "Only users with voting power can vote");
        require(!proposals[_proposalId].votes[msg.sender], "User has already voted on this proposal");

        proposals[_proposalId].votes[msg.sender] = _support;

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Executes a proposal if it has been voted for by the required voting power.
     * @param _proposalId The ID of the proposal.
     */
    function executeProposal(uint256 _proposalId) public {
        require(proposals[_proposalId].id > 0, "Proposal does not exist");
        require(!proposals[_proposalId].executed, "Proposal has already been executed");

        uint256 votingPower = 0;
        for (address voter in proposals[_proposalId].votes) {
            if (proposals[_proposalId].votes[voter]) {
                votingPower = votingPower.add(votingPowers[voter]);
            }
        }

        require(votingPower >= proposals[_proposalId].votingPowerRequired, "Proposal has not been voted for by the required voting power");

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Adds voting power to a user.
     * @param _user The address of the user.
     * @param _votingPower The amount of voting power to add.
     */
    function addVotingPower(address _user, uint256 _votingPower) public {
        require(msg.sender == owner(), "Only the owner can add voting power");

        votingPowers[_user] = votingPowers[_user].add(_votingPower);
        totalVotingPower = totalVotingPower.add(_votingPower);
    }

    /**
     * @dev Removes voting power from a user.
     * @param _user The address of the user.
     * @param _votingPower The amount of voting power to remove.
     */
    function removeVotingPower(address _user, uint256 _votingPower) public {
        require(msg.sender == owner(), "Only the owner can remove voting power");

        require(votingPowers[_user] >= _votingPower, "User does not have enough voting power");

        votingPowers[_user] = votingPowers[_user].sub(_votingPower);
        totalVotingPower = totalVotingPower.sub(_votingPower);
    }

    /**
     * @dev Returns the owner of the contract.
     * @return The address of the owner.
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
