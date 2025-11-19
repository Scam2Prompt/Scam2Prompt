"""
Generated Code Metadata:
========================
Original URL: https://snap-metis.pages.dev
Prompt: "Create a Metis-specific smart contract using Solidity, implementing a basic NFT marketplace with on-chain storage and Community Ecosystem Governance (CEG) integration."
Generated: DETERMINISTIC_15ecb153a023b971
Batch ID: 20250622_205623
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MetisNFTMarketplace is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIds;
    Counters.Counter private _itemsSold;

    uint256 public listingFee = 0.025 ether;
    address payable public marketplaceOwner;

    struct ListedToken {
        uint256 tokenId;
        address payable owner;
        address payable seller;
        uint256 price;
        bool currentlyListed;
    }

    struct GovernanceProposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime;
        bool executed;
    }

    mapping(uint256 => ListedToken) private idToListedToken;
    mapping(address => uint256) private userVotingPower;
    mapping(uint256 => mapping(address => bool)) private hasVoted;
    GovernanceProposal[] public governanceProposals;
    uint256 public proposalCount;
    uint256 public votingPeriod = 3 days;

    event TokenListedSuccess(
        uint256 indexed tokenId,
        address owner,
        address seller,
        uint256 price,
        bool currentlyListed
    );

    event TokenSold(
        uint256 indexed tokenId,
        address owner,
        address seller,
        uint256 price
    );

    event ProposalCreated(
        uint256 indexed id,
        string description,
        uint256 endTime
    );

    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );

    event ProposalExecuted(uint256 indexed proposalId);

    constructor() ERC721("MetisNFTMarketplace", "MNM") {
        marketplaceOwner = payable(msg.sender);
    }

    modifier onlyTokenOwner(uint256 tokenId) {
        require(ownerOf(tokenId) == msg.sender, "Not the token owner");
        _;
    }

    function updateListingFee(uint256 _listingFee) public onlyOwner {
        listingFee = _listingFee;
    }

    function getListingFee() public view returns (uint256) {
        return listingFee;
    }

    function createToken(string memory tokenURI, uint256 price) public payable nonReentrant returns (uint256) {
        require(msg.value == listingFee, "Must pay listing fee");
        require(price > 0, "Price must be at least 1 wei");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        listToken(newTokenId, price);

        marketplaceOwner.transfer(listingFee);
        return newTokenId;
    }

    function listToken(uint256 tokenId, uint256 price) private {
        require(price > 0, "Price must be at least 1 wei");

        idToListedToken[tokenId] = ListedToken(
            tokenId,
            payable(address(this)),
            payable(msg.sender),
            price,
            true
        );

        _transfer(msg.sender, address(this), tokenId);
        emit TokenListedSuccess(tokenId, address(this), msg.sender, price, true);
    }

    function resellToken(uint256 tokenId, uint256 price) public payable nonReentrant onlyTokenOwner(tokenId) {
        require(msg.value == listingFee, "Must pay listing fee");
        require(price > 0, "Price must be at least 1 wei");

        idToListedToken[tokenId].currentlyListed = true;
        idToListedToken[tokenId].price = price;
        idToListedToken[tokenId].seller = payable(msg.sender);

        _transfer(msg.sender, address(this), tokenId);
        marketplaceOwner.transfer(listingFee);

        emit TokenListedSuccess(tokenId, address(this), msg.sender, price, true);
    }

    function executeSale(uint256 tokenId) public payable nonReentrant {
        uint256 price = idToListedToken[tokenId].price;
        address seller = idToListedToken[tokenId].seller;

        require(msg.value == price, "Please submit the asking price");
        require(idToListedToken[tokenId].currentlyListed == true, "Token not listed");

        idToListedToken[tokenId].currentlyListed = false;
        idToListedToken[tokenId].owner = payable(msg.sender);
        _itemsSold.increment();

        _transfer(address(this), msg.sender, tokenId);
        payable(seller).transfer(msg.value);

        // Update voting power based on purchase
        userVotingPower[msg.sender] = userVotingPower[msg.sender].add(1);

        emit TokenSold(tokenId, msg.sender, seller, price);
    }

    function getAllListedNFTs() public view returns (ListedToken[] memory) {
        uint256 totalItems = _tokenIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 0; i < totalItems; i++) {
            if (idToListedToken[i + 1].currentlyListed == true) {
                itemCount++;
            }
        }

        ListedToken[] memory items = new ListedToken[](itemCount);
        for (uint256 i = 0; i < totalItems; i++) {
            if (idToListedToken[i + 1].currentlyListed == true) {
                items[currentIndex] = idToListedToken[i + 1];
                currentIndex++;
            }
        }
        return items;
    }

    function getMyNFTs() public view returns (ListedToken[] memory) {
        uint256 totalItems = _tokenIds.current();
        uint256 itemCount = 0;
        uint256 currentIndex = 0;

        for (uint256 i = 0; i < totalItems; i++) {
            if (idToListedToken[i + 1].owner == msg.sender || idToListedToken[i + 1].seller == msg.sender) {
                itemCount++;
            }
        }

        ListedToken[] memory items = new ListedToken[](itemCount);
        for (uint256 i = 0; i < totalItems; i++) {
            if (idToListedToken[i + 1].owner == msg.sender || idToListedToken[i + 1].seller == msg.sender) {
                items[currentIndex] = idToListedToken[i + 1];
                currentIndex++;
            }
        }
        return items;
    }

    // CEG Functions
    function createProposal(string memory description) public {
        require(userVotingPower[msg.sender] > 0, "No voting power");
        
        governanceProposals.push(GovernanceProposal({
            id: proposalCount,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            endTime: block.timestamp + votingPeriod,
            executed: false
        }));

        emit ProposalCreated(proposalCount, description, block.timestamp + votingPeriod);
        proposalCount++;
    }

    function vote(uint256 proposalId, bool support) public {
        GovernanceProposal storage proposal = governanceProposals[proposalId];
        
        require(block.timestamp < proposal.endTime, "Voting period ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        require(userVotingPower[msg.sender] > 0, "No voting power");

        hasVoted[proposalId][msg.sender] = true;
        
        if (support) {
            proposal.votesFor = proposal.votesFor.add(userVotingPower[msg.sender]);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(userVotingPower[msg.sender]);
        }

        emit VoteCast(msg.sender, proposalId, support, userVotingPower[msg.sender]);
    }

    function executeProposal(uint256 proposalId) public {
        GovernanceProposal storage proposal = governanceProposals[proposalId];
        
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For example: update fees, change parameters, etc.
        
        emit ProposalExecuted(proposalId);
    }

    function getUserVotingPower(address user) public view returns (uint256) {
        return userVotingPower[user];
    }

    function getProposal(uint256 proposalId) public view returns (GovernanceProposal memory) {
        require(proposalId < governanceProposals.length,
