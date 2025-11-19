"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Create a DAO governance smart contract in Solidity for MetaLeagues, including voting mechanisms for NFT leasing decisions and fund allocation.
Generated: DETERMINISTIC_d4eaafcfebd5ff5e
Batch ID: 20250612_151513
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
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
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

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title MetaLeagues DAO Governance Contract
 * @author [Your Name]
 * @notice This contract enables governance for MetaLeagues DAO, including voting mechanisms for NFT leasing decisions and fund allocation.
 */
contract MetaLeaguesDAO {
    // Using SafeMath for uint256 to prevent overflow
    using SafeMath for uint256;

    // Mapping of members and their voting power
    mapping(address => Member) public members;

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping of votes
    mapping(uint256 => mapping(address => Vote)) public votes;

    // Proposal counters
    uint256 public proposalCount;
    uint256 public memberCount;

    // NFT leasing and fund allocation variables
    address public nftAddress;
    address public fundAddress;

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed creator, string description);
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    // Structs
    struct Member {
        uint256 votingPower;
        bool active;
    }

    struct Proposal {
        uint256 id;
        address creator;
        string description;
        uint256 votingPowerRequired;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        bool nftLeasingProposal;
        address nftLeasingAddress;
        uint256 fundAllocationAmount;
    }

    struct Vote {
        bool support;
        bool cast;
    }

    // Modifiers
    modifier onlyActiveMember {
        require(members[msg.sender].active, "Only active members can perform this action");
        _;
    }

    modifier onlyExistingProposal(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Constructor
    constructor(address _nftAddress, address _fundAddress) public {
        nftAddress = _nftAddress;
        fundAddress = _fundAddress;
    }

    // Functions
    function addMember(address _member, uint256 _votingPower) public {
        require(msg.sender == fundAddress, "Only fund address can add members");
        members[_member] = Member(_votingPower, true);
        memberCount++;
    }

    function createProposal(string memory _description, uint256 _votingPowerRequired, bool _nftLeasingProposal, address _nftLeasingAddress, uint256 _fundAllocationAmount) public onlyActiveMember {
        proposalCount++;
        proposals[proposalCount] = Proposal(proposalCount, msg.sender, _description, _votingPowerRequired, 0, 0, false, _nftLeasingProposal, _nftLeasingAddress, _fundAllocationAmount);
        emit ProposalCreated(proposalCount, msg.sender, _description);
    }

    function castVote(uint256 _proposalId, bool _support) public onlyActiveMember onlyExistingProposal(_proposalId) {
        require(!votes[_proposalId][msg.sender].cast, "Already voted on this proposal");
        Proposal storage proposal = proposals[_proposalId];
        Member storage member = members[msg.sender];
        votes[_proposalId][msg.sender] = Vote(_support, true);
        if (_support) {
            proposal.yesVotes = proposal.yesVotes.add(member.votingPower);
        } else {
            proposal.noVotes = proposal.noVotes.add(member.votingPower);
        }
        emit VoteCast(_proposalId, msg.sender, _support);
    }

    function executeProposal(uint256 _proposalId) public onlyExistingProposal(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.yesVotes > proposal.votingPowerRequired, "Proposal did not pass");
        proposal.executed = true;
        if (proposal.nftLeasingProposal) {
            // Perform NFT leasing logic
            SafeERC721(nftAddress).transfer(proposal.nftLeasingAddress, 1);
        } else {
            // Perform fund allocation logic
            payable(proposal.creator).transfer(proposal.fundAllocationAmount);
        }
        emit ProposalExecuted(_proposalId);
    }
}
```
