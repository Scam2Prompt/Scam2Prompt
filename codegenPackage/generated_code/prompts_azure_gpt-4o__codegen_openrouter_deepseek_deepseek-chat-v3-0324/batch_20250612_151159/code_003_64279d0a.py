"""
Generated Code Metadata:
========================
Original URL: https://bridgeqom.pages.dev
Prompt: Provide documentation-based examples for integrating QOM.One Cards into a dApp, focusing on community-driven use cases.
Generated: DETERMINISTIC_64279d0adf0cc57c
Batch ID: 20250612_151159
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

/**
 * @title QOMOneCard
 * @dev Community-driven NFT representing QOM.One Cards with voting and governance features
 */
contract QOMOneCard is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct CardDetails {
        string name;
        string description;
        uint256 creationDate;
        address creator;
        uint256 voteCount;
    }

    mapping(uint256 => CardDetails) private _cardDetails;
    mapping(address => bool) private _hasVoted;
    mapping(uint256 => mapping(address => bool)) private _cardVoters;

    event CardMinted(uint256 indexed tokenId, address indexed creator, string name);
    event VoteCast(uint256 indexed tokenId, address indexed voter);
    event CardUpdated(uint256 indexed tokenId, string newDescription);

    constructor() ERC721("QOMOneCard", "QOMC") {}

    /**
     * @dev Mints a new QOM.One Card with community details
     * @param name The name of the card
     * @param description Description of the card's purpose
     * @param recipient Address receiving the card
     */
    function mintCard(string memory name, string memory description, address recipient) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(recipient, tokenId);
        
        _cardDetails[tokenId] = CardDetails({
            name: name,
            description: description,
            creationDate: block.timestamp,
            creator: recipient,
            voteCount: 0
        });

        emit CardMinted(tokenId, recipient, name);
    }

    /**
     * @dev Allows community members to vote on a card
     * @param tokenId The ID of the card being voted on
     */
    function voteForCard(uint256 tokenId) public {
        require(_exists(tokenId), "Card does not exist");
        require(!_cardVoters[tokenId][msg.sender], "Already voted for this card");
        
        _cardDetails[tokenId].voteCount += 1;
        _cardVoters[tokenId][msg.sender] = true;
        
        emit VoteCast(tokenId, msg.sender);
    }

    /**
     * @dev Updates card description (creator or owner only)
     * @param tokenId The ID of the card to update
     * @param newDescription New description for the card
     */
    function updateCardDescription(uint256 tokenId, string memory newDescription) public {
        require(_exists(tokenId), "Card does not exist");
        require(
            ownerOf(tokenId) == msg.sender || _cardDetails[tokenId].creator == msg.sender,
            "Not authorized to update"
        );
        
        _cardDetails[tokenId].description = newDescription;
        
        emit CardUpdated(tokenId, newDescription);
    }

    /**
     * @dev Gets card details
     * @param tokenId The ID of the card
     * @return CardDetails struct containing all card information
     */
    function getCardDetails(uint256 tokenId) public view returns (CardDetails memory) {
        require(_exists(tokenId), "Card does not exist");
        return _cardDetails[tokenId];
    }

    /**
     * @dev Checks if an address has voted for a specific card
     * @param tokenId The ID of the card
     * @param voter Address to check
     * @return bool Whether the address has voted
     */
    function hasVoted(uint256 tokenId, address voter) public view returns (bool) {
        return _cardVoters[tokenId][voter];
    }
}
```

```javascript
// QOM.One Card Integration Example for Frontend dApp
import { ethers } from 'ethers';
import QOMOneCardABI from './QOMOneCardABI.json';

const contractAddress = "0x123..."; // Replace with actual contract address

// Initialize provider and contract
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
const qomCardContract = new ethers.Contract(contractAddress, QOMOneCardABI, signer);

/**
 * Mint a new QOM.One Card
 * @param {string} name - Card name
 * @param {string} description - Card description
 * @param {string} recipientAddress - Recipient wallet address
 */
async function mintCard(name, description, recipientAddress) {
    try {
        const tx = await qomCardContract.mintCard(name, description, recipientAddress);
        await tx.wait();
        console.log('Card minted successfully');
    } catch (error) {
        console.error('Error minting card:', error);
    }
}

/**
 * Vote for a QOM.One Card
 * @param {number} tokenId - ID of the card to vote for
 */
async function voteForCard(tokenId) {
    try {
        const tx = await qomCardContract.voteForCard(tokenId);
        await tx.wait();
        console.log('Vote recorded successfully');
    } catch (error) {
        console.error('Error voting for card:', error);
    }
}

/**
 * Get card details
 * @param {number} tokenId - ID of the card
 * @returns {Object} Card details
 */
async function getCardDetails(tokenId) {
    try {
        const details = await qomCardContract.getCardDetails(tokenId);
        return {
            name: details.name,
            description: details.description,
            creationDate: new Date(details.creationDate * 1000),
            creator: details.creator,
            voteCount: details.voteCount.toString()
        };
    } catch (error) {
        console.error('Error fetching card details:', error);
        return null;
    }
}

/**
 * Check if user has voted for a card
 * @param {number} tokenId - ID of the card
 * @param {string} userAddress - User's wallet address
 * @returns {boolean} Voting status
 */
async function checkUserVote(tokenId, userAddress) {
    try {
        return await qomCardContract.hasVoted(tokenId, userAddress);
    } catch (error) {
        console.error('Error checking vote status:', error);
        return false;
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./QOMOneCard.sol";

/**
 * @title QOMOneCardCommunity
 * @dev Extension for community-driven features like proposals and rewards
 */
contract QOMOneCardCommunity {
    QOMOneCard public qomCard;

    struct Proposal {
        uint256 cardId;
        string description;
        uint256 votes;
        bool executed;
        address proposer;
    }

    Proposal[] public proposals;
    mapping(uint256 => uint256) public cardToProposal;
    mapping(address => uint256) public userRewards;

    event ProposalCreated(uint256 proposalId, uint256 cardId, address proposer);
    event ProposalExecuted(uint256 proposalId);
    event RewardClaimed(address user, uint256 amount);

    constructor(address _qomCardAddress) {
        qomCard = QOMOneCard(_qomCardAddress);
    }

    /**
     * @dev Create a community proposal linked to a QOM.One Card
     * @param cardId The card ID this proposal relates to
     * @param description Description of the proposal
     */
    function createProposal(uint256 cardId, string memory description) public {
        require(qomCard.ownerOf(cardId) != address(0), "Invalid card ID");
        
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            cardId: cardId,
            description: description,
            votes: 0,
            executed: false,
            proposer: msg.sender
        }));
        
        cardToProposal[cardId] = proposalId;
        emit ProposalCreated(proposalId, cardId, msg.sender);
    }

    /**
     * @dev Vote for a proposal using your QOM.One Card voting power
     * @param proposalId ID of the proposal to vote for
     */
    function voteForProposal(uint256 proposalId) public {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        
        uint256 cardId = proposal.cardId;
        require(qomCard.ownerOf(cardId) == msg.sender, "Not card owner");
        require(!qomCard.hasVoted(cardId, msg.sender), "Already voted");

        qomCard.voteForCard(cardId);
        proposal.votes += 1;
        
        // Reward voters
        userRewards[msg.sender] += 1;
    }

    /**
     * @dev Execute a proposal that has reached quorum
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal
