"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adidasverse.pages.dev
Prompt: Write a smart contract in Solidity for minting NFTs on the Ethereum blockchain, similar to the admission ticket described in the Adidas Metaverse collaboration.
Generated: DETERMINISTIC_f2d0598671b06485
Batch ID: 20250612_153517
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

// Importing the ERC721 standard interface and Ownable functionality from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for minting NFTs
contract AdmissionTicketNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event to log the minting of a new token
    event TicketMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("AdmissionTicket", "ATKT") {}

    // Function to mint a new NFT
    // Only the owner can mint new tokens
    function mintTicket(string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token
        _mint(msg.sender, tokenId);

        // Set the metadata URI for the token
        _setTokenURI(tokenId, tokenURI);

        // Emit the TicketMinted event
        emit TicketMinted(msg.sender, tokenId, tokenURI);
    }

    // Internal function to set token URI with error handling
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Public function to retrieve the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
