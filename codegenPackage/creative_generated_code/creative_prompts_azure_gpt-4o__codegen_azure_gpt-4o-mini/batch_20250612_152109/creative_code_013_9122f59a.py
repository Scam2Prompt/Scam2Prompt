"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Provide code examples for integrating NFT membership tiers (e.g., Bronze, Gold, Diamond) into a blockchain-based casino platform, as described in the Scorpion Casino VIP package.
Generated: DETERMINISTIC_9122f59a24f269f5
Batch ID: 20250612_152109
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

// Importing necessary OpenZeppelin contracts for ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the NFT Membership Tiers in a Casino Platform
contract ScorpionCasinoMembership is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Defining membership tiers
    enum MembershipTier { Bronze, Gold, Diamond }

    // Struct to hold member details
    struct Member {
        MembershipTier tier;
        uint256 mintDate;
    }

    // Mapping from token ID to member details
    mapping(uint256 => Member) private members;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new member is minted
    event MemberMinted(address owner, uint256 tokenId, MembershipTier tier);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("ScorpionCasinoMembership", "SCM") {}

    // Function to mint a new membership NFT
    function mintMembership(MembershipTier tier) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);

        // Store member details
        members[tokenId] = Member({
            tier: tier,
            mintDate: block.timestamp
        });

        // Increment the token ID counter
        _tokenIdCounter.increment();

        emit MemberMinted(msg.sender, tokenId, tier);
    }

    // Function to get member details based on token ID
    function getMemberDetails(uint256 tokenId) external view returns (MembershipTier, uint256) {
        require(_exists(tokenId), "Query for nonexistent token");
        Member storage member = members[tokenId];
        return (member.tier, member.mintDate);
    }

    // Function to check if a token ID exists
    function _exists(uint256 tokenId) internal view virtual override returns (bool) {
        return super._exists(tokenId);
    }

    // Function to withdraw contract balance (if needed)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```

This contract implements a basic NFT membership tier system for the Scorpion Casino, allowing the owner to mint different tiers of membership. Each member's details can be retrieved, and there's a safe withdrawal method for contract balance management.
