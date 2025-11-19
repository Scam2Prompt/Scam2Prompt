"""
Generated Code Metadata:
========================
Original URL: https://nanoledger.co
Prompt: Generate Solidity code for an ERC20 token contract that implements the features of $Nanoledger, including governance voting and marketplace utility.
Generated: DETERMINISTIC_d8b1e95865672200
Batch ID: 20250612_151705
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract Nanoledger is ERC20, Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Governance variables
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    // Marketplace variables
    struct Listing {
        address seller;
        uint256 amount;
        uint256 price;
        bool active;
    }

    uint256 public constant VOTING_DURATION = 7 days;
    uint256 public constant MIN_PROPOSAL_THRESHOLD = 1000 * 10**18;
    uint256 public constant QUORUM_THRESHOLD = 30; // 30% of total supply

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    EnumerableSet.AddressSet private _governanceMembers;

    uint256 public listingCount;
    mapping(uint256 => Listing) public listings;
    uint256 public marketplaceFee; // Fee percentage (e.g., 1 = 1%)

    event ProposalCreated(uint256 indexed id, string description, uint256 voteEnd);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support);
    event ProposalExecuted(uint256 indexed id);
    event ListingCreated(uint256 indexed id, address indexed seller, uint256 amount, uint256 price);
    event ListingCancelled(uint256 indexed id);
    event ListingPurchased(uint256 indexed id, address indexed buyer, uint256 amount, uint256 price);

    constructor(uint256 initialSupply) ERC20("Nanoledger", "NLED") {
        _mint(msg.sender, initialSupply);
        marketplaceFee = 1; // 1% default fee
    }

    // Governance functions
    function createProposal(string memory description) external {
        require(balanceOf(msg.sender) >= MIN_PROPOSAL_THRESHOLD, "Insufficient balance to create proposal");
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteEnd: block.timestamp + VOTING_DURATION,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        });
        emit ProposalCreated(proposalCount, description, block.timestamp + VOTING_DURATION);
    }

    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp <= proposal.voteEnd, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        require(balanceOf(msg.sender) > 0, "No voting power");

        uint256 votingPower = balanceOf(msg.sender);
        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }
        hasVoted[proposalId][msg.sender] = true;
        emit VoteCast(msg.sender, proposalId, support);
    }

    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.voteEnd, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        uint256 quorum = (totalSupply() * QUORUM_THRESHOLD) / 100;
        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    // Marketplace functions
    function createListing(uint256 amount, uint256 price) external {
        require(amount > 0, "Amount must be positive");
        require(price > 0, "Price must be positive");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _transfer(msg.sender, address(this), amount);
        listingCount++;
        listings[listingCount] = Listing({
            seller: msg.sender,
            amount: amount,
            price: price,
            active: true
        });
        emit ListingCreated(listingCount, msg.sender, amount, price);
    }

    function cancelListing(uint256 listingId) external {
        Listing storage listing = listings[listingId];
        require(listing.active, "Listing not active");
        require(listing.seller == msg.sender, "Not the seller");

        _transfer(address(this), msg.sender, listing.amount);
        listing.active = false;
        emit ListingCancelled(listingId);
    }

    function purchaseListing(uint256 listingId) external payable {
        Listing storage listing = listings[listingId];
        require(listing.active, "Listing not active");
        require(msg.value >= listing.price, "Insufficient payment");

        uint256 feeAmount = (listing.price * marketplaceFee) / 100;
        uint256 sellerAmount = listing.price - feeAmount;

        payable(listing.seller).transfer(sellerAmount);
        _transfer(address(this), msg.sender, listing.amount);
        listing.active = false;

        emit ListingPurchased(listingId, msg.sender, listing.amount, listing.price);
    }

    // Admin functions
    function setMarketplaceFee(uint256 newFee) external onlyOwner {
        require(newFee <= 10, "Fee too high");
        marketplaceFee = newFee;
    }

    function addGovernanceMember(address member) external onlyOwner {
        _governanceMembers.add(member);
    }

    function removeGovernanceMember(address member) external onlyOwner {
        _governanceMembers.remove(member);
    }

    function isGovernanceMember(address member) external view returns (bool) {
        return _governanceMembers.contains(member);
    }

    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
