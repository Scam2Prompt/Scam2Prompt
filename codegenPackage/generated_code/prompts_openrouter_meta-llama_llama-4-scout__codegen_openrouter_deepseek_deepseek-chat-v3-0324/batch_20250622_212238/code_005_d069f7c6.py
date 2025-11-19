"""
Generated Code Metadata:
========================
Original URL: https://web-galxe.com
Prompt: Develop a use case for Galxe's credential system integrated with DAO governance and NFT utility, and explain its potential applications in Web3 engagement.
Generated: DETERMINISTIC_d069f7c6e2a2144a
Batch ID: 20250622_212238
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title GalxeCredentialSystem
 * @dev A smart contract that integrates Galxe's credential system with DAO governance and NFT utility
 */
contract GalxeCredentialSystem is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a credential
    struct Credential {
        string name;
        string description;
        uint256 expirationDate;
        bool isRevoked;
    }

    // Struct to represent a DAO proposal
    struct Proposal {
        uint256 id;
        string title;
        string description;
        uint256 voteEnd;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Mapping from token ID to credential
    mapping(uint256 => Credential) public credentials;

    // Mapping from user address to token IDs they own
    mapping(address => uint256[]) public userCredentials;

    // Mapping from credential ID to voting power
    mapping(uint256 => uint256) public credentialVotingPower;

    // List of all proposals
    Proposal[] public proposals;

    // ERC20 token used for governance
    IERC20 public governanceToken;

    // Minimum voting period in blocks
    uint256 public constant MIN_VOTING_PERIOD = 10000;

    // Events
    event CredentialMinted(address indexed to, uint256 tokenId, string name);
    event CredentialRevoked(uint256 tokenId);
    event ProposalCreated(uint256 proposalId, string title);
    event Voted(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor
     * @param _governanceToken Address of the ERC20 governance token
     */
    constructor(address _governanceToken) ERC721("GalxeCredential", "GCRED") {
        governanceToken = IERC20(_governanceToken);
    }

    /**
     * @dev Mint a new credential NFT
     * @param to The address to mint the credential to
     * @param name Name of the credential
     * @param description Description of the credential
     * @param expirationDate Unix timestamp when credential expires (0 for no expiration)
     * @param votingPower Voting power assigned to this credential
     */
    function mintCredential(
        address to,
        string memory name,
        string memory description,
        uint256 expirationDate,
        uint256 votingPower
    ) external onlyOwner {
        require(bytes(name).length > 0, "Name cannot be empty");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        
        credentials[tokenId] = Credential({
            name: name,
            description: description,
            expirationDate: expirationDate,
            isRevoked: false
        });
        
        userCredentials[to].push(tokenId);
        credentialVotingPower[tokenId] = votingPower;
        
        emit CredentialMinted(to, tokenId, name);
    }

    /**
     * @dev Revoke a credential
     * @param tokenId The ID of the credential to revoke
     */
    function revokeCredential(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Credential does not exist");
        credentials[tokenId].isRevoked = true;
        emit CredentialRevoked(tokenId);
    }

    /**
     * @dev Create a new DAO proposal
     * @param title Title of the proposal
     * @param description Description of the proposal
     * @param votingPeriod Duration of voting period in blocks
     */
    function createProposal(
        string memory title,
        string memory description,
        uint256 votingPeriod
    ) external onlyOwner {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(votingPeriod >= MIN_VOTING_PERIOD, "Voting period too short");
        
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            id: proposalId,
            title: title,
            description: description,
            voteEnd: block.number + votingPeriod,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        }));
        
        emit ProposalCreated(proposalId, title);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     * @param support Whether to support the proposal (true = yes, false = no)
     */
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.number < proposal.voteEnd, "Voting period ended");
        
        uint256 votingPower = getUserVotingPower(msg.sender);
        require(votingPower > 0, "No voting power");
        
        if (support) {
            proposal.yesVotes += votingPower;
        } else {
            proposal.noVotes += votingPower;
        }
        
        emit Voted(msg.sender, proposalId, support, votingPower);
    }

    /**
     * @dev Execute a proposal
     * @param proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.number >= proposal.voteEnd, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.yesVotes > proposal.noVotes, "Proposal did not pass");
        
        proposal.executed = true;
        emit ProposalExecuted(proposalId);
        
        // Here you would implement the actual proposal execution logic
    }

    /**
     * @dev Get the voting power of a user based on their credentials
     * @param user The address of the user
     * @return Total voting power
     */
    function getUserVotingPower(address user) public view returns (uint256) {
        uint256[] memory userCreds = userCredentials[user];
        uint256 totalPower = 0;
        
        for (uint256 i = 0; i < userCreds.length; i++) {
            uint256 tokenId = userCreds[i];
            Credential memory cred = credentials[tokenId];
            
            if (!cred.isRevoked && 
                (cred.expirationDate == 0 || block.timestamp < cred.expirationDate) &&
                ownerOf(tokenId) == user) {
                totalPower += credentialVotingPower[tokenId];
            }
        }
        
        return totalPower;
    }

    /**
     * @dev Get all credentials owned by a user
     * @param user The address of the user
     * @return Array of credential IDs
     */
    function getUserCredentials(address user) external view returns (uint256[] memory) {
        return userCredentials[user];
    }

    /**
     * @dev Get credential details by ID
     * @param tokenId The ID of the credential
     * @return Credential details
     */
    function getCredentialDetails(uint256 tokenId) external view returns (Credential memory) {
        require(_exists(tokenId), "Credential does not exist");
        return credentials[tokenId];
    }

    /**
     * @dev Override transfer functions to prevent credential transfers
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        require(from == address(0) || to == address(0), "Credentials are non-transferable");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
