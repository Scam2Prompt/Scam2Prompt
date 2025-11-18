"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanoledger.co
Prompt: Generate Solidity code for an ERC20 token contract that implements the features of $Nanoledger, including governance voting and marketplace utility.
Generated: DETERMINISTIC_d8b1e95865672200
Batch ID: 20250612_151705
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
 * @title Nanoledger Token ($Nanoledger)
 * @dev ERC20 token implementation with governance voting and marketplace utility features.
 */
contract NanoledgerToken {
    // ERC20 token properties
    string public name = "$Nanoledger";
    string public symbol = "NANO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mappings for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Governance voting variables
    struct Proposal {
        string description;
        uint256 voteCount; // Number of tokens backing the proposal
        bool executed;
    }
    Proposal[] public proposals;
    mapping(address => uint256) public votingPower; // Tracks voting power per user

    // Marketplace utility variables
    struct Listing {
        address seller;
        string itemDescription;
        uint256 price;
        bool active;
    }
    Listing[] public marketplace;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ProposalCreated(uint256 proposalId, string description);
    event VoteCast(address indexed voter, uint256 proposalId, uint256 votingTokens);
    event ProposalExecuted(uint256 proposalId);
    event ItemListed(uint256 listingId, address indexed seller, string itemDescription, uint256 price);
    event ItemPurchased(uint256 listingId, address indexed buyer);

    // Contract Constructor
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * (10**decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC20 Functions

    /**
     * @dev Returns the balance of a given account.
     * @param account The account to query.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a recipient.
     * @param recipient The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend a specific amount of tokens on behalf of the caller.
     * @param spender The spender's address.
     * @param amount The amount of tokens to approve.
     * @return True if the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The sender's address.
     * @param recipient The recipient's address.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Cannot transfer from the zero address");
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the amount of tokens that a spender is allowed to spend on behalf of an owner.
     * @param owner The owner's address.
     * @param spender The spender's address.
     * @return The allowance amount.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Governance Voting Functions

    /**
     * @dev Creates a new governance proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) public {
        proposals.push(Proposal({ description: description, voteCount: 0, executed: false }));
        emit ProposalCreated(proposals.length - 1, description);
    }

    /**
     * @dev Casts a vote for a proposal using tokens.
     * @param proposalId The ID of the proposal to vote for.
     * @param amount The amount of tokens to vote with.
     */
    function vote(uint256 proposalId, uint256 amount) public {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(amount > 0, "Vote amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct tokens from voter's balance
        balances[msg.sender] -= amount;
        votingPower[msg.sender] += amount;

        // Add vote count to the proposal
        proposals[proposalId].voteCount += amount;

        emit VoteCast(msg.sender, proposalId, amount);
    }

    /**
     * @dev Executes a proposal if it has sufficient votes.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) public {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > totalSupply / 2, "Not enough votes to execute");

        proposal.executed = true;

        emit ProposalExecuted(proposalId);
    }

    // Marketplace Utility Functions

    /**
     * @dev Lists an item for sale in the marketplace.
     * @param itemDescription Description of the item.
     * @param price Price of the item in tokens.
     */
    function listItem(string memory itemDescription, uint256 price) public {
        require(price > 0, "Price must be greater than zero");

        marketplace.push(Listing({ seller: msg.sender, itemDescription: itemDescription, price: price, active: true }));
        emit ItemListed(marketplace.length - 1, msg.sender, itemDescription, price);
    }

    /**
     * @dev Purchases an item from the marketplace.
     * @param listingId The ID of the listing to purchase.
     */
    function purchaseItem(uint256 listingId) public {
        require(listingId < marketplace.length, "Invalid listing ID");
        Listing storage listing = marketplace[listingId];
        require(listing.active, "Listing is no longer active");
        require(balances[msg.sender] >= listing.price, "Insufficient balance");

        // Transfer tokens to the seller
        balances[msg.sender] -= listing.price;
        balances[listing.seller] += listing.price;

        // Mark listing as inactive
        listing.active = false;

        emit ItemPurchased(listingId, msg.sender);
    }
}
```
