"""
Generated Code Metadata:
========================
Original URL: https://moonbootsdao.web.app
Prompt: Explain how to implement the Golden Grenade VIP NFT membership process in a decentralized application for Moonboots DAO.
Generated: DETERMINISTIC_2b27ec87af7f5ae2
Batch ID: 20250612_162404
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// GoldenGrenadeNFT contract for Moonboots DAO VIP membership
contract GoldenGrenadeNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if an address holds a VIP membership
    mapping(address => bool) public isVIP;

    // Event emitted when a new VIP membership is minted
    event VIPMembershipMinted(address indexed member, uint256 tokenId);

    // Constructor to initialize the NFT with a name and symbol
    constructor() ERC721("Golden Grenade VIP Membership", "GGVIP") {}

    // Function to mint a new VIP membership NFT
    function mintVIPMembership() external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        
        // Mint the NFT to the caller's address
        _mint(msg.sender, tokenId);
        
        // Mark the caller as a VIP member
        isVIP[msg.sender] = true;

        // Emit the event for the new membership
        emit VIPMembershipMinted(msg.sender, tokenId);

        // Increment the token ID counter for the next mint
        _tokenIdCounter.increment();
    }

    // Function to check if an address is a VIP member
    function checkVIPStatus(address member) external view returns (bool) {
        return isVIP[member];
    }

    // Function to revoke VIP membership (only callable by the owner)
    function revokeVIPMembership(address member) external onlyOwner {
        require(isVIP[member], "Address is not a VIP member");
        
        // Burn the NFT associated with the member
        uint256 tokenId = tokenOfOwnerByIndex(member, balanceOf(member) - 1);
        _burn(tokenId);
        
        // Remove VIP status
        isVIP[member] = false;
    }

    // Function to withdraw contract balance (if any) to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
