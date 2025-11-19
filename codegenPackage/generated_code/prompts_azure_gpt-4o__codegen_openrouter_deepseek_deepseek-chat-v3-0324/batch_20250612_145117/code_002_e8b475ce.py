"""
Generated Code Metadata:
========================
Original URL: https://nidhidao.finance
Prompt: Generate a smart contract example for a DAO platform that includes wallet authentication, inspired by the functionality of NidhiDAO.
Generated: DETERMINISTIC_e8b475ceeb4f34ba
Batch ID: 20250612_145117
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/draft-EIP712.sol";

contract DAOPlatform is Ownable, EIP712 {
    using ECDSA for bytes32;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string title;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    // Struct to represent a member
    struct Member {
        address wallet;
        uint256 joinDate;
        uint256 votingPower;
        bool isActive;
    }

    // Constants
    string private constant SIGNING_DOMAIN = "DAOPlatform";
    string private constant SIGNATURE_VERSION = "1";
    uint256 public constant MIN_VOTING_POWER = 1;
    uint256 public constant VOTING_PERIOD = 7 days;

    // State variables
    IERC20 public governanceToken;
    uint256 public proposalCount;
    uint256 public memberCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => Member) public members;
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    // Events
    event MemberJoined(address indexed member, uint256 joinDate);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string title);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 votingPower);
    event ProposalExecuted(uint256 indexed proposalId, address indexed executor);

    // Modifiers
    modifier onlyMember() {
        require(members[msg.sender].isActive, "Not an active member");
        _;
    }

    modifier validProposal(uint256 proposalId) {
        require(proposalId <= proposalCount && proposalId != 0, "Invalid proposal ID");
        _;
    }

    constructor(address _governanceToken) EIP712(SIGNING_DOMAIN, SIGNATURE_VERSION) {
        governanceToken = IERC20(_governanceToken);
    }

    /**
     * @dev Join the DAO by staking governance tokens
     * @param amount The amount of governance tokens to stake
     */
    function joinDAO(uint256 amount) external {
        require(!members[msg.sender].isActive, "Already a member");
        require(amount >= MIN_VOTING_POWER, "Insufficient voting power");

        governanceToken.transferFrom(msg.sender, address(this), amount);

        members[msg.sender] = Member({
            wallet: msg.sender,
            joinDate: block.timestamp,
            votingPower: amount,
            isActive: true
        });

        memberCount++;
        emit MemberJoined(msg.sender, block.timestamp);
    }

    /**
     * @dev Create a new proposal
     * @param title The title of the proposal
     * @param description The description of the proposal
     */
    function createProposal(string memory title, string memory description) external onlyMember {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            proposer: msg.sender,
            title: title,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            startTime: block.timestamp,
            endTime: block.timestamp + VOTING_PERIOD,
            executed: false
        });

        emit ProposalCreated(proposalCount, msg.sender, title);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     * @param support Whether to support the proposal (true) or oppose it (false)
     */
    function vote(uint256 proposalId, bool support) external onlyMember validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.startTime && block.timestamp <= proposal.endTime, "Voting period closed");
        require(!hasVoted[msg.sender][proposalId], "Already voted");

        Member storage member = members[msg.sender];
        hasVoted[msg.sender][proposalId] = true;

        if (support) {
            proposal.votesFor += member.votingPower;
        } else {
            proposal.votesAgainst += member.votingPower;
        }

        emit Voted(proposalId, msg.sender, support, member.votingPower);
    }

    /**
     * @dev Execute a proposal if it has passed
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external onlyMember validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        proposal.executed = true;
        emit ProposalExecuted(proposalId, msg.sender);
    }

    /**
     * @dev Leave the DAO and withdraw staked tokens
     */
    function leaveDAO() external onlyMember {
        Member storage member = members[msg.sender];
        require(member.isActive, "Already left");

        governanceToken.transfer(msg.sender, member.votingPower);
        member.isActive = false;
        memberCount--;
    }

    /**
     * @dev Verify a signature for wallet authentication
     * @param signer The address of the signer
     * @param message The message that was signed
     * @param signature The signature to verify
     */
    function verifySignature(
        address signer,
        string memory message,
        bytes memory signature
    ) public view returns (bool) {
        bytes32 digest = _hashTypedDataV4(
            keccak256(abi.encode(keccak256("Message(string message)"), keccak256(bytes(message))))
        );
        address recoveredSigner = ECDSA.recover(digest, signature);
        return recoveredSigner == signer;
    }
}
```
